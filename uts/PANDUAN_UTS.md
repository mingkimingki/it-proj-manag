# Panduan UTS IT Project Management: Simulasi Komparatif PMBOK 4 dan PMBOK 7

> Berkas kerja: panduan untuk memahami dan mengerjakan UTS Semester Ganjil 2026/2027.
> Sumber soal: `ITM_UTS_GANJIL_202601_Pascasarjana_PJJ.docx` (folder ini).
> Kode mata kuliah: PJ059, S2 PJJ Informatika. Pengumpulan: PDF lewat **Waskita** (LMS kampus), waktu pengerjaan **5 hari sampai pukul 23.59 WIB**.
> Aturan penulisan: setiap istilah asing dijelaskan singkat saat pertama kali muncul, lalu dikumpulkan di **Glosarium** (Bagian 13).
> Tanda **[USULAN]** berarti usulan Claude. Butir itu belum diputuskan dan perlu disetujui dulu.

**Isian yang masih kosong:**

| Hal | Isi |
|---|---|
| Dikerjakan sendiri atau berkelompok (maks. 5 orang)? | Individu dulu. Peluang berkelompok tetap terbuka |
| Anggota kelompok (bila berkelompok) | Belum ada |
| Tanggal mulai UTS | November 2026 (tanggal pasti menyusul) |
| Batas pengumpulan | 5 hari sejak mulai, pukul 23.59 WIB (tanggal pasti menyusul) |

---

## Daftar isi

1. [Tugas ini sebenarnya apa?](#1-tugas-ini-sebenarnya-apa)
2. [Yang dikumpulkan dan cara dinilai](#2-yang-dikumpulkan-dan-cara-dinilai)
3. [Gambaran besar: satu proyek, dua cara pandang](#3-gambaran-besar-satu-proyek-dua-cara-pandang)
4. [Memahami studi kasus Nusantara Express](#4-memahami-studi-kasus-nusantara-express)
5. [Bagian 1: Dokumen PMBOK 4](#5-bagian-1-dokumen-pmbok-4)
6. [Bagian 2: Dokumen PMBOK 7](#6-bagian-2-dokumen-pmbok-7)
7. [Bagian 3: Analisis komparatif](#7-bagian-3-analisis-komparatif)
8. [Bagian 4: Refleksi manajerial](#8-bagian-4-refleksi-manajerial)
9. [Catatan kritis atas soal](#9-catatan-kritis-atas-soal)
10. [Susunan laporan PDF](#10-susunan-laporan-pdf)
11. [Tahapan pengerjaan dalam 5 hari](#11-tahapan-pengerjaan-dalam-5-hari)
12. [Daftar periksa dan pertanyaan untuk dosen](#12-daftar-periksa-dan-pertanyaan-untuk-dosen)
13. [Glosarium](#13-glosarium)
14. [Rujukan](#14-rujukan)

---

## 1. Tugas ini sebenarnya apa?

Kalian berperan sebagai **Project Manager** (manajer proyek) sebuah proyek fiktif: membangun *super app* untuk PT Nusantara Digital Indonesia. Proyeknya tidak dibuat sungguhan. Yang dikerjakan adalah **dokumen-dokumen manajemen proyeknya**.

Keunikan UTS ini: **proyek yang sama dikelola dua kali**, dengan dua "kacamata" dari PMI (*Project Management Institute*, lembaga standar manajemen proyek di Amerika Serikat):

| Kacamata | Pertanyaan utamanya | Bentuk hasilnya |
|---|---|---|
| **PMBOK 4** (2008) | "Proses apa yang harus dijalankan, dan dokumen apa yang dihasilkan?" | 10 dokumen formal, dari Business Case sampai Risk Register |
| **PMBOK 7** (2021) | "Prinsip apa yang memandu keputusan, dan bagaimana proyek menghasilkan nilai?" | Uraian penerapan prinsip dan *performance domain* |

Setelah dua kacamata itu dipakai, kalian **membandingkannya** (analisis komparatif) dan **menyimpulkan pelajaran sebagai manajer** (refleksi).

**PMBOK** (*Project Management Body of Knowledge*) adalah buku panduan standar manajemen proyek terbitan PMI. Kedua edisi ada di folder `materi/`.

---

## 2. Yang dikumpulkan dan cara dinilai

### Yang dikumpulkan

Satu **laporan komprehensif dalam PDF**, diunggah ke Waskita. Isinya tiga bagian:

1. Dokumen PMBOK 4 (Pra-Inisiasi, Inisiasi, Planning)
2. Dokumen PMBOK 7 (Value, Stakeholder & Team, Planning)
3. Analisis komparatif dan refleksi manajerial

Soal **tidak** meminta presentasi atau berkas dari aplikasi (berbeda dengan Tugas 2).

### Cara dinilai

| Aspek | Yang dinilai | Bobot |
|---|---|---|
| Dokumen PMBOK 4 | Kelengkapan dan **konsistensi** dokumen pra-inisiasi, inisiasi, planning | 25 |
| Dokumen PMBOK 7 | Pemahaman prinsip dan penerapan *domain* kinerja | 25 |
| Analisis komparatif | **Kedalaman** analisis perbedaan pendekatan dan relevansinya | 25 |
| Refleksi manajerial | *Insight* pribadi, argumentasi, konteks proyek TI | 15 |
| Format & visualisasi | Struktur laporan, tabel, diagram, kerapian | 10 |
| **Total** | | **100** |

### Pelajaran dari bobot ini

1. **Komparatif + refleksi = 40 poin.** Nilainya lebih besar dari paket PMBOK 4 (25), padahal PMBOK 4 punya 10 dokumen. Jadi jangan habiskan 4 hari untuk tabel PMBOK 4 lalu menulis perbandingan dalam semalam.
2. **Kata kunci PMBOK 4 adalah "konsisten".** Angka, nama, tanggal, dan kode harus sama di semua dokumen. Contohnya, anggaran di Business Case sama dengan di Charter, dan *milestone* di Charter muncul lagi di Gantt. Lihat Bagian 5.1.
3. **Kata kunci PMBOK 7 adalah "pemahaman" dan "penerapan".** Menyalin daftar 12 prinsip tidak cukup. Setiap prinsip harus dikaitkan dengan **keputusan nyata** di proyek Nusantara Express.
4. **Format bernilai 10 poin.** Diagram (grid stakeholder, WBS, Gantt, matriks risiko, rantai nilai) termasuk penilaian, bukan hiasan.

---

## 3. Gambaran besar: satu proyek, dua cara pandang

```
                  STUDI KASUS: Super App Nusantara Express (6 bulan)
                                       │
          ┌────────────────────────────┴────────────────────────────┐
          ▼                                                         ▼
  PMBOK 4 (berbasis PROSES)                                PMBOK 7 (berbasis PRINSIP)
  ─────────────────────────                                ──────────────────────────
  PRA-INISIASI                                             BUSINESS CONTEXT & VALUE
   1 Stakeholder Register ─┐                                • 3–5 prinsip yang relevan
   2 Stakeholder Mgmt Strat┤                                • Value Delivery System
   3 Business Case ────────┤
  INISIASI                 │                               STAKEHOLDER & TEAM
   4 Project Charter ◄─────┘                                • strategi kolaborasi & komunikasi
   5 Agenda Kick-off                                        • tim adaptif & pembagian peran
  PLANNING
   6 Team Contract                                         PLANNING
   7 Scope Statement                                        • perencanaan adaptif/incremental
   8 WBS ──► 9 Gantt/Milestone                              • risiko berbasis kompleksitas
   10 Risk Register
          │                                                         │
          └────────────────────────────┬────────────────────────────┘
                                       ▼
                ANALISIS KOMPARATIF  →  REFLEKSI MANAJERIAL
          (apa bedanya, mengapa,        (apa yang saya pelajari
           apa akibatnya di proyek ini)  sebagai manajer proyek TI)
```

Ada dua aturan agar laporan "nyambung":

- **Proyeknya sama persis.** Bagian PMBOK 7 tidak boleh mengarang proyek baru. Ia memakai stakeholder, modul, dan risiko yang sama dengan bagian PMBOK 4, hanya dikelola dengan cara pikir berbeda.
- **Perbandingan merujuk ke dokumen kalian sendiri.** Contoh kalimat yang baik: "Di Scope Statement (Bagian 2.7) fitur AI dikunci sejak awal. Di perencanaan PMBOK 7 (Bagian 3.3) fitur yang sama masuk *backlog* dan diuji dulu pada kelompok UMKM kecil."

---

## 4. Memahami studi kasus Nusantara Express

### Yang ditetapkan soal (tidak boleh diubah)

| Unsur | Isi dari soal |
|---|---|
| Organisasi | PT Nusantara Digital Indonesia |
| Produk | *Super App Omni-Channel* "Smart Retails & Delivery" |
| Modul | (1) *marketplace*, (2) logistik dengan *real-time tracking*, (3) pembayaran *digital wallet*, (4) rekomendasi produk berbasis AI untuk UMKM |
| Target waktu | **6 bulan** |
| Tim/divisi | Software Engineering, UI/UX, Infrastructure & Cybersecurity, Business Development, Operations & Logistics, Legal & Compliance |
| Kolaborasi | Lintas divisi **internal dan eksternal** |

Penjelasan istilah dari soal:
- ***Super app***: satu aplikasi yang menggabungkan banyak layanan (belanja, kirim barang, bayar).
- ***Omni-channel***: layanan bisa diakses dari berbagai saluran (aplikasi, web, toko fisik) dengan pengalaman yang menyatu.
- ***Real-time tracking***: posisi paket bisa dipantau saat itu juga.
- ***Digital wallet***: dompet digital, saldo uang elektronik di aplikasi.
- **UMKM**: Usaha Mikro, Kecil, dan Menengah.

### Yang harus kalian tetapkan sendiri (asumsi)

Soal tidak memberi angka. Asumsi berikut perlu **diputuskan sekali di awal**, lalu dipakai sama di semua dokumen:

| Asumsi | Contoh pertanyaan | Dipakai di |
|---|---|---|
| Tanggal mulai dan selesai proyek | Mulai kapan? Enam bulan berakhir kapan? | Charter, Gantt, Kick-off |
| Anggaran total | Berapa rupiah? Rinciannya untuk apa saja? | Business Case, Charter |
| Nama tokoh (fiktif) | Siapa sponsor, PM, kepala tiap divisi? | Semua dokumen |
| Mitra eksternal | Vendor *cloud*, mitra kurir, mitra pembayaran, kelompok UMKM percontohan? | Stakeholder Register, Risk Register |
| Lingkup rilis 6 bulan | Apakah keempat modul harus lengkap, atau versi awal dulu? | Scope Statement, WBS |

### Hal yang membuat kasus ini menarik untuk dibandingkan

- **Enam bulan untuk empat modul besar itu sangat ketat.** Ini bahan diskusi bagus: PMBOK 4 cenderung mengunci lingkup di awal, sedangkan PMBOK 7 membuka jalan untuk rilis bertahap.
- **Modulnya punya sifat berbeda.** Pembayaran dan keamanan terikat regulasi, jadi butuh kepastian. Rekomendasi AI dan antarmuka penuh ketidakpastian, jadi butuh eksperimen. Perbedaan ini mirip contoh **Sistem Informasi Rumah Sakit** di slide Minggu 04 (slide 43–48), yang dibagi menjadi bagian *waterfall* dan bagian Agile.
- **Banyak pihak eksternal** (kurir, UMKM, regulator, mitra pembayaran). Ini menguji manajemen stakeholder.

**[USULAN]** Regulasi yang mungkin relevan dan perlu dicek sebelum dipakai: UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi, serta aturan Bank Indonesia tentang penyelenggara uang elektronik/sistem pembayaran. Cukup disebut sebagai **kendala dan risiko**. Tidak perlu dibahas mendalam (lihat aturan detail di Bagian 9).

---

## 5. Bagian 1: Dokumen PMBOK 4

### 5.1 Benang merah: angka yang harus sama di semua dokumen

Konsistensi dinilai secara eksplisit. Buat **satu tabel "data induk"** di draf sebelum menulis dokumen apa pun, lalu salin dari situ:

| Data induk | Muncul di |
|---|---|
| Nama proyek, sponsor, PM | Semua dokumen |
| Tanggal mulai, tanggal selesai, *milestone* utama | Business Case (estimasi jadwal) → Charter → Agenda Kick-off → Gantt |
| Anggaran | Business Case → Charter |
| Daftar stakeholder (nama dan peran) | Register → Strategy → Charter (stakeholder utama) → Kick-off (peserta) → Team Contract (anggota tim) |
| Deliverable | Charter (ringkas) → Scope Statement (rinci) → WBS (dipecah) → Gantt (dijadwalkan) |
| Risiko awal | Business Case (risiko potensial) → Charter → Risk Register (rinci) |
| Kode WBS | WBS → Gantt → Risk Register (risiko menempel ke paket kerja) |

### 5.2 Peta 10 dokumen dan sumbernya

Contoh lengkap setiap dokumen ada di slide Minggu 04 (studi kasus **JWD Consulting**, slide 52–83). Urutan dokumennya **persis sama** dengan soal UTS. Jadikan itu cetakan utama.

| No | Dokumen | Tahap (soal) | Contoh di slide Minggu 04 | Slide pendukung | PMBOK 4 (hlm. buku) |
|---|---|---|---|---|---|
| 1 | Stakeholder Register | Pra-Inisiasi | slide 71–72 | 05 hlm 10–12 | 10.1 Identify Stakeholders, hlm 246 |
| 2 | Stakeholder Management Strategy | Pra-Inisiasi | slide 73–75 | 05 hlm 13–15 | 10.1.3.2, hlm 251 |
| 3 | Business Case | Pra-Inisiasi | slide 55–69 (JWD dan RME RS) | 05 hlm 6–9; 07 hlm 10–13 | masukan 4.1, hlm 75 |
| 4 | Project Charter | Inisiasi | slide 76–77 | 05 hlm 16–21; 07 hlm 17–18 | 4.1 Develop Project Charter, hlm 73 |
| 5 | Agenda Kick-off Meeting | Inisiasi | slide 78 | 05 hlm 22–26 | (tidak ada; dari Schwalbe) |
| 6 | Team Contract | Planning | – | 07 hlm 29 | (tidak ada; dari Schwalbe) |
| 7 | Project Scope Statement | Planning | slide 80 | 06 hlm 6–8 | 5.2 Define Scope, hlm 112 |
| 8 | WBS | Planning | slide 81 | 06 hlm 13–17 | 5.3 Create WBS, hlm 116 |
| 9 | Gantt / Milestone Chart | Planning | slide 82 | 06 hlm 18–21 | 6.5 Develop Schedule, hlm 152 (milestone chart hlm 157) |
| 10 | Risk Register | Planning | slide 83 | 06 hlm 29–31 | 11.2–11.5, hlm 282–301 (P×I matrix hlm 291) |

Nomor halaman PDF PMBOK 4 = halaman buku + 31. "05 hlm 12" artinya slide dosen `05. Project-Initiation-...pdf` halaman 12.

### 5.3 Isi minimum setiap dokumen

Setiap dokumen sebaiknya diawali **satu atau dua kalimat**: apa fungsinya dan proses PMBOK 4 mana yang menghasilkannya. Kalimat ini menunjukkan pemahaman metodologi.

#### (1) Stakeholder Register

**Fungsi:** daftar semua pihak yang terlibat atau terdampak proyek.
**Kolom** (gabungan slide 05 hlm 12 dan JWD slide 71): Nama/Pihak · Jabatan · Internal/Eksternal · Peran di proyek · Kepentingan (tinggi/sedang/rendah) · Pengaruh (tinggi/sedang/rendah) · Harapan utama.
**Jumlah:** slide 05 hlm 28 memakai patokan **minimal 8 stakeholder**. Untuk kasus ini wajar 10–14, karena ada 6 divisi ditambah pihak eksternal.
**Jangan lupa pihak eksternal:** UMKM penjual, pembeli, mitra kurir, mitra pembayaran/bank, vendor *cloud*, regulator.

#### (2) Stakeholder Management Strategy

**Fungsi:** cara mengelola setiap stakeholder sesuai posisinya.
**Isi:**
- **Power-Interest Grid** (slide 05 hlm 13), yaitu matriks empat kotak berdasarkan kekuasaan dan kepentingan. **Buat gambarnya.** Ini masuk nilai visualisasi.
- Tabel strategi (JWD slide 73): Nama · Kepentingan · Pengaruh · Kategori kuadran · Strategi.
- Empat strategi kuadran (slide 05 hlm 14): *Manage Closely*, *Keep Satisfied*, *Keep Informed*, *Monitor*.

#### (3) Business Case

**Fungsi:** menjawab "mengapa proyek ini layak dibiayai?"
**Struktur** (slide Minggu 04 slide 55, mengikuti Schwalbe):
1. Pendahuluan/latar belakang
2. Tujuan bisnis
3. Situasi saat ini dan pernyataan masalah/peluang
4. Asumsi kritis dan kendala
5. Analisis opsi dan rekomendasi (minimal 3 opsi, misalnya: tidak berbuat apa-apa / beli platform jadi / bangun sendiri)
6. Kebutuhan awal proyek
7. Estimasi anggaran dan analisis keuangan (**ROI**, *payback period*, atau **NPV**; lihat glosarium dan slide 07 hlm 11–12)
8. Estimasi jadwal
9. Risiko potensial

Studi kelayakan finansial, teknis, dan operasional (slide 05 hlm 9) bisa diringkas di butir 5 atau 7.
**Contoh terdekat:** Business Case RME RS Yogyakarta, slide Minggu 04 slide 64–69.

#### (4) Project Charter

**Fungsi:** dokumen resmi yang **mengesahkan** proyek dan memberi wewenang kepada PM.
**Komponen wajib** (slide 05 hlm 18): judul proyek · tujuan SMART · ringkasan lingkup (termasuk/tidak termasuk) · jadwal tingkat tinggi dengan **minimal 4 milestone** (patokan slide 05 hlm 28) · estimasi anggaran.
**Komponen pendukung:** PM dan wewenangnya · stakeholder utama · asumsi · kendala · **tanda tangan sponsor (simulasi)**.
**Contoh:** JWD slide 77, dan Charter "Aplikasi Mobile Bank Sampah" di slide 05 hlm 20.

#### (5) Agenda Kick-off Meeting

**Fungsi:** rapat pembuka resmi setelah Charter disetujui.
**Soal meminta *agenda*, bukan notulen.** Isinya: judul, tanggal, tujuan rapat, peserta, susunan acara dengan durasi, dan tempat untuk *action items*.
**Pola susunan acara** (slide 05 hlm 24, total sekitar 90 menit): Pembukaan & perkenalan (15') → Latar belakang & tujuan/Business Case (20') → Lingkup & deliverable (20') → Jadwal & milestone (15') → Peran, komunikasi & tanya jawab (20').
**Contoh format tabel:** JWD slide 78.

#### (6) Team Contract

**Fungsi:** kesepakatan tim tentang **cara bekerja sama**, untuk mencegah konflik.
**Isi** (slide 07 hlm 29): norma rapat (jam kerja, rapat daring/luring, toleransi keterlambatan, pencatat notulen) · metode pengambilan keputusan (*voting* atau konsensus) · prosedur penyelesaian konflik dan eskalasi.
**Tambahan yang lazim:** etika kerja, cara berkomunikasi (kanal dan waktu tanggap), partisipasi, tanda tangan anggota.
**Catatan konteks:** ini kontrak **tim proyek Nusantara Express** (enam divisi), bukan kontrak kelompok mahasiswa.

#### (7) Project Scope Statement

**Fungsi:** batas tegas apa yang dikerjakan dan apa yang tidak.
**Lima unsur** (slide 06 hlm 7): tujuan · deliverable · kendala · asumsi · kriteria penerimaan.
**Format contoh** (JWD slide 80): justifikasi proyek, karakteristik produk, deliverable manajemen proyek, deliverable produk, kriteria keberhasilan.
**Wajib ada:** bagian **"Di luar lingkup"** (*out of scope*). Ini senjata utama melawan ***scope creep***, yaitu penambahan pekerjaan diam-diam tanpa persetujuan (slide 06 hlm 8).

#### (8) Work Breakdown Structure (WBS)

**Fungsi:** memecah seluruh pekerjaan menjadi paket-paket kecil yang bisa dikelola.
**Aturan** (slide 06 hlm 13–15): bertingkat, **minimal 3 level** (sama dengan syarat Tugas 2), berorientasi deliverable, dan setiap paket diberi kode (1.1, 1.1.1, …).
**Sajikan dua bentuk:** diagram pohon (visual) dan tabel/daftar berkode (rinci).
**Pengalaman Tugas 2:** [tugas2/PANDUAN_Tugas2.md](../tugas2/PANDUAN_Tugas2.md) Bagian 4 sudah membahas cara menyusun WBS. Gunakan lagi.

#### (9) Project Schedule (Gantt Chart atau Milestone Chart)

**Fungsi:** kapan setiap paket kerja dikerjakan.
**Soal memberi pilihan** Gantt *atau* Milestone Chart. **[USULAN]** Buat **Gantt** (lebih kaya, dan alatnya sudah ada dari Tugas 2), ditambah **daftar milestone** ringkas. Milestone itu harus sama dengan di Charter.
**Isi Gantt:** aktivitas dari WBS (pakai kode WBS) · durasi · ketergantungan · milestone (berbentuk belah ketupat) · **total harus muat dalam 6 bulan**.
**Jalur kritis (CPM)** tidak diwajibkan soal UTS, tetapi baik disebut bila sudah dihitung (slide 06 hlm 20).
**Alat:** skrip ClickUp dan Excel dari Tugas 2 (`tugas2/clickup/`, `tugas2/Gantt_Chart_Project_IT.xlsx`) bisa dipakai ulang.

#### (10) Risk Register

**Fungsi:** daftar risiko beserta penilaian dan responsnya.
**Soal menyebut tiga kolom wajib:** **probabilitas, dampak, mitigasi**.
**Kolom lengkap yang disarankan:** No · Risiko · Kategori · Kode WBS terkait · Probabilitas (1–5) · Dampak (1–5) · Skor (P×D) · Tingkat · Strategi respons · Mitigasi · Pemilik risiko.
**Jumlah:** soal tidak menetapkan. Patokan dosen di tugas lain: 5 risiko (slide 07 hlm 31) dan 8 risiko (Tugas 2). **[USULAN]** 8–10 risiko, mencakup keempat modul.
**Tambahkan Probability-Impact Matrix** (matriks berwarna; PMBOK 4 hlm 291) sebagai visual.
**Contoh berkas dosen:** `tugas2/Contoh Usulan_Risk_Register (FIK_2026).xlsx`.

### 5.4 Kesalahan umum di bagian PMBOK 4

| Kesalahan | Akibat | Pencegahan |
|---|---|---|
| Angka berbeda antardokumen | Nilai "konsistensi" turun | Tabel data induk (5.1) |
| Gantt melebihi 6 bulan | Bertentangan dengan soal | Cek tanggal akhir Gantt terhadap Charter |
| Stakeholder hanya internal | Dokumen terlihat dangkal | Tambahkan UMKM, kurir, regulator, mitra pembayaran |
| WBS berisi kata kerja acak, bukan deliverable | Tidak sesuai kaidah WBS | Level 2 = deliverable/modul, level 3 = paket kerja |
| Risiko umum ("proyek terlambat") | Tidak spesifik | Tulis dengan pola sebab → kejadian → akibat |
| Kick-off ditulis sebagai notulen | Bukan yang diminta | Soal meminta **agenda** |

---

## 6. Bagian 2: Dokumen PMBOK 7

### 6.1 Perubahan cara pikir dari PMBOK 4 ke PMBOK 7

| PMBOK 4 | PMBOK 7 |
|---|---|
| 5 *process group* (kelompok proses) × 9 *knowledge area* (bidang pengetahuan) = 42 proses | **12 prinsip** + **8 *performance domain*** (bidang kinerja) |
| "Lakukan proses ini, hasilkan dokumen itu" | "Pegang prinsip ini, capai hasil di domain itu, pilih cara yang cocok" |
| Sukses = tepat lingkup, waktu, biaya | Sukses = **nilai (*value*)** benar-benar diterima stakeholder |

Sumber: slide 04 hlm 5, slide 08 hlm 4; PMBOK 7 bagian 1.3 (hlm Guide 6).

**Penting:** PMBOK 7 **tidak** menyatakan semua proyek harus Agile. Ia menyebut pendekatan prediktif, adaptif, dan *hybrid* (campuran) sebagai pilihan, dan memilihnya sesuai konteks (*tailoring*). Lihat PMBOK 7 bagian 2.3, hlm Guide 32–50, dan catatan kritis di Bagian 9.

### 6.2 Bagian A: Business Context & Value Delivery

#### (a) Prinsip PMBOK 7 yang relevan (minimal 3–5)

Ke-12 prinsip ada di PMBOK 7 bagian *Standard* bab 3 (hlm 21–59). Soal memberi contoh lima prinsip, dicetak tebal di tabel berikut:

| No | Prinsip (bahasa asli) | Label singkat | Hlm |
|---|---|---|---|
| 3.1 | Be a diligent, respectful, and caring steward | **Stewardship** | 24 |
| 3.2 | Create a collaborative project team environment | Team | 28 |
| 3.3 | Effectively engage with stakeholders | Stakeholders | 31 |
| 3.4 | Focus on value | Value | 34 |
| 3.5 | Recognize, evaluate, and respond to system interactions | **Systems Thinking** | 37 |
| 3.6 | Demonstrate leadership behaviors | **Leadership** | 40 |
| 3.7 | Tailor based on context | **Tailoring** | 44 |
| 3.8 | Build quality into processes and deliverables | Quality | 47 |
| 3.9 | Navigate complexity | Complexity | 50 |
| 3.10 | Optimize risk responses | Risk | 53 |
| 3.11 | Embrace adaptability and resiliency | **Adaptability** | 55 |
| 3.12 | Enable change to achieve the envisioned future state | Change | 58 |

Halaman PDF = halaman bagian *Standard* + 27.

**Cara menulis setiap prinsip (pola 4 langkah):**
1. **Bunyi prinsip:** satu kalimat, dengan rujukan halaman.
2. **Mengapa relevan di Nusantara Express:** kaitkan dengan fakta kasus.
3. **Wujud penerapan:** keputusan atau praktik konkret yang diambil PM.
4. **Bedanya dengan PMBOK 4:** satu kalimat. Ini sekaligus bahan untuk Bagian 3.

**[USULAN] lima prinsip dan alasannya:**

| Prinsip | Kaitan dengan kasus |
|---|---|
| Stewardship (3.1) | Proyek mengelola **uang dan data pribadi** pengguna lewat *digital wallet*. Tanggung jawab etis dan kepatuhan jadi inti. |
| Systems Thinking (3.5) | Empat modul saling bergantung. Contohnya, rekomendasi AI butuh data transaksi *marketplace*, dan pelacakan butuh data logistik. Perubahan satu modul berdampak ke modul lain. |
| Tailoring (3.7) | Modul pembayaran/keamanan butuh kepastian, modul AI/UI butuh eksperimen. Satu cara kerja tidak cocok untuk semua. |
| Adaptability (3.11) | Enam bulan, pasar berubah cepat, kebutuhan UMKM belum pasti. |
| Value (3.4) | Keberhasilan diukur dari adopsi UMKM dan transaksi, bukan sekadar aplikasi selesai dibangun. |

Prinsip lain yang juga kuat: Stakeholders (3.3), karena pihak eksternalnya banyak, dan Complexity (3.9).

#### (b) Value Delivery System (VDS)

**Sumber utama:** slide 08 hlm 5–14 dan 29–34; PMBOK 7 bagian *Standard* bab 2 "A System for Value Delivery" (hlm 7–19).

Ada dua hal yang perlu dijelaskan.

**1. Rantai penciptaan nilai** (slide 08 hlm 5, 9): **Output → Outcome → Benefit → Value**.

**[USULAN]** contoh untuk kasus ini:

```
OUTPUT                 OUTCOME                    BENEFIT                     VALUE
Super app rilis   →    UMKM berjualan dan     →   GMV naik X%, waktu       →  Posisi PT ND sebagai
(4 modul)              pembeli memakai            kirim turun Y%, biaya       ekosistem digital UMKM;
                       wallet & tracking          operasional turun Z%        inklusi digital
```
(GMV = *Gross Merchandise Value*, total nilai transaksi. Nilai X, Y, Z ditetapkan sendiri dan dipakai sebagai KPI; lihat slide 08 hlm 34.)

**2. Lapisan organisasi** (slide 08 hlm 10–23): tujuan strategis → *governance* (tata kelola) → portofolio → program → **proyek** → produk.
Jelaskan di mana proyek Super App berada. **[USULAN]**: portofolio "Transformasi Digital", program "Ekosistem UMKM", proyek "Super App rilis 6 bulan", lalu produk yang terus dikembangkan setelah proyek selesai.
Sebutkan juga **siapa yang memastikan manfaat** setelah proyek ditutup (*benefit realization*, slide 08 hlm 33). Inilah bedanya dengan PMBOK 4, yang berhenti di *Closing*.

**Template yang bisa dipakai langsung:** "Template Analisis Value" slide 08 hlm 30 (Tujuan · Stakeholder · Benefit · Cost · Risk · ROI/Value).

### 6.3 Bagian B: Stakeholder & Team Domain

Di PMBOK 7, ini **dua domain terpisah**:
- **Stakeholder Performance Domain**, bagian 2.1, hlm Guide 8–15
- **Team Performance Domain**, bagian 2.2, hlm Guide 16–31

Soal menggabungkannya. Tulis dua sub-bagian agar jelas.

#### (a) Strategi kolaborasi dan komunikasi dengan stakeholder

- PMBOK 7 memandang keterlibatan stakeholder sebagai **kegiatan terus-menerus**: identifikasi → pahami → prioritaskan → libatkan → pantau (hlm Guide 10–14). Bandingkan dengan PMBOK 4, yang menempatkannya di awal proyek.
- **Alat yang disarankan:** *Stakeholder Engagement Assessment Matrix* (PMBOK 7 hlm Guide 189). Matriks ini membandingkan tingkat keterlibatan **saat ini** dan **yang diinginkan** (*unaware, resistant, neutral, supportive, leading*) untuk setiap stakeholder. Ini bukan pengulangan Power-Interest Grid.
- Rencana komunikasi per kelompok: kanal, frekuensi, bentuk. Contohnya *sprint review*/demo untuk UMKM percontohan, laporan eksekutif untuk direksi, rapat kepatuhan dengan Legal.
- Perspektif nilai tiap stakeholder (slide 08 hlm 14): manajemen, pengguna, regulator, investor, tim TI.

#### (b) Pembentukan tim adaptif dan pembagian tanggung jawab

- Struktur tim. **[USULAN]**: tim lintas fungsi per modul (misalnya Tim Marketplace, Tim Logistik, Tim Wallet, Tim AI). Setiap tim berisi anggota dari beberapa divisi, ditambah tim pendukung (Infra & Security, Legal).
- Gaya kepemimpinan: *servant leadership* (pemimpin yang melayani dan menyingkirkan hambatan tim; PMBOK 7 hlm Guide 17).
- Pembagian tanggung jawab: **RACI Matrix** (siapa *Responsible, Accountable, Consulted, Informed*; slide 06 hlm 27). Bisa juga peran Agile seperti *Product Owner* per modul.
- ***Team charter***: istilah PMBOK 7 (hlm Guide 19) yang setara dengan **Team Contract** di PMBOK 4. Ini pasangan yang bagus untuk dibandingkan.

### 6.4 Bagian C: Planning Performance Domain

**Sumber:** PMBOK 7 bagian 2.4, hlm Guide 51–68. Bagian 2.3 (*Development Approach*, hlm 32–50) dan 2.8 (*Uncertainty*, hlm 116–129) juga perlu dirujuk.

#### (a) Pendekatan perencanaan adaptif/incremental

- Jelaskan **pendekatan pengembangan yang dipilih dan alasannya**. **[USULAN] *Hybrid***:
  - Prediktif untuk infrastruktur, keamanan, dan kepatuhan pembayaran.
  - Adaptif (*sprint* 2 minggu) untuk antarmuka, fitur *marketplace*, dan rekomendasi AI.

  Ini meniru pola kasus RS di slide Minggu 04 slide 46–48, dan diskusi JWD di slide 90.
- **Perencanaan bertingkat:** *roadmap* 6 bulan → rencana rilis → rencana *sprint*. Tingkat rinci menyesuaikan jarak waktu (*rolling wave planning*, PMBOK 7 hlm Guide 49).
- **Rilis *incremental*:** misalnya **MVP** (*Minimum Viable Product*, versi paling sederhana yang sudah berguna; PMBOK 7 hlm Guide 41) di bulan ke-3 untuk satu kota atau kelompok UMKM percontohan, lalu ditambah fitur sampai bulan ke-6. **[USULAN]**
- **Kaitkan dengan jadwal PMBOK 4:** milestone tetap dipakai, tetapi isi rilis bisa berubah lewat prioritas ulang *backlog* (daftar kebutuhan yang terus diurutkan).

#### (b) Strategi manajemen risiko berbasis kompleksitas dan ketidakpastian

PMBOK 7 membedakan beberapa jenis ketidakpastian (hlm Guide 119–122). Petakan risiko proyek ke dalamnya:

| Jenis | Arti | Contoh di kasus | Cara menghadapi |
|---|---|---|---|
| *Ambiguity* | Belum jelas apa yang sebenarnya dibutuhkan | Fitur AI apa yang benar-benar dipakai UMKM? | Eksperimen, prototipe, umpan balik cepat |
| *Complexity* | Banyak bagian saling memengaruhi | Integrasi 4 modul dan banyak mitra | *Systems thinking*, uji integrasi lebih awal, pecah per modul |
| *Volatility* | Kondisi berubah cepat | Regulasi, persaingan, harga *cloud* | Cadangan waktu/biaya, opsi alternatif |
| *Risk* | Kejadian tak pasti dengan dampak terukur | Kebocoran data, mitra kurir terlambat | Respons risiko seperti di Risk Register |

**Alat bantu yang disebut PMBOK 7:** Stacey Matrix dan Cynefin (hlm Guide 164–165). Keduanya memetakan tingkat kompleksitas untuk memilih pendekatan. Cukup dijelaskan singkat bila dipakai.

**Poin pembeda yang harus muncul:** di PMBOK 4 risiko dikelola terutama lewat **daftar** (Risk Register). Di PMBOK 7 ketidakpastian juga dikelola lewat **cara kerja**: rilis kecil, umpan balik cepat, dan cadangan (*reserve*).

---

## 7. Bagian 3: Analisis komparatif

Bagian ini bernilai **25 poin** dengan kriteria "**kedalaman**".

### 7.1 Tiga tingkat kedalaman

| Tingkat | Contoh kalimat | Nilai |
|---|---|---|
| 1. Deskriptif | "PMBOK 4 berbasis proses, PMBOK 7 berbasis prinsip." | Rendah: semua orang bisa menyalin ini |
| 2. Analitis | "…karena itu di PMBOK 4 lingkup dikunci di Scope Statement, sedangkan di PMBOK 7 lingkup dibiarkan berkembang lewat *backlog*." | Sedang |
| 3. Evaluatif + kontekstual | "…untuk modul *wallet*, penguncian lingkup gaya PMBOK 4 justru lebih tepat karena perubahan berisiko melanggar aturan pembayaran. Untuk modul AI, pendekatan PMBOK 7 lebih tepat karena kebutuhannya belum diketahui." | **Tinggi**: inilah yang dicari |

Targetnya: **setiap baris perbandingan mencapai tingkat 3.**

### 7.2 Dimensi pembanding yang disarankan

Gunakan tabel dengan kolom: **Dimensi · PMBOK 4 · PMBOK 7 · Bukti di laporan ini · Implikasi untuk Nusantara Express**.

| Dimensi | PMBOK 4 | PMBOK 7 | Pasangan dokumen di laporan |
|---|---|---|---|
| Dasar kerangka | 42 proses, 9 *knowledge area* | 12 prinsip, 8 domain | — |
| Ukuran keberhasilan | Lingkup, waktu, biaya terpenuhi | Nilai/manfaat diterima | Business Case ↔ VDS |
| Lingkup | Ditetapkan di awal, perubahan lewat *change control* formal | Berkembang lewat prioritas *backlog* | Scope Statement & WBS ↔ perencanaan adaptif |
| Jadwal | Gantt dengan *baseline* (rencana acuan) | *Roadmap*, rilis, *sprint* | Gantt ↔ rencana rilis |
| Stakeholder | Diidentifikasi dan diberi strategi di awal | Keterlibatan terus-menerus dan dipantau | Register & Strategy ↔ *engagement matrix* |
| Tim | Peran ditetapkan, kontrak tim | Tim lintas fungsi, *servant leadership*, *team charter* | Team Contract ↔ tim adaptif |
| Risiko | Register, P×I, mitigasi | Ketidakpastian, kompleksitas, adaptasi | Risk Register ↔ strategi ketidakpastian |
| Dokumentasi | Banyak dokumen formal | "Secukupnya", disesuaikan (*tailoring*) | Seluruh laporan |
| Kapan cocok | Kebutuhan stabil, regulasi ketat | Kebutuhan berubah, inovasi | Modul *wallet* ↔ modul AI |

Bahan perbandingan siap pakai: slide Minggu 04 slide 42 (relevansi edisi 4) dan slide 90 (JWD prediktif vs Agile).

### 7.3 Tambahkan sintesis, bukan hanya perbedaan

Akhiri bagian ini dengan **kesimpulan rekomendasi**. Misalnya: "Untuk Nusantara Express, pendekatan terbaik adalah kombinasi: dokumen dan kendali PMBOK 4 untuk bagian X, prinsip dan cara kerja PMBOK 7 untuk bagian Y." Sertakan alasannya.

Pendukung dari materi: slide Minggu 04 slide 41–42 menjelaskan bahwa PMBOK 8 (2025) **menghidupkan kembali** kelompok proses sebagai *Focus Areas* dan memadukannya dengan prinsip. Jadi kedua cara pandang memang saling melengkapi, bukan saling menggantikan.

---

## 8. Bagian 4: Refleksi manajerial

Bobotnya **15 poin**, dengan kriteria: *insight* pribadi, argumentasi, dan konteks proyek TI.

**Bedanya dengan analisis komparatif:** komparatif membahas **kedua kerangka**. Refleksi membahas **kalian sebagai manajer**: apa yang dipelajari, apa yang akan dilakukan berbeda, dan mengapa.

**Pertanyaan pemandu** (pilih 3–4, jawab dengan argumen):
1. Dokumen PMBOK 4 mana yang paling **berguna**, dan mana yang terasa paling **formalitas**, untuk proyek seperti ini? Mengapa?
2. Bagian mana yang **paling sulit** ditulis dengan cara pandang PMBOK 7? Apa artinya bagi manajer proyek?
3. Apakah target 6 bulan **realistis**? Bagaimana kalian akan berbicara dengan sponsor soal ini?
4. Kalau benar-benar menjadi PM proyek ini, **satu keputusan pertama** apa yang akan diambil, dan prinsip apa yang mendasarinya?
5. Apa kaitannya dengan pengalaman kerja/proyek TI kalian sendiri, atau dengan kasus nasional dari slide (PDNS 2, Coretax DJP; slide Minggu 04 slide 32–34)?

**Ciri refleksi yang baik:** memakai kata "saya/kami", berpendapat dan memberi alasan, berani menyebut kelemahan, dan merujuk ke dokumen yang sudah dibuat.
**Hindari:** ringkasan ulang teori, atau kalimat umum seperti "kedua edisi sama-sama penting".

Bila dikerjakan berkelompok, lihat pertanyaan untuk dosen di Bagian 12.

---

## 9. Catatan kritis atas soal

Beberapa hal di soal tidak persis sama dengan isi PMBOK. **[USULAN]** Ikuti struktur soal, karena penilai memeriksa sesuai soal. Lalu tambahkan **catatan singkat** di laporan, misalnya di kotak catatan atau catatan kaki, untuk menunjukkan pemahaman. Jangan dijadikan bab tersendiri.

| No | Di soal | Di PMBOK | Saran |
|---|---|---|---|
| 1 | Stakeholder Register dan Strategy masuk **Pra-Inisiasi** | PMBOK 4: keduanya hasil proses 10.1 *Identify Stakeholders* di **Initiating** (hlm 246–251). Slide Minggu 04 slide 70–75 juga menaruhnya di Inisiasi. | Ikuti soal, beri catatan |
| 2 | Business Case, Kick-off, Team Contract disebut "dokumen PMBOK 4" | Ketiganya dari buku Schwalbe. PMBOK 4 hanya menyebut *business case* sebagai **masukan** Charter (hlm 75) | Sebut sumbernya Schwalbe dan materi kuliah |
| 3 | "Sembilan area pengetahuan" | Benar untuk PMBOK 4. Slide 06 hlm 5 menyebut **10**, karena itu versi PMBOK 5/6 (menambah *Stakeholder Management*) | Pakai **9** di bagian PMBOK 4 |
| 4 | "Stakeholder & Team Domain" | Dua domain terpisah (2.1 dan 2.2) | Tulis dua sub-bagian |
| 5 | Risiko di bawah "Planning Domain" | Ketidakpastian punya domain sendiri, *Uncertainty* (2.8) | Rujuk 2.4 dan 2.8 sekaligus |
| 6 | Kesan bahwa PMBOK 4 = *waterfall* dan PMBOK 7 = Agile | PMBOK 7 mendukung prediktif, adaptif, dan *hybrid*. PMBOK 4 juga mengakui proses berulang | Hindari dikotomi sederhana di analisis komparatif |

**Pengingat tingkat detail:** yang dinilai adalah **dokumen manajemen proyek**, bukan desain teknis aplikasi. Arsitektur sistem, model AI, atau alur API tidak perlu dirinci. Cukup disebut sebagai deliverable atau risiko.

---

## 10. Susunan laporan PDF

**[USULAN]** kerangka laporan:

```
Halaman judul (logo, judul, nama/NIM, dosen, mata kuliah PJ059)
Daftar isi · daftar tabel · daftar gambar
BAB 1  Pendahuluan
       1.1 Ringkasan studi kasus Nusantara Express
       1.2 Asumsi proyek (tabel data induk)
       1.3 Sistematika laporan
BAB 2  Dokumen PMBOK 4th Edition
       2.1 Pra-Inisiasi: Stakeholder Register · Stakeholder Mgmt Strategy (+ grid) · Business Case
       2.2 Inisiasi: Project Charter · Agenda Kick-off Meeting
       2.3 Planning: Team Contract · Scope Statement · WBS (+ diagram) · Gantt · Risk Register (+ matriks P×I)
BAB 3  Dokumen PMBOK 7th Edition
       3.1 Business Context & Value Delivery (prinsip + diagram VDS/rantai nilai)
       3.2 Stakeholder & Team Domain
       3.3 Planning Performance Domain (+ roadmap rilis, peta ketidakpastian)
BAB 4  Analisis Komparatif (tabel dimensi + sintesis rekomendasi)
BAB 5  Refleksi Manajerial
BAB 6  Kesimpulan
Glosarium
Daftar Pustaka
Lampiran (tabel besar, Gantt ukuran penuh)
```

### Visual yang disarankan (untuk nilai format 10%)

| Visual | Bab |
|---|---|
| Power-Interest Grid | 2.1 |
| Diagram pohon WBS | 2.3 |
| Gantt Chart dan daftar milestone | 2.3 |
| Probability-Impact Matrix berwarna | 2.3 |
| Rantai Output → Outcome → Benefit → Value | 3.1 |
| Struktur tim adaptif / RACI | 3.2 |
| *Roadmap* rilis 6 bulan | 3.3 |
| Tabel perbandingan PMBOK 4 vs 7 | 4 |

---

## 11. Tahapan pengerjaan dalam 5 hari

**[USULAN]** urutan kerja. Prinsipnya: bahan komparatif **dicatat sejak hari pertama**, bukan ditulis di akhir.

| Hari | Kegiatan | Hasil |
|---|---|---|
| **1** | Baca panduan ini dan slide Minggu 04 slide 52–90. Tetapkan **data induk** (tanggal, anggaran, tokoh, lingkup). Tulis Stakeholder Register, Strategy (+ grid), Business Case | Pra-Inisiasi selesai |
| **2** | Charter, Agenda Kick-off, Team Contract, Scope Statement | Inisiasi dan awal Planning |
| **3** | WBS, Gantt (6 bulan), Risk Register (+ matriks). Cek konsistensi dengan tabel 5.1 | PMBOK 4 selesai |
| **4** | PMBOK 7: prinsip, VDS, Stakeholder & Team, Planning & ketidakpastian | PMBOK 7 selesai |
| **5** | Analisis komparatif, refleksi, kesimpulan, glosarium, daftar pustaka. Rapikan format, buat PDF, **unggah ke Waskita sebelum 23.59** | PDF terkumpul |

**Kebiasaan harian:** setiap selesai satu dokumen PMBOK 4, catat satu kalimat di berkas draf: "Kalau dengan PMBOK 7, bagian ini akan…". Catatan ini menjadi bahan utama Bab 4.

**Penjaga konsistensi:**
- **Kerja individu (saat ini):** peran ini dipegang sendiri. Di Hari 3 dan Hari 5, cocokkan semua dokumen dengan tabel data induk (Bagian 5.1).
- **Bila nanti terbentuk kelompok:** pembagian kerja per bab. Satu orang menjadi penjaga konsistensi, yaitu memegang tabel data induk dan memeriksa semua dokumen di Hari 3 dan 5.

**[USULAN] struktur folder** (mengikuti pola tugas sebelumnya, belum dibuat): `uts/soal/` (berkas .docx soal), `uts/draf/` (Markdown per bab), `uts/hasil/` (PDF final).

---

## 12. Daftar periksa dan pertanyaan untuk dosen

### Daftar periksa sebelum mengunggah

**PMBOK 4**
- [ ] Sepuluh dokumen ada, berurutan sesuai soal
- [ ] Data induk sama di semua dokumen (nama, tanggal, anggaran, milestone)
- [ ] Stakeholder minimal 8, termasuk pihak eksternal; grid Power-Interest ada
- [ ] Business Case memuat analisis opsi dan analisis keuangan
- [ ] Charter memuat tujuan SMART, minimal 4 milestone, anggaran, tanda tangan sponsor
- [ ] Kick-off berbentuk **agenda**
- [ ] Scope Statement memuat bagian "di luar lingkup" dan kriteria penerimaan
- [ ] WBS minimal 3 level dan berkode; Gantt memakai kode WBS dan **berakhir ≤ 6 bulan**
- [ ] Risk Register memuat probabilitas, dampak, mitigasi; matriks P×I ada

**PMBOK 7**
- [ ] 3–5 prinsip, masing-masing dengan pola 4 langkah
- [ ] VDS: rantai nilai dan posisi proyek di lapisan organisasi; KPI disebut
- [ ] Stakeholder dan Team ditulis sebagai dua sub-bagian
- [ ] Pendekatan perencanaan (*hybrid*/adaptif) beserta alasannya
- [ ] Risiko dipetakan ke jenis ketidakpastian

**Komparatif, refleksi, format**
- [ ] Setiap baris perbandingan mencapai tingkat 3 (evaluatif + kontekstual)
- [ ] Ada sintesis/rekomendasi
- [ ] Refleksi berisi pendapat pribadi beserta alasannya
- [ ] Semua tabel dan gambar bernomor dan berjudul; istilah dijelaskan; glosarium ada
- [ ] Berkas berformat **PDF**; nama berkas sesuai ketentuan (bila ada)

### Pertanyaan yang perlu ditanyakan ke dosen

1. *(Relevan bila jadi berkelompok)* Apakah **refleksi manajerial** ditulis per anggota (karena kriterianya "*insight* pribadi") atau satu untuk kelompok?
2. Apakah ada batas jumlah halaman atau format penamaan berkas? (Tugas di slide 05 hlm 28 memakai pola `NIM_Nama_Tugas5.pdf`.)
3. Penempatan Stakeholder Register di Pra-Inisiasi (soal) berbeda dengan PMBOK 4 (Initiating). Cukup mengikuti soal?
4. Bolehkah angka anggaran dan nama tokoh sepenuhnya fiktif?

---

## 13. Glosarium

| Istilah | Penjelasan singkat |
|---|---|
| Adaptif (*adaptive*) | Pendekatan yang merencanakan dan mengerjakan secara bertahap sambil menyesuaikan diri dengan umpan balik; contohnya Agile |
| Agile | Keluarga pendekatan kerja iteratif, misalnya Scrum dan Kanban (slide 04) |
| *Ambiguity* | Ketidakjelasan tentang apa yang sebenarnya dibutuhkan atau terjadi |
| *Backlog* | Daftar kebutuhan/fitur yang diurutkan berdasarkan prioritas dan bisa diurutkan ulang |
| *Baseline* | Versi rencana yang disetujui dan menjadi acuan pembanding kemajuan |
| *Benefit realization* | Upaya memastikan manfaat proyek benar-benar tercapai, termasuk setelah proyek selesai |
| *Business Case* | Dokumen justifikasi bisnis: mengapa proyek layak dibiayai |
| *Change control* | Prosedur formal untuk menyetujui atau menolak perubahan |
| *Complexity* | Kondisi ketika banyak bagian saling memengaruhi sehingga akibat sulit diramalkan |
| CPM (*Critical Path Method*) | Metode mencari rangkaian aktivitas terpanjang yang menentukan durasi proyek |
| Cynefin / Stacey Matrix | Model untuk memetakan tingkat kompleksitas masalah dan memilih pendekatan |
| *Deliverable* | Hasil kerja yang harus diserahkan |
| *Digital wallet* | Dompet digital; saldo uang elektronik di aplikasi |
| GMV (*Gross Merchandise Value*) | Total nilai transaksi barang di *marketplace* |
| *Governance* | Tata kelola: sistem pengarahan, pengawasan, dan pengambilan keputusan |
| Gantt Chart | Diagram batang jadwal aktivitas pada sumbu waktu |
| *Hybrid* | Gabungan pendekatan prediktif dan adaptif dalam satu proyek |
| *Incremental* | Produk dirilis sebagian demi sebagian, setiap bagian sudah bisa dipakai |
| *Kick-off meeting* | Rapat pembuka resmi proyek setelah Charter disetujui |
| KPI (*Key Performance Indicator*) | Indikator terukur untuk menilai pencapaian |
| *Knowledge area* | Bidang pengetahuan manajemen proyek di PMBOK 4 (9 bidang: integrasi, lingkup, waktu, biaya, mutu, SDM, komunikasi, risiko, pengadaan) |
| *Milestone* | Titik penting di jadwal, berdurasi nol, misalnya "MVP dirilis" |
| MVP (*Minimum Viable Product*) | Versi produk paling sederhana yang sudah berguna bagi pengguna |
| NPV (*Net Present Value*) | Nilai sekarang dari selisih manfaat dan biaya di masa depan |
| *Omni-channel* | Layanan menyatu di berbagai saluran (aplikasi, web, toko fisik) |
| *Output / Outcome / Benefit / Value* | Hasil fisik → perubahan perilaku → manfaat terukur → dampak strategis jangka panjang (slide 08 hlm 9) |
| *Payback period* | Lama waktu sampai investasi kembali modal |
| *Performance domain* | Kelompok kegiatan yang saling terkait dan menentukan keberhasilan proyek (PMBOK 7 punya 8) |
| PMBOK | *Project Management Body of Knowledge*, buku standar manajemen proyek terbitan PMI |
| PMI | *Project Management Institute*, lembaga standar manajemen proyek |
| Power-Interest Grid | Matriks empat kotak untuk memetakan stakeholder berdasarkan kekuasaan dan kepentingan |
| Prediktif (*predictive*) | Pendekatan yang menetapkan lingkup, jadwal, dan biaya di awal; sering disebut *waterfall* |
| Prinsip (*principle*) | Pedoman perilaku dan keputusan; PMBOK 7 punya 12 |
| Probability-Impact Matrix | Matriks untuk menilai risiko dari peluang terjadi dan besar dampaknya |
| *Process group* | Kelompok proses PMBOK 4: Initiating, Planning, Executing, Monitoring & Controlling, Closing |
| *Project Charter* | Dokumen resmi yang mengesahkan proyek dan memberi wewenang kepada PM |
| RACI Matrix | Tabel pembagian peran: *Responsible* (mengerjakan), *Accountable* (penanggung jawab akhir), *Consulted* (dimintai pendapat), *Informed* (diberi tahu) |
| *Real-time tracking* | Pemantauan posisi secara langsung saat itu juga |
| *Risk Register* | Daftar risiko beserta penilaian dan rencana responsnya |
| *Roadmap* | Peta rencana rilis tingkat tinggi dalam rentang waktu |
| *Rolling wave planning* | Merencanakan rinci untuk waktu dekat dan garis besar untuk waktu jauh, lalu dirinci bertahap |
| ROI (*Return on Investment*) | Perbandingan keuntungan dengan biaya investasi |
| *Scope creep* | Penambahan lingkup diam-diam tanpa persetujuan formal |
| *Scope Statement* | Dokumen batas lingkup proyek: tujuan, deliverable, kendala, asumsi, kriteria penerimaan |
| *Servant leadership* | Gaya memimpin dengan melayani tim dan menyingkirkan hambatan |
| SMART | Tujuan yang *Specific, Measurable, Achievable, Relevant, Time-bound* (spesifik, terukur, bisa dicapai, relevan, berbatas waktu) |
| *Sprint* | Siklus kerja pendek (biasanya 2 minggu) dalam Scrum |
| *Stakeholder* | Pemangku kepentingan: pihak yang terlibat atau terdampak proyek |
| *Stakeholder Engagement Assessment Matrix* | Matriks yang membandingkan tingkat keterlibatan stakeholder saat ini dan yang diinginkan |
| *Stewardship* | Sikap bertanggung jawab, etis, dan peduli dalam mengelola sumber daya dan kepercayaan |
| *Super app* | Satu aplikasi yang menggabungkan banyak layanan |
| *Systems thinking* | Melihat proyek sebagai sistem yang bagian-bagiannya saling memengaruhi |
| *Tailoring* | Menyesuaikan pendekatan, proses, dan dokumen dengan konteks proyek |
| *Team Contract / Team charter* | Kesepakatan tim tentang cara bekerja sama |
| UMKM | Usaha Mikro, Kecil, dan Menengah |
| *Value Delivery System* | Kerangka PMBOK 7 yang menghubungkan strategi, tata kelola, portofolio, program, proyek, dan produk untuk menghasilkan nilai |
| *Volatility* | Kondisi yang berubah cepat dan tidak terduga |
| Waskita | LMS (sistem pembelajaran daring) kampus, tempat mengunggah UTS |
| WBS (*Work Breakdown Structure*) | Pemecahan pekerjaan proyek secara bertingkat menjadi paket kerja |
| *Work package* | Paket kerja: tingkat terendah WBS yang bisa dijadwalkan dan dianggarkan |

---

## 14. Rujukan

**Materi dosen (folder `materi/`)**
- Slide Minggu 04, Emha Taufiq Luthfi (13 Okt 2026): slide 20 (*tailoring*), 32–34 (PDNS 2, Coretax), 41–42 (PMBOK 8 dan relevansi edisi 4), 43–48 (kasus RS: versi PMBOK 4 vs 7), 52–83 (studi kasus JWD: contoh semua dokumen), 90 (JWD prediktif vs Agile).
- Slide Melwin Syafrizal: `04` Metodologi (hlm 5: PMBOK 4 vs 7), `05` Inisiasi (Business Case, Stakeholder, Charter, Kick-off), `06` Planning (Scope, WBS, Schedule, RACI, Risk), `07` Integrasi (keuangan hlm 11–13, Team Contract hlm 29), `08` Value Delivery System.
- PMI. (2008). *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)* (4th ed.). Halaman PDF = halaman buku + 31.
- PMI. (2021). *The Standard for Project Management and A Guide to the Project Management Body of Knowledge (PMBOK® Guide)* (7th ed.). Halaman PDF = halaman *Standard* + 27; halaman *Guide* + 95.

**Acuan buku yang dipakai slide**
- Schwalbe, K. (2010). *Managing Information Technology Projects* (6th ed.). Course Technology, Cengage Learning. Sumber studi kasus JWD, Business Case, Team Contract, dan Kick-off.

**Bekal dari tugas sebelumnya**
- [tugas2/PANDUAN_Tugas2.md](../tugas2/PANDUAN_Tugas2.md): cara menyusun WBS, Gantt, dan Risk Register.
- `tugas2/clickup/`: skrip pembuat Gantt di ClickUp.
- `tugas2/Contoh Usulan_Risk_Register (FIK_2026).xlsx`: contoh format Risk Register dari dosen.
