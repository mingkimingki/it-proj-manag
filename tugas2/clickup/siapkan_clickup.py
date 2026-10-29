"""Menyiapkan bahan ClickUp dari laporan Tugas 2 (../draf/laporan_tugas2.md).

Jalankan:
    python3 siapkan_clickup.py

Hasil (di folder ini):
    clickup_import_spdc.csv   berkas impor spreadsheet ClickUp (pilihan A)
    ketergantungan.md         daftar ketergantungan untuk dibuat manual di Gantt (pilihan A)

Fungsi data() juga dipakai buat_clickup.py (pilihan B, lewat API).
Hari kerja ke-n diubah ke tanggal kalender: mulai Senin 4 Januari 2027, Senin–Jumat, hari libur tidak dihitung.
"""
import csv
import datetime as dt
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
SUMBER = DIR.parent / "draf" / "laporan_tugas2.md"
MULAI = dt.date(2027, 1, 4)
NAMA_LIST = "SPDC - Sistem Peringatan Dini Cuaca Publik"
# 1.1.2 dan 1.1.3 berjalan sepanjang proyek (tidak ada di tabel jadwal): dari M1 sampai serah terima (M5)
SEPANJANG_PROYEK = {"1.1.2": ("M1", "M5"), "1.1.3": ("M1", "M5")}


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


def hari_kerja(n):
    """Tanggal kalender untuk hari kerja ke-n (n = 1 adalah tanggal MULAI)."""
    d, hitung = MULAI, 1
    while hitung < n:
        d += dt.timedelta(days=1)
        if d.weekday() < 5:
            hitung += 1
    return d


def data():
    md = SUMBER.read_text(encoding="utf8")
    jadwal = {}
    for c in ambil_tabel(md, "| Kode | Aktivitas | O |"):
        kode = polos(c[0])
        jadwal[kode] = dict(dur=int(polos(c[6])), pendahulu=[x.strip() for x in polos(c[7]).split(",") if x.strip() not in ("", "–")],
                            es=int(c[8]), ef=int(c[9]), fl=int(polos(c[12])), nama=polos(c[1]))
    for kode, (dari, sampai) in SEPANJANG_PROYEK.items():
        jadwal[kode] = dict(dur=None, pendahulu=[], es=jadwal[dari]["ef"], ef=jadwal[sampai]["ef"], fl=None, nama=None)

    fase, tugas = [], []
    for c in ambil_tabel(md, "| Kode | Work package | Uraian |"):
        kode, nama = polos(c[0]), polos(c[1])
        if kode.count(".") == 1:
            fase.append(dict(kode=kode, nama=nama, anak=[]))
            continue
        j = jadwal[kode]
        tag = [polos(c[4]).lower()] + (["jalur-kritis"] if j["fl"] == 0 else [])
        ket = "Berjalan sepanjang proyek." if j["dur"] is None else \
            f"Durasi: {j['dur']} hari kerja. Pendahulu: {', '.join(j['pendahulu']) or '-'}. Float: {j['fl']} hari."
        t = dict(id=f"WBS-{kode}", kode=kode, nama=f"{kode} {nama}",
                 deskripsi=f"{polos(c[2])}\n\nHasil: {polos(c[3])}\nPenanggung jawab: {polos(c[4])}\n{ket}",
                 mulai=hari_kerja(j["es"] + 1), selesai=hari_kerja(j["ef"]), tag=tag,
                 pendahulu=[(f"WBS-{p}" if p[0].isdigit() else p) for p in j["pendahulu"]])
        tugas.append(t)
        fase[-1]["anak"].append(t)
    for f in fase:
        f.update(id=f"WBS-{f['kode']}", nama=f"{f['kode']} {f['nama']}",
                 deskripsi=f"Fase {f['kode']} ({len(f['anak'])} work package).",
                 mulai=min(t["mulai"] for t in f["anak"]), selesai=max(t["selesai"] for t in f["anak"]), tag=["fase"])
    milestone = []
    for kode, j in jadwal.items():
        if kode.startswith("M"):
            tgl = hari_kerja(j["ef"])
            milestone.append(dict(id=kode, kode=kode, nama=f"◆ {kode} {j['nama'].lstrip('◆ ')}",
                                  deskripsi=f"Milestone (durasi 0), akhir hari kerja ke-{j['ef']}.",
                                  mulai=tgl, selesai=tgl, tag=["milestone", "jalur-kritis"] if j["fl"] == 0 else ["milestone"],
                                  pendahulu=[(f"WBS-{p}" if p[0].isdigit() else p) for p in j["pendahulu"]]))
    return fase, tugas, milestone


def tulis_csv(fase, tugas, milestone):
    with open(DIR / "clickup_import_spdc.csv", "w", newline="", encoding="utf-8") as f:
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
    baris = [(x, p) for x in tugas + milestone for p in x["pendahulu"]]
    baris.sort(key=lambda b: (b[0]["mulai"], b[0]["id"]))
    isi = ["# Daftar ketergantungan (untuk dibuat manual di Gantt ClickUp)", "",
           f"Semua hubungan berjenis **Finish-to-Start**: tugas di kolom kanan baru boleh mulai setelah tugas di kolom kiri selesai. "
           f"Jumlah: **{len(baris)} ketergantungan**. Urutan mengikuti tanggal mulai, jadi bisa dikerjakan dari atas ke bawah.", "",
           "Cara membuat di Gantt ClickUp: arahkan kursor ke batang tugas di kolom **Pendahulu**, tarik titik di ujung kanannya "
           "ke batang tugas di kolom **Tugas**. Centang kolom terakhir setelah selesai.", "",
           "| No | Pendahulu (selesai dulu) | Tugas (mulai sesudahnya) | ✓ |", "|---|---|---|---|"]
    for i, (x, p) in enumerate(baris, 1):
        isi.append(f"| {i} | {nama[p]} | {x['nama']} | ☐ |")
    (DIR / "ketergantungan.md").write_text("\n".join(isi) + "\n", encoding="utf8")
    return len(baris)


if __name__ == "__main__":
    fase, tugas, milestone = data()
    tulis_csv(fase, tugas, milestone)
    n = tulis_ketergantungan(tugas, milestone)
    print(f"{len(fase)} fase, {len(tugas)} work package, {len(milestone)} milestone, {n} ketergantungan")
    print(f"Mulai {MULAI:%A %d %B %Y}; selesai {max(m['selesai'] for m in milestone):%A %d %B %Y}")
