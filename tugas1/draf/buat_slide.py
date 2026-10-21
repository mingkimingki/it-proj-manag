"""Membuat slide presentasi Tugas 1 (Analisis Distribusi Effort — Phoenix Pay), 10 menit.

Versi untuk audiens awam: istilah diganti kata sehari-hari (istilah asli dalam kurung),
ada slide "Istilah kunci", kotak "Istilah di slide ini", dan slide cadangan "Daftar istilah".

Jalankan dengan venv mata kuliah (berisi python-pptx):
    ../../.venv/bin/python buat_slide.py

Hasil: ../hasil/Tugas1_DistribusiEffort_Phoenix_Slide.pptx
Diagram diambil dari ../hasil/*.png (buat dulu dengan buat_diagram.py).
"""
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

HASIL = Path(__file__).resolve().parent.parent / "hasil"
OUT = HASIL / "Tugas1_DistribusiEffort_Phoenix_Slide.pptx"

PUTIH = RGBColor(0xFF, 0xFF, 0xFF)
NAVY = RGBColor(0x1B, 0x2A, 0x4A)
TINTA = RGBColor(0x1F, 0x1F, 0x1F)
ABU = RGBColor(0x52, 0x51, 0x4E)
REDUP = RGBColor(0x89, 0x87, 0x81)
BIRU = RGBColor(0x2A, 0x78, 0xD6)
BIRU_MUDA = RGBColor(0xEA, 0xF2, 0xFC)
MERAH = RGBColor(0xD0, 0x3B, 0x3B)
MERAH_MUDA = RGBColor(0xFB, 0xEA, 0xEA)
ABU_MUDA = RGBColor(0xF3, 0xF3, 0xF1)   # latar kotak "Istilah"
JUDUL_FONT, ISI_FONT = "Cambria", "Calibri"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
KOSONG = prs.slide_layouts[6]
nomor = {"n": 0}


def teks(slide, x, y, w, h, isi, size=16, color=TINTA, bold=False, italic=False,
         font=ISI_FONT, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space_after=6):
    """isi: str, atau list paragraf; tiap paragraf str atau list run (teks, {opsi})."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for side in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, side, Inches(0.05))
    paragraf = isi if isinstance(isi, list) else [isi]
    for i, par in enumerate(paragraf):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        runs = par if isinstance(par, list) else [(par, {})]
        for t, opt in runs:
            r = p.add_run()
            r.text = t
            f = r.font
            f.name = opt.get("font", font)
            f.size = Pt(opt.get("size", size))
            f.bold = opt.get("bold", bold)
            f.italic = opt.get("italic", italic)
            f.color.rgb = opt.get("color", color)
    return tb


def kotak(slide, x, y, w, h, fill=BIRU_MUDA, bentuk=MSO_SHAPE.ROUNDED_RECTANGLE, line=None, radius=0.08):
    s = slide.shapes.add_shape(bentuk, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(1.25)
    s.shadow.inherit = False
    if bentuk == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    return s


def lingkaran_nomor(slide, x, y, angka, d=0.55, fill=BIRU, size=18):
    c = kotak(slide, x, y, d, d, fill=fill, bentuk=MSO_SHAPE.OVAL)
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(angka)
    r.font.name, r.font.size, r.font.bold, r.font.color.rgb = ISI_FONT, Pt(size), True, PUTIH
    return c


def istilah(slide, x, y, w, h, pasangan, size=13):
    """Kotak 'Istilah di slide ini': pasangan = [(istilah, penjelasan), ...]."""
    kotak(slide, x, y, w, h, fill=ABU_MUDA, radius=0.06)
    baris = [[("Istilah di slide ini", {"bold": True, "color": NAVY})]]
    for t, d in pasangan:
        baris.append([(t + ": ", {"bold": True}), (d, {})])
    teks(slide, x + 0.15, y + 0.08, w - 0.3, h - 0.16, baris, size=size, color=TINTA, space_after=3)


def slide_baru(judul=None, catatan="", tampil_nomor=True):
    s = prs.slides.add_slide(KOSONG)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = PUTIH
    nomor["n"] += 1
    if judul:
        teks(s, 0.6, 0.35, 12.1, 0.9, judul, size=32, bold=True, color=NAVY, font=JUDUL_FONT,
             anchor=MSO_ANCHOR.MIDDLE)
    if tampil_nomor:
        teks(s, 12.2, 7.0, 0.8, 0.35, str(nomor["n"]), size=11, color=REDUP, align=PP_ALIGN.RIGHT)
    if catatan:
        s.notes_slide.notes_text_frame.text = catatan
    return s


# =============== 1. Judul ===============
s = slide_baru(tampil_nomor=False, catatan=(
    "Selamat pagi/siang. Saya akan membahas mengapa sebuah proyek sistem gaji pemerintah Kanada, bernama Phoenix, "
    "gagal. Fokusnya bagaimana tenaga dan waktu proyek, yang disebut effort, dibagi ke lima kelompok kegiatan "
    "pengelolaan proyek: memulai, merencanakan, mengerjakan, memeriksa, dan menutup."))
teks(s, 0.9, 1.3, 11.5, 0.5, "TUGAS 1 — IT PROJECT MANAGEMENT", size=16, bold=True, color=BIRU)
teks(s, 0.9, 1.85, 11.5, 1.5, ["Analisis Distribusi Effort Proyek:", "Studi Kasus Phoenix Pay System (Kanada)"],
     size=36, bold=True, color=NAVY, font=JUDUL_FONT, space_after=0)
teks(s, 0.9, 3.45, 11.5, 0.8,
     "Mengapa sistem gaji untuk 290.000 pegawai pemerintah gagal, dilihat dari pembagian tenaga dan waktu (effort) proyek",
     size=18, italic=True, color=ABU)
for i, (nama, arti) in enumerate([("Initiating", "memulai"), ("Planning", "merencanakan"),
                                  ("Executing", "mengerjakan"), ("Monitoring &\nControlling", "memeriksa"),
                                  ("Closing", "menutup")]):
    x = 0.9 + i * 1.75
    lingkaran_nomor(s, x, 4.75, i + 1, d=0.5, size=16)
    teks(s, x - 0.4, 5.3, 1.3, 0.9, [nama, [(arti, {"italic": True, "color": BIRU})]],
         size=12, color=ABU, align=PP_ALIGN.CENTER, space_after=0)
teks(s, 9.9, 4.7, 3.0, 1.8, [
    [("Nama: ", {"bold": True}), ("[isi nama]", {"color": MERAH})],
    [("NIM: ", {"bold": True}), ("[isi NIM]", {"color": MERAH})],
    "S2 Informatika — Universitas Amikom Yogyakarta",
    "Dosen: Emha Taufiq Luthfi, Ph.D.",
], size=13, color=TINTA, space_after=2)

# =============== 2. Apa & mengapa ===============
s = slide_baru("Apa yang dianalisis dan mengapa Phoenix?", catatan=(
    "Pertanyaannya: bagaimana tenaga dan waktu proyek dibagi, apakah seimbang, dan apakah ketidakseimbangan itu "
    "menjelaskan kegagalan. Saya memilih Phoenix karena tiga hal: ada pemeriksaan resmi dari lembaga pemeriksa negara "
    "Kanada, setara BPK; pemeriksa memakai buku standar PMBOK yang juga materi kuliah kita; dan laporannya berisi "
    "angka konkret."))
kotak(s, 0.6, 1.55, 5.2, 4.0, fill=BIRU_MUDA)
teks(s, 0.95, 1.85, 4.6, 0.5, "PERTANYAAN ANALISIS", size=14, bold=True, color=BIRU)
teks(s, 0.95, 2.4, 4.6, 3.0, [
    "Bagaimana tenaga dan waktu (effort) proyek dibagi ke lima kelompok kegiatan?",
    "Apakah pembagiannya seimbang?",
    "Apakah ketidakseimbangan itu menjelaskan kegagalan proyek?",
], size=18, color=TINTA, space_after=14)
alasan = [
    ("Diperiksa resmi", "OAG, lembaga pemeriksa keuangan negara Kanada (seperti BPK), menerbitkan laporan lengkap pada 2018."),
    ("Kerangka sama dengan kuliah", "Pemeriksa memakai PMBOK Guide, buku standar pengelolaan proyek yang juga materi kuliah."),
    ("Angkanya konkret", "Ada data berapa fitur dibuang, berapa pengujian gagal, dan berapa bulan jadwal dipadatkan."),
]
for i, (h, d) in enumerate(alasan):
    y = 1.6 + i * 1.65
    lingkaran_nomor(s, 6.3, y + 0.1, i + 1)
    teks(s, 7.05, y, 5.7, 0.45, h, size=20, bold=True, color=NAVY)
    teks(s, 7.05, y + 0.5, 5.7, 1.0, d, size=16, color=ABU)

# =============== 3. Istilah kunci (baru) ===============
s = slide_baru("Enam istilah kunci", catatan=(
    "Sebelum masuk ke kasus, enam istilah yang akan sering muncul. Effort adalah tenaga dan waktu. Process group adalah "
    "lima kelompok kegiatan pengelolaan proyek. Pilot adalah uji coba di satu tempat dulu. Go-live adalah saat sistem "
    "mulai dipakai sungguhan. Waterfall berarti dikerjakan berurutan dan diluncurkan sekaligus, sedangkan Agile "
    "dikerjakan dalam putaran pendek yang hasilnya langsung dicoba pengguna."))
kunci = [
    ("Effort", "Tenaga dan waktu yang dipakai untuk mengerjakan proyek"),
    ("Process group", "Lima kelompok kegiatan mengelola proyek: memulai, merencanakan, mengerjakan, memeriksa, menutup"),
    ("Uji coba (pilot)", "Mencoba sistem baru di satu tempat dulu sebelum dipakai semua"),
    ("Go-live", "Saat sistem baru mulai dipakai sungguhan"),
    ("Waterfall", "Dikerjakan berurutan: rencana lengkap, bangun, uji, lalu diluncurkan sekaligus"),
    ("Agile", "Dikerjakan dalam putaran pendek (1–4 minggu); tiap putaran langsung dicoba pengguna"),
]
for i, (h, d) in enumerate(kunci):
    x = 0.6 + (i % 3) * 4.1
    y = 1.5 + (i // 3) * 2.6
    kotak(s, x, y, 3.9, 2.35, fill=BIRU_MUDA)
    teks(s, x + 0.3, y + 0.25, 3.3, 0.55, h, size=22, bold=True, color=BIRU, font=JUDUL_FONT)
    teks(s, x + 0.3, y + 0.9, 3.3, 1.35, d, size=16, color=TINTA)

# =============== 4. Teori ===============
s = slide_baru("Lima kelompok kegiatan dan angka pembanding", catatan=(
    "Menurut PMBOK, ada lima kelompok kegiatan. Yang penting: kelimanya berjalan bersamaan sepanjang proyek, bukan "
    "bergiliran. Kegiatan memeriksa berjalan dari awal sampai akhir. Sebagai pembanding, saya pakai data Crowe dari slide "
    "kuliah: manajer proyek terbaik memakai 21 persen waktunya untuk merencanakan, manajer lain hanya 11 persen dan "
    "lebih banyak mengerjakan. Ini data survei, jadi hanya menunjukkan kecenderungan."))
kelompok = [
    ("Initiating", "memulai", "Memutuskan proyek dikerjakan dan tujuannya"),
    ("Planning", "merencanakan", "Apa, kapan, berapa biaya, apa risikonya"),
    ("Executing", "mengerjakan", "Membangun sistem sesuai rencana"),
    ("Monitoring &\nControlling", "memeriksa", "Memeriksa, menguji, memperbaiki penyimpangan"),
    ("Closing", "menutup", "Menyerahkan hasil, mengevaluasi"),
]
for i, (h, arti, d) in enumerate(kelompok):
    x = 0.6 + i * 2.45
    kotak(s, x, 1.45, 2.25, 2.55, fill=BIRU_MUDA)
    lingkaran_nomor(s, x + 0.2, 1.6, i + 1, d=0.45, size=15)
    teks(s, x + 0.2, 2.1, 1.95, 0.8, [h, [(arti, {"italic": True, "color": BIRU, "bold": False, "size": 14})]],
         size=15, bold=True, color=NAVY, space_after=0)
    teks(s, x + 0.2, 3.0, 1.95, 0.95, d, size=13, color=ABU, space_after=0)
teks(s, 0.6, 4.1, 12.1, 0.45,
     "Kelimanya berjalan bersamaan sepanjang proyek, bukan bergiliran; kegiatan memeriksa berlangsung dari awal sampai akhir.",
     size=15, italic=True, color=ABU)
tbl = s.shapes.add_table(3, 6, Inches(0.6), Inches(4.7), Inches(8.6), Inches(1.5)).table
isi_tbl = [["Porsi waktu manajer proyek", "Mulai", "Rencana", "Kerja", "Periksa", "Tutup"],
           ["Manajer proyek terbaik (Alpha)", "2%", "21%", "69%", "5%", "3%"],
           ["Manajer proyek lain", "1%", "11%", "82%", "4%", "2%"]]
for j, w in enumerate([3.3, 1.06, 1.06, 1.06, 1.06, 1.06]):
    tbl.columns[j].width = Inches(w)
for i, row in enumerate(isi_tbl):
    for j, v in enumerate(row):
        c = tbl.cell(i, j)
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY if i == 0 else (PUTIH if i == 2 else BIRU_MUDA)
        c.text = ""
        p = c.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER
        r = p.add_run(); r.text = v
        r.font.name, r.font.size = ISI_FONT, Pt(14)
        r.font.bold = (i == 0) or (j == 2)
        r.font.color.rgb = PUTIH if i == 0 else TINTA
istilah(s, 9.45, 4.7, 3.3, 2.1, [
    ("Alpha", "sekitar 2% manajer proyek terbaik"),
    ("Sumber", "survei Crowe (2006), slide kuliah; menunjukkan kecenderungan, bukan bukti sebab-akibat"),
])

# =============== 5. Kasus dalam angka ===============
s = slide_baru("Phoenix Pay dalam angka", catatan=(
    "Phoenix adalah sistem gaji untuk sekitar 290 ribu pegawai di 101 kementerian dan lembaga Kanada, dibangun oleh "
    "perusahaan IBM. Masalah bermula dari uang: anggaran yang disetujui 155 juta dolar, padahal biayanya diperkirakan "
    "274 juta. Sistem tetap dipakai pada 2016. Setahun kemudian, lebih dari 520 juta dolar gaji salah atau terlambat, "
    "dan separuh pegawai menerima slip gaji yang salah."))
angka = [
    ("290.000", "pegawai di 101 kementerian/lembaga digaji lewat Phoenix", BIRU, BIRU_MUDA),
    ("US$155 jt → 274 jt", "uang yang disetujui vs biaya yang ternyata dibutuhkan (+77%)", BIRU, BIRU_MUDA),
    ("> US$520 jt", "gaji salah atau terlambat dibayar (Juni 2017)", MERAH, MERAH_MUDA),
    ("51%", "pegawai menerima slip gaji yang salah (April 2017)", MERAH, MERAH_MUDA),
]
for i, (big, small, warna, latar) in enumerate(angka):
    x = 0.6 + (i % 2) * 6.15
    y = 1.5 + (i // 2) * 2.45
    kotak(s, x, y, 5.95, 2.2, fill=latar)
    teks(s, x + 0.35, y + 0.25, 5.3, 1.0, big, size=40, bold=True, color=warna, font=JUDUL_FONT)
    teks(s, x + 0.35, y + 1.3, 5.3, 0.75, small, size=17, color=TINTA)
teks(s, 0.6, 6.5, 12.1, 0.45,
     "Mulai dipakai: 24 Feb 2016 (34 lembaga) dan 21 Apr 2016 (67 lembaga). Pembangun: IBM. Sumber: OAG Kanada (2018).",
     size=13, color=REDUP)

# =============== 6. Lini waktu ===============
s = slide_baru("Lini waktu: pemeriksaan yang dilewati", catatan=(
    "Titik biru adalah kejadian penting proyek; tanda silang merah adalah pemeriksaan yang seharusnya dilakukan tetapi "
    "dilewati. 2012: biaya ternyata jauh lebih besar, tetapi rencana tidak disusun ulang; lebih dari 100 fitur dibuang. "
    "2015: uji coba dibatalkan. 2016: saran untuk meluncurkan bertahap dan menjalankan sistem lama bersama sistem baru "
    "diabaikan, keputusan mulai memakai sistem tidak dicatat, dan jeda antar tahap dipersingkat dari tujuh ke dua bulan."))
s.shapes.add_picture(str(HASIL / "Tugas1_DistribusiEffort_Phoenix_Diagram2_LiniWaktu.png"),
                     Inches(0.5), Inches(1.35), width=Inches(9.0))
istilah(s, 9.75, 1.45, 3.0, 4.6, [
    ("Pilot", "uji coba di satu tempat dulu"),
    ("Parallel run", "sistem lama dan baru dijalankan bersamaan, hasilnya dibandingkan"),
    ("Go-live", "mulai dipakai sungguhan"),
    ("Phase gate", "pemeriksaan sebelum lanjut ke tahap berikutnya"),
    ("Gartner", "perusahaan konsultan teknologi"),
])

# =============== 7. Distribusi effort ===============
s = slide_baru("Pembagian effort: Phoenix vs angka pembanding", catatan=(
    "Batang biru dan oranye adalah data pembanding dari Crowe; batang hijau berarsir adalah perkiraan saya untuk Phoenix, "
    "berdasarkan temuan pemeriksa. Phoenix memakai sekitar 8 persen untuk merencanakan, lebih kecil dari manajer biasa; "
    "86 persen untuk mengerjakan; dan hanya sekitar 3 persen untuk memeriksa dan menguji. Ini perkiraan, bukan hasil "
    "ukur, tetapi polanya jelas."))
s.shapes.add_picture(str(HASIL / "Tugas1_DistribusiEffort_Phoenix_Diagram1_Effort.png"),
                     Inches(0.5), Inches(1.4), width=Inches(8.6))
kotak(s, 9.35, 1.45, 3.4, 3.55, fill=BIRU_MUDA)
teks(s, 9.6, 1.6, 3.0, 3.3, [
    [("Merencanakan ~8%", {"bold": True, "color": NAVY, "size": 19})],
    "lebih kecil dari manajer terbaik (21%) dan manajer lain (11%)",
    [("Mengerjakan ~86%", {"bold": True, "color": NAVY, "size": 19})],
    "paling besar",
    [("Memeriksa & menguji ~3%", {"bold": True, "color": MERAH, "size": 19})],
    "dikurangi tepat sebelum dipakai",
], size=14, color=ABU, space_after=3)
istilah(s, 9.35, 5.15, 3.4, 1.65, [
    ("Estimasi", "perkiraan penulis dari laporan pemeriksa, bukan hasil ukur"),
    ("M&C", "Monitoring & Controlling = memeriksa"),
], size=12)

# =============== 8. Tiga ketimpangan ===============
s = slide_baru("Tiga ketidakseimbangan penyebab kegagalan", catatan=(
    "Ada tiga ketidakseimbangan. Pertama, ketika biaya naik 77 persen, rencana tidak disusun ulang; yang dilakukan hanya "
    "membuang fitur. Kedua, pemeriksaan dan pengujian dikurangi justru saat paling dibutuhkan: 20 persen fitur yang gagal "
    "diuji tidak diuji ulang, dan uji coba dibatalkan. Ini terjadi karena waktu dan biaya dikunci, sehingga yang "
    "dikorbankan adalah mutu. Ketiga, tidak ada pemeriksaan sebelum lanjut ke tahap kedua."))
kolom = [
    ("1", "Rencana tidak disusun ulang", "+77%",
     "biaya naik, tetapi yang dilakukan hanya membuang lebih dari 100 fitur", BIRU, BIRU_MUDA),
    ("2", "Pemeriksaan & pengujian dikurangi", "20%",
     "fitur yang gagal diuji tidak diuji ulang; uji coba dibatalkan", MERAH, MERAH_MUDA),
    ("3", "Tak ada pemeriksaan antartahap", "7 → 2 bln",
     "jeda tahap 1 ke tahap 2 dipersingkat; keputusan mulai pakai tidak dicatat", MERAH, MERAH_MUDA),
]
for i, (n, h, big, d, warna, latar) in enumerate(kolom):
    x = 0.6 + i * 4.1
    kotak(s, x, 1.45, 3.9, 4.0, fill=latar)
    lingkaran_nomor(s, x + 0.3, 1.65, n, fill=warna)
    teks(s, x + 0.3, 2.3, 3.3, 0.95, h, size=19, bold=True, color=NAVY)
    teks(s, x + 0.3, 3.2, 3.3, 0.85, big, size=34, bold=True, color=warna, font=JUDUL_FONT)
    teks(s, x + 0.3, 4.1, 3.3, 1.3, d, size=15, color=TINTA)
istilah(s, 0.6, 5.65, 12.15, 1.2, [
    ("Fitur", "kemampuan sistem, misalnya menghitung lembur atau gaji rapel"),
    ("Mengapa mutu dikorbankan", "tanggal dan uang dikunci, jadi yang dikurangi adalah isi pekerjaan dan pengujian (triple constraint)"),
], size=13)

# =============== 9. Waterfall vs Agile ===============
s = slide_baru("Waterfall vs Agile: cara kerja mana yang cocok?", catatan=(
    "Phoenix dikerjakan cara Waterfall: rencana lengkap dulu, dibangun, lalu diluncurkan sekaligus. Dalam cara ini "
    "pengujian menumpuk di akhir, sehingga paling mudah dikurangi saat jadwal mepet. Agile membagi pekerjaan jadi "
    "putaran pendek yang langsung diuji. Untuk Phoenix, yang paling cocok adalah gabungan atau hybrid: bagian dasar "
    "direncanakan lengkap, peluncuran bertahap per lembaga sambil menjalankan sistem lama, dan fitur yang belum jelas "
    "dikerjakan dalam putaran pendek."))
segmen = [("Waterfall (berurutan)", BIRU_MUDA, NAVY), ("Hybrid (gabungan)", BIRU, PUTIH), ("Agile (putaran pendek)", BIRU_MUDA, NAVY)]
for i, (lbl, latar, warna_teks) in enumerate(segmen):
    k = kotak(s, 0.6 + i * 4.1, 1.45, 3.9, 0.75, fill=latar)
    tf = k.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    r = p.add_run(); r.text = lbl
    r.font.name, r.font.size, r.font.bold, r.font.color.rgb = ISI_FONT, Pt(18), True, warna_teks
teks(s, 4.7, 2.25, 3.9, 0.4, "▲ cocok untuk Phoenix", size=14, bold=True, color=BIRU, align=PP_ALIGN.CENTER)
dua = [
    ("Waterfall: menumpuk", ["Rencana besar di awal", "Pengujian menumpuk di akhir", "→ paling mudah dikurangi saat jadwal mepet"]),
    ("Agile: menyebar", ["Rencana kecil di tiap putaran", "Diuji & dicoba pengguna tiap 1–4 minggu", "→ tidak ada satu titik besar untuk dikurangi"]),
]
for i, (h, items) in enumerate(dua):
    x = 0.6 + i * 4.1
    kotak(s, x, 2.8, 3.9, 2.7, fill=BIRU_MUDA)
    teks(s, x + 0.3, 2.95, 3.3, 0.5, h, size=17, bold=True, color=NAVY)
    teks(s, x + 0.3, 3.5, 3.3, 1.95, items, size=15, color=TINTA, space_after=6)
kotak(s, 8.8, 2.8, 3.95, 2.7, fill=PUTIH, line=BIRU)
teks(s, 9.05, 2.95, 3.5, 0.5, "Hybrid untuk Phoenix", size=17, bold=True, color=BIRU)
teks(s, 9.05, 3.5, 3.5, 1.95, [
    "Bagian dasar (aturan gaji, keamanan) direncanakan lengkap",
    "Diluncurkan bertahap per lembaga, sistem lama tetap jalan",
    "Fitur yang belum jelas dikerjakan dalam putaran pendek",
], size=15, color=TINTA, space_after=6)
istilah(s, 0.6, 5.65, 12.15, 1.2, [
    ("Putaran (sprint)", "satu siklus kerja pendek 1–4 minggu"),
    ("Alasan hybrid (PMBOK 7)", "risiko tinggi & aturan ketat → perlu rencana matang; kebutuhan belum pasti & bisa per lembaga → bertahap"),
], size=13)

# =============== 10. Rekomendasi ===============
s = slide_baru("Rekomendasi untuk proyek serupa", catatan=(
    "Lima rekomendasi utama. Satu, buktikan dulu perkiraan manfaat dengan data nyata. Dua, kalau biaya atau jadwal "
    "melenceng jauh, rencana wajib disusun ulang dan dilaporkan. Tiga, uji coba dan menjalankan sistem lama bersama "
    "sistem baru tidak boleh dihapus. Empat, harus ada pemeriksa dari luar tim proyek yang lapor langsung ke pimpinan. "
    "Lima, keputusan mulai memakai sistem dicatat tertulis. Catatan: cara kerja Agile saja tidak menyelesaikan "
    "masalah pengawasan seperti ini."))
rek = [
    ("Memulai", "Buktikan perkiraan manfaat dengan data nyata sebelum proyek disetujui"),
    ("Merencanakan", "Bila biaya/jadwal melenceng jauh: wajib rencana baru dan lapor ke pemberi dana"),
    ("Memeriksa", "Uji coba dan menjalankan sistem lama-baru bersamaan tidak boleh dihapus"),
    ("Memeriksa", "Ada pemeriksa dari luar tim proyek (audit internal) yang lapor langsung ke pimpinan"),
    ("Menutup", "Keputusan mulai memakai sistem dicatat tertulis: syarat jelas, siapa yang memutuskan"),
]
for i, (pg, r) in enumerate(rek):
    y = 1.45 + i * 0.98
    lingkaran_nomor(s, 0.6, y + 0.1, i + 1)
    teks(s, 1.35, y + 0.1, 1.9, 0.5, pg, size=15, bold=True, color=BIRU)
    teks(s, 3.25, y + 0.05, 5.45, 0.9, r, size=16, color=TINTA)
kotak(s, 9.0, 1.5, 3.75, 4.55, fill=MERAH_MUDA)
teks(s, 9.3, 1.75, 3.2, 0.6, "Catatan penting", size=18, bold=True, color=MERAH)
teks(s, 9.3, 2.4, 3.2, 3.5, [
    "Cara kerja Agile saja tidak menyelesaikan semua masalah Phoenix.",
    "Masalah pengawasan (siapa mengawasi, siapa berhak memutuskan) tetap bisa terjadi dengan cara kerja apa pun.",
    "Yang dibutuhkan: pemeriksa yang tidak memihak.",
], size=15, color=TINTA, space_after=8)

# =============== 11. Pelajaran ===============
s = slide_baru(catatan=(
    "Kesimpulannya satu kalimat: tanggal peluncuran tidak boleh lebih kuat daripada bukti kesiapan. Pola yang sama "
    "terjadi di bank TSB di Inggris tahun 2018 dan pada sistem pajak Coretax tahun 2025. Bagi proyek TI pemerintah di "
    "Indonesia, termasuk peralihan sistem pengamatan cuaca di BMKG tempat saya bekerja, pelajarannya sama. Terima kasih."))
teks(s, 0.9, 1.0, 11.5, 0.5, "PELAJARAN UTAMA", size=16, bold=True, color=BIRU)
teks(s, 0.9, 1.55, 11.5, 2.0, "Tanggal peluncuran tidak boleh lebih kuat daripada bukti kesiapan",
     size=40, bold=True, color=NAVY, font=JUDUL_FONT)
pola = [
    ("Phoenix Pay, Kanada (2016)", "Uji coba dibatalkan, pengujian dikurangi, keputusan mulai pakai tidak dicatat"),
    ("Bank TSB, Inggris (2018)", "Tanggal ditetapkan dulu, pekerjaan dipaksa muat; pengujian dipadatkan (pengawas keuangan Inggris/FCA, 2022)"),
    ("Coretax DJP, Indonesia (2025)", "Sistem pajak baru: gangguan login dan faktur saat banyak pengguna serentak (slide kuliah)"),
]
for i, (h, d) in enumerate(pola):
    x = 0.9 + i * 3.95
    kotak(s, x, 3.85, 3.7, 2.35, fill=BIRU_MUDA)
    teks(s, x + 0.25, 4.05, 3.2, 0.7, h, size=16, bold=True, color=NAVY)
    teks(s, x + 0.25, 4.75, 3.2, 1.4, d, size=14, color=TINTA)
teks(s, 0.9, 6.45, 11.3, 0.5,
     "Relevan untuk proyek TI pemerintah di Indonesia, termasuk peralihan sistem pengamatan cuaca di BMKG.",
     size=15, italic=True, color=ABU)

# =============== 12. Daftar istilah (cadangan) ===============
s = slide_baru("Daftar istilah (cadangan)", catatan="Slide cadangan untuk menjawab pertanyaan; tidak perlu dipresentasikan.")
glos = [
    ("Effort", "tenaga dan waktu proyek"),
    ("Process group", "5 kelompok kegiatan mengelola proyek"),
    ("Initiating", "memulai: memutuskan proyek dan tujuannya"),
    ("Planning", "merencanakan: apa, kapan, biaya, risiko"),
    ("Executing", "mengerjakan: membangun sistem"),
    ("Monitoring & Controlling", "memeriksa, menguji, memperbaiki"),
    ("Closing", "menutup: serah terima, evaluasi"),
    ("PMBOK Guide", "buku standar pengelolaan proyek"),
    ("OAG", "lembaga pemeriksa negara Kanada (seperti BPK)"),
    ("Uji coba (pilot)", "dicoba di satu tempat dulu"),
    ("Parallel run", "sistem lama dan baru jalan bersamaan"),
    ("Go-live", "mulai dipakai sungguhan"),
    ("Phase gate", "pemeriksaan sebelum tahap berikutnya"),
    ("Waterfall", "berurutan, diluncurkan sekaligus"),
    ("Agile", "putaran pendek, langsung dicoba pengguna"),
    ("Hybrid", "gabungan Waterfall dan Agile"),
    ("Triple constraint", "3 batasan: isi pekerjaan, waktu, biaya"),
    ("Audit internal", "pemeriksa di dalam instansi, lapor ke pimpinan"),
]
for k, bagian in enumerate((glos[:9], glos[9:])):
    tbl = s.shapes.add_table(len(bagian), 2, Inches(0.6 + k * 6.2), Inches(1.4), Inches(5.95), Inches(5.2)).table
    tbl.columns[0].width, tbl.columns[1].width = Inches(2.2), Inches(3.75)
    for i, (t, d) in enumerate(bagian):
        for j, v in enumerate((t, d)):
            c = tbl.cell(i, j)
            c.fill.solid()
            c.fill.fore_color.rgb = BIRU_MUDA if i % 2 == 0 else PUTIH
            c.text = ""
            r = c.text_frame.paragraphs[0].add_run(); r.text = v
            r.font.name, r.font.size, r.font.bold = ISI_FONT, Pt(13), (j == 0)
            r.font.color.rgb = NAVY if j == 0 else TINTA

# =============== 13. Daftar pustaka ===============
s = slide_baru("Daftar Pustaka", catatan="Slide cadangan; tidak perlu dipresentasikan.")
teks(s, 0.6, 1.4, 12.1, 5.5, [
    "Crowe, A. (2006). Alpha project managers: What the top 2% know that everyone else does not. Velociteach.",
    "Financial Conduct Authority. (2022). Final notice: TSB Bank plc. https://www.fca.org.uk/publication/final-notices/tsb-bank-plc-2022.pdf",
    "Luthfi, E. T. (2026). IT project management: Pertemuan 4 [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.",
    "Office of the Auditor General of Canada. (2018). Report 1—Building and implementing the Phoenix pay system. 2018 Spring Reports of the Auditor General of Canada.",
    "Project Management Institute. (2008). A guide to the project management body of knowledge (PMBOK® Guide) (4th ed.). Project Management Institute.",
    "Project Management Institute. (2021). A guide to the project management body of knowledge (PMBOK® Guide) (7th ed.). Project Management Institute.",
], size=14, color=TINTA, space_after=10)

prs.save(OUT)
print("dibuat:", OUT)
