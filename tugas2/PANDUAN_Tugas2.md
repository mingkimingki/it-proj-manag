# Panduan Tugas 2 (Kelompok): WBS, Jadwal, dan Daftar Risiko Proyek TI

> Berkas kerja: panduan untuk memahami dan mengerjakan Tugas 2.
> Sumber soal: gambar `Tugas 2 (Kelompok).png`, sama dengan slide dosen Pertemuan 6 (`06. Project-Planning-Core-PMBOK.pdf`, hlm. 34).
> Aturan penulisan: setiap istilah asing dijelaskan singkat saat pertama kali muncul, lalu dikumpulkan di **Glosarium** (Bagian 12).
> Contoh "website toko kue" di panduan ini hanya **ilustrasi**. Proyek yang dikerjakan tetap pilihan kelompok.

---

## Daftar isi

1. [Tugas ini sebenarnya apa?](#1-tugas-ini-sebenarnya-apa)
2. [Yang dikumpulkan dan cara dinilai](#2-yang-dikumpulkan-dan-cara-dinilai)
3. [Gambaran besar: tiga dokumen yang saling terhubung](#3-gambaran-besar-tiga-dokumen-yang-saling-terhubung)
4. [Bagian 1: WBS](#4-bagian-1-wbs-daftar-pekerjaan-bertingkat)
5. [Bagian 2: Gantt Chart dan jadwal](#5-bagian-2-gantt-chart-dan-jadwal)
6. [Bagian 3: Risk Register](#6-bagian-3-risk-register-daftar-risiko)
7. [Dua berkas contoh dari dosen: apa yang ditiru, apa yang tidak](#7-dua-berkas-contoh-dari-dosen-apa-yang-ditiru-apa-yang-tidak)
8. [Tahapan pengerjaan langkah demi langkah](#8-tahapan-pengerjaan-langkah-demi-langkah)
9. [Susunan dokumen PDF dan slide presentasi](#9-susunan-dokumen-pdf-dan-slide-presentasi)
10. [Daftar periksa sebelum mengumpulkan](#10-daftar-periksa-sebelum-mengumpulkan)
11. [Hal yang perlu ditanyakan ke dosen](#11-hal-yang-perlu-ditanyakan-ke-dosen)
12. [Glosarium](#12-glosarium)
13. [Rujukan](#13-rujukan)

---

## 1. Tugas ini sebenarnya apa?

Bayangkan kelompok kalian disewa untuk membuat sebuah sistem TI. Sebelum satu baris kode pun ditulis, klien meminta **rencana kerja** yang menjawab tiga pertanyaan:

1. **Apa saja yang harus dikerjakan?** → dijawab oleh **WBS**
2. **Kapan setiap pekerjaan dikerjakan, dan berapa lama?** → dijawab oleh **Gantt Chart dan jadwal**
3. **Apa yang bisa membuat proyek gagal, dan bagaimana mencegahnya?** → dijawab oleh **Risk Register**

Itulah isi Tugas 2. Proyeknya **tidak perlu dibuat sungguhan**. Yang dinilai adalah **rencananya**.

Soal menyebut tugas ini harus "mengintegrasikan seluruh *knowledge area*" menjadi satu dokumen yang "kohesif". *Knowledge area* (bidang pengetahuan) adalah pembagian topik manajemen proyek di PMBOK, misalnya lingkup (*scope*), jadwal (*schedule*), dan risiko (*risk*). **PMBOK** (*Project Management Body of Knowledge*) adalah buku standar manajemen proyek dari PMI, rujukan utama mata kuliah ini. "Kohesif" berarti ketiga dokumen **saling nyambung**, bukan tiga tabel terpisah (lihat Bagian 3).

---

## 2. Yang dikumpulkan dan cara dinilai

### Yang dikumpulkan

| No | Berkas | Keterangan |
|---|---|---|
| 1 | **Dokumen PDF** | Laporan berisi WBS, jadwal, dan daftar risiko beserta penjelasannya |
| 2 | **Berkas dari alat digital** | Berkas asli dari aplikasi manajemen proyek. Soal menyebut **Jira, ClickUp, atau MS Project** |
| 3 | **Presentasi 10 menit** | Satu presentasi untuk satu kelompok |

### Syarat minimum per bagian

| Bagian | Syarat dari soal |
|---|---|
| WBS | Minimal **3 level**; semua *work package* yang relevan tercantum; dibuat dengan **alat digital** |
| Jadwal | Berbentuk **Gantt Chart**; ada **estimasi durasi**, **ketergantungan aktivitas**, **milestone**, dan **jalur kritis** |
| Risk Register | Minimal **8 risiko proyek**; dianalisis dengan **Probability-Impact Matrix**; tiap risiko punya **rencana respons yang rinci** |

### Cara dinilai

| Kriteria | Bobot | Artinya dalam praktik |
|---|---|---|
| Kelengkapan dan kedalaman konten | 40% | Semua syarat di atas terpenuhi, isinya masuk akal dan tidak dangkal |
| Ketepatan penggunaan metodologi PMBOK | 40% | Istilah, proses, dan teknik PMBOK dipakai dengan benar dan **disebut namanya** |
| Kualitas presentasi dan komunikasi | 20% | Presentasi jelas, runtut, dan tepat 10 menit |

**Pelajaran dari bobot ini:** metodologi bobotnya sama dengan isi. Jadi jangan hanya mengisi tabel. Tulis juga **teknik PMBOK apa yang dipakai dan mengapa**. Contohnya: "durasi diperkirakan dengan *three-point estimation*", "urutan ditentukan dengan *Precedence Diagramming Method*", "jalur kritis dihitung dengan *Critical Path Method*".

---

## 3. Gambaran besar: tiga dokumen yang saling terhubung

```
        RINGKASAN PROYEK (lingkup)
                  │
                  ▼
   ┌─────────────────────────────┐
   │ 1. WBS                      │  "Apa yang dikerjakan?"
   │    1.3.2 Keranjang & pesan  │
   └──────────────┬──────────────┘
                  │ kode yang sama
                  ▼
   ┌─────────────────────────────┐
   │ 2. JADWAL / GANTT           │  "Kapan dan berapa lama?"
   │    1.3.2 → 6 hari, jalur    │
   │    kritis                   │
   └──────────────┬──────────────┘
                  │ pekerjaan yang terancam
                  ▼
   ┌─────────────────────────────┐
   │ 3. RISK REGISTER            │  "Apa yang bisa salah?"
   │    R-03: programmer sakit   │
   │    saat 1.3.2 → proyek telat│
   └──────────────┬──────────────┘
                  │ respons risiko bisa
                  │ menambah pekerjaan/waktu
                  └──────► kembali perbarui WBS & jadwal
```

Tiga prinsip supaya dokumennya kohesif:

1. **Kode WBS dipakai di mana-mana.** Pekerjaan "1.3.2" di WBS juga bernama "1.3.2" di jadwal dan di daftar risiko.
2. **Risiko diambil dari WBS dan jadwal.** Pekerjaan yang berada di jalur kritis atau bergantung pada pihak luar adalah sumber risiko paling penting.
3. **Respons risiko kembali ke rencana.** Kalau respons sebuah risiko berupa "tambah waktu cadangan 2 hari" atau "tambah pekerjaan uji keamanan", tambahkan juga ke WBS dan jadwal. Inilah arti "integrasi" di slide 07.

---

## 4. Bagian 1: WBS (daftar pekerjaan bertingkat)

### 4.1 Pengertian

**WBS** (*Work Breakdown Structure*) adalah pemecahan **seluruh** pekerjaan proyek menjadi bagian-bagian yang makin kecil, tersusun bertingkat seperti daftar isi buku. Proses ini di PMBOK disebut **dekomposisi** (*decomposition*), yaitu memecah sesuatu yang besar menjadi bagian kecil.

Bagian paling bawah disebut **work package** (paket kerja): unit pekerjaan yang sudah cukup kecil untuk diberi penanggung jawab, diperkirakan durasi dan biayanya, lalu dipantau kemajuannya (slide 06, hlm. 13).

### 4.2 Level menurut slide dosen (slide 06, hlm. 15)

| Level | Isi | Contoh |
|---|---|---|
| 1 | Proyek | Website Toko Kue Online |
| 2 | Fase | Analisis & Desain, Pembuatan, Pengujian |
| 3 | Tugas | Desain tampilan, Rancang database |
| 4 | Sub-tugas (*work package*) | (opsional, untuk tugas yang masih terlalu besar) |

Soal meminta **minimal 3 level**. Kalau WBS kalian berhenti di level 3, maka level 3 itulah *work package*-nya.

Contoh WBS resmi ada di PMBOK 4: Gambar 5-9 (WBS disusun per fase, hlm. 119) dan Gambar 5-10 (WBS disusun per *deliverable*, hlm. 120). Gambar contoh WBS di slide 06 hlm. 16 tidak ikut ter-ekspor ke PDF (hanya kotak abu-abu), jadi pakai gambar PMBOK sebagai acuan.

### 4.3 Contoh WBS (website toko kue)

```
1   Website Toko Kue Online
├── 1.1 Manajemen Proyek
│   ├── 1.1.1 Rencana proyek
│   └── 1.1.2 Rapat kemajuan mingguan
├── 1.2 Analisis & Desain
│   ├── 1.2.1 Kumpulkan kebutuhan pemilik toko
│   ├── 1.2.2 Desain tampilan (mockup)
│   └── 1.2.3 Rancang database
├── 1.3 Pembuatan
│   ├── 1.3.1 Halaman katalog kue
│   ├── 1.3.2 Keranjang & pemesanan
│   └── 1.3.3 Integrasi pembayaran online
├── 1.4 Pengujian
│   ├── 1.4.1 Uji fungsi
│   └── 1.4.2 UAT oleh pemilik toko
└── 1.5 Peluncuran
    ├── 1.5.1 Siapkan hosting & domain
    └── 1.5.2 Pelatihan pemilik toko
```

Beberapa istilah di contoh ini:
- *Mockup*: gambar rancangan tampilan sebelum dibuat sungguhan.
- *UAT* (*User Acceptance Testing*): uji coba oleh pengguna untuk memastikan sistem sesuai kebutuhannya.
- *Hosting*: tempat (server) website disimpan dan dijalankan.

### 4.4 Aturan penting

- **Aturan 100%** (*100% rule*, PMBOK 4, Bagian 5.3, hlm. 120). Jumlah semua pekerjaan di level bawah harus sama dengan pekerjaan di level atasnya. Tidak boleh ada yang terlewat, dan tidak boleh ada pekerjaan di luar lingkup. Itu sebabnya **"1.1 Manajemen Proyek" ikut masuk WBS**: rapat, laporan, dan perencanaan juga pekerjaan.
- **WBS berisi hasil kerja (kata benda), bukan langkah-langkah (kata kerja).** Contoh: "Halaman katalog kue", bukan "Mengetik kode HTML".
- **Milestone tidak dimasukkan ke WBS.** Milestone bukan pekerjaan, melainkan penanda waktu. Tempatnya di jadwal (Bagian 5).
- **Beri kode bernomor** (1, 1.1, 1.1.1). Kode ini dipakai lagi di jadwal dan daftar risiko.
- **Nilai tambah: kamus WBS** (*WBS Dictionary*, PMBOK 4, Bagian 5.3.3). Tabel singkat yang menjelaskan setiap *work package*: deskripsi, hasil, dan penanggung jawab. Tidak diwajibkan soal, tetapi menambah kedalaman isi.

### 4.5 Kesalahan yang sering terjadi

| Kesalahan | Akibat | Perbaikan |
|---|---|---|
| Hanya 2 level | Syarat soal tidak terpenuhi | Pecah lagi sampai minimal 3 level |
| Lupa pekerjaan manajemen proyek, pelatihan pengguna, atau migrasi data | Melanggar aturan 100% | Telusuri ulang dari awal sampai akhir proyek |
| Memasukkan milestone ke WBS | Salah metodologi | Pindahkan milestone ke jadwal |
| *Work package* terlalu besar ("Bikin aplikasi") | Durasi tidak bisa diperkirakan | Pecah sampai bisa dikerjakan dalam hitungan hari hingga sekitar 2 minggu |
| WBS hanya dibuat di Word | Soal meminta alat digital | Susun di alat digital, lalu tangkapan layarnya dimasukkan ke PDF |

---

## 5. Bagian 2: Gantt Chart dan jadwal

### 5.1 Pengertian

**Gantt Chart** adalah jadwal berbentuk batang mendatar di atas garis waktu. Panjang batang menunjukkan lama pekerjaan (slide 06, hlm. 19).

Gantt Chart hanyalah **gambar akhirnya**. Di baliknya ada empat proses PMBOK yang perlu disebut di laporan (slide 06, hlm. 18):

| Proses PMBOK | Pertanyaan yang dijawab | Hasil |
|---|---|---|
| *Define Activities* | Kegiatan apa saja? | Daftar aktivitas (dari *work package* WBS) |
| *Sequence Activities* | Urutannya bagaimana? Mana yang harus menunggu? | Daftar ketergantungan |
| *Estimate Activity Durations* | Berapa lama masing-masing? | Durasi setiap aktivitas |
| *Develop Schedule* | Kapan mulai dan selesai? Mana yang kritis? | Gantt Chart, daftar milestone, jalur kritis, *baseline* |

*Baseline* jadwal adalah versi jadwal yang sudah disetujui dan menjadi patokan untuk mengukur keterlambatan nanti.

### 5.2 Estimasi durasi: pilih dan sebutkan tekniknya

Slide 06 (hlm. 21) menyebut tiga teknik. Tuliskan teknik yang dipakai di laporan:

| Teknik | Cara | Kapan dipakai |
|---|---|---|
| *Expert judgment* (penilaian ahli) | Bertanya kepada orang yang berpengalaman | Paling cepat |
| *Analogous estimation* (estimasi analogi) | Meniru durasi dari proyek serupa di masa lalu | Bila ada data proyek mirip |
| *Three-point estimation* / PERT | Tiga perkiraan: Optimis (O), Paling mungkin (M), Pesimis (P). Durasi = **(O + 4M + P) / 6** | Paling dianjurkan untuk tugas ini karena menunjukkan metodologi |

Contoh *three-point* untuk "1.3.2 Keranjang & pemesanan": O = 4 hari, M = 6 hari, P = 8 hari → (4 + 24 + 8) / 6 = **6 hari**.

### 5.3 Ketergantungan aktivitas

Ketergantungan (*dependency*) artinya sebuah aktivitas harus menunggu aktivitas lain. Aktivitas yang ditunggu disebut **pendahulu** (*predecessor*); yang menunggu disebut **penerus** (*successor*).

PMBOK menyebut cara ini *Precedence Diagramming Method* atau PDM (PMBOK 4, Bagian 6.2.2.1, hlm. 137). Ada empat jenis hubungan:

| Jenis | Arti | Contoh |
|---|---|---|
| **FS** (*Finish-to-Start*) | B baru **mulai** setelah A **selesai** | Uji fungsi mulai setelah fitur selesai dibuat. **Paling sering dipakai** |
| SS (*Start-to-Start*) | B boleh mulai setelah A mulai | Penulisan panduan pengguna mulai bersamaan dengan pembuatan fitur |
| FF (*Finish-to-Finish*) | B baru boleh selesai setelah A selesai | Dokumentasi selesai setelah fitur terakhir selesai |
| SF (*Start-to-Finish*) | B baru boleh selesai setelah A mulai | Sangat jarang dipakai |

Untuk tugas ini, kebanyakan cukup memakai **FS**.

### 5.4 Contoh tabel jadwal dan cara menghitung jalur kritis

Satuan waktu: hari kerja. Pekerjaan "1.1 Manajemen Proyek" berjalan sepanjang proyek, jadi tidak dimasukkan ke perhitungan jalur kritis.

| Kode | Aktivitas | Durasi | Pendahulu | Mulai paling awal (ES) | Selesai paling awal (EF) | Mulai paling lambat (LS) | Selesai paling lambat (LF) | *Float* |
|---|---|---|---|---|---|---|---|---|
| A | 1.2.1 Kumpulkan kebutuhan | 3 | – | 0 | 3 | 0 | 3 | **0** |
| B | 1.2.2 Desain tampilan | 4 | A | 3 | 7 | 3 | 7 | **0** |
| C | 1.2.3 Rancang database | 2 | A | 3 | 5 | 5 | 7 | 2 |
| M1 | ◆ Desain disetujui | 0 | B, C | 7 | 7 | 7 | 7 | **0** |
| D | 1.3.1 Halaman katalog | 5 | M1 | 7 | 12 | 7 | 12 | **0** |
| E | 1.3.2 Keranjang & pemesanan | 6 | D | 12 | 18 | 12 | 18 | **0** |
| F | 1.3.3 Integrasi pembayaran | 4 | C | 5 | 9 | 14 | 18 | 9 |
| G | 1.5.1 Hosting & domain | 2 | A | 3 | 5 | 21 | 23 | 18 |
| H | 1.4.1 Uji fungsi | 3 | E, F | 18 | 21 | 18 | 21 | **0** |
| I | 1.4.2 UAT pemilik toko | 2 | H | 21 | 23 | 21 | 23 | **0** |
| M2 | ◆ Website online | 0 | I, G | 23 | 23 | 23 | 23 | **0** |
| J | 1.5.2 Pelatihan pemilik toko | 1 | M2 | 23 | 24 | 23 | 24 | **0** |

**Cara menghitung** (*Critical Path Method* atau CPM, PMBOK 4, Bagian 6.5.2.2, hlm. 153; slide 06, hlm. 20):

1. **Hitung maju** (*forward pass*). Mulai dari aktivitas pertama dengan ES = 0. EF = ES + durasi. ES aktivitas berikutnya = EF **terbesar** dari semua pendahulunya. Contoh: H menunggu E (EF 18) dan F (EF 9), jadi ES H = **18**.
2. **Durasi proyek** = EF terbesar = **24 hari**.
3. **Hitung mundur** (*backward pass*). Mulai dari aktivitas terakhir dengan LF = 24. LS = LF − durasi. LF aktivitas sebelumnya = LS **terkecil** dari semua penerusnya.
4. ***Float*** (kelonggaran, disebut juga *slack*) = LS − ES. Ini menunjukkan berapa hari aktivitas boleh terlambat tanpa membuat proyek terlambat.
5. **Jalur kritis** = rangkaian aktivitas dengan *float* = 0:

   **A → B → M1 → D → E → H → I → M2 → J = 3 + 4 + 0 + 5 + 6 + 3 + 2 + 0 + 1 = 24 hari**

Artinya: kalau "1.3.2 Keranjang & pemesanan" terlambat 2 hari, seluruh proyek ikut terlambat 2 hari. Sebaliknya, "1.3.3 Integrasi pembayaran" boleh terlambat sampai 9 hari tanpa mengganggu tanggal selesai.

Alat seperti MS Project menghitung semua ini otomatis. Meski begitu, sebaiknya kelompok **memahami cara hitungnya**, karena dosen bisa bertanya saat presentasi.

### 5.5 Contoh Gantt Chart

█ = aktivitas di jalur kritis, ░ = aktivitas dengan *float*, ◆ = milestone

```
Hari ke-                      123456789012345678901234
A 1.2.1 Kumpulkan kebutuhan   ███
B 1.2.2 Desain tampilan          ████
C 1.2.3 Rancang database         ░░
M1 Desain disetujui                 ◆
D 1.3.1 Halaman katalog              █████
E 1.3.2 Keranjang & pesan                 ██████
F 1.3.3 Integrasi bayar            ░░░░
G 1.5.1 Hosting & domain         ░░
H 1.4.1 Uji fungsi                              ███
I 1.4.2 UAT pemilik toko                           ██
M2 Website online                                   ◆
J 1.5.2 Pelatihan pemilik                            █
```

### 5.6 Milestone

**Milestone** (tonggak) adalah titik pencapaian penting yang **durasinya nol**, misalnya "Desain disetujui" atau "Website online". Milestone membantu klien dan dosen melihat kemajuan tanpa membaca setiap aktivitas. Buat **daftar milestone** tersendiri di laporan, dan beri setiap fase minimal satu milestone di akhirnya.

PMBOK 4 Gambar 6-14 (hlm. 158) memberi contoh tiga bentuk tampilan jadwal: **jadwal milestone**, **Gantt Chart**, dan **diagram jaringan** (kotak-kotak aktivitas yang dihubungkan panah). Laporan yang menampilkan ketiganya terlihat lebih lengkap.

### 5.7 Alat digital

| Alat | Bentuk | Catatan |
|---|---|---|
| **ClickUp** | Website | **Disarankan.** Ada paket gratis dengan tampilan Gantt dan ketergantungan. Menurut ulasan, pemakaian Gantt di paket gratis dibatasi (disebut 100 kali per bulan). Apakah fitur jalur kritis termasuk paket gratis, sumber-sumber tidak sepakat; tabel perbandingan buatan ClickUp menyebut paket Business. Cara memakainya ada di Bagian 5.8 |
| MS Project | Program Windows | Paling lengkap dan menghitung jalur kritis otomatis, tetapi berbayar dan tidak berjalan di Linux |
| Jira | Website | Populer di tim programmer. Menurut sumber yang ditemukan, tampilan *timeline* butuh paket berbayar (Standard) dan jalur kritis tidak ada bawaan |
| GanttProject / ProjectLibre | Program gratis | Bisa dipakai di Linux. GanttProject disebut di slide 06 (hlm. 19). **Tidak disebut di soal**, jadi tanyakan dulu ke dosen |

Informasi paket dan harga di atas berasal dari penelusuran web (Oktober 2026), sebagian dari situs pesaing. Cek ulang di aplikasinya langsung. Kalau alat yang dipakai tidak bisa menampilkan jalur kritis, hitung secara manual seperti Bagian 5.4 dan tampilkan di PDF.

### 5.8 Cara memakai ClickUp untuk tugas ini

Cukup **satu anggota** yang memegang ClickUp; anggota lain menyiapkan isinya (WBS, durasi, pendahulu) di kertas atau spreadsheet lebih dulu.

**Susunan ClickUp cocok dengan WBS.** ClickUp menyusun isinya bertingkat: *Workspace* (ruang kerja kelompok) → *Space* (area) → *List* (daftar) → *Task* (tugas) → *Subtask* (sub-tugas). Pemetaannya:

| WBS | Di ClickUp | Contoh |
|---|---|---|
| Level 1 (proyek) | *List* | Website Toko Kue Online |
| Level 2 (fase) | *Task* | 1.2 Analisis & Desain |
| Level 3 (*work package*) | *Subtask* | 1.2.1 Kumpulkan kebutuhan |
| Level 4 (opsional) | *Subtask* di dalam *subtask* | |

**Langkah-langkah:**

1. **Daftar** di clickup.com dengan email atau akun Google, lalu pilih paket gratis. Koordinator membuat *Workspace* dan mengundang anggota lain.
2. **Buat wadah proyek.** Buat satu *Space* (misalnya "Tugas 2 ITPM"), lalu di dalamnya satu *List* bernama proyek kalian.
3. **Ketik WBS.** Masukkan setiap fase (level 2) sebagai *task*. **Sertakan kode WBS di namanya**, misalnya "1.3 Pembuatan". Buka setiap *task*, lalu tambahkan *work package* (level 3) sebagai *subtask*, misalnya "1.3.2 Keranjang & pemesanan".
4. **Isi tanggal.** Pada setiap *subtask*, isi tanggal mulai (*start date*) dan tanggal selesai (*due date*) sesuai hasil perhitungan jadwal.
5. **Tambahkan milestone.** Buat *task* bernama misalnya "◆ Website online" dengan tanggal mulai sama dengan tanggal selesai. ClickUp juga punya fitur milestone khusus, tetapi ketersediaannya bisa bergantung paket.
6. **Buka tampilan Gantt.** Tambahkan tampilan (*view*) baru dan pilih **Gantt**. Pekerjaan akan tampil sebagai batang di atas kalender.
7. **Buat ketergantungan.** Di tampilan Gantt, tarik titik di ujung batang pendahulu ke batang penerusnya; akan muncul garis panah. Di dalam *task*, ketergantungan ini tercatat sebagai *waiting on* (menunggu) dan *blocking* (menghalangi).
8. **Tampilkan jalur kritis.** Buka pengaturan Gantt (ikon roda gigi), lalu aktifkan **Show critical path**. Pekerjaan di jalur kritis akan berwarna merah. Kalau pilihan ini tidak muncul di paket gratis, hitung manual (Bagian 5.4).
9. **Simpan bukti.** Ambil tangkapan layar tampilan *List* (untuk WBS) dan Gantt (untuk jadwal) untuk PDF. Karena ClickUp berbasis web, "berkas tools digital" bisa berupa tautan berbagi (*share link*) atau ekspor tabel; tanyakan dosen bentuk yang diterima (Bagian 11).

Nama tombol dan menu bisa sedikit berbeda karena ClickUp sering memperbarui tampilannya. Panduan resminya ada di pusat bantuan ClickUp (lihat Bagian 13).

### 5.9 Kesalahan yang sering terjadi

| Kesalahan | Perbaikan |
|---|---|
| Tanggal diketik manual tanpa ketergantungan | Isi kolom pendahulu; biarkan alat menghitung tanggal |
| Tidak ada milestone | Tambahkan milestone berdurasi 0 di akhir setiap fase |
| Jalur kritis tidak ditandai | Beri warna berbeda dan sebutkan rangkaiannya di laporan |
| Urutan tidak logis (misalnya UAT mulai sebelum uji sistem selesai) | Periksa ulang setiap pendahulu |
| Durasi tanpa dasar | Sebutkan teknik estimasi yang dipakai |

---

## 6. Bagian 3: Risk Register (daftar risiko)

### 6.1 Pengertian

**Risiko** adalah kejadian yang **belum terjadi** tetapi **mungkin terjadi**, dan kalau terjadi akan memengaruhi proyek. **Risk Register** adalah tabel yang mencatat semua risiko beserta nilai dan rencana penanganannya. Dokumen ini "hidup": diperbarui sepanjang proyek (slide 06, hlm. 30).

Alur manajemen risiko menurut slide dosen (slide 06, hlm. 29):

**Identifikasi risiko → Analisis risiko → Perencanaan respons → Pemantauan**

### 6.2 Langkah 1: Identifikasi (minimal 8 risiko)

Cara menemukan risiko:
- **Telusuri WBS satu per satu.** Tanyakan: "Apa yang bisa salah di pekerjaan ini?"
- **Perhatikan aktivitas di jalur kritis.** Keterlambatan di sana langsung menunda proyek.
- **Perhatikan ketergantungan pada pihak luar**: *vendor* (penyedia barang/jasa), klien, dan layanan pihak ketiga.
- **Pakai *Risk Breakdown Structure* (RBS)**, yaitu pohon kategori risiko dari PMBOK 4 (Gambar 11-4, hlm. 280). Telusuri setiap cabang dan tanyakan: "Adakah risiko jenis ini di proyek kami?"

  ```
  Proyek
  ├── Teknis: kebutuhan; teknologi; kompleksitas & antarmuka; kinerja & keandalan; mutu
  ├── Eksternal: subkontraktor & pemasok; regulasi; pasar; pelanggan; cuaca
  ├── Organisasi: ketergantungan antarproyek; sumber daya; pendanaan; prioritas
  └── Manajemen proyek: estimasi; perencanaan; pengendalian; komunikasi
  ```
- **Pakai daftar kategori** di berkas contoh dosen (sheet "RISK REGISTER FIK", baris 19–35). Contohnya: risiko kebutuhan, teknis, keamanan siber, data, integrasi, infrastruktur, pengujian, SDM, adopsi pengguna, keuangan, hukum, vendor.
- **Lihat contoh risiko umum proyek TI** di slide 06 (hlm. 31) dan slide 11 (hlm. 22): *scope creep*, serangan siber, kegagalan server, anggota tim kunci keluar, dan keterlambatan vendor.

Ambil risiko dari **beberapa kategori berbeda** supaya daftarnya tidak menumpuk di satu jenis.

Cara menulis risiko yang baik: **sebab → kejadian → akibat**. Contoh: "Karena pemilik toko belum pernah memakai toko online (*sebab*), ia terus meminta fitur baru setelah kebutuhan disepakati (*kejadian*), sehingga jadwal pembuatan mundur (*akibat*)."

### 6.3 Langkah 2: Analisis dengan Probability-Impact Matrix

Setiap risiko diberi dua nilai:
- **Kemungkinan (K)**, *probability*: seberapa besar peluangnya terjadi.
- **Dampak (D)**, *impact*: seberapa parah akibatnya kalau terjadi.

**Nilai risiko = K × D.** Nilai ini lalu dipetakan ke **Probability-Impact Matrix** (matriks kemungkinan × dampak), yaitu tabel warna yang menunjukkan risiko mana yang harus ditangani lebih dulu (PMBOK 4, Bagian 11.3.2.2, hlm. 290–292).

**Skala kemungkinan** (dari berkas contoh dosen, sheet "Skala Resiko"):

| Nilai | Tipe | Peluang terjadi |
|---|---|---|
| 5 | Sangat sering | 50% |
| 4 | Sering | 20% |
| 3 | Sedang | 10% |
| 2 | Jarang | 5% |
| 1 | Hampir tidak pernah | 2% |

**Skala dampak untuk proyek** (dari PMBOK 4, Gambar 11-5, hlm. 281). Skala dampak di berkas contoh dosen dibuat untuk operasional fakultas (layanan, pembelajaran, penelitian). PMBOK mengukur dampak risiko proyek terhadap **empat sasaran proyek: biaya, waktu, lingkup, dan mutu**:

| Nilai | Tipe | Biaya | Waktu | Lingkup | Mutu |
|---|---|---|---|---|---|
| 5 | Serius | Naik > 40% | Bertambah > 20% | Hasil akhir proyek praktis tidak berguna | Hasil akhir proyek praktis tidak berguna |
| 4 | Tinggi | Naik 20–40% | Bertambah 10–20% | Pengurangan lingkup tidak dapat diterima *sponsor* | Penurunan mutu tidak dapat diterima *sponsor* |
| 3 | Sedang | Naik 10–20% | Bertambah 5–10% | Bagian utama lingkup terdampak | Penurunan mutu perlu persetujuan *sponsor* |
| 2 | Rendah | Naik < 10% | Bertambah < 5% | Bagian kecil lingkup terdampak | Hanya fungsi yang sangat menuntut yang terdampak |
| 1 | Sangat rendah | Kenaikan tidak berarti | Tambahan tidak berarti | Pengurangan lingkup nyaris tak terasa | Penurunan mutu nyaris tak terasa |

*Sponsor* adalah pihak yang mendanai dan mengesahkan proyek (dalam contoh ini, pemilik toko). Nama tipe (Serius sampai Sangat rendah) mengikuti berkas contoh dosen supaya seragam dengan skala kemungkinan.

Cara memakai tabel ini:
- Persentase dihitung dari **total anggaran** atau **total durasi proyek**. Contoh: proyek toko kue berdurasi 24 hari, jadi terlambat 2 hari = 8% → **nilai 3**.
- Kalau sebuah risiko mengenai beberapa sasaran sekaligus, ambil **nilai tertinggi**.
- PMBOK menyebut tabel ini **contoh yang perlu disesuaikan** dengan proyek. Kelompok boleh mengubah batasnya, asalkan **ditulis di laporan sebelum dipakai**.

**Level risiko** (dari berkas contoh dosen):

| Level | Nilai K × D | Penanganan |
|---|---|---|
| Kritikal | 20–25 | Tidak dapat ditoleransi; tindakan wajib segera dan dipantau pimpinan |
| Tinggi | 13–19 | Ditoleransi hanya bila tindakan sudah diterapkan dan diperiksa |
| Sedang | 6–12 | Ditoleransi bila pencegahan rutin sudah berjalan |
| Rendah | 1–5 | Dapat ditoleransi; cukup ditinjau berkala |

**Matriks 5 × 5** (angka = K × D; huruf = level). Posisi tiga contoh risiko di Bagian 6.5 ditandai di sel masing-masing:

| K ↓ / D → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 R | 10 S | 15 T | 20 K | 25 K |
| **4** | 4 R | 8 S | 12 S **(R-01)** | 16 T | 20 K |
| **3** | 3 R | 6 S | 9 S | 12 S **(R-02)** | 15 T |
| **2** | 2 R | 4 R | 6 S | 8 S **(R-03)** | 10 S |
| **1** | 1 R | 2 R | 3 R | 4 R | 5 R |

R = Rendah, S = Sedang, T = Tinggi, K = Kritikal. Di laporan, warnai selnya: hijau, kuning, oranye, merah.

Slide 11 (hlm. 21) memakai peta risiko (*heatmap*) berukuran 3 × 3 (rendah/menengah/tinggi), sedangkan berkas contoh dosen memakai 5 × 5. **Pilih satu dan pakai konsisten.** Panduan ini memakai 5 × 5 karena lebih rinci dan sesuai berkas contoh dosen.

### 6.4 Langkah 3: Rencana respons

Untuk risiko negatif (ancaman), PMBOK punya **lima strategi**. Edisi ke-4 menyebut empat (Bagian 11.5.2.1, hlm. 302–303); edisi ke-7 menambahkan *escalate* (Bagian 2.8.5.1, hlm. 122).

| Strategi | Arti | Contoh (toko kue) |
|---|---|---|
| **Avoid** (hindari) | Ubah rencana supaya ancaman hilang sama sekali | Pembayaran kartu kredit dikeluarkan dari lingkup tahap pertama; hanya transfer bank |
| **Transfer** (alihkan) | Serahkan dampak dan penanganannya ke pihak ketiga | Memakai *payment gateway* resmi supaya keamanan data kartu menjadi tanggung jawab penyedia |
| **Mitigate** (kurangi) | Turunkan kemungkinan dan/atau dampaknya | *Pair programming* supaya pekerjaan tidak bergantung pada satu orang |
| **Accept** (terima) | Tidak ada tindakan pencegahan. **Aktif**: siapkan cadangan waktu/biaya (*contingency reserve*). **Pasif**: cukup dicatat | Menyisihkan 2 hari cadangan di akhir jadwal |
| **Escalate** (naikkan) | Masalah di luar wewenang tim, diserahkan ke pihak yang lebih berwenang | Keputusan soal izin usaha online diserahkan ke pemilik toko |

*Payment gateway* adalah layanan perantara pembayaran online. *Pair programming* adalah dua programmer mengerjakan satu kode bersama.

"Rencana respons yang **rinci**" (kata soal) berarti setiap risiko minimal punya:
1. **Strategi** (salah satu dari lima di atas)
2. **Tindakan konkret**: apa yang dilakukan
3. **Pemilik risiko** (*risk owner*): siapa yang bertanggung jawab
4. **Pemicu** (*trigger*): tanda bahwa risiko mulai terjadi
5. **Batas waktu**: kapan tindakan dijalankan
6. **Risiko sisa** (*residual risk*): nilai K × D setelah tindakan dijalankan

### 6.5 Contoh isi Risk Register

| ID | Kategori | Uraian risiko (sebab → kejadian → akibat) | WBS | K | D | K×D | Level | Strategi & tindakan | Pemicu | Pemilik | Batas waktu | Residual K×D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Kebutuhan | Pemilik toko belum paham toko online → terus meminta fitur baru setelah kebutuhan disepakati (*scope creep*) → pembuatan mundur ± 2 hari (≈ 8% durasi proyek) | 1.2.1, 1.3.x | 4 | 3 | 12 | Sedang | **Mitigate**: daftar kebutuhan ditandatangani di M1; setiap permintaan baru lewat formulir *change request* dan dinilai dampaknya | Ada permintaan fitur di luar daftar kebutuhan | Manajer proyek | Sebelum M1 (hari ke-7) | 2 × 3 = 6 (Sedang) |
| R-02 | Vendor | Penyedia *payment gateway* lambat menyetujui akun → integrasi pembayaran tertunda → fitur pembayaran belum siap saat peluncuran | 1.3.3 | 3 | 4 | 12 | Sedang | **Mitigate**: daftar akun di hari pertama proyek. **Accept aktif**: siapkan transfer bank manual sebagai cadangan | Akun belum disetujui di hari ke-10 | Programmer *backend* | Hari ke-1 | 2 × 3 = 6 (Sedang) |
| R-03 | SDM | Programmer utama berhalangan ± 3 hari saat mengerjakan 1.3.2 (jalur kritis) → seluruh proyek terlambat ± 3 hari (≈ 12% durasi proyek) | 1.3.2 | 2 | 4 | 8 | Sedang | **Mitigate**: *pair programming* dan catatan kode harian supaya anggota lain bisa melanjutkan | Programmer tidak hadir lebih dari 1 hari | Manajer proyek | Sejak hari ke-7 | 2 × 2 = 4 (Rendah) |

Nilai dampak (D) di tabel ini mengikuti skala PMBOK di Bagian 6.3. R-01: terlambat 8% → 3. R-02: fitur pembayaran tidak siap saat peluncuran, pengurangan lingkup yang tidak dapat diterima pemilik toko → 4. R-03: terlambat 12% → 4. Residual R-03 menjadi D = 2 karena dengan *pair programming* keterlambatan diperkirakan kurang dari 1 hari (< 5%).

*Scope creep* adalah pertambahan lingkup pekerjaan tanpa proses perubahan resmi (slide 06, hlm. 8). *Change request* adalah permintaan perubahan resmi yang dinilai dulu dampaknya sebelum disetujui. *Backend* adalah bagian sistem di sisi server.

Perhatikan hubungan R-02 dengan jadwal: aktivitas F (1.3.3) punya *float* 9 hari. Jadi penundaan persetujuan akun sampai sekitar seminggu belum menunda proyek. Analisis yang menghubungkan risiko dengan jalur kritis seperti ini menunjukkan dokumen yang **kohesif**.

### 6.6 Kesalahan yang sering terjadi

| Kesalahan | Perbaikan |
|---|---|
| Menulis risiko organisasi (anggaran fakultas, akreditasi) | Tulis risiko **proyek**: yang bisa menggagalkan jadwal, biaya, lingkup, atau mutu proyek ini |
| Menulis masalah yang sudah terjadi | Risiko adalah kejadian yang **mungkin** terjadi |
| Semua respons berupa "mitigasi" | Pakai strategi yang sesuai; minimal ada beberapa jenis strategi |
| Respons kabur ("lebih berhati-hati") | Tulis tindakan konkret, pemilik, pemicu, dan batas waktu |
| Matriks tidak digambar | Gambar matriks 5 × 5 berwarna dan tempatkan setiap risiko di dalamnya |
| Tidak ada nilai residual | Tambahkan K × D setelah tindakan |

---

## 7. Dua berkas contoh dari dosen: apa yang ditiru, apa yang tidak

### 7.1 `Gantt_Chart_Project_IT.xlsx`

Isinya templat jadwal proyek sistem inventaris (April–Juli 2024): 4 *epic* (kelompok pekerjaan besar), yaitu Design, Development, Testing, dan Deployment, dengan total 15 tugas. Kolomnya: nama tugas, ID, durasi, tanggal mulai, tanggal selesai, dan garis waktu per minggu.

| Tiru | Jangan tiru |
|---|---|
| Struktur fase → tugas | Tidak ada kolom pendahulu (ketergantungan) |
| Kolom ID, durasi, tanggal mulai, tanggal selesai | Tidak ada milestone dan jalur kritis |
| Kolom penanggung jawab dan status | Batang Gantt belum diwarnai (sel garis waktu kosong) |
| | Kolom status dan pemilik menimpa kolom garis waktu (kolom F–G) |
| | Urutan janggal: UAT (mulai 17 Juni) dimulai sebelum uji sistem (mulai 24 Juni) |

**Kesimpulan:** pakai sebagai gambaran bentuk saja. Jadwal yang dikumpulkan sebaiknya dibuat di alat digital yang menghitung ketergantungan dan jalur kritis.

### 7.2 `Contoh Usulan_Risk_Register (FIK_2026).xlsx`

Berkas ini berisi tiga sheet:
1. **Skala Resiko**: skala dampak 1–5, skala kemungkinan 1–5, dan level risiko berdasarkan nilai K × D.
2. **RISK REGISTER FIK**: templat 20 kolom (identifikasi, analisis, pengendalian, rencana kegiatan, risiko sisa), ditambah catatan berisi 15 kategori risiko proyek TI.
3. **Usulan Risiko**: contoh terisi 20 risiko. Hitungan K × D dan levelnya konsisten.

| Tiru | Jangan tiru |
|---|---|
| Skala kemungkinan 1–5 dan level risiko | **Isinya**: 20 contoh adalah risiko **organisasi fakultas**, bukan risiko proyek |
| Susunan kolom: uraian → konsekuensi → K, D, nilai, level → pengendalian → PJ → residual | Skala dampak versi fakultas; ganti dengan skala biaya/waktu/lingkup/mutu dari PMBOK (Bagian 6.3) |
| 15 kategori risiko proyek TI di catatan sheet 2 | Batas waktu "triwulanan/semesteran"; proyek perlu tanggal atau hari ke-sekian |
| Kolom residual (risiko sisa) | Matriks 5 × 5 tidak tergambar; buat sendiri |

**Kolom yang perlu ditambahkan** supaya sesuai PMBOK dan slide 06: **ID risiko**, **kode WBS terkait**, **strategi respons** (avoid/transfer/mitigate/accept/escalate), dan **pemicu**.

---

## 8. Tahapan pengerjaan langkah demi langkah

Tahapan di bawah sengaja diurutkan supaya setiap dokumen dibangun dari dokumen sebelumnya.

### Tahap 0: Siapkan kelompok

- Tetapkan satu **koordinator** (berperan sebagai manajer proyek kelompok).
- Bagi peran. Contoh untuk 4 orang:

| Peran | Tanggung jawab utama |
|---|---|
| Koordinator | Ringkasan proyek, penyatuan dokumen, pengecekan konsistensi kode WBS |
| Penanggung jawab WBS | WBS dan kamus WBS |
| Penanggung jawab jadwal | Durasi, ketergantungan, Gantt di alat digital, jalur kritis |
| Penanggung jawab risiko | Risk Register dan matriks |

Semua anggota tetap ikut **curah pendapat** (*brainstorming*) saat menyusun WBS dan mencari risiko.
- Sepakati **alat digital** yang dipakai (Bagian 5.7) dan tempat menyimpan berkas bersama.

### Tahap 1: Baca materi

- Slide 06 (*Project Planning Core PMBOK*): **sumber utama tugas ini**. Fokus ke hlm. 13–21 (WBS, jadwal, CPM, estimasi) dan hlm. 29–31 (risiko).
- Slide 07 (*Integrasi Project Plan*): soal keterhubungan antar-rencana.
- Bagian PMBOK yang dirujuk di panduan ini (lihat Bagian 13).

### Tahap 2: Pilih proyek

Kriteria proyek yang baik untuk tugas ini:
- **Proyek TI yang realistis**: aplikasi, website, sistem informasi, atau migrasi sistem.
- **Ukuran sedang**, sekitar 3–6 bulan dengan 20–40 *work package*. Terlalu kecil membuat WBS dangkal; terlalu besar membuat kelompok kewalahan.
- **Domainnya dipahami kelompok**, misalnya sistem di tempat kerja salah satu anggota.
- **Punya pihak luar** (vendor, klien, layanan pihak ketiga), supaya risikonya beragam.

**Pertimbangkan proyek yang bisa dipakai ulang.** Beberapa tugas di pertemuan berikutnya juga memakai proyek pilihan:
- Slide 10 (hlm. 29): *Execution Plan* dan *Sprint Plan* untuk "proyek IT pilihan Anda"
- Slide 11 (hlm. 29): dasbor pemantauan proyek, dengan pilihan topik **Smart Campus**, IoT Monitoring, Cybersecurity Dashboard, atau **AI Assistant**
- Slide 12 (hlm. 29): dokumen *Lessons Learned* untuk **Smart Campus** atau **AI Assistant**

Kalau Tugas 2 memakai Smart Campus atau AI Assistant, WBS, jadwal, dan daftar risikonya bisa dipakai lagi di tugas-tugas itu. Belum pasti semua tugas tersebut benar-benar diberikan, jadi anggap ini pertimbangan, bukan keharusan.

### Tahap 3: Tulis ringkasan proyek (1 halaman)

Tidak diminta langsung oleh soal, tetapi WBS tidak bisa disusun tanpa lingkup yang jelas. Contoh bentuk yang ringkas ada di slide 05 (hlm. 20): *Project Charter* "Aplikasi Mobile Bank Sampah". *Project Charter* (piagam proyek) adalah dokumen resmi yang mengesahkan dimulainya proyek. Contoh itu memuat tujuan, lingkup (termasuk yang **tidak** dikerjakan), jadwal dengan milestone, anggaran, manajer proyek, dan *sponsor*. Pakai juga lima komponen *Project Scope Statement* (pernyataan lingkup proyek) dari slide 06 (hlm. 7):

1. **Tujuan** (*objective*): apa yang ingin dicapai
2. ***Deliverable***: hasil kerja yang diserahkan
3. **Batasan** (*constraints*): anggaran, waktu, jumlah orang
4. **Asumsi** (*assumptions*): hal yang dianggap benar
5. **Kriteria penerimaan** (*acceptance criteria*): syarat hasil dinyatakan selesai

Tulis juga **apa yang tidak termasuk** proyek, supaya batasnya jelas.

### Tahap 4: Susun WBS

1. Mulai dari level 1 (nama proyek), lalu level 2 (fase).
2. Pecah setiap fase menjadi level 3, dan level 4 bila perlu.
3. Cek aturan 100%: apakah manajemen proyek, pengujian, pelatihan, migrasi data, dan dokumentasi sudah masuk?
4. Beri kode bernomor.
5. Masukkan ke alat digital; ambil tangkapan layar untuk PDF.
6. (Nilai tambah) Buat kamus WBS ringkas.

### Tahap 5: Tentukan aktivitas dan perkirakan durasi

1. Setiap *work package* menjadi satu atau beberapa aktivitas di jadwal, dengan **kode WBS yang sama**.
2. Perkirakan durasi. Disarankan memakai *three-point estimation*; tampilkan tabel O, M, P untuk aktivitas penting.
3. Tentukan satuan waktu (hari kerja atau minggu) dan pakai secara konsisten.

### Tahap 6: Tentukan ketergantungan

1. Untuk setiap aktivitas, tanyakan: "Apa yang **harus** selesai sebelum ini bisa mulai?"
2. Isi kolom pendahulu. Gunakan FS kecuali ada alasan khusus.
3. Pastikan tidak ada aktivitas "menggantung" (tanpa pendahulu atau penerus), kecuali aktivitas pertama dan terakhir.

### Tahap 7: Susun jadwal di alat digital

1. Masukkan aktivitas, durasi, dan pendahulu. Biarkan alat menghitung tanggal. Langkah rinci untuk ClickUp ada di Bagian 5.8.
2. Tambahkan **milestone** berdurasi 0 di akhir setiap fase.
3. Tampilkan dan tandai **jalur kritis**. Kalau alat tidak bisa, hitung manual (Bagian 5.4).
4. Simpan sebagai ***baseline***.
5. Ambil tangkapan layar Gantt untuk PDF, dan simpan berkas aslinya untuk dikumpulkan.

### Tahap 8: Identifikasi risiko

1. Adakan sesi curah pendapat bersama seluruh anggota.
2. Telusuri WBS, jalur kritis, dan ketergantungan pada pihak luar (Bagian 6.2).
3. Kumpulkan lebih dari 8 risiko, lalu pilih yang paling relevan. Pastikan berasal dari beberapa kategori.
4. Tulis dengan format sebab → kejadian → akibat.

### Tahap 9: Analisis risiko

1. Tetapkan dan tuliskan skala K dan D (Bagian 6.3).
2. Beri nilai K dan D untuk setiap risiko, dengan alasan singkat.
3. Hitung K × D dan tentukan level.
4. Gambar matriks 5 × 5 berwarna dan tempatkan setiap risiko.
5. Urutkan risiko dari nilai tertinggi.

### Tahap 10: Rencana respons dan integrasi

1. Untuk setiap risiko, isi strategi, tindakan, pemilik, pemicu, dan batas waktu (Bagian 6.4).
2. Hitung nilai residual.
3. **Integrasikan:** kalau respons menambah pekerjaan atau waktu cadangan, tambahkan ke WBS dan jadwal, lalu periksa apakah jalur kritis berubah.

### Tahap 11: Susun dokumen PDF

Lihat susunan yang disarankan di Bagian 9.1.

### Tahap 12: Buat slide dan latihan presentasi

Lihat Bagian 9.2. Latihan minimal sekali dengan pengatur waktu supaya pas 10 menit.

### Tahap 13: Periksa dan kumpulkan

Pakai daftar periksa di Bagian 10.

---

## 9. Susunan dokumen PDF dan slide presentasi

### 9.1 Susunan PDF yang disarankan

1. **Sampul**: judul, nama proyek, nama dan NIM anggota, dosen pengampu
2. **Pendahuluan**: latar belakang dan ringkasan proyek (lingkup, *deliverable*, batasan, asumsi, kriteria penerimaan)
3. **Metodologi**: proses dan teknik PMBOK yang dipakai, serta alat digitalnya
4. **WBS**: diagram, tabel berkode, dan kamus WBS
5. **Jadwal**: tabel aktivitas (durasi, pendahulu), estimasi durasi, Gantt Chart, daftar milestone, dan jalur kritis beserta penjelasannya
6. **Risk Register**: skala K dan D, matriks 5 × 5, tabel register lengkap, dan penjelasan respons untuk risiko tertinggi
7. **Keterkaitan antar-dokumen**: tabel kode WBS → aktivitas jadwal → risiko terkait, plus perubahan rencana akibat respons risiko
8. **Kesimpulan**
9. **Glosarium** dan **daftar pustaka**
10. **Lampiran**: tangkapan layar alat digital

### 9.2 Slide presentasi 10 menit

| Bagian | Waktu | Isi |
|---|---|---|
| Pembuka | 1 menit | Proyek apa, tujuannya, dan lingkupnya |
| WBS | 2,5 menit | Diagram WBS dan aturan 100% |
| Jadwal | 3 menit | Gantt, milestone, jalur kritis, dan teknik estimasi |
| Risiko | 3 menit | Matriks, 3 risiko teratas, dan respons rincinya |
| Penutup | 0,5 menit | Keterkaitan ketiga dokumen dan kesimpulan |

Gunakan sekitar 8–12 slide. Satu slide satu pesan.

---

## 10. Daftar periksa sebelum mengumpulkan

**WBS**
- [ ] Minimal 3 level
- [ ] Semua *work package* lengkap (aturan 100%), termasuk manajemen proyek
- [ ] Setiap elemen punya kode bernomor
- [ ] Dibuat di alat digital

**Jadwal**
- [ ] Setiap aktivitas punya durasi, dan teknik estimasinya disebutkan
- [ ] Setiap aktivitas punya pendahulu (kecuali yang pertama)
- [ ] Ada milestone berdurasi 0
- [ ] Jalur kritis ditandai dan dijelaskan
- [ ] Kode aktivitas sama dengan kode WBS

**Risk Register**
- [ ] Minimal 8 risiko **proyek**, dari beberapa kategori
- [ ] Skala K dan D ditulis
- [ ] Matriks 5 × 5 berwarna digambar
- [ ] Setiap risiko punya strategi, tindakan, pemilik, pemicu, batas waktu, dan nilai residual
- [ ] Setiap risiko merujuk ke kode WBS

**Keseluruhan**
- [ ] Istilah dan proses PMBOK disebut dengan benar
- [ ] Respons risiko yang menambah pekerjaan sudah masuk ke WBS dan jadwal
- [ ] Berkas PDF dan berkas alat digital siap dikumpulkan
- [ ] Presentasi sudah dilatih dan pas 10 menit

---

## 11. Hal yang perlu ditanyakan ke dosen

1. **Tenggat pengumpulan** dan cara mengumpulkan.
2. **Apakah alat selain Jira, ClickUp, atau MS Project boleh dipakai** (misalnya GanttProject atau ProjectLibre)?
3. **Hubungan dengan "Tugas: Final Project Planning" di slide 07 (hlm. 31).** Tugas itu meminta *Project Charter*, *Scope Statement* dan WBS, *Team Contract*, jadwal, RTM (minimal 5 persyaratan), dan Risk Register (5 risiko). Isinya mirip tetapi tidak sama dengan Tugas 2. Apakah keduanya tugas yang sama atau terpisah? Kalau terpisah, hasil Tugas 2 bisa dipakai ulang.
4. **Jumlah anggota** per kelompok.
5. **Bentuk "berkas tools digital"** bila memakai alat berbasis web seperti ClickUp: tautan berbagi, berkas ekspor, atau tangkapan layar?

---

## 12. Glosarium

| Istilah | Penjelasan |
|---|---|
| *Acceptance criteria* | Kriteria penerimaan; syarat yang harus dipenuhi agar hasil kerja dinyatakan selesai |
| *Accept* | Strategi respons risiko: menerima risiko; aktif (siapkan cadangan) atau pasif (cukup dicatat) |
| *Analogous estimation* | Estimasi durasi berdasarkan data proyek serupa di masa lalu |
| *Assumptions* | Asumsi; hal yang dianggap benar tanpa pembuktian sebagai dasar perencanaan |
| *Avoid* | Strategi respons risiko: mengubah rencana supaya ancaman hilang |
| *Backend* | Bagian sistem di sisi server yang mengolah data |
| *Backward pass* | Hitung mundur dalam CPM untuk mencari waktu mulai dan selesai paling lambat |
| *Baseline* | Versi rencana yang sudah disetujui dan menjadi patokan pengukuran |
| *Brainstorming* | Curah pendapat; sesi mengumpulkan ide sebanyak-banyaknya bersama |
| *Change request* | Permintaan perubahan resmi yang dinilai dampaknya sebelum disetujui |
| *Constraints* | Batasan proyek, misalnya anggaran, waktu, dan jumlah orang |
| *Contingency reserve* | Cadangan waktu, biaya, atau sumber daya untuk menghadapi risiko |
| CPM (*Critical Path Method*) | Teknik menghitung jalur terpanjang dalam jadwal untuk menemukan jalur kritis |
| Dekomposisi (*decomposition*) | Memecah pekerjaan besar menjadi bagian yang lebih kecil |
| *Deliverable* | Hasil kerja konkret yang diserahkan kepada klien atau pengguna |
| *Dependency* | Ketergantungan; hubungan ketika satu aktivitas harus menunggu aktivitas lain |
| *Epic* | Kelompok pekerjaan besar yang berisi banyak tugas |
| ES / EF | *Early Start* / *Early Finish*: waktu mulai / selesai paling awal sebuah aktivitas |
| *Escalate* | Strategi respons risiko: menyerahkan risiko ke pihak yang lebih berwenang |
| *Expert judgment* | Estimasi berdasarkan pendapat orang yang berpengalaman |
| FS, SS, FF, SF | Jenis ketergantungan: *Finish-to-Start*, *Start-to-Start*, *Finish-to-Finish*, *Start-to-Finish* |
| *Float* / *slack* | Kelonggaran; berapa hari aktivitas boleh terlambat tanpa menunda proyek |
| *Forward pass* | Hitung maju dalam CPM untuk mencari waktu mulai dan selesai paling awal |
| Gantt Chart | Jadwal berbentuk batang mendatar di atas garis waktu |
| *Heatmap* (peta risiko) | Matriks berwarna kemungkinan × dampak untuk memprioritaskan risiko |
| *Hosting* | Tempat (server) website disimpan dan dijalankan |
| *Impact* (dampak, D) | Seberapa parah akibat risiko bila terjadi |
| Jalur kritis (*critical path*) | Rangkaian aktivitas dengan *float* nol; keterlambatannya langsung menunda proyek |
| *Knowledge area* | Bidang pengetahuan manajemen proyek di PMBOK, misalnya lingkup, jadwal, risiko |
| LS / LF | *Late Start* / *Late Finish*: waktu mulai / selesai paling lambat tanpa menunda proyek |
| *Milestone* | Tonggak; titik pencapaian penting berdurasi nol |
| *Mitigate* | Strategi respons risiko: menurunkan kemungkinan dan/atau dampak |
| *Mockup* | Gambar rancangan tampilan sebelum dibuat sungguhan |
| *Pair programming* | Dua programmer mengerjakan satu kode bersama |
| *Payment gateway* | Layanan perantara pembayaran online |
| PDM (*Precedence Diagramming Method*) | Metode menggambar urutan aktivitas dengan kotak dan panah ketergantungan |
| PERT / *three-point estimation* | Estimasi durasi dari tiga perkiraan: (Optimis + 4 × Paling mungkin + Pesimis) / 6 |
| PMBOK | *Project Management Body of Knowledge*; buku standar manajemen proyek dari PMI |
| *Predecessor* / *successor* | Aktivitas pendahulu (yang ditunggu) / penerus (yang menunggu) |
| *Probability* (kemungkinan, K) | Seberapa besar peluang risiko terjadi |
| Probability-Impact Matrix | Matriks kemungkinan × dampak untuk menentukan prioritas risiko |
| *Project Charter* | Piagam proyek; dokumen resmi yang mengesahkan dimulainya proyek |
| *Project Scope Statement* | Pernyataan lingkup proyek: tujuan, *deliverable*, batasan, asumsi, kriteria penerimaan |
| RBS (*Risk Breakdown Structure*) | Pohon kategori risiko untuk membantu menemukan risiko dari berbagai sumber |
| *Residual risk* | Risiko sisa; nilai risiko setelah tindakan respons dijalankan |
| Risiko | Kejadian yang belum terjadi tetapi mungkin terjadi dan memengaruhi proyek |
| *Risk owner* | Pemilik risiko; orang yang bertanggung jawab memantau dan menangani satu risiko |
| Risk Register | Daftar risiko beserta nilai dan rencana responsnya |
| RTM (*Requirements Traceability Matrix*) | Tabel yang menelusuri setiap kebutuhan sampai ke hasil kerjanya |
| *Scope* | Lingkup; batas pekerjaan yang termasuk dan tidak termasuk proyek |
| *Scope creep* | Pertambahan lingkup pekerjaan tanpa proses perubahan resmi |
| *Share link* | Tautan berbagi; alamat web untuk membuka isi aplikasi tanpa harus masuk ke akun pemiliknya |
| *Sponsor* | Pihak yang mendanai dan mengesahkan proyek |
| *Subtask* | Sub-tugas; tugas di dalam tugas lain (di ClickUp dipakai untuk level 3 WBS) |
| *Transfer* | Strategi respons risiko: mengalihkan dampak dan penanganan risiko ke pihak ketiga |
| *Trigger* | Pemicu; tanda bahwa sebuah risiko mulai terjadi |
| UAT (*User Acceptance Testing*) | Uji coba oleh pengguna untuk memastikan sistem sesuai kebutuhannya |
| *Vendor* | Penyedia barang atau jasa dari luar organisasi |
| WBS (*Work Breakdown Structure*) | Pemecahan seluruh pekerjaan proyek secara bertingkat |
| *WBS Dictionary* | Kamus WBS; penjelasan rinci setiap elemen WBS |
| *Work package* | Paket kerja; elemen terbawah WBS yang bisa ditugaskan, diestimasi, dan dipantau |

---

## 13. Rujukan

**Materi dosen** (folder `materi/Slide Dosen (Melwin Syafrizal)-20261025/`)
- **Slide 06**, *Project Planning (Core PMBOK)*: hlm. 7 (*Scope Statement*), 8 (*scope creep*), 13–17 (WBS), 18–21 (jadwal, Gantt, CPM, estimasi), 29–31 (risiko), 34 (soal Tugas Kelompok). **Sumber utama.**
- Slide 07, *Integrasi Project Plan*: hlm. 22 (*baseline*), 27 (RTM), 31 (Tugas: *Final Project Planning*).
- Slide 05, *Project Initiation*: hlm. 18–20 (komponen dan contoh *Project Charter* "Aplikasi Mobile Bank Sampah").
- Slide 03, *Process Group*: hlm. 11–12 (kegiatan dan hasil perencanaan, strategi respons risiko).
- Slide 01, *IT Project Management*: hlm. 25 (alat dan teknik per *knowledge area*), 51–52 (contoh Gantt dan diagram jaringan MS Project).
- Slide 11, *Monitoring and Controlling*: hlm. 19–22 (pemantauan risiko, siklus risiko, *heatmap*, risiko umum proyek TI).
- Slide 10, 11, dan 12, hlm. 29: tugas-tugas berikutnya yang juga memakai proyek pilihan.
- `tugas2/Gantt_Chart_Project_IT.xlsx` dan `tugas2/Contoh Usulan_Risk_Register (FIK_2026).xlsx`.

**PMBOK**
- Project Management Institute. (2008). *A guide to the project management body of knowledge (PMBOK® Guide)* (4th ed.). PMI.
  - Gambar 5-9 dan 5-10, hlm. 119–120: contoh WBS per fase dan per *deliverable*
  - Bagian 5.3, hlm. 120: aturan 100% dan kamus WBS
  - Bagian 6.2.2.1, hlm. 137 (Gambar 6-7, hlm. 139): *Precedence Diagramming Method*
  - Bagian 6.5.2.2, hlm. 153: *Critical Path Method*
  - Gambar 6-14, hlm. 158: contoh jadwal milestone, Gantt, dan diagram jaringan
  - Gambar 11-4, hlm. 280: *Risk Breakdown Structure*
  - Gambar 11-5, hlm. 281: skala dampak untuk empat sasaran proyek
  - Bagian 11.3.2.2, hlm. 290–292 (Gambar 11-10): *Probability and Impact Matrix*
  - Bagian 11.5.2.1, hlm. 302–303: strategi respons risiko negatif
- Project Management Institute. (2021). *A guide to the project management body of knowledge (PMBOK® Guide)* (7th ed.). PMI.
  - Bagian 2.8.5.1, hlm. 122: lima strategi respons ancaman, termasuk *escalate*

> Nomor halaman PMBOK = nomor halaman buku, bukan nomor halaman PDF.

**Alat digital** (ditelusuri Oktober 2026; sebagian dari situs pesaing, jadi cek ulang di aplikasinya)
- ClickUp Help, *How to use Gantt charts for project planning*: https://help.clickup.com/hc/en-us/articles/40982447293207-How-to-use-Gantt-charts-for-project-planning
- ClickUp, *Jira Gantt Chart vs. ClickUp Gantt Chart*: https://clickup.com/blog/jira-gantt-charts-vs-clickup
- ClickUp, *10 Best Free Gantt Chart Maker Software*: https://clickup.com/blog/gantt-charts/
- ClickUp, *Jira Gantt Chart Review*: https://clickup.com/learn/topic/project-management/tools/jira/gantt-charts/
- Atlassian Community, *Critical path*: https://community.atlassian.com/forums/Jira-questions/Critical-path/qaa-p/3174480
