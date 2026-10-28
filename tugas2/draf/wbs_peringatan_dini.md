# Draf Tugas 2 — Tahap 1: Lingkup dan WBS
## Sistem Peringatan Dini Cuaca Publik Berbasis IoT (Audio-Visual) Terintegrasi Data BMKG

> Berkas kerja (draf), disusun bertahap:
> **Tahap 1: lingkup + WBS (berkas ini)** → Tahap 2: jadwal (durasi, ketergantungan, milestone, jalur kritis) → Tahap 3: Risk Register → Tahap 4: penyatuan ke PDF dan ClickUp.
> Keputusan dasar (28 Oktober 2026): 6 perangkat di 3 wilayah DIY, durasi ±4 bulan, sponsor BPBD, tim proyek simulasi 5 orang.
> Aturan penulisan: istilah asing dijelaskan saat pertama muncul dan dikumpulkan di Glosarium.

---

## 1. Ringkasan proyek (*Project Scope Statement*)

### 1.1 Latar belakang

BMKG menerbitkan **peringatan dini cuaca** untuk 0–6 jam ke depan di situsnya, per provinsi. Informasi ini hanya sampai ke warga yang sedang membuka situs atau media sosial BMKG. Warga di tempat umum (pasar, terminal, sekolah, pinggir sungai) sering tidak menerimanya tepat waktu.

Proyek ini membangun sistem yang **membaca halaman peringatan dini BMKG secara berkala**. Bila ada wilayah sasaran yang disebut, sistem **otomatis menyalakan perangkat audio-visual** di wilayah tersebut: panel LED bertuliskan pesan peringatan, lampu rotari, dan sirene/suara.

Sistem **tidak membuat prakiraan cuaca sendiri**. Sistem hanya meneruskan peringatan resmi BMKG.

### 1.2 Cara kerja sistem

```
Halaman peringatan dini BMKG (per provinsi)
        │  dibuka berkala oleh Playwright (Python) di server
        ▼
Server: cari nama wilayah sasaran di teks halaman
        │  ada  → status AKTIF
        │  tidak ada di 3 pengecekan berturut-turut → status SELESAI
        │  halaman gagal dimuat → status TETAP, admin diberi tanda
        ▼
Kirim perintah lewat MQTT ke topik wilayah
        ▼
Perangkat IoT (firmware C++) di wilayah itu
        → panel LED matrix menampilkan pesan
        → lampu rotari menyala (lewat relay)
        → sirene/suara berbunyi
        → kirim heartbeat berkala ke server
```

Istilah dalam diagram:
- *Playwright*: pustaka untuk mengendalikan peramban web secara otomatis, sehingga program bisa membaca halaman seperti manusia.
- *MQTT*: cara kirim pesan ringan untuk perangkat IoT. Setiap wilayah menjadi satu "topik"; perangkat yang berlangganan topik itu menerima perintahnya.
- *Firmware*: program yang tertanam di papan elektronik.
- *Relay*: sakelar listrik yang dikendalikan papan IoT.
- *Heartbeat*: sinyal "saya masih hidup" dari perangkat ke server.

### 1.3 Tujuan (SMART)

Dalam **±4 bulan**, memasang dan mengoperasikan **6** perangkat peringatan audio-visual di **3** wilayah percontohan. Perangkat harus menyala **paling lambat 10 menit** setelah wilayahnya muncul di halaman peringatan dini BMKG.

*SMART*: tujuan yang Spesifik, Terukur (*Measurable*), Dapat dicapai (*Achievable*), Relevan, dan Berbatas waktu (*Time-bound*).

Contoh wilayah percontohan (DIY, dekat kampus): Kota Yogyakarta, Kab. Sleman, Kab. Bantul.

### 1.4 Hasil yang diserahkan (*deliverables*)

1. Server berisi modul pemantau BMKG, pencocok wilayah, pengelola status, MQTT broker, dan dasbor admin
2. **6** unit perangkat IoT audio-visual yang terpasang di lokasi
3. Daftar wilayah sasaran beserta variasi namanya
4. Dokumen: spesifikasi kebutuhan, desain sistem, laporan uji, manual operator, dan SOP
5. Pelatihan operator dan sosialisasi ke warga

*MQTT broker*: program di server yang menerima dan meneruskan pesan MQTT. *SOP* (*Standard Operating Procedure*): prosedur kerja baku.

### 1.5 Di luar lingkup

- Membuat prakiraan atau peringatan cuaca sendiri; sistem hanya meneruskan data BMKG
- Sensor cuaca (penakar hujan, anemometer, dan sejenisnya)
- Aplikasi HP untuk warga
- Peringatan gempa dan tsunami
- Perawatan perangkat setelah masa serah terima

### 1.6 Batasan (*constraints*)

- Durasi: **±4 bulan**
- Tim proyek: **5 orang** untuk 6 peran; Engineer IoT merangkap Teknisi Lapangan (pekerjaan keduanya tidak bertabrakan di jadwal). Tim ini adalah **simulasi skenario**, berbeda dengan kelompok mahasiswa penyusun dokumen
- Anggaran: belum dirinci (di luar permintaan tugas)
- Sumber data hanya halaman publik BMKG; tidak ada kerja sama data resmi

### 1.7 Asumsi (*assumptions*)

- Halaman peringatan dini BMKG per provinsi tetap bisa diakses publik dan dibaca berkala
- Tautan halaman per provinsi sudah tersedia
- Lokasi pemasangan punya listrik PLN dan sinyal 4G atau Wi-Fi
- Mitra (misalnya BPBD) bersedia menjadi pemilik sistem dan operator
- Izin pemasangan dari pemilik lokasi atau pemda bisa diperoleh

*BPBD*: Badan Penanggulangan Bencana Daerah.

### 1.8 Pemangku kepentingan (*stakeholders*)

| Pihak | Peran |
|---|---|
| BPBD | *Sponsor* (pendana dan pemilik sistem) dan operator |
| Warga di sekitar perangkat | Pengguna akhir yang menerima peringatan |
| Pemilik lokasi pemasangan | Pemberi izin dan penyedia listrik |
| BMKG | Sumber data, **bukan** pihak dalam proyek |
| Pemasok komponen | Penyedia board IoT, panel LED, lampu, audio, dan *enclosure* |
| Tim proyek | Pelaksana |

*Stakeholder*: semua pihak yang terdampak atau berkepentingan dengan proyek. *Enclosure*: kotak pelindung perangkat.

### 1.9 Kriteria penerimaan (*acceptance criteria*)

| No | Kriteria | Target |
|---|---|---|
| 1 | Waktu dari wilayah muncul di BMKG sampai perangkat menyala | ≤ 10 menit |
| 2 | Salah cocok pada daftar uji nama wilayah yang mirip | 0 kasus |
| 3 | Perangkat mati otomatis setelah wilayah hilang dari halaman | Setelah 3 pengecekan berturut-turut |
| 4 | Halaman BMKG gagal dimuat | Status tidak berubah; admin menerima tanda |
| 5 | Perangkat mati/terputus terdeteksi di dasbor | ≤ 5 menit |
| 6 | Perangkat tetap bekerja saat listrik padam | ≥ 4 jam dengan baterai cadangan |
| 7 | Pesan panel LED terbaca di siang hari | Dari jarak 20 m |

### 1.10 Pendekatan pengerjaan

**Prediktif** (*Waterfall*, tahap demi tahap) untuk keseluruhan proyek. Alasannya, pengadaan komponen, perakitan, dan pemasangan perangkat keras harus berurutan dan sulit diubah di tengah jalan. Pengembangan perangkat lunak server boleh dikerjakan bertahap di dalam fasenya.

### 1.11 Alat dan lingkungan pengembangan

| Alat | Fungsi | Biaya |
|---|---|---|
| VS Code | Editor kode untuk Python (server) dan C++ (firmware) | Gratis |
| PlatformIO | Ekstensi VS Code untuk firmware board IoT: kompilasi, upload ke board, dan pengelolaan *library* | Gratis |
| Claude Code | Asisten pemrograman AI untuk membantu menulis dan memeriksa kode | Berbayar (langganan) |
| Python + Playwright | Bahasa dan pustaka untuk modul pemantau BMKG | Gratis |
| Git | Penyimpan riwayat versi kode, supaya kode tim tidak saling tertimpa dan setiap perubahan bisa ditelusuri | Gratis |

*Ekstensi*: tambahan fitur yang dipasang ke dalam aplikasi. *Library*: kumpulan kode siap pakai.

**Aturan pemakaian Claude Code:**
- Semua kode yang dibantu AI **ditinjau oleh anggota tim** (tinjauan kode, *code review*) sebelum digabungkan ke repositori.
- Kata sandi server, kunci akses, dan data rahasia lainnya **tidak dimasukkan** ke dalam percakapan dengan AI.

---

## 2. WBS (*Work Breakdown Structure*)

Disusun per fase (mengikuti pola PMBOK 4, Gambar 5-9). **3 level, 8 fase, 43 *work package*.**

```
1 Sistem Peringatan Dini Cuaca Publik (SPDC)
├── 1.1 Manajemen Proyek
│   ├── 1.1.1 Project charter dan rencana proyek
│   ├── 1.1.2 Rapat dan laporan kemajuan
│   ├── 1.1.3 Pengendalian perubahan dan pemantauan risiko
│   └── 1.1.4 Penutupan proyek dan lessons learned
├── 1.2 Analisis Kebutuhan
│   ├── 1.2.1 Kebutuhan pemangku kepentingan
│   ├── 1.2.2 Studi halaman peringatan dini BMKG
│   ├── 1.2.3 Daftar wilayah sasaran dan variasi nama
│   ├── 1.2.4 Survei lokasi pemasangan
│   └── 1.2.5 Spesifikasi kebutuhan sistem (SRS)
├── 1.3 Desain Sistem
│   ├── 1.3.1 Arsitektur sistem
│   ├── 1.3.2 Desain logika status peringatan
│   ├── 1.3.3 Desain database wilayah dan perangkat
│   ├── 1.3.4 Desain rangkaian perangkat keras
│   ├── 1.3.5 Desain pesan LED dan pola audio-lampu
│   └── 1.3.6 Desain dasbor admin
├── 1.4 Pengadaan
│   ├── 1.4.1 Daftar komponen (BOM)
│   ├── 1.4.2 Pemilihan pemasok dan pembelian komponen
│   ├── 1.4.3 Sewa server (VPS) dan domain
│   ├── 1.4.4 Izin pemasangan
│   └── 1.4.5 Penyiapan alat pengembangan
├── 1.5 Pengembangan Perangkat Lunak Server
│   ├── 1.5.1 Modul pemantau BMKG (Playwright)
│   ├── 1.5.2 Modul pencocokan nama wilayah
│   ├── 1.5.3 Modul pengelola status peringatan
│   ├── 1.5.4 Layanan pengirim perintah (MQTT)
│   ├── 1.5.5 Dasbor admin
│   └── 1.5.6 Pemantauan heartbeat dan notifikasi admin
├── 1.6 Pengembangan Perangkat IoT
│   ├── 1.6.1 Perakitan prototipe
│   ├── 1.6.2 Firmware C++
│   ├── 1.6.3 Fitur heartbeat dan sambung ulang otomatis
│   ├── 1.6.4 Fitur diagnosa jarak jauh
│   └── 1.6.5 Perakitan unit produksi
├── 1.7 Pengujian
│   ├── 1.7.1 Uji unit perangkat lunak
│   ├── 1.7.2 Uji pencocokan nama wilayah
│   ├── 1.7.3 Uji perangkat keras
│   ├── 1.7.4 Uji integrasi ujung ke ujung
│   ├── 1.7.5 Uji kegagalan
│   └── 1.7.6 Uji coba lapangan dan UAT
└── 1.8 Pemasangan dan Peluncuran
    ├── 1.8.1 Pemasangan perangkat di lokasi
    ├── 1.8.2 Deploy perangkat lunak server dan pengamanan dasar
    ├── 1.8.3 Konfigurasi wilayah dan pendaftaran perangkat
    ├── 1.8.4 Sosialisasi ke warga
    ├── 1.8.5 Pelatihan operator
    └── 1.8.6 Serah terima dan dokumentasi
```

### Catatan penyusunan

- **Aturan 100%** (PMBOK 4, Bagian 5.3): pekerjaan manajemen proyek (1.1), pengadaan (1.4), *deploy* server (1.8.2), sosialisasi (1.8.4), dan pelatihan (1.8.5) ikut dimasukkan, karena semuanya pekerjaan yang harus dilakukan.
- **Milestone tidak masuk WBS.** Milestone akan ditambahkan di Tahap 2 (jadwal).
- **Pengadaan dibuat fase tersendiri** karena proyek ini membeli komponen, menyewa server, dan berlangganan alat pengembangan. Ini sekaligus menunjukkan *knowledge area* Procurement (pengadaan) dari PMBOK.
- **Keputusan desain yang sudah disetujui** (28 Oktober 2026) dan tempatnya di WBS:
  - Playwright mencari teks nama wilayah tanpa bergantung pada bentuk elemen HTML (1.5.1, 1.5.2).
  - Tautan halaman per provinsi sudah tersedia (1.2.2).
  - Peringatan dianggap selesai bila wilayah tidak lagi muncul di halaman, dengan aturan 3 pengecekan berturut-turut; halaman yang gagal dimuat tidak mengubah status (1.3.2, 1.5.3).
  - Pencocokan per kata utuh, dengan daftar variasi nama dan daftar nama mirip yang harus ditolak (1.2.3, 1.5.2, 1.7.2).
  - MQTT untuk mengirim perintah dari server ke perangkat (1.5.4, 1.6.2).
  - Lampu rotari dikendalikan lewat relay. Komponen pendukung: speaker/amplifier, baterai/UPS, modem 4G, *enclosure* tahan air, panel LED *outdoor*, serta sensor arus dan tegangan (1.3.4, 1.4.1).
  - Heartbeat dan diagnosa jarak jauh (1.5.6, 1.6.3, 1.6.4).
  - Dasbor admin (1.3.6, 1.5.5), termasuk aktivasi peringatan manual sebagai rencana darurat.
  - Board IoT: ESP32 (1.4.1).
  - Alat pengembangan: VS Code, PlatformIO, Claude Code, Python + Playwright, dan Git (1.11, 1.4.5).
  - Pendekatan prediktif (1.10) dan angka kriteria penerimaan (1.9).

---

## 3. Kamus WBS (*WBS Dictionary*)

Penanggung jawab ditulis sebagai **peran**, bukan nama orang:
- **MP**: Manajer Proyek
- **AS**: Analis Sistem
- **PS**: Programmer Server
- **EI**: Engineer IoT
- **QA**: Penguji (*Quality Assurance*)
- **TL**: Teknisi Lapangan

Satu orang boleh memegang lebih dari satu peran.

### 1.1 Manajemen Proyek

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.1.1 | Project charter dan rencana proyek | Menyusun piagam proyek, WBS, jadwal, anggaran, Risk Register, dan rencana komunikasi | Project charter; rencana manajemen proyek | MP |
| 1.1.2 | Rapat dan laporan kemajuan | Rapat mingguan tim dan laporan kemajuan ke sponsor | Notulen; laporan mingguan | MP |
| 1.1.3 | Pengendalian perubahan dan pemantauan risiko | Menilai setiap permintaan perubahan; memperbarui Risk Register | *Change log*; Risk Register terbaru | MP |
| 1.1.4 | Penutupan proyek dan lessons learned | Evaluasi akhir dan pencatatan pelajaran | Laporan penutupan; dokumen lessons learned | MP |

### 1.2 Analisis Kebutuhan

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.2.1 | Kebutuhan pemangku kepentingan | Wawancara BPBD/pemda dan perwakilan warga: wilayah prioritas, jam operasi, bentuk pesan | Catatan kebutuhan | AS |
| 1.2.2 | Studi halaman peringatan dini BMKG | Mengamati halaman per provinsi: cara penulisan wilayah, frekuensi pembaruan, tampilan saat tidak ada peringatan, tampilan peringatan yang belum mulai berlaku | Laporan studi halaman; daftar tautan provinsi | AS |
| 1.2.3 | Daftar wilayah sasaran dan variasi nama | Mendata wilayah sasaran, ejaan yang mungkin muncul, dan nama mirip yang harus ditolak | Daftar wilayah; daftar nama mirip | AS |
| 1.2.4 | Survei lokasi pemasangan | Mengecek listrik, sinyal, ketinggian pasang, keamanan, dan jarak pandang | Laporan survei per lokasi | TL |
| 1.2.5 | Spesifikasi kebutuhan sistem (SRS) | Merumuskan kebutuhan fungsional dan nonfungsional, termasuk kriteria penerimaan | Dokumen SRS | AS |

*SRS* (*Software Requirements Specification*): dokumen spesifikasi kebutuhan sistem. *Kebutuhan fungsional*: apa yang dilakukan sistem. *Kebutuhan nonfungsional*: seberapa baik sistem bekerja (kecepatan, keandalan, keamanan).

### 1.3 Desain Sistem

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.3.1 | Arsitektur sistem | Rancangan hubungan server, MQTT broker, database, dasbor, dan perangkat | Diagram arsitektur | AS |
| 1.3.2 | Desain logika status peringatan | Aturan AKTIF / SELESAI / GAGAL MUAT, aturan 3 pengecekan, interval pengecekan | Diagram status dan aturannya | AS |
| 1.3.3 | Desain database wilayah dan perangkat | Struktur data wilayah, variasi nama, perangkat, riwayat status | Skema database | PS |
| 1.3.4 | Desain rangkaian perangkat keras | Skema board IoT, relay, panel LED, audio, catu daya, dan baterai cadangan | Skema rangkaian | EI |
| 1.3.5 | Desain pesan LED dan pola audio-lampu | Teks pesan, pola kedip lampu, pola bunyi sirene, dan jam senyap bila disepakati | Spesifikasi pesan dan pola | AS |
| 1.3.6 | Desain dasbor admin | Rancangan tampilan: status wilayah, status perangkat, mode uji, aktivasi peringatan manual, riwayat | *Mockup* dasbor | PS |

*Mockup*: gambar rancangan tampilan sebelum dibuat.

### 1.4 Pengadaan

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.4.1 | Daftar komponen (BOM) | Board IoT **ESP32** (diprogram dengan C++ melalui PlatformIO), panel LED *outdoor*, lampu rotari, relay, speaker/amplifier, catu daya, baterai/UPS, modem 4G, *enclosure* tahan air, sensor arus dan tegangan | BOM dengan spesifikasi dan perkiraan harga | EI |
| 1.4.2 | Pemilihan pemasok dan pembelian komponen | Membandingkan pemasok, memesan, dan memeriksa barang datang | Komponen diterima; bukti pembelian | MP |
| 1.4.3 | Sewa server (VPS) dan domain | Memilih penyedia, menyewa, dan menyiapkan akses | Server siap pakai | PS |
| 1.4.4 | Izin pemasangan | Mengurus izin dari pemilik lokasi, kelurahan, atau pemda | Surat izin per lokasi | MP |
| 1.4.5 | Penyiapan alat pengembangan | Berlangganan Claude Code; memasang VS Code, PlatformIO, dan Python + Playwright di komputer tim; membuat repositori Git bersama | Alat siap pakai; repositori kode | PS |

*BOM* (*Bill of Materials*): daftar komponen beserta jumlah dan spesifikasinya. *VPS* (*Virtual Private Server*): server sewaan di internet. *UPS*: catu daya cadangan berbaterai.

### 1.5 Pengembangan Perangkat Lunak Server

Semua modul ditulis dengan Python di VS Code, boleh dibantu Claude Code, dan **ditinjau anggota tim lain** sebelum digabungkan ke repositori (Bagian 1.11). Setiap *work package* sudah mencakup ***debugging*** saat menulis kode.

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.5.1 | Modul pemantau BMKG (Playwright) | Membuka halaman provinsi yang relevan secara berkala, mengambil teks halaman, dan memastikan halaman berhasil dimuat | Modul Python | PS |
| 1.5.2 | Modul pencocokan nama wilayah | Mencocokkan per kata utuh dengan variasi nama, menolak nama mirip | Modul Python | PS |
| 1.5.3 | Modul pengelola status peringatan | Menerapkan aturan AKTIF / SELESAI / GAGAL MUAT dan menyimpan riwayat | Modul Python | PS |
| 1.5.4 | Layanan pengirim perintah (MQTT) | Memasang MQTT broker; mengirim perintah nyala/mati ke topik wilayah | Broker dan modul pengirim | PS |
| 1.5.5 | Dasbor admin | Mengelola wilayah dan perangkat, melihat status, menyalakan mode uji, dan menyalakan peringatan secara manual bila pembacaan BMKG terganggu (rencana darurat risiko R-03) | Aplikasi web dasbor | PS |
| 1.5.6 | Pemantauan heartbeat dan notifikasi admin | Mendeteksi perangkat yang tidak mengirim heartbeat; memberi tahu admin | Modul pemantau dan notifikasi | PS |

### 1.6 Pengembangan Perangkat IoT

Firmware ditulis dengan C++ di VS Code + PlatformIO, boleh dibantu Claude Code, dan **ditinjau anggota tim lain** sebelum di-*upload* ke unit produksi (Bagian 1.11). Setiap *work package* sudah mencakup ***debugging*** firmware di board, memakai PlatformIO.

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.6.1 | Perakitan prototipe | Merakit satu unit uji di meja kerja | 1 unit prototipe | EI |
| 1.6.2 | Firmware C++ | Koneksi jaringan, berlangganan topik MQTT, kendali panel LED, relay lampu, dan audio | Firmware versi 1 | EI |
| 1.6.3 | Fitur heartbeat dan sambung ulang otomatis | Mengirim heartbeat; menyambung ulang otomatis saat jaringan putus | Firmware versi akhir | EI |
| 1.6.4 | Fitur diagnosa jarak jauh | Perangkat melaporkan kondisi daya, koneksi, dan keluaran; admin dapat menjalankan uji diri dari dasbor | Firmware dengan fitur diagnosa | EI |
| 1.6.5 | Perakitan unit produksi | Merakit **6** unit di dalam *enclosure* tahan air | Unit siap pasang | EI |

### 1.7 Pengujian

Setiap pengujian berjalan dengan pola **uji → perbaiki → uji ulang**. Penguji (QA) menemukan dan mencatat *bug*; Programmer Server (PS) atau Engineer IoT (EI) memperbaikinya; lalu QA menguji ulang. Waktu perbaikan *bug* sudah termasuk di durasi setiap pengujian (lihat jadwal Tahap 2).

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.7.1 | Uji unit perangkat lunak | Menguji setiap modul server secara terpisah | Laporan uji unit | QA |
| 1.7.2 | Uji pencocokan nama wilayah | Menguji dengan daftar nama mirip (misalnya "Batu" vs "Batubara") dan nama di luar daftar peringatan | Laporan uji; 0 salah cocok | QA |
| 1.7.3 | Uji perangkat keras | Uji tahan air, panas, baterai cadangan ≥ 4 jam, dan keterbacaan LED di siang hari | Laporan uji perangkat keras | QA |
| 1.7.4 | Uji integrasi ujung ke ujung | Alur lengkap BMKG → server → perangkat, dengan halaman uji tiruan; memperbaiki *bug* yang ditemukan dan menguji ulang | Laporan uji; waktu ≤ 10 menit | QA |
| 1.7.5 | Uji kegagalan | Halaman BMKG tidak bisa diakses, internet perangkat putus, listrik padam; memperbaiki *bug* yang ditemukan dan menguji ulang | Laporan uji kegagalan | QA |
| 1.7.6 | Uji coba lapangan dan UAT | Menjalankan sistem di lokasi percontohan; diuji dan disetujui sponsor; termasuk perbaikan kecil yang diminta sponsor | Berita acara UAT | QA |

*UAT* (*User Acceptance Testing*): uji penerimaan oleh pengguna atau sponsor. *Halaman uji tiruan*: halaman buatan tim yang meniru halaman BMKG, supaya pengujian tidak perlu menunggu peringatan sungguhan.

### 1.8 Pemasangan dan Peluncuran

| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| 1.8.1 | Pemasangan perangkat di lokasi | Memasang unit, menyambung listrik dan jaringan, uji nyala di tempat | Unit terpasang dan berfungsi | TL |
| 1.8.2 | Deploy perangkat lunak server dan pengamanan dasar | Memasang semua modul ke server produksi; mengatur *firewall*, HTTPS, dan *backup* berkala | Server produksi berjalan dan aman | PS |
| 1.8.3 | Konfigurasi wilayah dan pendaftaran perangkat | Mendaftarkan setiap unit ke wilayah dan topiknya di dasbor | Data perangkat lengkap | PS |
| 1.8.4 | Sosialisasi ke warga | Menjelaskan arti pesan, lampu, dan bunyi; tindakan yang harus dilakukan warga | Materi sosialisasi; daftar hadir | MP |
| 1.8.5 | Pelatihan operator | Melatih petugas memakai dasbor, membaca tanda gangguan, dan mode uji | Daftar hadir; manual operator | AS |
| 1.8.6 | Serah terima dan dokumentasi | Menyerahkan sistem, kode, manual, dan SOP kepada sponsor | Berita acara serah terima | MP |

---

## 4. Keputusan dasar (28 Oktober 2026)

1. Jumlah perangkat dan wilayah percontohan: 6 perangkat di 3 wilayah DIY
2. Durasi target proyek: ±4 bulan
3. Sponsor: BPBD
4. Tim proyek (simulasi): 5 orang untuk 6 peran (MP, AS, PS, EI, QA, TL); EI merangkap TL
5. Interval pengecekan halaman BMKG: 5 menit (dasar kriteria "≤ 10 menit")
---

## Glosarium

| Istilah | Penjelasan |
|---|---|
| *Acceptance criteria* | Kriteria penerimaan; syarat hasil dinyatakan selesai dan diterima |
| *Assumptions* | Asumsi; hal yang dianggap benar sebagai dasar perencanaan |
| BOM (*Bill of Materials*) | Daftar komponen beserta jumlah dan spesifikasinya |
| BPBD | Badan Penanggulangan Bencana Daerah |
| *Change log* | Catatan semua permintaan perubahan dan keputusannya |
| Claude Code | Asisten pemrograman berbasis AI yang membantu menulis dan memeriksa kode |
| *Code review* (tinjauan kode) | Pemeriksaan kode oleh anggota tim lain sebelum kode dipakai |
| *Constraints* | Batasan proyek: waktu, biaya, jumlah orang |
| *Backup* | Salinan data cadangan |
| *Bug* | Kesalahan dalam program |
| *Debugging* | Mencari dan memperbaiki *bug* |
| *Deliverable* | Hasil kerja yang diserahkan |
| *Deploy* | Memasang program ke server sungguhan agar bisa dipakai |
| *Firewall* | Penyaring akses jaringan; hanya akses yang diizinkan yang bisa masuk |
| HTTPS | Sambungan web terenkripsi |
| *Enclosure* | Kotak pelindung perangkat, misalnya tahan air |
| Ekstensi | Tambahan fitur yang dipasang ke dalam aplikasi |
| *Firmware* | Program yang tertanam di papan elektronik |
| Git | Alat penyimpan riwayat versi kode |
| *Heartbeat* | Sinyal berkala dari perangkat yang menandakan perangkat masih hidup |
| IoT (*Internet of Things*) | Perangkat fisik yang tersambung ke internet |
| *Lessons learned* | Catatan pelajaran dari proyek untuk proyek berikutnya |
| *Library* | Kumpulan kode siap pakai |
| *Mockup* | Gambar rancangan tampilan sebelum dibuat |
| MQTT | Protokol kirim pesan ringan untuk IoT, berbasis topik |
| MQTT *broker* | Program server yang menerima dan meneruskan pesan MQTT |
| PlatformIO | Ekstensi VS Code untuk menulis, mengompilasi, dan meng-*upload* firmware ke board IoT |
| *Playwright* | Pustaka untuk mengendalikan peramban web secara otomatis |
| Prediktif / *Waterfall* | Pendekatan proyek tahap demi tahap secara berurutan |
| *Project charter* | Piagam proyek; dokumen resmi yang mengesahkan dimulainya proyek |
| *Relay* | Sakelar listrik yang dikendalikan oleh papan elektronik |
| Repositori | Tempat penyimpanan kode bersama beserta riwayat perubahannya |
| SMART | Tujuan yang Spesifik, Terukur, Dapat dicapai, Relevan, dan Berbatas waktu |
| SOP | *Standard Operating Procedure*; prosedur kerja baku |
| *Sponsor* | Pihak yang mendanai dan mengesahkan proyek |
| SRS | *Software Requirements Specification*; dokumen spesifikasi kebutuhan sistem |
| *Stakeholder* | Pihak yang terdampak atau berkepentingan dengan proyek |
| UAT | *User Acceptance Testing*; uji penerimaan oleh pengguna atau sponsor |
| Uji ulang | Menguji kembali setelah *bug* diperbaiki, untuk memastikan perbaikan berhasil dan tidak merusak bagian lain |
| UPS | Catu daya cadangan berbaterai |
| VPS | *Virtual Private Server*; server sewaan di internet |
| VS Code | *Visual Studio Code*; aplikasi editor kode gratis |
| WBS | *Work Breakdown Structure*; pemecahan seluruh pekerjaan proyek secara bertingkat |
| *WBS Dictionary* | Kamus WBS; penjelasan rinci setiap elemen WBS |
| *Work package* | Elemen terbawah WBS yang bisa ditugaskan, diestimasi, dan dipantau |
