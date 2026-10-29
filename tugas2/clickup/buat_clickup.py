"""Mengisi List ClickUp dengan WBS, jadwal, dan ketergantungan Tugas 2 lewat ClickUp API v2 (pilihan B).

Persiapan (lihat PETUNJUK_CLICKUP.md):
    1. Buat List kosong di ClickUp, salin List ID dari alamat web-nya.
    2. Buat API token pribadi (Settings → Apps → API Token).

Jalankan dari folder ini:
    export CLICKUP_TOKEN="pk_..."            # token TIDAK disimpan di berkas mana pun
    python3 buat_clickup.py --uji LIST_ID    # hanya menampilkan rencana, tidak mengirim apa pun
    python3 buat_clickup.py LIST_ID          # membuat tugas, subtask, lalu ketergantungan

Kalau berhenti di tengah jalan, jalankan ulang perintah yang sama: tugas yang sudah dibuat
tercatat di clickup_id.json dan tidak dibuat dua kali.
Hanya memakai pustaka standar Python (tidak perlu pip install).
"""
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from siapkan_clickup import data

API = "https://api.clickup.com/api/v2"
CATATAN = Path(__file__).resolve().parent / "clickup_id.json"
WIB = dt.timezone(dt.timedelta(hours=7))
JEDA = 0.7   # detik antarpermintaan; paket gratis dibatasi ±100 permintaan per menit


def ms(tanggal):
    """Tanggal → milidetik epoch, pukul 12.00 WIB, supaya tidak bergeser hari di zona waktu Asia."""
    return int(dt.datetime(tanggal.year, tanggal.month, tanggal.day, 12, tzinfo=WIB).timestamp() * 1000)


def kirim(token, metode, jalur, isi):
    req = urllib.request.Request(API + jalur, data=json.dumps(isi).encode(), method=metode,
                                 headers={"Authorization": token, "Content-Type": "application/json"})
    for _ in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(JEDA)
                return json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            if e.code == 429:            # terlalu banyak permintaan: tunggu lalu ulangi
                time.sleep(30)
                continue
            raise SystemExit(f"Gagal {metode} {jalur}: HTTP {e.code} {e.read().decode(errors='replace')}")
    raise SystemExit(f"Gagal {metode} {jalur}: batas permintaan terus terlampaui")


def isi_tugas(x, induk=None):
    isi = {"name": x["nama"], "description": x["deskripsi"], "tags": x["tag"],
           "start_date": ms(x["mulai"]), "start_date_time": False,
           "due_date": ms(x["selesai"]), "due_date_time": False}
    if induk:
        isi["parent"] = induk
    return isi


def main():
    argumen = [a for a in sys.argv[1:] if not a.startswith("--")]
    uji = "--uji" in sys.argv
    if len(argumen) != 1:
        raise SystemExit(__doc__)
    list_id = argumen[0]
    token = os.environ.get("CLICKUP_TOKEN", "")
    if not uji and not token.startswith("pk_"):
        raise SystemExit("Isi dulu variabel CLICKUP_TOKEN dengan API token pribadi (diawali pk_).")

    fase, tugas, milestone = data()
    sudah = json.loads(CATATAN.read_text()) if CATATAN.exists() else {}
    urutan = [(f, None) for f in fase] + [(t, f["id"]) for f in fase for t in f["anak"]] + [(m, None) for m in milestone]
    ketergantungan = [(x["id"], p) for x in tugas + milestone for p in x["pendahulu"]]
    jumlah_sudah = sum(1 for k in sudah if not k.startswith("_"))
    print(f"List {list_id}: {len(urutan)} tugas ({jumlah_sudah} sudah dibuat), {len(ketergantungan)} ketergantungan")

    # 1) Tugas: fase dulu (induk), lalu work package sebagai subtask, lalu milestone
    for x, induk in urutan:
        if x["id"] in sudah:
            continue
        if uji:
            print(f"  [uji] buat {x['nama']}  {x['mulai']} s.d. {x['selesai']}" + (f"  (subtask dari {induk})" if induk else ""))
            continue
        hasil = kirim(token, "POST", f"/list/{list_id}/task", isi_tugas(x, sudah[induk] if induk else None))
        sudah[x["id"]] = hasil["id"]
        CATATAN.write_text(json.dumps(sudah, indent=1))
        print(f"  dibuat: {x['nama']}")

    # 2) Ketergantungan Finish-to-Start: tugas menunggu pendahulunya
    selesai = set(tuple(k) for k in json.loads(CATATAN.read_text()).get("_ketergantungan", [])) if CATATAN.exists() else set()
    for tgs, pend in ketergantungan:
        if (tgs, pend) in selesai:
            continue
        if uji:
            print(f"  [uji] {tgs} menunggu {pend}")
            continue
        kirim(token, "POST", f"/task/{sudah[tgs]}/dependency", {"depends_on": sudah[pend]})
        selesai.add((tgs, pend))
        sudah["_ketergantungan"] = sorted(selesai)
        CATATAN.write_text(json.dumps(sudah, indent=1))
        print(f"  {tgs} menunggu {pend}")
    print("Selesai." if not uji else "Mode uji: tidak ada yang dikirim ke ClickUp.")


if __name__ == "__main__":
    main()
