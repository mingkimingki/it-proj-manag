"""Menggabungkan tangkapan layar Gantt ClickUp (../bukti/) menjadi dua gambar bersih untuk laporan.

Jalankan dari folder ini:
    python3 gabung_gantt.py

Hasil (di folder ini, aman di-commit karena sudah bersih):
    gantt_clickup_ringkas.png   55 baris: daftar bertingkat (akar, 5 cabang, 42 paket kerja) + M0–M6.
                                Untuk Bab 2.3.4 (halaman A4).
    gantt_clickup_utuh.png      97 baris: seluruh tampilan Gantt sesuai urutan gulir, termasuk daftar kedua
                                (42 paket kerja yang ditampilkan ulang oleh opsi "Separate" di ClickUp)
                                + M0–M6. Untuk lampiran (halaman lebih besar).

Pembersihan: ikon di tepi kiri dan bilah atas (nama workspace, foto profil) dipotong; tanda air
"Activate Windows" di kanan bawah dihapus (piksel abu-abu diganti warna latar di atasnya; batang merah dan label hitam tetap).

Tangkapan layar asli di ../bukti/ tidak diubah. Bila tangkapan layar diganti, periksa ulang URUTAN,
PERTAMA (posisi tengah baris pertama), dan pemakaian baris di bawah.
Hanya memerlukan Pillow.
"""
from pathlib import Path

from PIL import Image

DIR = Path(__file__).resolve().parent
BUKTI = DIR.parent / "bukti"
X0, X1 = 52, 1680            # potong ikon kiri dan ruang kosong setelah Juli
KEPALA = (125, 177)          # baris judul kolom dan nama bulan
JARAK = 28.8                 # tinggi satu baris tugas (piksel)
TANDA_AIR = (1590, 820, 1850, 875)

# Gambar sesuai urutan gulir: nama berkas dan posisi tengah baris pertamanya (piksel).
URUTAN = {
    "atas":    ("XJuG793.png", 190),   # akar, 1.1 … 1.3.9 (bertingkat)            25 baris
    "tengah":  ("3HlFuAu.png", 193),   # 1.3.9 … 1.5.5 (bertingkat), 1.1.1 kedua   25 baris
    "kedua_a": ("Y93OGRF.png", 190),   # 1.5.5, daftar kedua 1.1.1 … 1.3.12        25 baris
    "kedua_b": ("IxDUd58.png", 196),   # daftar kedua 1.3.12 … 1.5.5, M0 … M5      25 baris
    "bawah":   ("3NyOPqi.png", 193),   # daftar kedua 1.4.1 … 1.5.5, M0 … M6       24 baris
}


def buka(kunci):
    berkas, _ = URUTAN[kunci]
    im = Image.open(BUKTI / berkas).convert("RGB")
    px = im.load()
    x0, y0, x1, y1 = TANDA_AIR
    for x in range(x0, min(x1, im.width)):
        latar = px[x, y0 - 4]            # warna latar kolom ini, tepat di atas tanda air
        for y in range(y0, min(y1, im.height)):
            r, g, b = px[x, y]
            if max(r, g, b) - min(r, g, b) < 14 and 100 < r < 253:
                px[x, y] = latar
    return im


def baris(kunci, dari, sampai):
    """Potongan baris ke-`dari` sampai ke-`sampai` (0 = baris pertama gambar itu)."""
    _, pertama = URUTAN[kunci]
    atas = round(pertama + dari * JARAK - JARAK / 2)
    bawah = round(pertama + sampai * JARAK + JARAK / 2)
    return buka(kunci).crop((X0, atas, X1, bawah))


def susun(bagian, nama):
    kepala = buka("atas").crop((X0, KEPALA[0], X1, KEPALA[1]))
    bagian = [kepala] + bagian
    hasil = Image.new("RGB", (X1 - X0, sum(b.height for b in bagian)), "white")
    y = 0
    for b in bagian:
        hasil.paste(b, (0, y))
        y += b.height
    hasil.save(DIR / nama, optimize=True)
    return hasil.size


if __name__ == "__main__":
    ringkas = [baris("atas", 0, 23),     # akar … 1.3.8
               baris("tengah", 0, 23),   # 1.3.9 … 1.5.5
               baris("bawah", 17, 23)]   # M0 … M6
    utuh = [baris("atas", 0, 24),        # akar … 1.3.9
            baris("tengah", 1, 24),      # 1.3.10 … 1.1.1 (daftar kedua)
            baris("kedua_a", 2, 24),     # 1.1.2 … 1.3.12
            baris("kedua_b", 1, 24),     # 1.3.13 … M5
            baris("bawah", 23, 23)]      # M6
    print("gantt_clickup_ringkas.png", susun(ringkas, "gantt_clickup_ringkas.png"), "55 baris")
    print("gantt_clickup_utuh.png   ", susun(utuh, "gantt_clickup_utuh.png"), "97 baris")
