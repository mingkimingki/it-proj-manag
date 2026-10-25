"""Membuat diagram untuk Tugas 1 (Analisis Distribusi Effort — Phoenix Pay).

Jalankan dengan Python sistem (berisi matplotlib; venv mata kuliah tidak berisi matplotlib):
    /usr/bin/python3 buat_diagram.py

Hasil (PNG, 200 dpi) di ../hasil/:
    Tugas1_DistribusiEffort_Phoenix_Diagram1_Effort.png          (laporan)
    Tugas1_DistribusiEffort_Phoenix_Diagram2_LiniWaktu.png       (laporan)
    Tugas1_DistribusiEffort_Phoenix_Diagram1_Effort_slide.png    (slide: huruf besar, tanpa judul ganda)
    Tugas1_DistribusiEffort_Phoenix_Diagram2_LiniWaktu_slide.png (slide: huruf besar, istilah Indonesia)

Sumber data:
- Crowe (2006), Alpha Project Managers — via slide Pertemuan 4 (slide 30).
- Estimasi Phoenix — draf_effort_phoenix.md, Bagian 4.3.
- Lini waktu — OAG Kanada (2018), Report 1, Exhibit 1.1 dan paragraf 1.32–1.102.
  Semua angka uang dalam dolar Kanada (C$).
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
KRITIS = "#d03b3b"  # warna status "critical" — hanya untuk titik kendali yang dilewati
LATAR = "#fcfcfb"
TINTA, TINTA2, REDUP, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": REDUP,
    "axes.labelcolor": TINTA2,
    "xtick.color": TINTA2,
    "ytick.color": TINTA2,
    "figure.facecolor": LATAR,
    "axes.facecolor": LATAR,
    "savefig.facecolor": LATAR,
})

PREFIX = "Tugas1_DistribusiEffort_Phoenix_"


# ----------------------------------------------------------------------------- Diagram 1
def diagram_effort(mode):
    slide = mode == "slide"
    if slide:
        kelompok = ["Initiating\n(memulai)", "Planning\n(merencanakan)", "Executing\n(mengerjakan)",
                    "Monitoring &\nControlling\n(memeriksa)", "Closing\n(menutup)"]
        seri_nama = ["Manajer proyek terbaik (Crowe, 2006)", "Manajer proyek lain (Crowe, 2006)",
                     "Phoenix Pay (perkiraan penulis)"]
    else:
        kelompok = ["Initiating", "Planning", "Executing", "Monitoring &\nControlling", "Closing"]
        seri_nama = ["Manajer proyek Alpha (Crowe, 2006)", "Manajer proyek lain (Crowe, 2006)",
                     "Phoenix Pay (estimasi penulis)"]
    seri = [
        (seri_nama[0], [2, 21, 69, 5, 3], BIRU, None),
        (seri_nama[1], [1, 11, 82, 4, 2], ORANYE, None),
        (seri_nama[2], [2, 8, 86, 3, 1], TOSKA, "///"),
    ]
    fs = 15 if slide else 10
    lebar, celah = 0.26, 0.02
    fig, ax = plt.subplots(figsize=(11, 6.2) if slide else (10, 5.6), dpi=200)

    for i, (nama, nilai, warna, arsir) in enumerate(seri):
        xs = [k + (i - 1) * (lebar + celah) for k in range(len(kelompok))]
        ax.bar(xs, nilai, width=lebar, color=warna, label=nama, hatch=arsir,
               edgecolor=LATAR if arsir is None else "white", linewidth=0, zorder=3)
        for k, (x, v) in enumerate(zip(xs, nilai)):
            if k in (1, 2, 3):  # label langsung selektif: kelompok kunci
                ax.text(x, v + 1.2, f"{v}%", ha="center", va="bottom",
                        fontsize=fs - 1 if slide else 9, color=TINTA, zorder=4)

    ax.set_xticks(range(len(kelompok)))
    ax.set_xticklabels(kelompok, color=TINTA, fontsize=fs - 1 if slide else fs)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Porsi perhatian manajemen proyek (%)", fontsize=fs - 1 if slide else fs)
    ax.tick_params(axis="y", labelsize=fs - 2 if slide else 9, length=0)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.legend(loc="upper left", frameon=False, fontsize=fs - 2 if slide else 9, labelcolor=TINTA)

    if slide:
        fig.text(0.01, 0.01, "Arsiran = perkiraan penulis dari laporan OAG Kanada (2018), bukan hasil ukur.",
                 fontsize=11, color=REDUP, ha="left", va="bottom")
        fig.tight_layout(rect=(0, 0.04, 1, 1))
        out = HASIL / f"{PREFIX}Diagram1_Effort_slide.png"
    else:
        fig.suptitle("Distribusi effort per process group: Phoenix Pay vs patokan Crowe (2006)",
                     x=0.06, ha="left", fontsize=13, fontweight="bold", color=TINTA)
        ax.set_title("Phoenix: Planning dan Monitoring & Controlling lebih kecil, Executing lebih dominan",
                     loc="left", fontsize=10, color=TINTA2, pad=10)
        fig.text(0.06, 0.015,
                 "Sumber: Crowe (2006) via slide Pertemuan 4 ITPM (porsi waktu manajer proyek, data survei); "
                 "Phoenix = estimasi penulis dari laporan OAG Kanada (2018), bukan data terukur.\n"
                 "Arsiran garis miring menandai nilai estimasi. Nilai lengkap: Tabel 1 laporan.",
                 fontsize=7.5, color=REDUP, ha="left", va="bottom")
        fig.tight_layout(rect=(0.02, 0.07, 1, 0.97))
        out = HASIL / f"{PREFIX}Diagram1_Effort.png"
    fig.savefig(out)
    plt.close(fig)
    return out


# ----------------------------------------------------------------------------- Diagram 2
def _tonggak(ax, t, label, tx, ty, fs):
    ax.annotate(label, xy=(t, 0), xytext=(tx, ty), ha="center", va="bottom" if ty > 0 else "top",
                fontsize=fs, color=TINTA,
                arrowprops=dict(arrowstyle="-", color=REDUP, linewidth=1, shrinkA=2, shrinkB=5), zorder=2)
    ax.scatter([t], [0], s=70, color=BIRU, edgecolor=LATAR, linewidth=2, zorder=3)


def _dilewati(ax, t, label, tx, ty, fs):
    ax.annotate("✕ " + label, xy=(t, 0), xytext=(tx, ty), ha="center", va="bottom" if ty > 0 else "top",
                fontsize=fs, color=TINTA,
                bbox=dict(boxstyle="round,pad=0.35", facecolor="#fbeaea", edgecolor=KRITIS, linewidth=0.8),
                arrowprops=dict(arrowstyle="-", color=KRITIS, linewidth=1, linestyle=(0, (3, 2)),
                                shrinkA=0, shrinkB=5), zorder=2)
    ax.scatter([t], [0], s=90, marker="X", color=KRITIS, edgecolor=LATAR, linewidth=1.5, zorder=4)


def _sumbu(ax, awal, akhir, ylim):
    ax.plot([awal, akhir], [0, 0], color=REDUP, linewidth=2, zorder=1)
    ax.set_xlim(awal, akhir)
    ax.set_ylim(*ylim)
    ax.yaxis.set_visible(False)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_position(("data", ylim[0]))
    ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)


def diagram_lini_waktu(mode):
    slide = mode == "slide"
    fs = 12 if slide else 8.5
    fs_kotak = 11.5 if slide else 8
    ylim = (-3.4, 3.4)

    if slide:
        T = {
            "bc": "2009\nUsulan & business case", "tender": "2010\nTender", "ibm": "Jun 2011\nKontrak IBM",
            "impl": "Des 2012\nMulai dibangun",
            "x2012": "2012: biaya C\\$274 jt vs\nanggaran C\\$155 jt →\nTIDAK direncanakan ulang;\n>100 fitur dibuang",
            "x2015": "Jun 2015: uji coba\nDIBATALKAN",
            "g": "11 Feb: saran Gartner\n(bertahap + sistem lama\ntetap jalan) DIABAIKAN",
            "w": "18 Feb: dilaporkan \"siap\";\nkeputusan mulai pakai\nTIDAK dicatat",
            "gel1": "24 Feb\nTahap 1\n(34 lembaga)", "gel2": "21 Apr\nTahap 2\n(67 lembaga)",
            "jeda": "jeda hanya 2 bulan (rencana 7)",
        }
    else:
        T = {
            "bc": "2009 (musim semi)\nBusiness case &\nusulan awal", "tender": "Jun–Okt 2010\nTender terbuka",
            "ibm": "Jun 2011\nKontrak IBM", "impl": "Des 2012\nPendanaan disetujui,\nimplementasi dimulai",
            "x2012": "Musim semi 2012: perkiraan biaya\nC\\$274 jt vs anggaran C\\$155 jt →\nTIDAK ada perencanaan ulang;\n>100 fungsi dipangkas",
            "x2015": "Jun 2015: uji coba (pilot)\nDIBATALKAN, tidak\ndijadwalkan ulang",
            "g": "11 Feb: saran Gartner\n(bertahap + parallel run)\nDIABAIKAN",
            "w": "18 Feb: wamen diberi tahu\n\"semua siap\"; keputusan\ngo-live TIDAK dicatat",
            "gel1": "24 Feb\nGelombang 1\n(34 instansi)", "gel2": "21 Apr\nGelombang 2\n(67 instansi)",
            "jeda": "jarak antargelombang 2 bulan (rencana 7)",
        }

    fig, (kiri, kanan) = plt.subplots(1, 2, figsize=(13, 6.4) if slide else (11.5, 5.8), dpi=200,
                                      gridspec_kw={"width_ratios": [1.55, 1], "wspace": 0.08})

    # --- Panel kiri: 2009–2015 (skala tahunan)
    _sumbu(kiri, date(2008, 11, 1), date(2015, 12, 31), ylim)
    _tonggak(kiri, date(2009, 4, 1), T["bc"], date(2009, 11, 1) if slide else date(2009, 4, 1), 0.9, fs)
    _tonggak(kiri, date(2010, 6, 1), T["tender"], date(2010, 6, 1), -0.9, fs)
    _tonggak(kiri, date(2011, 6, 1), T["ibm"], date(2011, 6, 1), 0.9, fs)
    _tonggak(kiri, date(2012, 12, 1), T["impl"], date(2013, 3, 1), -0.9, fs)
    _dilewati(kiri, date(2012, 4, 1), T["x2012"], date(2011, 6, 1), -2.0, fs_kotak)
    _dilewati(kiri, date(2015, 6, 1), T["x2015"], date(2014, 3, 1), 2.0, fs_kotak)
    kiri.xaxis.set_major_locator(mdates.YearLocator())
    kiri.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    kiri.tick_params(axis="x", labelsize=fs)
    kiri.set_title("2009–2015", loc="left", fontsize=fs + 1, color=TINTA2, pad=6)

    # --- Panel kanan: Jan–Apr 2016 (diperbesar, skala mingguan)
    _sumbu(kanan, date(2016, 1, 25), date(2016, 5, 8), ylim)
    _dilewati(kanan, date(2016, 2, 11), T["g"], date(2016, 2, 22), 2.0, fs_kotak)
    _dilewati(kanan, date(2016, 2, 18), T["w"], date(2016, 2, 25), -2.0, fs_kotak)
    _tonggak(kanan, date(2016, 2, 24), T["gel1"], date(2016, 3, 12), 0.75, fs)
    _tonggak(kanan, date(2016, 4, 21), T["gel2"], date(2016, 4, 21), 0.75, fs)
    # Rentang antar tahap (bukan satu titik): kurung dari 24 Feb ke 21 Apr
    y = -0.6
    kanan.annotate("", xy=(date(2016, 2, 24), y), xytext=(date(2016, 4, 21), y),
                   arrowprops=dict(arrowstyle="|-|", color=KRITIS, linewidth=1.5, mutation_scale=6))
    kanan.text(date(2016, 2, 27), y - 0.12, T["jeda"], ha="left", va="top",
               fontsize=fs_kotak, color=KRITIS, fontweight="bold")
    kanan.xaxis.set_major_locator(mdates.MonthLocator())
    kanan.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    kanan.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    kanan.tick_params(axis="x", labelsize=fs - 1)
    kanan.set_title("Jan–Apr 2016 (diperbesar)", loc="left", fontsize=fs + 1, color=TINTA2, pad=6)
    kanan.set_facecolor("#f6f8fb")

    legenda = ("● biru = kejadian proyek     ✕ merah = pemeriksaan yang dilewati" if slide else
               "● biru = tonggak proyek     ✕ merah = titik kendali (Planning / Monitoring & Controlling / phase gate) yang dilewati")
    if slide:
        fig.text(0.01, 0.965, legenda, fontsize=12, color=TINTA2, ha="left", va="top")
        fig.text(0.01, 0.01, "Sumber: OAG Kanada (2018). C$ = dolar Kanada.", fontsize=10.5, color=REDUP)
        fig.subplots_adjust(left=0.02, right=0.99, top=0.86, bottom=0.08)
        out = HASIL / f"{PREFIX}Diagram2_LiniWaktu_slide.png"
    else:
        fig.suptitle("Lini waktu proyek Phoenix Pay (2009–2016) dan titik kendali yang dilewati",
                     x=0.02, ha="left", fontsize=13, fontweight="bold", color=TINTA)
        fig.text(0.02, 0.905, legenda, fontsize=9, color=TINTA2, ha="left", va="top")
        fig.text(0.02, 0.012,
                 "Sumber: Office of the Auditor General of Canada (2018), Report 1 — Exhibit 1.1 dan paragraf "
                 "1.32, 1.40, 1.76–1.78, 1.101–1.102. C$ = dolar Kanada.",
                 fontsize=7.5, color=REDUP, ha="left", va="bottom")
        fig.subplots_adjust(left=0.02, right=0.99, top=0.82, bottom=0.09)
        out = HASIL / f"{PREFIX}Diagram2_LiniWaktu.png"
    fig.savefig(out)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for m in ("laporan", "slide"):
        for p in (diagram_effort(m), diagram_lini_waktu(m)):
            print("dibuat:", p)
