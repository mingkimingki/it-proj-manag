# Materi Kuliah — IT Project Management

Program Studi S2 Informatika, Universitas Amikom Yogyakarta — Semester Ganjil 2026/2027
Dosen pengampu: Melwin Syafrizal, S.Kom., M.Eng., Ph.D.  
Slide Pertemuan 4 oleh Emha Taufiq Luthfi, S.T., M.Kom., Ph.D.

## Tujuan folder

Folder ini menyimpan **materi dari dosen** yang dipakai bersama oleh **semua tugas** mata kuliah ini.

## Mengapa folder ini di luar `tugas1/`?

PMBOK dan slide mingguan adalah materi mata kuliah, bukan milik satu tugas. PMBOK kemungkinan besar dipakai lagi di tugas-tugas berikutnya. Dengan menyimpannya di satu tempat, semua tugas mengambil dari sumber yang sama, sehingga materi tidak tercecer di folder tugas lama dan tidak ada salinan ganda.

## Isi folder

| Berkas | Isi | Bagian penting yang sudah dipakai |
|---|---|---|
| `00 - PMBOK Guide Fourth Edition_protected.pdf` | PMBOK edisi ke-4 (PMI, 2008). Standar berbasis proses: 5 *process group* (Initiating, Planning, Executing, Monitoring & Controlling, Closing) dan 9 *knowledge area*. | Bab 2.1: siklus hidup proyek (Gambar 2-1 biaya dan staf, Gambar 2-2 biaya perubahan); Bab 3: *process group* (Gambar 3-2 interaksi *process group*, Tabel 3-1 pemetaan ke *knowledge area*) |
| `01 - PMBOK Guide Seventh Edition.pdf` | PMBOK edisi ke-7 (PMI, 2021). Standar berbasis prinsip: 12 prinsip dan 8 *performance domain*. | Bagian 2.3: *Development Approach and Life Cycle* (pendekatan *predictive*/Waterfall, *hybrid*, *adaptive*/Agile, dan faktor pemilihannya) |
| `Minggu 04 - ITPM S2 PJJ Ganjil 2026-2027 Emha TL 13 Oktober 2026.pptx` | Slide Pertemuan 4 (13 Oktober 2026): *process group*, pemetaan ke *knowledge area*, perkembangan PMBOK 4–8, *tailoring*, studi kasus JWD Consulting. | Slide 12 (*process group* tumpang tindih); slide 30–31 (data Crowe 2006: persentase waktu per *process group*); slide 32–34 (kasus nasional PDNS 2 dan Coretax DJP); slide 43–48 (kasus RS versi PMBOK 4 vs 7); slide 52–83 (contoh dokumen JWD, dipakai UTS); slide 90 (JWD versi prediktif vs Agile) |
| `Slide Dosen (Melwin Syafrizal)-20261025/` | Slide pertemuan 01–08 dan 10–12 (PDF), ditambah `01. IT project management.pptx` (versi PowerPoint slide 01, isinya sama dengan PDF-nya). **Slide 09 belum ada.** | UTS: 04 (PMBOK 4 vs 7), 05 (Inisiasi), 06 (Planning), 07 (Integrasi, Team Contract hlm 29), 08 (Value Delivery System) |
| `Bacaan tambahan/` | Bacaan di luar slide inti: 4 buku COBIT 2019 (ISACA, tata kelola TI) dan artikel Rathnayake dkk. (2026), *Challenges to lean principles adoption in software project management*, *Information and Software Technology* 198, 108209. | Belum dipakai. COBIT tidak diperlukan untuk UTS; artikel Lean opsional untuk refleksi/komparatif UTS |

## Catatan

- Berkas PMBOK edisi ke-4 **terkunci** (tidak bisa disalin atau diubah), tetapi tetap bisa dibaca.
- Data persentase Crowe (2006) di slide 30 tersimpan sebagai **grafik**, bukan teks. Nilainya: manajer proyek Alpha 2/21/69/5/3%, manajer proyek lain 1/11/82/4/2% (Initiating/Planning/Executing/M&C/Closing).
- Nomor halaman PMBOK 4 di PDF = nomor halaman buku + 31 (contoh: halaman buku 15 = halaman PDF 46).
- Nomor halaman PMBOK 7 di PDF: bagian *Standard* = halaman buku + 27; bagian *Guide* = halaman buku + 95.
- 13 Nov 2026: tujuh slide PDF yang diunduh ulang ke akar folder ini dihapus karena identik dengan isi folder `Slide Dosen …`.

## Aturan penambahan

Materi baru dari dosen (misalnya slide Minggu 05, Minggu 06) disimpan di folder ini dengan pola nama yang sama seperti berkas yang sudah ada. Sebelum menyimpan, cek dulu apakah berkasnya sudah ada (hindari salinan ganda). Bacaan di luar slide inti masuk `Bacaan tambahan/`.

## Struktur folder mata kuliah

```
it-proj-manag/
├── materi/        ← materi dosen, dipakai lintas tugas (folder ini)
├── tugas1/        ← Analisis Distribusi Effort Proyek
│   ├── soal/      instruksi tugas dari dosen
│   ├── draf/      berkas kerja (Markdown)
│   ├── sumber/    dokumen rujukan yang diunduh
│   └── hasil/     berkas final yang dikumpulkan
├── tugas2/        ← WBS, Jadwal, dan Risk Register (kelompok)
├── tugas-RTM1/    ← RTM#1 Literature Review
└── uts/           ← UTS: simulasi komparatif PMBOK 4 dan 7 (PANDUAN_UTS.md)
```
