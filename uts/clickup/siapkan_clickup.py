"""Menyiapkan bahan ClickUp dari draf UTS (../draf/01_pmbok4.md): WBS (Tabel 2.11), milestone (Tabel 2.12),
dan jadwal (Tabel 2.13). Diadaptasi dari tugas2/clickup/siapkan_clickup.py.

Jalankan:
    python3 siapkan_clickup.py

Hasil (di folder ini):
    clickup_import_uts.csv   berkas impor spreadsheet ClickUp (pilihan A, cadangan)
    ketergantungan.md        daftar ketergantungan, termasuk hubungan yang tidak dibuat di ClickUp

Fungsi data() juga dipakai buat_clickup.py (pilihan B, lewat API).

Pendahulu dibaca dari kolom "Pendahulu": kode WBS (1.3.1), rentang (1.3.1–1.3.6), dan milestone (M4).
ClickUp hanya mengenal ketergantungan "selesai lalu mulai" (Finish-to-Start). Hubungan yang di jadwal
berjenis "mulai bersamaan" atau "mulai sebelum pendahulu selesai" (pendahulu selesai SETELAH tugas
mulai) tidak dibuat di ClickUp, tetapi dicatat di ketergantungan.md.
"""
import csv
import datetime as dt
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
SUMBER = DIR.parent / "draf" / "01_pmbok4.md"
TAHUN = 2027
NAMA_LIST = "Super App Nusantara Express (UTS ITPM)"
BULAN = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Mei": 5, "Jun": 6}


def sel(baris):
    return [c.strip() for c in baris.strip().strip("|").split("|")]


def polos(teks):
    """Buang markup Markdown (**, *) supaya rapi di ClickUp."""
    return re.sub(r"\*+", "", teks).strip()


def ambil_tabel(md, kepala):
    blok = []
    for b in md[md.index(kepala):].splitlines():
        if not b.startswith("|"):
            break
        blok.append(sel(b))
    return blok[2:]


def tanggal(teks):
    """'1 Feb' atau 'Sen, 4 Jan 2027' → date."""
    m = re.search(r"(\d{1,2}) (Jan|Feb|Mar|Apr|Mei|Jun)", teks)
    if not m:
        raise ValueError(f"tanggal tidak dikenali: {teks!r}")
    return dt.date(TAHUN, BULAN[m.group(2)], int(m.group(1)))


def kode_dalam(teks):
    """Ambil semua kode WBS level 3 dan milestone dari teks; rentang a–b diperluas."""
    hasil = []
    for a, b in re.findall(r"(\d\.\d\.\d+)\s*[–-]\s*(\d\.\d\.\d+)", teks):
        awal, akhir = int(a.split(".")[2]), int(b.split(".")[2])
        induk = a.rsplit(".", 1)[0]
        hasil += [f"{induk}.{i}" for i in range(awal, akhir + 1)]
    teks = re.sub(r"(\d\.\d\.\d+)\s*[–-]\s*(\d\.\d\.\d+)", "", teks)
    hasil += re.findall(r"\b\d\.\d\.\d+\b", teks)
    hasil += re.findall(r"\bM\d\b", teks)
    urut = []
    for k in hasil:
        if k not in urut:
            urut.append(k)
    return urut


def data():
    md = SUMBER.read_text(encoding="utf8")

    wbs = {}
    for c in ambil_tabel(md, "| Kode | Paket kerja | Hasil kerja | PJ |"):
        wbs[polos(c[0])] = dict(nama=polos(c[1]), hasil=polos(c[2]), pj=polos(c[3]))

    jadwal = {}
    for c in ambil_tabel(md, "| Kode | Paket kerja | Mulai | Selesai | Hari kerja | Pendahulu | Kritis |"):
        kode = polos(c[0])
        if kode.count(".") != 2:
            continue
        selesai = tanggal(c[3])
        mulai = selesai if polos(c[2]) in ("—", "-") else tanggal(c[2])
        jadwal[kode] = dict(mulai=mulai, selesai=selesai, hari=polos(c[4]), teks_pendahulu=polos(c[5]),
                            pendahulu=[k for k in kode_dalam(c[5]) if k != kode], kritis="●" in c[6])

    milestone = []
    for c in ambil_tabel(md, "| Kode | Milestone | Tanggal | Syarat tercapai |"):
        kode = polos(c[0])
        tgl = tanggal(c[2])
        milestone.append(dict(id=kode, kode=kode, nama=f"◆ {kode} {polos(c[1])}", mulai=tgl, selesai=tgl,
                              deskripsi=f"Milestone, {polos(c[2])}.\nSyarat tercapai: {polos(c[3])}",
                              tag=["milestone"], pendahulu_kode=kode_dalam(c[3])))

    fase, tugas = [], []
    for kode, w in wbs.items():
        if kode.count(".") == 1:
            fase.append(dict(kode=kode, nama=w["nama"], anak=[]))
            continue
        if kode.count(".") != 2:
            continue
        j = jadwal[kode]
        tag = [t.strip().lower() for t in w["pj"].split(",")] + (["jalur-kritis"] if j["kritis"] else [])
        t = dict(id=f"WBS-{kode}", kode=kode, nama=f"{kode} {w['nama']}", mulai=j["mulai"], selesai=j["selesai"],
                 deskripsi=(f"Hasil kerja: {w['hasil']}\nPenanggung jawab: {w['pj']}\n"
                            f"Durasi: {j['hari']} hari kerja. Pendahulu: {j['teks_pendahulu']}"
                            + ("\nJalur kritis." if j["kritis"] else "")),
                 tag=tag, pendahulu_kode=j["pendahulu"])
        tugas.append(t)
        fase[-1]["anak"].append(t)
    for f in fase:
        f.update(id=f"WBS-{f['kode']}", nama=f"{f['kode']} {f['nama']}",
                 deskripsi=f"Level 2 WBS ({len(f['anak'])} paket kerja).",
                 mulai=min(t["mulai"] for t in f["anak"]), selesai=max(t["selesai"] for t in f["anak"]), tag=["fase"])

    # Ketergantungan: pisahkan Finish-to-Start (dibuat di ClickUp) dari hubungan lain (hanya dicatat)
    semua = {t["kode"]: t for t in tugas} | {m["kode"]: m for m in milestone}
    for x in tugas + milestone:
        x["pendahulu"], x["lain"] = [], []
        for k in x.pop("pendahulu_kode"):
            p = semua[k]
            jenis_ms = x["kode"].startswith("M")
            fs = p["selesai"] <= x["mulai"] if jenis_ms else p["selesai"] < x["mulai"]
            (x["pendahulu"] if fs else x["lain"]).append(p["id"])
    return fase, tugas, milestone


def tulis_csv(fase, tugas, milestone):
    with open(DIR / "clickup_import_uts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Task ID", "Task Name", "Description", "Start Date", "Due Date", "Tags", "Subtask IDs"])
        for x in fase:
            w.writerow([x["id"], x["nama"], x["deskripsi"], x["mulai"].isoformat(), x["selesai"].isoformat(),
                        ",".join(x["tag"]), ",".join(t["id"] for t in x["anak"])])
            for t in x["anak"]:
                w.writerow([t["id"], t["nama"], t["deskripsi"], t["mulai"].isoformat(), t["selesai"].isoformat(),
                            ",".join(t["tag"]), ""])
        for m in milestone:
            w.writerow([m["id"], m["nama"], m["deskripsi"], m["mulai"].isoformat(), m["selesai"].isoformat(),
                        ",".join(m["tag"]), ""])


def tulis_ketergantungan(tugas, milestone):
    nama = {t["id"]: t["nama"] for t in tugas + milestone}
    fs = sorted([(x, p) for x in tugas + milestone for p in x["pendahulu"]], key=lambda b: (b[0]["mulai"], b[0]["id"]))
    lain = sorted([(x, p) for x in tugas + milestone for p in x["lain"]], key=lambda b: (b[0]["mulai"], b[0]["id"]))
    isi = ["# Daftar ketergantungan jadwal UTS (Tabel 2.13 dan 2.12)", "",
           f"**A. Finish-to-Start ({len(fs)} hubungan)**: dibuat otomatis oleh buat_clickup.py, atau dibuat manual "
           "di Gantt ClickUp bila memakai impor CSV. Tugas di kolom kanan baru mulai setelah tugas di kolom kiri selesai.", "",
           "Cara manual di Gantt ClickUp: arahkan kursor ke batang di kolom **Pendahulu**, tarik titik di ujung kanannya "
           "ke batang di kolom **Tugas**.", "",
           "| No | Pendahulu (selesai dulu) | Tugas (mulai sesudahnya) | ✓ |", "|---|---|---|---|"]
    isi += [f"| {i} | {nama[p]} | {x['nama']} | ☐ |" for i, (x, p) in enumerate(fs, 1)]
    isi += ["", f"**B. Hubungan lain ({len(lain)} hubungan)**: TIDAK dibuat di ClickUp, karena pendahulu belum selesai "
            "ketika tugas dimulai (pola \"mulai bersamaan\" atau \"mulai sebelum pendahulu selesai\" di Tabel 2.13). "
            "ClickUp hanya mengenal Finish-to-Start, jadi hubungan ini cukup dijelaskan di laporan.", "",
            "| No | Pendahulu | Tugas | Pendahulu selesai | Tugas mulai |", "|---|---|---|---|---|"]
    tgl = {t["id"]: t for t in tugas + milestone}
    isi += [f"| {i} | {nama[p]} | {x['nama']} | {tgl[p]['selesai']:%d %b} | {x['mulai']:%d %b} |"
            for i, (x, p) in enumerate(lain, 1)]
    (DIR / "ketergantungan.md").write_text("\n".join(isi) + "\n", encoding="utf8")
    return len(fs), len(lain)


if __name__ == "__main__":
    fase, tugas, milestone = data()
    tulis_csv(fase, tugas, milestone)
    n_fs, n_lain = tulis_ketergantungan(tugas, milestone)
    print(f"{len(fase)} fase, {len(tugas)} paket kerja, {len(milestone)} milestone; "
          f"{n_fs} ketergantungan Finish-to-Start, {n_lain} hubungan lain (hanya dicatat)")
    print(f"Mulai {min(t['mulai'] for t in tugas):%A %d %B %Y}; selesai {max(m['selesai'] for m in milestone):%A %d %B %Y}")
