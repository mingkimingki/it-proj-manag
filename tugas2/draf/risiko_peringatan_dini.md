# Draf Tugas 2 — Tahap 3: Risk Register
## Sistem Peringatan Dini Cuaca Publik Berbasis IoT (Audio-Visual) Terintegrasi Data BMKG

> Berkas kerja (draf), disusun bertahap:
> Tahap 1: lingkup + WBS (`wbs_peringatan_dini.md`) → Tahap 2: jadwal (`jadwal_peringatan_dini.md`) → **Tahap 3: Risk Register (berkas ini)** → Tahap 4: penyatuan ke PDF dan ClickUp.
> **[USULAN]** Daftar risiko, nilai K dan D, serta rencana respons adalah usulan awal dari Claude, disusun dari diskusi sebelumnya. Kelompok boleh menambah, menghapus, atau mengubah nilainya.
> **Sudah disetujui (28 Oktober 2026):** aktivasi peringatan manual dari dasbor (R-03), cadangan waktu 5 hari (R-06), dan board ESP32.

---

## 1. Ringkasan

| Hal | Hasil |
|---|---|
| Jumlah risiko | **10 risiko proyek** (syarat soal: minimal 8) |
| Level awal | 2 Tinggi, 8 Sedang |
| Level setelah respons (*residual*) | 6 Sedang, 4 Rendah |
| Risiko teratas | R-01 Pengiriman komponen terlambat (16) · R-03 Halaman BMKG berubah atau akses diblokir (15) |
| Strategi yang dipakai | *Avoid*, *Mitigate*, *Transfer*, *Accept* (aktif), dan *Escalate* |

---

## 2. Dasar penyusunan (metodologi PMBOK)

| Proses PMBOK | Yang dilakukan di sini |
|---|---|
| *Identify Risks* | Risiko dicari dengan menelusuri WBS, jalur kritis jadwal, dan *Risk Breakdown Structure* (RBS; PMBOK 4, Gambar 11-4, hlm. 280). Kategori RBS: **Teknis**, **Eksternal**, **Organisasi**, **Manajemen proyek** |
| *Perform Qualitative Risk Analysis* | Setiap risiko diberi nilai Kemungkinan (K) dan Dampak (D) 1–5, lalu dipetakan ke **Probability-Impact Matrix** (PMBOK 4, Bagian 11.3.2.2, hlm. 290–292) |
| *Plan Risk Responses* | Setiap risiko diberi strategi respons (PMBOK 4, Bagian 11.5.2.1, hlm. 302–303; PMBOK 7, Bagian 2.8.5.1, hlm. 122), tindakan, pemilik, pemicu, batas waktu, dan nilai sisa |

### 2.1 Skala kemungkinan (K)

Dari berkas contoh dosen (`Contoh Usulan_Risk_Register (FIK_2026).xlsx`, sheet "Skala Resiko"):

| Nilai | Tipe | Peluang terjadi |
|---|---|---|
| 5 | Sangat sering | 50% |
| 4 | Sering | 20% |
| 3 | Sedang | 10% |
| 2 | Jarang | 5% |
| 1 | Hampir tidak pernah | 2% |

### 2.2 Skala dampak (D)

Dari PMBOK 4, Gambar 11-5 (hlm. 281). Kolom waktu dihitung dari durasi proyek **92 hari kerja** (Tahap 2):

| Nilai | Tipe | Waktu (dari 92 hari) | Lingkup | Mutu |
|---|---|---|---|---|
| 5 | Serius | Mundur > 20% (> 18 hari) | Hasil akhir praktis tidak berguna | Hasil akhir praktis tidak berguna |
| 4 | Tinggi | Mundur 10–20% (± 10–18 hari) | Pengurangan lingkup tidak dapat diterima sponsor | Penurunan mutu tidak dapat diterima sponsor |
| 3 | Sedang | Mundur 5–10% (± 5–9 hari) | Bagian utama lingkup terdampak | Penurunan mutu perlu persetujuan sponsor |
| 2 | Rendah | Mundur < 5% (< 5 hari) | Bagian kecil lingkup terdampak | Hanya fungsi yang sangat menuntut yang terdampak |
| 1 | Sangat rendah | Tidak berarti | Nyaris tak terasa | Nyaris tak terasa |

Bila satu risiko mengenai beberapa sasaran, dipakai **nilai tertinggi**. Kolom biaya PMBOK tidak dipakai, karena anggaran proyek belum ditetapkan.

### 2.3 Level risiko

Dari berkas contoh dosen. Nilai risiko = K × D.

| Level | Nilai | Penanganan |
|---|---|---|
| Kritikal | 20–25 | Tidak dapat ditoleransi; tindakan wajib segera |
| Tinggi | 13–19 | Ditoleransi hanya bila tindakan sudah diterapkan dan diperiksa |
| Sedang | 6–12 | Ditoleransi bila pencegahan rutin sudah berjalan |
| Rendah | 1–5 | Dapat ditoleransi; cukup ditinjau berkala |

---

## 3. Risk Register

Pemilik risiko ditulis sebagai peran (lihat kamus WBS): **MP** Manajer Proyek, **AS** Analis Sistem, **PS** Programmer Server, **EI** Engineer IoT, **QA** Penguji, **TL** Teknisi Lapangan.

| ID | Kategori (RBS) | Uraian risiko (sebab → kejadian → akibat) | WBS | K | D | K×D | Level | Strategi | Pemilik | Residual K×D |
|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Eksternal: pemasok | Stok komponen (panel LED *outdoor*, board, modem) kosong atau dikirim dari luar negeri → **pengiriman terlambat ± 10 hari** → pembelian komponen ada di jalur kritis, sehingga seluruh proyek mundur ± 11% | 1.4.2 | 4 | 4 | **16** | **Tinggi** | *Avoid* + *Mitigate* | MP | 2 × 3 = 6 (Sedang) |
| R-02 | Eksternal: regulasi | Pemilik lokasi atau pemda lambat memberi izin → **izin terlambat melebihi kelonggarannya** (lebih dari ± 54 hari) → pemasangan dan UAT mundur ± 2 minggu | 1.4.4, 1.8.1 | 2 | 4 | 8 | Sedang | *Escalate* + *Mitigate* | MP | 1 × 4 = 4 (Rendah) |
| R-03 | Teknis: sumber data | Situs BMKG diubah atau membatasi akses otomatis (misalnya memblokir permintaan berulang) → **modul pemantau tidak bisa membaca peringatan** → fungsi utama sistem tidak berjalan | 1.2.2, 1.5.1 | 3 | 5 | **15** | **Tinggi** | *Mitigate* + *Accept* aktif | PS | 2 × 3 = 6 (Sedang) |
| R-04 | Teknis: mutu | Nama wilayah mirip atau ditulis berbeda (misalnya "Kota Yogyakarta" dan "Yogyakarta") → **salah cocok**: sirene menyala di wilayah yang salah, atau tidak menyala di wilayah yang benar → mutu tidak dapat diterima sponsor | 1.2.3, 1.5.2, 1.7.2 | 3 | 4 | 12 | Sedang | *Mitigate* | AS | 1 × 4 = 4 (Rendah) |
| R-05 | Teknis: keandalan | Listrik atau internet di lokasi putus saat cuaca buruk → **perangkat tidak menerima perintah** → kriteria penerimaan 4 dan 6 gagal saat UAT | 1.3.4, 1.6.3, 1.7.5 | 3 | 4 | 12 | Sedang | *Mitigate* | EI | 2 × 3 = 6 (Sedang) |
| R-06 | Teknis: pengujian | Server, MQTT, dan perangkat baru pertama kali dijalankan bersama → ***bug*** **jauh lebih banyak dari perkiraan** saat uji integrasi dan uji kegagalan (keduanya di jalur kritis) → proyek mundur ± 5–9 hari | 1.7.4, 1.7.5 | 3 | 3 | 9 | Sedang | *Mitigate* + *Accept* aktif | QA | 2 × 2 = 4 (Rendah) |
| R-07 | Organisasi: sumber daya | Firmware hanya dikuasai satu orang (Engineer IoT) → **EI sakit atau keluar** saat mengerjakan 1.6.x (jalur kritis) → firmware tertunda ± 2 minggu | 1.6.1–1.6.4 | 2 | 4 | 8 | Sedang | *Mitigate* | MP | 2 × 3 = 6 (Sedang) |
| R-08 | Teknis: teknologi | Kode dibantu Claude Code tanpa diperiksa dengan teliti → **kode mengandung kesalahan atau celah keamanan, atau data rahasia (kata sandi, kunci akses) ikut terkirim/tersimpan** → server rentan dibobol; mutu tidak dapat diterima | 1.4.5, 1.5.x, 1.6.x, 1.8.2 | 3 | 4 | 12 | Sedang | *Mitigate* | PS | 2 × 3 = 6 (Sedang) |
| R-09 | Eksternal: pelanggan | Warga belum paham arti bunyi dan lampu, atau sirene terlalu keras/sering → **warga mengeluh**, sponsor meminta sirene dimatikan → fungsi audio berkurang | 1.3.5, 1.8.4 | 4 | 3 | 12 | Sedang | *Mitigate* | AS | 2 × 3 = 6 (Sedang) |
| R-10 | Eksternal: lingkungan | Perangkat dipasang di tempat umum → **dicuri atau dirusak** → unit harus diganti; percontohan di lokasi itu terganggu | 1.8.1 | 2 | 3 | 6 | Sedang | *Transfer* + *Mitigate* | TL | 2 × 2 = 4 (Rendah) |

---

## 4. Probability-Impact Matrix

Sebelum respons (angka = K × D; huruf = level):

| K ↓ / D → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 R | 10 S | 15 T | 20 K | 25 K |
| **4** | 4 R | 8 S | 12 S **R-09** | 16 T **R-01** | 20 K |
| **3** | 3 R | 6 S | 9 S **R-06** | 12 S **R-04, R-05, R-08** | 15 T **R-03** |
| **2** | 2 R | 4 R | 6 S **R-10** | 8 S **R-02, R-07** | 10 S |
| **1** | 1 R | 2 R | 3 R | 4 R | 5 R |

Setelah respons (*residual*):

| K ↓ / D → | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 R | 10 S | 15 T | 20 K | 25 K |
| **4** | 4 R | 8 S | 12 S | 16 T | 20 K |
| **3** | 3 R | 6 S | 9 S | 12 S | 15 T |
| **2** | 2 R | 4 R **R-06, R-10** | 6 S **R-01, R-03, R-05, R-07, R-08, R-09** | 8 S | 10 S |
| **1** | 1 R | 2 R | 3 R | 4 R **R-02, R-04** | 5 R |

R = Rendah, S = Sedang, T = Tinggi, K = Kritikal. Di PDF, sel diwarnai hijau (Rendah), kuning (Sedang), oranye (Tinggi), dan merah (Kritikal).

---

## 5. Rencana respons rinci

Minggu ke- mengacu pada jadwal Tahap 2.

### R-01 Pengiriman komponen terlambat (16, Tinggi → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Avoid***: menghilangkan ketergantungan pada barang impor. ***Mitigate***: mengurangi kemungkinan dan dampak keterlambatan |
| Tindakan | 1) Saat menyusun BOM (1.4.1), utamakan komponen yang **tersedia di pemasok dalam negeri**; board ESP32 dipilih antara lain karena mudah didapat di toko elektronik lokal. 2) Siapkan **minimal dua pemasok** untuk setiap komponen utama. 3) Pesan **segera** setelah BOM disetujui. 4) Beli **1 unit komponen cadangan** untuk setiap jenis. 5) Bila perlu, gunakan *fast tracking* (jadwal Tahap 2, Bagian 8): komponen prototipe dibeli lebih dulu |
| Pemicu | Pemasok belum mengonfirmasi stok dalam 2 hari kerja setelah pesanan, atau nomor resi belum ada di hari ke-5 |
| Pemilik | MP |
| Batas waktu | Daftar pemasok siap sebelum 1.4.2 dimulai (minggu 7) |
| Residual | K 2 × D 3 = **6 (Sedang)**: keterlambatan masih mungkin, tetapi dengan pemasok cadangan diperkirakan < 9 hari |

### R-02 Izin pemasangan terlambat (8, Sedang → 4, Rendah)

| Butir | Isi |
|---|---|
| Strategi | ***Escalate***: izin dari pemda dan pemilik lokasi berada **di luar wewenang tim proyek**, sehingga diserahkan ke sponsor (BPBD) yang punya jalur antarinstansi. ***Mitigate***: mempercepat pengurusan |
| Tindakan | 1) Ajukan izin **langsung setelah survei lokasi** (1.2.4) selesai. 2) Minta **surat dukungan dari BPBD** untuk dilampirkan. 3) Saat survei, tetapkan **satu lokasi cadangan** untuk setiap wilayah |
| Pemicu | Belum ada jawaban 10 hari kerja setelah pengajuan |
| Pemilik | MP (eskalasi ke sponsor) |
| Batas waktu | Pengajuan izin di minggu 4 |
| Residual | K 1 × D 4 = **4 (Rendah)**: dengan dukungan BPBD dan lokasi cadangan, kemungkinannya kecil |

### R-03 Halaman BMKG berubah atau akses diblokir (15, Tinggi → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate***: membuat pembacaan tahan terhadap perubahan. ***Accept* aktif**: menyiapkan rencana darurat bila tetap terjadi |
| Tindakan | 1) Playwright mencari **teks nama wilayah tanpa bergantung pada bentuk elemen HTML** (keputusan desain). 2) Pengecekan **setiap 5 menit dan hanya halaman provinsi yang relevan**, supaya tidak membebani server BMKG. 3) Status **"gagal muat"** dan notifikasi ke admin (1.5.3, 1.5.6). 4) Saat studi halaman (1.2.2), periksa apakah BMKG menyediakan *feed* RSS/CAP sebagai **sumber cadangan**. 5) **Rencana darurat**: admin dapat menyalakan peringatan secara manual dari dasbor (1.5.5) bila pembacaan otomatis terganggu |
| Pemicu | Modul pemantau mencatat "gagal muat" 3 kali berturut-turut, atau teks penanda halaman tidak ditemukan |
| Pemilik | PS |
| Batas waktu | Studi halaman di minggu 2; modul pemantau di minggu 6–7 |
| Residual | K 2 × D 3 = **6 (Sedang)**: bila terjadi, sistem tetap bisa dipakai lewat sumber cadangan atau mode manual |

### R-04 Salah cocok nama wilayah (12, Sedang → 4, Rendah)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate*** |
| Tindakan | 1) Pencocokan **per kata utuh** (keputusan desain). 2) Susun **daftar variasi nama** dan **daftar nama mirip yang harus ditolak** (1.2.3). 3) Uji khusus pencocokan nama (1.7.2) dengan target **0 salah cocok** (kriteria penerimaan 2) |
| Pemicu | Uji 1.7.2 menemukan satu atau lebih salah cocok, atau muncul penulisan nama wilayah baru di halaman BMKG |
| Pemilik | AS |
| Batas waktu | Daftar nama di minggu 3; uji di minggu 8 |
| Residual | K 1 × D 4 = **4 (Rendah)** |

### R-05 Listrik atau internet di lokasi putus (12, Sedang → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate*** |
| Tindakan | 1) Baterai cadangan/UPS untuk **≥ 4 jam** (kriteria penerimaan 6). 2) **Modem 4G** sebagai jalur internet bila Wi-Fi tidak tersedia. 3) Fitur **sambung ulang otomatis** dan **heartbeat** (1.6.3). 4) Saat survei (1.2.4), pilih titik dengan **sinyal baik**. 5) Uji kegagalan (1.7.5) mensimulasikan listrik padam dan internet putus |
| Pemicu | Uji baterai < 4 jam, atau heartbeat hilang > 5 menit saat pengujian |
| Pemilik | EI |
| Batas waktu | Desain rangkaian di minggu 5–6; uji kegagalan di minggu 15–16 |
| Residual | K 2 × D 3 = **6 (Sedang)**: padam lebih lama dari kapasitas baterai tetap mungkin |

### R-06 *Bug* lebih banyak dari perkiraan (9, Sedang → 4, Rendah)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate*** + ***Accept* aktif** |
| Tindakan | 1) **Uji dini**: uji pencocokan nama (minggu 8) dan uji unit (minggu 10–11) dijalankan jauh sebelum uji integrasi. 2) **Tinjauan kode** untuk setiap perubahan. 3) **Halaman uji tiruan**, supaya uji integrasi tidak perlu menunggu peringatan BMKG sungguhan. 4) **Cadangan waktu 5 hari kerja** dipegang manajer proyek (*contingency reserve*, PMBOK 4, Bagian 6.4.2.5, hlm. 150). Cadangan ini tidak dimasukkan ke jadwal sebagai aktivitas; bila terpakai seluruhnya, proyek selesai paling lambat di hari ke-97 |
| Pemicu | Masih ada *bug* berat yang belum diperbaiki di hari ke-5 uji integrasi |
| Pemilik | QA |
| Batas waktu | Uji dini di minggu 8–11 |
| Residual | K 2 × D 2 = **4 (Rendah)** |

### R-07 Engineer IoT berhalangan (8, Sedang → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate***: mengurangi ketergantungan pada satu orang |
| Tindakan | 1) Semua firmware disimpan di **Git** dengan catatan perubahan harian. 2) Firmware **ditinjau oleh PS**, sehingga ada orang kedua yang memahaminya. 3) Skema rangkaian (1.3.4) didokumentasikan lengkap |
| Pemicu | EI tidak hadir lebih dari 2 hari kerja selama minggu 9–12 |
| Pemilik | MP |
| Batas waktu | Mulai minggu 9 (perakitan prototipe) |
| Residual | K 2 × D 3 = **6 (Sedang)**: pengganti tetap butuh waktu mempelajari, diperkirakan < 1 minggu |

### R-08 Kesalahan kode atau kebocoran data dari pemakaian Claude Code (12, Sedang → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate*** |
| Tindakan | 1) **Tinjauan kode wajib** oleh anggota lain sebelum kode digabungkan (aturan di Tahap 1, Bagian 1.11). 2) Kata sandi dan kunci akses **disimpan di berkas konfigurasi terpisah yang tidak ikut ke repositori**, dan tidak pernah dimasukkan ke percakapan dengan AI. 3) Pemeriksaan keamanan dasar saat *deploy* (1.8.2): *firewall*, HTTPS, dan memastikan tidak ada data rahasia di repositori |
| Pemicu | Tinjauan kode menemukan bagian yang tidak bisa dijelaskan penulisnya, atau ada data rahasia terdeteksi di repositori |
| Pemilik | PS |
| Batas waktu | Aturan berlaku sejak penyiapan alat (minggu 2) |
| Residual | K 2 × D 3 = **6 (Sedang)** |

### R-09 Keluhan warga terhadap sirene (12, Sedang → 6, Sedang)

| Butir | Isi |
|---|---|
| Strategi | ***Mitigate*** |
| Tindakan | 1) Pola bunyi, volume, dan jam senyap **disepakati bersama sponsor** saat desain (1.3.5). 2) **Sosialisasi** sebelum sistem dipakai (1.8.4): arti setiap bunyi dan lampu, serta tindakan yang harus dilakukan warga. 3) Tombol **senyapkan sementara** di dasbor untuk keadaan tertentu. 4) Volume diatur ulang saat uji lapangan |
| Pemicu | Ada keluhan warga selama uji lapangan |
| Pemilik | AS |
| Batas waktu | Desain di minggu 5; sosialisasi di minggu 16 |
| Residual | K 2 × D 3 = **6 (Sedang)** |

### R-10 Perangkat dicuri atau dirusak (6, Sedang → 4, Rendah)

| Butir | Isi |
|---|---|
| Strategi | ***Transfer***: mengalihkan beban kerugian ke pihak ketiga. ***Mitigate***: mempersulit pencurian |
| Tindakan | 1) **Asuransi perangkat**, atau **perjanjian dengan pemilik lokasi** yang mencantumkan tanggung jawab keamanan. 2) Pasang di **ketinggian** dengan *enclosure* **terkunci**. 3) Fitur diagnosa (1.6.4) segera memberi tahu admin bila perangkat mati tanpa sebab teknis |
| Pemicu | Perangkat terputus tanpa sebab teknis, atau ada laporan kerusakan fisik |
| Pemilik | TL |
| Batas waktu | Perjanjian atau asuransi selesai sebelum pemasangan (minggu 14) |
| Residual | K 2 × D 2 = **4 (Rendah)** |

---

## 6. Keterkaitan dengan WBS dan jadwal

Sesuai prinsip integrasi (slide 07), respons risiko yang menambah pekerjaan harus masuk kembali ke WBS dan jadwal:

| Respons | Tempat di WBS | Dampak ke jadwal |
|---|---|---|
| Komponen dalam negeri, dua pemasok, unit cadangan (R-01) | Sudah tercakup di 1.4.1 dan 1.4.2 | Tidak ada |
| Lokasi cadangan dan surat dukungan BPBD (R-02) | Sudah tercakup di 1.2.4 dan 1.4.4 | Tidak ada |
| Aktivasi peringatan manual dari dasbor (R-03) | **Ditambahkan** ke uraian 1.3.6 (Desain dasbor) dan 1.5.5 (Dasbor admin) | Durasi 1.5.5 tidak diubah karena fiturnya kecil; bila ternyata lebih lama, masih tertutup kelonggaran 10 hari pekerjaan perangkat lunak |
| Uji dini, tinjauan kode, halaman uji tiruan (R-06, R-08) | Sudah tercakup di 1.5.x, 1.7.1, 1.7.2, 1.7.4 | Tidak ada |
| Cadangan waktu 5 hari (R-06) | Bukan *work package*; dipegang manajer proyek | Batas selesai terburuk: hari ke-97 |
| Asuransi atau perjanjian lokasi (R-10) | Masuk anggaran (1.1.1) dan izin (1.4.4) | Tidak ada |

**Pemantauan:** Risk Register ditinjau dalam rapat mingguan (1.1.2) dan diperbarui melalui 1.1.3 (Pengendalian perubahan dan pemantauan risiko), sesuai siklus risiko di slide 11 (hlm. 19–20).

---

## Glosarium

| Istilah | Penjelasan |
|---|---|
| *Accept* aktif | Strategi respons: risiko diterima, tetapi disiapkan cadangan atau rencana darurat |
| *Avoid* | Strategi respons: mengubah rencana supaya ancaman hilang |
| *Contingency reserve* | Cadangan waktu atau biaya untuk menghadapi risiko |
| *Escalate* | Strategi respons: risiko di luar wewenang tim diserahkan ke pihak yang lebih berwenang |
| Kemungkinan (K) | Seberapa besar peluang risiko terjadi |
| Dampak (D) | Seberapa parah akibat risiko bila terjadi |
| *Mitigate* | Strategi respons: menurunkan kemungkinan dan/atau dampak |
| Pemicu (*trigger*) | Tanda bahwa sebuah risiko mulai terjadi |
| Pemilik risiko (*risk owner*) | Orang yang bertanggung jawab memantau dan menangani satu risiko |
| Probability-Impact Matrix | Matriks kemungkinan × dampak untuk menentukan prioritas risiko |
| RBS (*Risk Breakdown Structure*) | Pohon kategori risiko untuk membantu menemukan risiko |
| *Residual risk* | Risiko sisa; nilai risiko setelah respons dijalankan |
| Risk Register | Daftar risiko beserta nilai dan rencana responsnya |
| *Transfer* | Strategi respons: mengalihkan dampak dan penanganan risiko ke pihak ketiga |
