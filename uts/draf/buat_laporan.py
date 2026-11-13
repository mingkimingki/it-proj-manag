"""Merakit laporan UTS IT Project Management (.docx dan .pdf) dari berkas draf Markdown.
Diadaptasi dari tugas2/draf/buat_laporan.py.

Jalankan dari folder ini dengan venv mata kuliah (berisi python-docx dan Pillow):
    ../../.venv/bin/python buat_laporan.py

Sumber (urutan di laporan):
    04_pendahuluan_penutup.md   sampul, Bab 1, lalu penanda <!-- SISIPKAN: BAB 2-5 -->, Bab 6, glosarium, pustaka, lampiran
    01_pmbok4.md                Bab 2
    02_pmbok7.md                Bab 3
    03_komparatif_refleksi.md   Bab 4 (berhenti sebelum "# Bab 5"; bahan refleksi tidak ikut)
    05_refleksi.md              Bab 5 (bila belum ada, dipasang penanda "belum ditulis")

Hasil: ../hasil/UTS_ITPM_EkaPutraKurnia_25.55.2927.docx dan .pdf.
PDF dibuat dua kali dengan LibreOffice: putaran pertama untuk membaca nomor halaman, putaran kedua untuk
mengisi daftar isi, daftar tabel, dan daftar gambar.

Pembersihan otomatis: kotak "Keputusan pengguna"/[USULAN]/catatan kerja dibuang; tanda [USULAN] dan [CEK]
dihapus; rujukan ke data induk diganti rujukan ke Tabel 1.1; sketsa diagram (blok kode) diganti diagram jadi.
"""
import re
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Emu, Pt, RGBColor
from PIL import Image

DRAF = Path(__file__).resolve().parent
HASIL = DRAF.parent / "hasil"
NAMA = "UTS_ITPM_EkaPutraKurnia_25.55.2927"
TOKEN = re.compile(r"(\*\*\*|\*\*|\*)")
WARNA_TINGKAT = {"Rendah": "C6E0B4", "Sedang": "FFE699", "Tinggi": "F4B183", "Sangat tinggi": "FF7C80"}
ABU, BIRU_TUA, BIRU_MUDA = "E8E8E8", "1F4E79", "DDEBF7"


# =====================================================================================
# 1. Menyusun dan membersihkan naskah
# =====================================================================================
def baca(nama):
    return (DRAF / nama).read_text(encoding="utf8")


def naskah():
    kerangka = baca("04_pendahuluan_penutup.md")
    awal, akhir = kerangka.split("<!-- SISIPKAN: BAB 2-5 -->")
    bab4 = baca("03_komparatif_refleksi.md").split("\n# Bab 5")[0]
    ref = DRAF / "05_refleksi.md"
    bab5 = ref.read_text(encoding="utf8") if ref.exists() else \
        "# Bab 5 — Refleksi Manajerial\n\n<!-- BELUM_DITULIS -->\n"
    return "\n\n".join([awal, baca("01_pmbok4.md"), baca("02_pmbok7.md"), bab4, bab5, akhir])


BUANG_KUTIPAN = ("Keputusan pengguna", "[USULAN]", "Berkas kerja", "Penilaian pengaruh dan kepentingan sudah",
                 "**[CEK]**", "ditulis sendiri oleh penulis laporan", "Dicatat dari jawaban", "Rumusan kalimat")
GANTI = [
    (r"\s*\*\*\[USULAN\]\*\*", ""), (r"\s*\[USULAN\]", ""), (r"\s*\[CEK\]", ""),
    (r"\*\*\[CEK sumber: (.*?)\]\*\*", r"(\1)"),
    (r"^(# .*?) \(draf\)\s*$", r"\1"),
    (r"^(\*\*(?:Tabel|Gambar) \d+\.\d+.*?)\s*\([^)]*(?:dirakit|perakitan|sketsa)[^)]*\)\s*$", r"\1"),
    (r"data induk Bagian 8", "Tabel 1.1"),
    (r"bahan Risk Register di data induk Bagian 9", "daftar risiko awal yang dikumpulkan sejak penyusunan Stakeholder Register"),
    (r"\[([^\]]+)\]\((?!http)[^)]+\)", r"\1"),        # tautan ke berkas lokal → teksnya saja
    (r"^\*\*Pemindahan ke ClickUp:\*\*.*$",
     "**Jadwal di ClickUp:** setiap baris Tabel 2.13 dimasukkan ke ClickUp sebagai satu tugas dengan kode WBS di awal "
     "namanya, dikelompokkan per level 2. Pendahulu diisi sebagai ketergantungan, dan M0–M6 dibuat sebagai *milestone*. "
     "Gambar 2.3 memperlihatkan hasilnya; tampilan utuh ada di Lampiran A."),
]


def bersihkan(md):
    keluar, kutipan = [], []

    def tutup_kutipan():
        if kutipan:
            isi = "\n".join(kutipan)
            if not any(k in isi for k in BUANG_KUTIPAN):
                keluar.append("<!-- CATATAN -->\n" + isi + "\n<!-- /CATATAN -->")
            kutipan.clear()

    for b in md.splitlines():
        if b.startswith(">"):
            kutipan.append(b[1:].strip())
            continue
        tutup_kutipan()
        keluar.append(b)
    tutup_kutipan()
    md = "\n".join(keluar)
    for pola, ganti in GANTI:
        md = re.sub(pola, ganti, md, flags=re.M)
    return md


# =====================================================================================
# 2. Dokumen dan gaya
# =====================================================================================
def dokumen_baru():
    """Dokumen kosong dengan ukuran halaman dan gaya laporan."""
    d = Document()
    s0 = d.sections[0]
    s0.page_width, s0.page_height = Cm(21), Cm(29.7)
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(s0, side, Cm(2.5))
    normal = d.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    normal.font.size = Pt(12)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25
    for nama, ukuran in (("Heading 1", 15), ("Heading 2", 13), ("Heading 3", 12), ("Heading 4", 12), ("Title", 18)):
        st = d.styles[nama]
        st.font.name = "Arial"
        st.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
        st.font.size = Pt(ukuran)
        st.font.bold = True
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.paragraph_format.space_before = Pt(12 if nama != "Heading 1" else 0)
        st.paragraph_format.space_after = Pt(6)
    d.styles["Heading 4"].font.italic = True
    d.styles["Heading 4"].font.size = Pt(11.5)
    return d


doc = None


def lebar_isi():
    s = doc.sections[-1]
    return s.page_width - s.left_margin - s.right_margin


def isi_runs(par, teks, ukuran=None, warna=None):
    tebal = miring = False
    for bagian in TOKEN.split(teks):
        if bagian == "***":
            tebal, miring = not tebal, not miring
        elif bagian == "**":
            tebal = not tebal
        elif bagian == "*":
            miring = not miring
        elif bagian:
            r = par.add_run(bagian)
            r.bold, r.italic = tebal or None, miring or None
            if ukuran:
                r.font.size = Pt(ukuran)
            if warna:
                r.font.color.rgb = RGBColor.from_string(warna)
    return par


def p(teks, align=WD_ALIGN_PARAGRAPH.JUSTIFY, ukuran=None, warna=None):
    par = doc.add_paragraph()
    par.alignment = align
    return isi_runs(par, teks, ukuran, warna)


def butir(teks, tingkat=0, nomor=None):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = par.paragraph_format
    kiri = Cm(0.9 + 0.8 * tingkat)
    pf.left_indent, pf.first_line_indent, pf.space_after = kiri, Cm(-0.6), Pt(3)
    tanda = f"{nomor}." if nomor else ("•" if tingkat == 0 else "–")
    isi_runs(par, f"{tanda}\t{teks}")
    pf.tab_stops.add_tab_stop(kiri)


def arsir(cell, warna):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), warna)
    tcPr.append(shd)


def atur_lebar(t, lebar):
    tblPr = t._tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW"); tblPr.append(tblW)
    tblW.set(qn("w:w"), str(sum(Emu(x).twips for x in lebar))); tblW.set(qn("w:type"), "dxa")
    for gc, w in zip(t._tbl.tblGrid.findall(qn("w:gridCol")), lebar):
        gc.set(qn("w:w"), str(Emu(w).twips))
    for row in t.rows:
        for i, c in enumerate(row.cells):
            c.width = lebar[i]


def rapat(t, center=False, jaga=False):
    for n, row in enumerate(t.rows):
        for c in row.cells:
            for par in c.paragraphs:
                par.paragraph_format.space_after = Pt(0)
                par.paragraph_format.line_spacing = 1.05
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
                par.paragraph_format.keep_with_next = jaga and n < len(t.rows) - 1
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement("w:cantSplit"); cs.set(qn("w:val"), "true"); trPr.append(cs)


def ulang_header(t):
    trPr = t.rows[0]._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)


DAFTAR_TABEL, DAFTAR_GAMBAR, DAFTAR_JUDUL = [], [], []
_ID_PENANDA = [0]


def tandai(par, nama):
    """Pasang bookmark (tujuan tautan) di sekeliling isi paragraf."""
    _ID_PENANDA[0] += 1
    awal = OxmlElement("w:bookmarkStart")
    awal.set(qn("w:id"), str(_ID_PENANDA[0])); awal.set(qn("w:name"), nama)
    akhir = OxmlElement("w:bookmarkEnd"); akhir.set(qn("w:id"), str(_ID_PENANDA[0]))
    par._p.insert(1 if par._p.pPr is not None else 0, awal)
    par._p.append(akhir)


def judul_keterangan(teks):
    """Judul tabel/gambar (miring, 10 pt, di tengah) dan catat untuk daftar tabel/gambar."""
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.keep_with_next = True
    par.paragraph_format.space_before = Pt(8)
    isi_runs(par, teks.replace("**", ""), 10)
    for r in par.runs:
        r.italic = True if not r.italic else None
    polos = re.sub(r"\*+", "", teks).strip()
    daftar = DAFTAR_GAMBAR if polos.startswith("Gambar") else DAFTAR_TABEL
    daftar.append(polos)
    tandai(par, f"{'g' if daftar is DAFTAR_GAMBAR else 't'}{len(daftar)}")


def lebar_kolom(header, baris, ukuran):
    """Lebar kolom (EMU): minimal selebar kata terpanjang, sisanya dibagi menurut panjang isi."""
    per_huruf = Cm(0.021 * ukuran)      # perkiraan lebar rata-rata satu huruf pada ukuran ini
    pad = Cm(0.45)
    W = lebar_isi()
    minimal, ingin = [], []
    for j in range(len(header)):
        sel_kol = [re.sub(r"\*+", "", r[j]) for r in [header] + baris if j < len(r)]
        kata = max((len(w) for c in sel_kol for w in c.split()), default=1)
        terpanjang = max(len(c) for c in sel_kol)
        minimal.append(int(kata * per_huruf + pad))
        ingin.append(int(min(terpanjang, 48) * per_huruf + pad))
    ingin = [max(a, b) for a, b in zip(minimal, ingin)]
    if sum(minimal) >= W:
        return [int(x * W / sum(minimal)) for x in minimal]
    if sum(ingin) <= W:
        return [int(x * W / sum(ingin)) for x in ingin]
    sisa = W - sum(minimal)
    tambah = [b - a for a, b in zip(minimal, ingin)]
    return [int(a + sisa * t / sum(tambah)) for a, t in zip(minimal, tambah)]


def tabel(header, baris, judul=None):
    if judul:
        judul_keterangan(judul)
    nkol = len(header)
    ukuran = 10 if nkol <= 4 else 9 if nkol <= 6 else 8 if nkol <= 9 else 7.5
    t = doc.add_table(rows=1, cols=nkol)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    matriks_risiko = bool(judul and judul.startswith("**Gambar 2.4"))
    kol_tingkat = [i for i, h in enumerate(header) if h.strip("* ") == "Tingkat"]
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        isi_runs(c.paragraphs[0], f"**{h.replace('**', '')}**", ukuran)
        arsir(c, ABU)
    for b in baris:
        b = (b + [""] * nkol)[:nkol]
        cells = t.add_row().cells
        for i, v in enumerate(b):
            isi_runs(cells[i].paragraphs[0], v, ukuran)
            if i in kol_tingkat and v.strip("* ") in WARNA_TINGKAT:
                arsir(cells[i], WARNA_TINGKAT[v.strip("* ")])
        if matriks_risiko:
            pk = int(re.match(r"\*?\*?(\d)", b[0]).group(1))
            arsir(cells[0], ABU)
            for d in range(1, 6):
                skor = pk * d
                tingkat = "Rendah" if skor <= 4 else "Sedang" if skor <= 9 else "Tinggi" if skor <= 16 else "Sangat tinggi"
                arsir(cells[d], WARNA_TINGKAT[tingkat])
    if matriks_risiko:
        atur_lebar(t, [int(lebar_isi() * x / 6.4) for x in [1.4] + [1.0] * 5])
    else:
        atur_lebar(t, lebar_kolom(header, baris, ukuran))
    rapat(t, center=matriks_risiko, jaga=len(baris) <= 8)
    ulang_header(t)
    if matriks_risiko:
        p("Hijau = Rendah (1–4) · kuning = Sedang (5–9) · jingga = Tinggi (10–16) · merah = Sangat tinggi (20–25). "
          "Angka dalam kurung = skor P × D.", align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(0)


def kotak_catatan(teks_baris):
    """Kutipan non-kerja (mis. "Mengapa tidak memakai NPV?") sebagai kotak berarsir satu sel."""
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    c = t.cell(0, 0)
    arsir(c, "F2F2F2")
    pertama = True
    for blok in "\n".join(teks_baris).split("\n\n"):
        for b in [x for x in blok.splitlines() if x.strip()]:
            par = c.paragraphs[0] if pertama else c.add_paragraph()
            pertama = False
            isi_runs(par, b, 10.5)
            par.paragraph_format.space_after = Pt(3)
            par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    atur_lebar(t, [lebar_isi()])
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


# =====================================================================================
# 3. Diagram pengganti sketsa
# =====================================================================================
def sel(baris):
    return [c.strip() for c in baris.strip().strip("|").split("|")]


def ambil_tabel(md, kepala):
    blok = []
    for b in md[md.index(kepala):].splitlines():
        if not b.startswith("|"):
            break
        blok.append(sel(b))
    return blok[2:]


def polos(t):
    return re.sub(r"\*+", "", t).strip()


def kotak_teks(cell, judul, isi, warna, putih=False, ukuran=9.5):
    arsir(cell, warna)
    par = cell.paragraphs[0]
    isi_runs(par, f"**{judul}**", ukuran + 0.5, "FFFFFF" if putih else None)
    for b in isi:
        isi_runs(cell.add_paragraph(), b, ukuran, "FFFFFF" if putih else None)


def gambar_grid(md, judul):
    judul_keterangan(judul)
    kotak = {"Manage Closely": [], "Keep Satisfied": [], "Keep Informed": [], "Monitor": []}
    for c in ambil_tabel(md, "| No | Pihak | Pengaruh | Kepentingan | Kotak |"):
        kotak[polos(c[4])].append(f"{polos(c[0])} {polos(c[1])}")
    t = doc.add_table(rows=3, cols=3)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    isi_runs(t.cell(0, 0).paragraphs[0], "**Pengaruh tinggi**", 9.5)
    isi_runs(t.cell(1, 0).paragraphs[0], "**Pengaruh rendah**", 9.5)
    isi_runs(t.cell(2, 1).paragraphs[0], "**Kepentingan rendah**", 9.5)
    isi_runs(t.cell(2, 2).paragraphs[0], "**Kepentingan tinggi**", 9.5)
    for c in (t.cell(0, 0), t.cell(1, 0), t.cell(2, 1), t.cell(2, 2)):
        arsir(c, ABU)
    kotak_teks(t.cell(0, 1), "Keep Satisfied (jaga tetap puas)", kotak["Keep Satisfied"], "FFE699")
    kotak_teks(t.cell(0, 2), "Manage Closely (libatkan erat)", kotak["Manage Closely"], "F4B183")
    kotak_teks(t.cell(1, 1), "Monitor (pantau)", kotak["Monitor"], "E2EFDA")
    kotak_teks(t.cell(1, 2), "Keep Informed (beri informasi rutin)", kotak["Keep Informed"], BIRU_MUDA)
    atur_lebar(t, [Cm(2.6), int((lebar_isi() - Cm(2.6)) / 2), int((lebar_isi() - Cm(2.6)) / 2)])
    rapat(t, jaga=True)
    for i in (0, 1):
        for par in t.cell(i, 0).paragraphs:
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for j in (1, 2):
        t.cell(2, j).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p("Penilaian \"sedang\" ditempatkan ke kotak terdekat berdasarkan pertimbangan di Tabel 2.1.",
      align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)


def gambar_wbs(md, judul):
    judul_keterangan("Gambar 2.2 Diagram pohon WBS (level 1–3)")
    fase = []
    for c in ambil_tabel(md, "| Kode | Paket kerja | Hasil kerja | PJ |"):
        kode, nama = polos(c[0]), polos(c[1])
        if kode.count(".") == 1:
            fase.append((kode, nama, []))
        elif kode.count(".") == 2:
            fase[-1][2].append((kode, nama))
    t = doc.add_table(rows=3, cols=len(fase))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    puncak = t.cell(0, 0).merge(t.cell(0, len(fase) - 1))
    isi_runs(puncak.paragraphs[0], "**1  Super App Nusantara Express**", 12, "FFFFFF")
    arsir(puncak, BIRU_TUA)
    for j, (kode, nama, wps) in enumerate(fase):
        isi_runs(t.cell(1, j).paragraphs[0], f"**{kode} {nama}**", 9)
        arsir(t.cell(1, j), "BDD7EE")
        for n, (k, nm) in enumerate(wps):
            par = t.cell(2, j).paragraphs[0] if n == 0 else t.cell(2, j).add_paragraph()
            isi_runs(par, f"**{k}** {nm}", 8)
            par.paragraph_format.space_after = Pt(3)
    atur_lebar(t, [int(lebar_isi() / len(fase))] * len(fase))
    rapat(t)
    for r in t.rows[:2]:
        for c in r.cells:
            for par in c.paragraphs:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p(f"Baris atas = level 1 (proyek), baris tengah = level 2 ({len(fase)} cabang), kolom bawah = level 3 "
      f"({sum(len(f[2]) for f in fase)} paket kerja). WBS menunjukkan pemecahan pekerjaan, bukan urutan; urutan ada di jadwal.",
      align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)


def gambar_berkas(judul, jalur, lebar=None):
    judul_keterangan(judul)
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.add_run().add_picture(str((DRAF / jalur).resolve()), width=lebar or lebar_isi())


def baris_kotak(judul, kolom, warna, panah=True, catatan=None):
    """Diagram mendatar: kotak-kotak dengan panah di antaranya."""
    judul_keterangan(judul)
    n = len(kolom)
    ncol = 2 * n - 1 if panah else n
    t = doc.add_table(rows=1, cols=ncol)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    lebar = []
    for j in range(ncol):
        c = t.cell(0, j)
        if panah and j % 2 == 1:
            isi_runs(c.paragraphs[0], "**→**", 16)
            lebar.append(Cm(0.8))
        else:
            k = kolom[j // 2 if panah else j]
            kotak_teks(c, k[0], k[1], warna[j // 2 if panah else j])
            lebar.append(None)
    sisa = lebar_isi() - sum(x for x in lebar if x)
    lebar = [x or int(sisa / n) for x in lebar]
    atur_lebar(t, lebar)
    rapat(t)
    if panah:
        for j in range(1, ncol, 2):
            t.cell(0, j).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if catatan:
        p(catatan, align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)


def gambar_rantai_nilai(judul):
    baris_kotak("Gambar 3.1 Rantai nilai Nusantara Express", [
        ("OUTPUT", ["Rilis 1 (31 Mar 2027) dan Rilis 2 (15 Jun 2027)", "4 modul, seluruh DIY"]),
        ("OUTCOME", ["UMKM berjualan; pembeli belanja dan membayar lewat *wallet*",
                     "1.000 UMKM dan 20.000 pembeli aktif (30 Jun 2027)"]),
        ("BENEFIT", ["Pendapatan Rp 11,0 M (tahun 1) s.d. Rp 52,8 M (tahun 3)", "Balik modal ± 2,5 tahun"]),
        ("VALUE", ["Finansial, operasional, pelanggan, strategis, sosial (Tabel 3.3)"]),
    ], ["BDD7EE", "C6E0B4", "FFE699", "F8CBAD"],
        catatan="Hanya *output* yang terjadi selama proyek; *outcome* mulai April 2027, *benefit* dan *value* sebagian besar setelah proyek ditutup.")


def gambar_vds(judul):
    judul_keterangan("Gambar 3.2 Posisi proyek dalam *Value Delivery System* PT ND (fiktif)")
    lapis = [
        ("Strategi PT ND", "Menjadi ekosistem digital bagi UMKM Indonesia", BIRU_TUA, True),
        ("Tata kelola", "Direksi (dibantu Komite Pengarah untuk proyek ini)", "2E75B6", True),
        ("Portofolio", "Transformasi Digital PT ND", "9DC3E6", False),
        ("Program", "Ekosistem Digital UMKM", "BDD7EE", False),
        ("Proyek", None, BIRU_MUDA, False),
        ("Produk", "Nusantara Express, terus dikembangkan selama siklus hidupnya", "E2EFDA", False),
        ("Operasional", "Operations & Logistics dan Business Development (setelah serah terima M6)", "F2F2F2", False),
    ]
    t = doc.add_table(rows=len(lapis), cols=3)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, (nama, isi, warna, putih) in enumerate(lapis):
        isi_runs(t.cell(i, 0).paragraphs[0], f"**{nama}**", 10)
        arsir(t.cell(i, 0), ABU)
        if isi is None:
            kotak_teks(t.cell(i, 1), "Super App Nusantara Express (Jan–Jun 2027)", ["◄ proyek ini"], "F4B183")
            kotak_teks(t.cell(i, 2), "Proyek lanjutan: perluasan ke luar DIY",
                       ["setelah proyek (butir L5 Scope Statement)"], BIRU_MUDA)
        else:
            m = t.cell(i, 1).merge(t.cell(i, 2))
            kotak_teks(m, isi, [], warna, putih)
    atur_lebar(t, [Cm(3.2), int((lebar_isi() - Cm(3.2)) / 2), int((lebar_isi() - Cm(3.2)) / 2)])
    rapat(t, jaga=True)
    for r in t.rows:
        for c in r.cells[1:]:
            for par in c.paragraphs:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p("Lapisan atas menurunkan strategi, target *outcome*, dan prinsip ke bawah; lapisan bawah mengirim laporan "
      "kemajuan dan data pemakaian ke atas (aliran informasi dua arah, PMBOK 7 *Standard* hlm 11).",
      align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)


def gambar_tiga_lapis(judul):
    judul_keterangan("Gambar 3.3 Tiga lapis rencana")
    lapis = [
        ("Lapis 1 — *Roadmap* 6 bulan (tetap)",
         "M0 4 Jan · M1 6 Jan · M2 29 Jan · M3 31 Mar · M4 30 Apr · M5 15 Jun · M6 30 Jun; anggaran dan kriteria K1–K7"),
        ("Lapis 2 — Rencana rilis (ditinjau di M2 dan M4)",
         "Rilis 1: isi wajib + pelengkap. Rilis 2: dirinci pada April (1.4.1), setelah data Rilis 1 tersedia"),
        ("Lapis 3 — Rencana *sprint* (disusun tim di awal tiap *sprint*)",
         "S0 desain · S1 · S2 · S3* (1 minggu) · uji + UAT · S4′ desain Rilis 2 · M4 · S4 · S5 · uji + UAT"),
    ]
    t = doc.add_table(rows=len(lapis), cols=2)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for i, ((a, b), w) in enumerate(zip(lapis, ("BDD7EE", "C6E0B4", "FFE699"))):
        isi_runs(t.cell(i, 0).paragraphs[0], f"**{a}**", 9.5)
        arsir(t.cell(i, 0), w)
        isi_runs(t.cell(i, 1).paragraphs[0], b, 9.5)
    atur_lebar(t, [Cm(5.2), lebar_isi() - Cm(5.2)])
    rapat(t, jaga=True)
    p("Makin dekat waktunya, makin rinci rencananya (*progressive elaboration*). Lapis 1 dikendalikan Komite Pengarah; "
      "lapis 3 diatur tim modul.", align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=9.5)


def gambar_dari_sketsa(judul, md_sumber):
    nomor = re.match(r"\*\*Gambar (\d+\.\d+)", judul).group(1)
    if nomor == "2.1":
        gambar_grid(md_sumber, "Gambar 2.1 Power-Interest Grid")
    elif nomor == "2.2":
        gambar_wbs(md_sumber, judul)
    elif nomor == "2.3":
        gambar_berkas("Gambar 2.3 Gantt Chart di ClickUp (batang merah = jalur kritis menurut perhitungan ClickUp)",
                      "../clickup/gantt_clickup_ringkas.png")
    elif nomor == "3.1":
        gambar_rantai_nilai(judul)
    elif nomor == "3.2":
        gambar_vds(judul)
    elif nomor == "3.3":
        gambar_tiga_lapis(judul)
    else:
        raise SystemExit(f"Tidak ada diagram pengganti untuk {judul}")


# =====================================================================================
# 4. Halaman: sampul, daftar, kepala/kaki halaman
# =====================================================================================
def nomor_halaman(section, mulai=None, format_=None):
    par = section.footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = par.add_run()
    for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar"); el.set(qn("w:fldCharType"), tag)
        else:
            el = OxmlElement("w:instrText"); el.set(qn("xml:space"), "preserve"); el.text = txt
        r._r.append(el)
    r.font.size = Pt(10)
    for el in section._sectPr.findall(qn("w:pgNumType")):     # add_section menyalin pengaturan section sebelumnya
        section._sectPr.remove(el)
    pg = OxmlElement("w:pgNumType")
    if mulai:
        pg.set(qn("w:start"), str(mulai))
    if format_:
        pg.set(qn("w:fmt"), format_)
    section._sectPr.append(pg)


def kepala_halaman(section, teks):
    par = section.header.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = par.add_run(teks)
    r.italic = True
    r.font.size = Pt(9)


def sampul(data):
    for _ in range(2):
        doc.add_paragraph()
    par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.add_run().add_picture(str((DRAF / data["logo"]).resolve()), width=Cm(4.5))
    doc.add_paragraph()
    t = doc.add_paragraph(style="Title"); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.add_run(data["judul"])
    for kunci, ukuran in (("subjudul", 13), ("jenis", 13)):
        par = doc.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = par.add_run(data[kunci]); r.font.size = Pt(ukuran)
    for _ in range(3):
        doc.add_paragraph()
    p("Disusun oleh:", align=WD_ALIGN_PARAGRAPH.CENTER)
    for a in data["anggota"].split("; "):
        nama, nim = a.split("|")
        par = p(f"**{nama}**", align=WD_ALIGN_PARAGRAPH.CENTER); par.paragraph_format.space_after = Pt(0)
        p(f"NIM {nim}", align=WD_ALIGN_PARAGRAPH.CENTER)
    for _ in range(3):
        doc.add_paragraph()
    for kunci in ("dosen", "prodi", "kampus", "waktu"):
        par = p(data[kunci], align=WD_ALIGN_PARAGRAPH.CENTER, ukuran=11 if kunci == "dosen" else None)
        par.paragraph_format.space_after = Pt(2)
        if kunci in ("prodi", "kampus"):
            for r in par.runs:
                r.bold = True


def baris_daftar(teks, halaman, indent=0, tebal=False, tujuan=None):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(indent)
    pf.space_after = Pt(1)
    pf.line_spacing = 1.1
    pf.tab_stops.add_tab_stop(lebar_isi(), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    r = par.add_run(f"{teks}\t{halaman}")
    r.font.size = Pt(11)
    r.bold = tebal or None
    if tujuan:      # bungkus run dalam tautan internal ke bookmark tujuan (teks tetap hitam, tanpa garis bawah)
        hl = OxmlElement("w:hyperlink")
        hl.set(qn("w:anchor"), tujuan); hl.set(qn("w:history"), "1")
        par._p.remove(r._r); hl.append(r._r); par._p.append(hl)


def halaman_daftar(judul_daftar, entri, nomor, awalan):
    h = doc.add_heading(judul_daftar, level=1)
    for n, (jenis, teks) in enumerate(entri, 1):
        if jenis in (1, 2, 3):
            baris_daftar(teks, nomor.get(teks, "…"), indent=[0, 0, 0.6, 1.2][jenis], tebal=jenis == 1,
                         tujuan=f"{awalan}{n}")
        else:
            baris_daftar(teks, nomor.get(teks, "…"), indent=0, tujuan=f"{awalan}{n}")
    return h


# =====================================================================================
# 5. Merender naskah
# =====================================================================================
def render(md):
    baris = md.splitlines()
    i = 0
    paragraf = []
    judul_tertunda = None
    pertama_h1 = True

    def tutup():
        nonlocal paragraf
        if paragraf:
            p(" ".join(paragraf))
            paragraf = []

    while i < len(baris):
        b = baris[i].rstrip()
        s = b.strip()
        if s.startswith("<!--"):
            tutup()
            komentar = s
            while not komentar.endswith("-->"):
                i += 1
                komentar += "\n" + baris[i]
            isi_k = komentar[4:-3].strip()
            if isi_k == "CATATAN":
                isi_catatan = []
                i += 1
                while baris[i].strip() != "<!-- /CATATAN -->":
                    isi_catatan.append(baris[i]); i += 1
                kotak_catatan(isi_catatan)
            elif isi_k == "BELUM_DITULIS":
                p("**[Bab ini ditulis sendiri oleh penulis dan belum diisi. Sumbernya: uts/draf/05_refleksi.md.]**",
                  warna="C00000")
            elif isi_k.startswith("GAMBAR_HALAMAN_BESAR:"):
                judul, jalur = [x.strip() for x in isi_k.split(":", 1)[1].split("|")]
                halaman_besar(judul, jalur)
            i += 1
            continue
        if not s or s == "---":
            tutup(); i += 1; continue
        if s.startswith("#"):
            tutup()
            if judul_tertunda:
                raise SystemExit(f"Judul tanpa tabel/gambar: {judul_tertunda}")
            tingkat = len(s) - len(s.lstrip("#"))
            teks = s[tingkat:].strip()
            h = doc.add_heading("", level=min(tingkat, 4))
            if tingkat == 1:
                # "Mulai di halaman baru" pada judul bab, bukan paragraf pemisah: tidak menyisakan halaman kosong
                # bila halaman sebelumnya pas penuh.
                h.paragraph_format.page_break_before = not pertama_h1
                pertama_h1 = False
            isi_runs(h, teks)
            h.paragraph_format.keep_with_next = True
            if tingkat <= 3:
                DAFTAR_JUDUL.append((tingkat, polos(teks)))
                tandai(h, f"j{len(DAFTAR_JUDUL)}")
            i += 1
            continue
        m_jdl = re.match(r"^\*\*(Tabel|Gambar) \d+\.\d+.*", s)
        if m_jdl:
            tutup()
            judul_tertunda = s
            i += 1
            continue
        if s.startswith("```"):
            tutup()
            i += 1
            while not baris[i].strip().startswith("```"):
                i += 1
            i += 1
            if judul_tertunda and judul_tertunda.startswith("**Gambar"):
                gambar_dari_sketsa(judul_tertunda, md)
            judul_tertunda = None
            continue
        if s.startswith("|"):
            tutup()
            blok = []
            while i < len(baris) and baris[i].startswith("|"):
                blok.append(sel(baris[i])); i += 1
            tabel(blok[0], blok[2:], judul_tertunda)
            judul_tertunda = None
            continue
        mb = re.match(r"^(\s*)- (.*)", b)
        mn = re.match(r"^(\s*)(\d+)\. (.*)", b)
        if mb or mn:
            tutup()
            if mb:
                butir(mb.group(2), tingkat=1 if len(mb.group(1)) >= 2 else 0)
            else:
                butir(mn.group(3), tingkat=1 if len(mn.group(1)) >= 2 else 0, nomor=mn.group(2))
            i += 1
            continue
        paragraf.append(s)     # paragraf penjelasan di antara judul dan tabel tetap ditulis; judul menunggu tabelnya
        i += 1
    tutup()


def halaman_besar(judul, jalur):
    """Gambar pada halaman yang ukurannya mengikuti gambar (untuk Gantt utuh)."""
    berkas = (DRAF / jalur).resolve()
    w, h = Image.open(berkas).size
    lebar_gbr = Cm(30)
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.PORTRAIT
    s.page_width = Cm(33)
    s.page_height = Cm(30 * h / w + 6)
    for side in ("left_margin", "right_margin"):
        setattr(s, side, Cm(1.5))
    s.top_margin, s.bottom_margin = Cm(2), Cm(2)
    for el in s._sectPr.findall(qn("w:pgNumType")):
        s._sectPr.remove(el)
    judul_keterangan(judul)
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.add_run().add_picture(str(berkas), width=lebar_gbr)


# =====================================================================================
# 6. Membangun dokumen (dua putaran untuk nomor halaman)
# =====================================================================================
def bangun(nomor):
    global doc
    doc = dokumen_baru()
    md = bersihkan(naskah())
    m = re.search(r"<!-- SAMPUL\n(.*?)-->", md, re.S)
    data = dict(b.split(": ", 1) for b in m.group(1).strip().splitlines())
    md = re.sub(r"<!-- SAMPUL\n.*?-->", "", md, flags=re.S)

    sampul(data)
    depan = doc.add_section(WD_SECTION.NEW_PAGE)
    depan.header.is_linked_to_previous = False
    depan.footer.is_linked_to_previous = False
    kepala_halaman(depan, data["header"])
    nomor_halaman(depan, mulai=1, format_="lowerRoman")
    entri_judul = nomor.get("_judul", [])
    halaman_daftar("Daftar Isi", entri_judul, nomor, "j")
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    halaman_daftar("Daftar Tabel", [(0, x) for x in nomor.get("_tabel", [])], nomor, "t")
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    halaman_daftar("Daftar Gambar", [(0, x) for x in nomor.get("_gambar", [])], nomor, "g")

    isi = doc.add_section(WD_SECTION.NEW_PAGE)
    isi.header.is_linked_to_previous = False
    isi.footer.is_linked_to_previous = False
    kepala_halaman(isi, data["header"])
    nomor_halaman(isi, mulai=1)
    DAFTAR_JUDUL.clear(); DAFTAR_TABEL.clear(); DAFTAR_GAMBAR.clear()
    render(md)
    return doc


def ke_pdf(docx, folder):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(folder), str(docx)],
                   check=True, capture_output=True)
    return Path(folder) / (docx.stem + ".pdf")


def baca_halaman(pdf):
    jumlah = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                                                             text=True).stdout).group(1))
    halaman = []
    for n in range(1, jumlah + 1):
        t = subprocess.run(["pdftotext", "-layout", "-f", str(n), "-l", str(n), str(pdf), "-"],
                           capture_output=True, text=True).stdout
        halaman.append(t)
    return halaman


def kunci_cari(teks):
    return re.sub(r"[^0-9a-z]", "", teks.lower())[:45]


def cari_nomor(halaman, entri, awal_isi):
    """Cari halaman setiap entri (berurutan) mulai dari halaman isi pertama; kembalikan nomor halaman isi."""
    hasil, pos = {}, awal_isi
    datar = [re.sub(r"[^0-9a-z]", "", h.lower()) for h in halaman]
    for teks in entri:
        k = kunci_cari(teks)
        for n in range(pos, len(datar)):
            if k and k in datar[n]:
                hasil[teks] = str(n - awal_isi + 1)
                pos = n
                break
    return hasil


if __name__ == "__main__":
    HASIL.mkdir(exist_ok=True)
    keluaran = HASIL / f"{NAMA}.docx"
    with tempfile.TemporaryDirectory() as tmp:
        # Putaran 1: nomor halaman belum diketahui
        bangun({})
        judul1, tabel1, gambar1 = list(DAFTAR_JUDUL), list(DAFTAR_TABEL), list(DAFTAR_GAMBAR)
        doc.save(Path(tmp) / "p1.docx")
        # Putaran 2: daftar dengan entri lengkap (nomor "…") agar jumlah halaman depan sudah final
        bangun({"_judul": judul1, "_tabel": tabel1, "_gambar": gambar1})
        doc.save(Path(tmp) / "p2.docx")
        hal = baca_halaman(ke_pdf(Path(tmp) / "p2.docx", tmp))
        awal_isi = next(n for n, h in enumerate(hal) if "Bab 1 — Pendahuluan" in h and "Daftar Isi" not in h
                        and "1.1 Latar belakang" in h)
        nomor = {"_judul": judul1, "_tabel": tabel1, "_gambar": gambar1}
        nomor.update(cari_nomor(hal, [t for _, t in judul1], awal_isi))
        nomor.update(cari_nomor(hal, tabel1, awal_isi))
        nomor.update(cari_nomor(hal, gambar1, awal_isi))
        hilang = [t for _, t in judul1 if t not in nomor] + [t for t in tabel1 + gambar1 if t not in nomor]
        # Putaran 3: final
        bangun(nomor)
        doc.save(keluaran)
    pdf = ke_pdf(keluaran, HASIL)
    print("Tersimpan:", keluaran)
    print("Tersimpan:", pdf)
    print(f"Judul {len(judul1)}, tabel {len(tabel1)}, gambar {len(gambar1)}; tanpa nomor halaman: {len(hilang)}")
    for t in hilang[:10]:
        print("  -", t)
