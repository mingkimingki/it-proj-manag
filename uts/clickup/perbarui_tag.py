"""Menyesuaikan tag "jalur-kritis" dan deskripsi tugas di ClickUp setelah jalur kritis Tabel 2.13 diperbaiki.

Membaca clickup_id.json (tugas yang sudah dibuat buat_clickup.py) dan data terbaru dari siapkan_clickup.py, lalu:
    - memperbarui deskripsi setiap paket kerja (baris "Jalur kritis." ikut menyesuaikan);
    - menambah tag "jalur-kritis" pada paket kerja kritis dan menghapusnya dari yang tidak kritis.
Tanggal, nama, dan ketergantungan tidak diubah.

Jalankan dari folder ini:
    export CLICKUP_TOKEN="pk_..."        # token TIDAK disimpan di berkas mana pun
    python3 perbarui_tag.py --uji         # hanya menampilkan rencana
    python3 perbarui_tag.py               # mengirim perubahan (± 84 permintaan, ± 1 menit)
Aman dijalankan berulang kali.
"""
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
TAG = "jalur-kritis"
JEDA = 0.7


def kirim(token, metode, jalur, isi=None, boleh_404=False):
    req = urllib.request.Request(API + jalur, data=json.dumps(isi).encode() if isi is not None else None, method=metode,
                                 headers={"Authorization": token, "Content-Type": "application/json"})
    for _ in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                time.sleep(JEDA)
                return
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(30)
                continue
            if boleh_404 and e.code == 404:
                time.sleep(JEDA)
                return
            raise SystemExit(f"Gagal {metode} {jalur}: HTTP {e.code} {e.read().decode(errors='replace')}")
    raise SystemExit(f"Gagal {metode} {jalur}: batas permintaan terus terlampaui")


def main():
    uji = "--uji" in sys.argv
    token = os.environ.get("CLICKUP_TOKEN", "")
    if not uji and not token.startswith("pk_"):
        raise SystemExit("Isi dulu variabel CLICKUP_TOKEN dengan API token pribadi (diawali pk_).")
    if not CATATAN.exists():
        raise SystemExit("clickup_id.json tidak ditemukan; jalankan buat_clickup.py lebih dulu.")
    sudah = json.loads(CATATAN.read_text())
    _, tugas, _ = data()
    kritis = [t for t in tugas if TAG in t["tag"]]
    print(f"{len(tugas)} paket kerja, {len(kritis)} kritis: {', '.join(t['kode'] for t in kritis)}")
    for t in tugas:
        tid = sudah.get(t["id"])
        if not tid:
            print(f"  lewati {t['kode']}: belum ada di clickup_id.json")
            continue
        aksi = "tambah tag" if TAG in t["tag"] else "hapus tag"
        if uji:
            print(f"  [uji] {t['kode']}: perbarui deskripsi; {aksi}")
            continue
        kirim(token, "PUT", f"/task/{tid}", {"description": t["deskripsi"]})
        if TAG in t["tag"]:
            kirim(token, "POST", f"/task/{tid}/tag/{TAG}", {})
        else:
            kirim(token, "DELETE", f"/task/{tid}/tag/{TAG}", boleh_404=True)
        print(f"  {t['kode']}: deskripsi diperbarui; {aksi}")
    print("Selesai." if not uji else "Mode uji: tidak ada yang dikirim ke ClickUp.")


if __name__ == "__main__":
    main()
