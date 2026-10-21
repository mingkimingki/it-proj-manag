"""Membuat dua diagram untuk Tugas 1 (Analisis Distribusi Effort — Phoenix Pay).

Jalankan dari folder mana pun:
    python3 buat_diagram.py

Hasil (PNG, 200 dpi) disimpan di ../hasil/:
    Tugas1_DistribusiEffort_Phoenix_Diagram1_Effort.png
    Tugas1_DistribusiEffort_Phoenix_Diagram2_LiniWaktu.png

Sumber data:
- Crowe (2006), Alpha Project Managers — via slide Pertemuan 4 (slide 30).
- Estimasi Phoenix — draf_effort_phoenix.md, Bagian 4.3.
- Lini waktu — OAG Kanada (2018), Report 1, Exhibit 1.1 dan paragraf 1.32–1.102.
"""
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

HASIL = Path(__file__).resolve().parent.parent / "hasil"
HASIL.mkdir(exist_ok=True)

# Palet (divalidasi untuk buta warna, mode terang): slot kategorikal 1–3.
BIRU, ORANYE, TOSKA = "#2a78d6", "#eb6834", "#1baf7a"
KRITIS = "#d03b3b"  # warna status "critical" — hanya untuk titik kendali yang hilang
LATAR = "#fcfcfb"
TINTA, TINTA2, REDUP, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": REDUP,
    "axes.labelcolor": TINTA2,
    "xtick.color": TINTA2,
    "ytick.color": TINTA2,
    "figure.facecolor": LATAR,
    "axes.facecolor": LATAR,
    "savefig.facecolor": LATAR,
})


def diagram_effort():
    kelompok = ["Initiating", "Planning", "Executing", "Monitoring &\nControlling", "Closing"]
    seri = [
        ("Manajer proyek Alpha (Crowe, 2006)", [2, 21, 69, 5, 3], BIRU, None),
        ("Manajer proyek lain (Crowe, 2006)", [1, 11, 82, 4, 2], ORANYE, None),
        ("Phoenix Pay (estimasi penulis)", [2, 8, 86, 3, 1], TOSKA, "///"),
    ]
    lebar, celah = 0.26, 0.02
    fig, ax = plt.subplots(figsize=(10, 5.6), dpi=200)

    for i, (nama, nilai, warna, arsir) in enumerate(seri):
        xs = [k + (i - 1) * (lebar + celah) for k in range(len(kelompok))]
        bars = ax.bar(xs, nilai, width=lebar, color=warna, label=nama,
                      hatch=arsir, edgecolor=LATAR if arsir is None else "white",
                      linewidth=0 if arsir is None else 0.0, zorder=3)
        # Label langsung yang selektif: kelompok kunci (Planning, Executing, M&C).
        for k, (x, v) in enumerate(zip(xs, nilai)):
            if k in (1, 2, 3):
                ax.text(x, v + 1.2, f"{v}%", ha="center", va="bottom",
                        fontsize=9, color=TINTA, zorder=4)

    ax.set_xticks(range(len(kelompok)))
    ax.set_xticklabels(kelompok, color=TINTA)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Persentase waktu / effort (%)")
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)

    fig.suptitle("Distribusi effort per process group: Phoenix Pay vs patokan Crowe (2006)",
                 x=0.06, ha="left", fontsize=13, fontweight="bold", color=TINTA)
    ax.set_title("Phoenix: Planning dan Monitoring & Controlling lebih kecil, Executing lebih dominan",
                 loc="left", fontsize=10, color=TINTA2, pad=10)
    ax.legend(loc="upper left", frameon=False, fontsize=9, labelcolor=TINTA)
    fig.text(0.06, 0.015,
             "Sumber: Crowe (2006) via slide Pertemuan 4 ITPM (porsi waktu manajer proyek, data survei); "
             "Phoenix = estimasi penulis dari laporan OAG Kanada (2018), bukan data terukur.\n"
             "Arsiran garis miring menandai nilai estimasi. Nilai lengkap: Tabel 4.3 laporan.",
             fontsize=7.5, color=REDUP, ha="left", va="bottom")
    fig.tight_layout(rect=(0.02, 0.07, 1, 0.97))
    out = HASIL / "Tugas1_DistribusiEffort_Phoenix_Diagram1_Effort.png"
    fig.savefig(out)
    plt.close(fig)
    return out


def diagram_lini_waktu():
    # (tanggal titik, label, posisi teks (tanggal, y)) — tonggak dari OAG Exhibit 1.1
    tonggak = [
        (date(2009, 4, 1), "2009 (musim semi)\nBusiness case &\nusulan awal", (date(2009, 4, 1), 0.9)),
        (date(2010, 6, 1), "Jun–Okt 2010\nTender terbuka", (date(2010, 6, 1), -0.9)),
        (date(2011, 6, 1), "Jun 2011\nKontrak IBM", (date(2011, 6, 1), 0.9)),
        (date(2012, 12, 1), "Des 2012\nPendanaan disetujui,\nimplementasi dimulai", (date(2012, 12, 1), -0.9)),
        (date(2016, 2, 24), "24 Feb 2016\nGelombang 1\n(34 instansi)", (date(2015, 9, 15), 0.9)),
        (date(2016, 4, 21), "21 Apr 2016\nGelombang 2\n(67 instansi)", (date(2016, 10, 1), -0.9)),
    ]
    # Titik kendali yang hilang (warna status kritis + simbol ✕ + label). "\$" agar tidak dibaca sebagai rumus.
    hilang = [
        (date(2012, 4, 1), "Musim semi 2012: perkiraan biaya\nUS\\$274 jt vs anggaran US\\$155 jt →\nTIDAK ada perencanaan ulang;\n>100 fungsi dipangkas",
         (date(2011, 9, 1), -2.1)),
        (date(2015, 6, 1), "Jun 2015: uji coba (pilot)\nDIBATALKAN, tidak\ndijadwalkan ulang",
         (date(2013, 12, 1), 2.25)),
        (date(2016, 2, 11), "Feb 2016: saran Gartner (bertahap +\nparallel run) DIABAIKAN; keputusan\ngo-live TIDAK dicatat",
         (date(2014, 12, 1), -2.1)),
        (date(2016, 3, 23), "Jarak antargelombang\ndipadatkan 7 → 2 bulan",
         (date(2016, 9, 1), 2.25)),
    ]

    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=200)
    awal, akhir = date(2008, 12, 1), date(2017, 6, 30)
    ax.plot([awal, akhir], [0, 0], color=REDUP, linewidth=2, zorder=1)

    for t, label, (tx, ty) in tonggak:
        ax.annotate(label, xy=(t, 0), xytext=(tx, ty), ha="center",
                    va="bottom" if ty > 0 else "top", fontsize=8.5, color=TINTA,
                    arrowprops=dict(arrowstyle="-", color=REDUP, linewidth=1,
                                    shrinkA=2, shrinkB=5), zorder=2)
        ax.scatter([t], [0], s=70, color=BIRU, edgecolor=LATAR, linewidth=2, zorder=3)

    for t, label, (tx, ty) in hilang:
        ax.annotate("✕ " + label, xy=(t, 0), xytext=(tx, ty), ha="center",
                    va="bottom" if ty > 0 else "top", fontsize=8, color=TINTA,
                    bbox=dict(boxstyle="round,pad=0.35", facecolor="#fbeaea", edgecolor=KRITIS, linewidth=0.8),
                    arrowprops=dict(arrowstyle="-", color=KRITIS, linewidth=1, linestyle=(0, (3, 2)),
                                    shrinkA=0, shrinkB=5), zorder=2)
        ax.scatter([t], [0], s=90, marker="X", color=KRITIS, edgecolor=LATAR, linewidth=1.5, zorder=4)

    ax.set_xlim(awal, akhir)
    ax.set_ylim(-3.6, 3.4)
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.yaxis.set_visible(False)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_position(("data", -3.6))
    ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)

    fig.suptitle("Lini waktu proyek Phoenix Pay (2009–2016) dan titik kendali yang hilang",
                 x=0.04, ha="left", fontsize=13, fontweight="bold", color=TINTA)
    ax.set_title("● biru = tonggak proyek     ✕ merah = titik kendali (Planning / Monitoring & Controlling / phase gate) yang dilewati",
                 loc="left", fontsize=9, color=TINTA2, pad=8)
    fig.text(0.04, 0.012,
             "Sumber: Office of the Auditor General of Canada (2018), Report 1 — Exhibit 1.1 dan paragraf 1.32, 1.40, 1.76–1.78, 1.102.",
             fontsize=7.5, color=REDUP, ha="left", va="bottom")
    fig.tight_layout(rect=(0.01, 0.04, 1, 0.97))
    out = HASIL / "Tugas1_DistribusiEffort_Phoenix_Diagram2_LiniWaktu.png"
    fig.savefig(out)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for p in (diagram_effort(), diagram_lini_waktu()):
        print("dibuat:", p)
