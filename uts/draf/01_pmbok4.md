# Bab 2 — Dokumen PMBOK 4th Edition (draf)

> Berkas kerja UTS. Data (nama, tanggal, anggaran) diambil dari [00_data_induk.md](00_data_induk.md).
> Penilaian pengaruh dan kepentingan sudah diputuskan pengguna (13 Nov 2026).
> Isi kolom **Harapan utama**, **Strategi**, dan **Komunikasi** masih **[USULAN]** dan perlu ditinjau serta ditulis ulang dengan bahasa sendiri.

---

## 2.1 Pra-Inisiasi

> **Catatan penempatan:** soal menaruh Stakeholder Register dan Stakeholder Management Strategy di Pra-Inisiasi. Di PMBOK 4, keduanya adalah hasil proses **10.1 Identify Stakeholders** dalam kelompok proses *Initiating* (PMBOK 4 hlm 246–251). Laporan mengikuti urutan soal, dan catatan ini dicantumkan sebagai keterangan.

### 2.1.1 Stakeholder Register

*Stakeholder* (pemangku kepentingan) adalah orang, kelompok, atau lembaga yang terlibat dalam proyek, terdampak oleh proyek, atau bisa memengaruhi proyek. *Stakeholder Register* adalah daftar semua pihak itu beserta peran, pengaruh, dan kepentingannya. Dokumen ini menjadi acuan untuk mengelola komunikasi sepanjang proyek (slide 05 hlm 12; contoh JWD di slide Minggu 04 slide 71–72).

- **Pengaruh**: seberapa besar kuasa pihak itu atas proyek, yaitu apakah ia bisa memutuskan, menghentikan, atau memaksakan perubahan, dan apakah ia sulit diganti.
- **Kepentingan**: seberapa besar pihak itu peduli pada hasil proyek.

**Tabel 2.1 Stakeholder Register Proyek Super App Nusantara Express**

| No | Nama / Pihak | Jabatan / Bentuk | Int/Eks | Peran di proyek | Kepentingan | Pengaruh | Harapan utama |
|---|---|---|---|---|---|---|---|
| S01 | Ahmad Fauzan Hakim | Direktur Utama | Internal | Sponsor proyek; pemberi dana dan otorisasi | Tinggi | Tinggi | Platform menjadi sumber pendapatan baru; Rilis 1 berhasil sehingga layak dilanjutkan pada evaluasi M4 |
| S02 | Muhammad Fadhil | Direktur Keuangan | Internal | Menyetujui rincian anggaran dan mencairkan dana bertahap | Tinggi | Tinggi | Biaya tidak melampaui Rp 15 miliar; laporan biaya berkala; balik modal sesuai Business Case |
| S03 | Eka Putra Kurnia | Project Manager | Internal | Memimpin perencanaan, pelaksanaan, dan pengendalian proyek | Tinggi | Tinggi | Proyek selesai sesuai lingkup, waktu, dan biaya; tim bekerja solid |
| S04 | Zaki Farhan Maulana dan tim | Kepala Software Engineering | Internal | Membangun aplikasi (*marketplace*, *tracking*, *wallet*, AI) | Tinggi | Sedang | Kebutuhan jelas sejak awal; beban kerja wajar; pilihan teknologi tepat |
| S05 | Ali Akbar Ramadhan | Kepala UI/UX | Internal | Merancang antarmuka dan pengalaman pengguna | Tinggi | Sedang | Aplikasi mudah dipakai UMKM yang belum terbiasa dengan teknologi digital |
| S06 | Hasan Arifin | Kepala Infrastructure & Cybersecurity | Internal | Menyiapkan infrastruktur dan menjamin keamanan; memberi persetujuan keamanan sebelum rilis | Tinggi | Tinggi | Keamanan data dan transaksi lolos uji sebelum setiap rilis |
| S07 | Yusuf Kamil Hidayat | Kepala Business Development | Internal | Menjalin kerja sama dengan UMKM, kurir, dan mitra pembayaran | Tinggi | Sedang | Jumlah UMKM dan mitra yang bergabung sesuai target |
| S08 | Umar Hamzah | Kepala Operations & Logistics | Internal | Mengoperasikan layanan; penerima serah terima di M6 | Tinggi | Sedang | Sistem stabil dan mudah dioperasikan setelah serah terima |
| S09 | Ibrahim Hanif | Kepala Legal & Compliance | Internal | Mengurus izin, kontrak mitra, dan kepatuhan regulasi | Tinggi | Tinggi | Semua izin dan kontrak selesai sebelum peluncuran |
| S10 | Dewan Komisaris | Organ pengawas perusahaan | Internal | Mengawasi keputusan investasi direksi | Rendah | Tinggi | Investasi memberi manfaat dan tata kelolanya baik |
| S11 | Paguyuban UMKM Barokah Yogyakarta (fiktif) | Asosiasi UMKM | Eksternal | Mitra percontohan Rilis 1 di Yogyakarta | Tinggi | Tinggi | Biaya berjualan rendah, penjualan naik, ada pendampingan |
| S12 | UMKM penjual (perorangan) | Pelaku usaha | Eksternal | Pengguna sisi penjual | Tinggi | Rendah | Mudah mendaftar dan berjualan; dana penjualan cepat cair |
| S13 | Pembeli / pengguna aplikasi | Masyarakat | Eksternal | Pengguna sisi pembeli; peserta survei dan uji coba | Sedang | Rendah | Belanja mudah dan aman, ongkos kirim terjangkau, pelacakan akurat |
| S14 | PT Amanah Ekspres Logistik (fiktif) | Perusahaan kurir | Eksternal | Mitra pengiriman barang | Sedang | Sedang | Volume kiriman bertambah; integrasi sistem sederhana |
| S15 | PT Berkah Pay Indonesia (fiktif) | Penyelenggara pembayaran berizin | Eksternal | Mitra layanan *digital wallet*; *wallet* berjalan di bawah izin uang elektronik milik mitra ini | Tinggi | Tinggi | Volume transaksi tinggi; kepatuhan terhadap aturan pembayaran terjaga |
| S16 | PT Nur Awan Teknologi (fiktif) | Penyedia *cloud* | Eksternal | Penyedia server dan layanan *cloud* | Rendah | Sedang | Kontrak jangka panjang; pemakaian layanan sesuai perjanjian |
| S17 | PT Al-Hifzh Keamanan Siber (fiktif) | Konsultan keamanan | Eksternal | Melakukan uji keamanan (*penetration test*) sebelum rilis | Rendah | Rendah | Lingkup uji jelas dan jadwal pasti |
| S18 | Bank Indonesia | Regulator | Eksternal | Pengatur dan pengawas sistem pembayaran | Rendah | Tinggi | Layanan pembayaran mematuhi ketentuan dan melindungi konsumen **[CEK]** |
| S19 | Kementerian Komunikasi dan Digital | Regulator | Eksternal | Pendaftaran penyelenggara sistem elektronik; pelindungan data | Rendah | Tinggi | Aplikasi terdaftar dan data pribadi pengguna terlindungi **[CEK]** |
| S20 | Dinas Koperasi dan UKM DIY | Pemerintah daerah | Eksternal | Mitra pendukung pembinaan UMKM di DIY | Sedang | Rendah | UMKM DIY makin mampu berjualan secara digital |

*Penetration test*: uji keamanan dengan mencoba membobol sistem secara sah untuk menemukan celah sebelum dimanfaatkan penjahat.

### 2.1.2 Stakeholder Management Strategy

*Stakeholder Management Strategy* adalah rencana cara mengelola setiap stakeholder sesuai posisinya. Posisi itu dipetakan dengan **Power-Interest Grid**, yaitu matriks empat kotak berdasarkan pengaruh (*power*) dan kepentingan (*interest*) (slide 05 hlm 13–15; contoh JWD di slide Minggu 04 slide 73–75). Penilaian "sedang" ditempatkan ke kotak terdekat berdasarkan pertimbangan di Tabel 2.1.

**Gambar 2.1 Power-Interest Grid (sketsa; diagram final dibuat saat perakitan laporan)**

```
   PENGARUH
      ▲
      │  KEEP SATISFIED                    │  MANAGE CLOSELY
      │  (jaga tetap puas)                 │  (libatkan erat)
TINGGI│  S10 Dewan Komisaris               │  S01 Direktur Utama
      │  S16 Penyedia cloud (sedang)       │  S02 Direktur Keuangan
      │  S18 Bank Indonesia                │  S03 Project Manager
      │  S19 Kementerian Kom. & Digital    │  S06 Kepala Infra & Cyber
      │                                    │  S09 Kepala Legal
      │                                    │  S11 Paguyuban UMKM
      │                                    │  S15 Mitra pembayaran
      ├────────────────────────────────────┼─────────────────────────────────
      │  MONITOR                           │  KEEP INFORMED
      │  (pantau)                          │  (beri informasi rutin)
RENDAH│  S17 Konsultan keamanan            │  S04 Kepala SE & tim (sedang)
      │                                    │  S05 Kepala UI/UX (sedang)
      │                                    │  S07 Kepala BizDev (sedang)
      │                                    │  S08 Kepala Ops & Logistik (sedang)
      │                                    │  S12 UMKM perorangan
      │                                    │  S13 Pembeli
      │                                    │  S14 Mitra kurir (sedang)
      │                                    │  S20 Dinas Koperasi & UKM DIY
      └────────────────────────────────────┴─────────────────────────────────►
                    RENDAH                              TINGGI      KEPENTINGAN
```

**Strategi per kotak** (slide 05 hlm 14):
- ***Manage Closely***: libatkan dalam pengambilan keputusan, rapat rutin, laporan kemajuan rinci.
- ***Keep Satisfied***: penuhi syarat dan harapannya. Beri ringkasan eksekutif, dan libatkan hanya pada keputusan besar.
- ***Keep Informed***: beri informasi perkembangan secara rutin dan minta umpan balik.
- ***Monitor***: pantau perubahan posisinya dan beri informasi secukupnya.

**Tabel 2.2 Stakeholder Management Strategy**

| No | Pihak | Pengaruh | Kepentingan | Kotak | Strategi | Komunikasi (bentuk · frekuensi) |
|---|---|---|---|---|---|---|
| S01 | Direktur Utama | Tinggi | Tinggi | *Manage Closely* | Libatkan di setiap keputusan *milestone*, terutama keputusan lanjut atau berhenti di M4 | Rapat pengarah · bulanan, ditambah di setiap *milestone* |
| S02 | Direktur Keuangan | Tinggi | Tinggi | *Manage Closely* | Ajukan pencairan bertahap per *milestone* disertai realisasi biaya | Laporan biaya · bulanan |
| S03 | Project Manager | Tinggi | Tinggi | *Manage Closely* | Pemegang kendali harian; menjadi penghubung semua pihak | — |
| S06 | Kepala Infra & Cyber | Tinggi | Tinggi | *Manage Closely* | Masukkan persetujuan keamanan sebagai syarat rilis; libatkan sejak desain | Rapat tim · mingguan |
| S09 | Kepala Legal | Tinggi | Tinggi | *Manage Closely* | Petakan semua izin di awal; pantau statusnya sebagai jalur kritis rilis | Rapat tim · mingguan; laporan status izin · dua mingguan |
| S11 | Paguyuban UMKM Barokah | Tinggi | Tinggi | *Manage Closely* | Ajak menyusun kebutuhan dan ikut uji coba; tunjuk perwakilan tetap | Lokakarya · awal proyek; uji coba · sebelum Rilis 1 dan Rilis 2 |
| S15 | Mitra pembayaran | Tinggi | Tinggi | *Manage Closely* | Kunci kontrak dan jadwal integrasi lebih awal; uji kepatuhan bersama | Rapat teknis · dua mingguan |
| S10 | Dewan Komisaris | Tinggi | Rendah | *Keep Satisfied* | Laporkan lewat Direktur Utama; libatkan pada keputusan besar | Ringkasan eksekutif · per *milestone* utama |
| S16 | Penyedia *cloud* | Sedang | Rendah | *Keep Satisfied* | Tetapkan jaminan tingkat layanan di kontrak; siapkan rencana cadangan | Tinjauan layanan · bulanan |
| S18 | Bank Indonesia | Tinggi | Rendah | *Keep Satisfied* | Penuhi persyaratan lewat mitra pembayaran dan tim Legal | Melalui Legal · sesuai ketentuan |
| S19 | Kementerian Kom. & Digital | Tinggi | Rendah | *Keep Satisfied* | Selesaikan pendaftaran sistem elektronik sebelum Rilis 1 | Melalui Legal · sesuai ketentuan |
| S04 | Kepala SE & tim | Sedang | Tinggi | *Keep Informed* | Libatkan dalam estimasi; atur cara kerja di Team Contract | Rapat tim · mingguan |
| S05 | Kepala UI/UX | Sedang | Tinggi | *Keep Informed* | Hubungkan langsung dengan masukan UMKM dari uji coba | Rapat tim · mingguan |
| S07 | Kepala BizDev | Sedang | Tinggi | *Keep Informed* | Selaraskan target perekrutan UMKM dan mitra dengan jadwal rilis | Rapat tim · mingguan |
| S08 | Kepala Ops & Logistik | Sedang | Tinggi | *Keep Informed* | Libatkan sejak awal agar siap menerima serah terima di M6 | Rapat tim · mingguan |
| S12 | UMKM perorangan | Rendah | Tinggi | *Keep Informed* | Sosialisasi dan pelatihan lewat paguyuban | Grup pesan dan pelatihan · menjelang rilis |
| S13 | Pembeli | Rendah | Sedang | *Keep Informed* | Survei kebutuhan dan uji coba terbatas | Survei · awal proyek; uji coba · sebelum rilis |
| S14 | Mitra kurir | Sedang | Sedang | *Keep Informed* | Bagikan rencana integrasi dan perkiraan volume | Rapat koordinasi · bulanan |
| S20 | Dinas Koperasi & UKM DIY | Rendah | Sedang | *Keep Informed* | Ajak membantu sosialisasi ke UMKM | Audiensi · awal proyek; undangan peluncuran |
| S17 | Konsultan keamanan | Rendah | Rendah | *Monitor* | Kelola lewat kontrak dan jadwal uji yang pasti | Sesuai jadwal uji |

### 2.1.3 Business Case

*Business Case* adalah dokumen justifikasi bisnis yang menjawab pertanyaan "mengapa proyek ini layak dibiayai?" (slide 05 hlm 6–9). Di PMBOK 4, *business case* menjadi **masukan** bagi proses 4.1 *Develop Project Charter* (hlm 75). Struktur di bawah mengikuti contoh Schwalbe yang dipakai di slide Minggu 04 slide 55–69.

> Keputusan pengguna: masalah/peluang opsi C (gabungan), target moderat, tiga opsi solusi, model pendapatan komisi + iklan + selisih ongkos kirim, analisis keuangan tanpa NPV (prinsip tanpa riba).
> Angka anggaran, asumsi pendapatan, dan bobot penilaian opsi: **[USULAN]** yang sudah disetujui untuk dipakai; tetap bisa diubah di data induk.

#### 1.0 Latar belakang

PT Nusantara Digital Indonesia (PT ND) berencana membangun **Nusantara Express**, *super app omni-channel* yang menyatukan empat layanan dalam satu aplikasi: *marketplace*, pengiriman dengan pelacakan *real-time*, pembayaran *digital wallet*, dan rekomendasi produk berbasis AI untuk UMKM. Proyek dijalankan selama ± 6 bulan (4 Januari – 30 Juni 2027) dengan melibatkan enam divisi internal dan sejumlah mitra eksternal.

#### 2.0 Tujuan bisnis

Tujuan dirumuskan dengan kaidah **SMART** (*Specific, Measurable, Achievable, Relevant, Time-bound*: spesifik, terukur, bisa dicapai, relevan, berbatas waktu).

| No | Tujuan | Ukuran | Batas waktu |
|---|---|---|---|
| T1 | Rilis 1 (*marketplace*, *tracking*, *wallet* dasar) beroperasi di Yogyakarta | Aplikasi tersedia untuk umum dan lolos uji keamanan | 31 Maret 2027 (M3) |
| T2 | Menghimpun UMKM aktif | **1.000 UMKM aktif** (minimal 1 transaksi per bulan) | 30 Juni 2027 |
| T3 | Menghimpun pembeli aktif | **20.000 pembeli aktif** (minimal 1 pembelian per bulan) | 30 Juni 2027 |
| T4 | Rilis 2 (rekomendasi AI dan perluasan wilayah) beroperasi | Fitur rekomendasi aktif bagi seluruh UMKM terdaftar | 15 Juni 2027 (M5) |
| T5 | Investasi kembali | Balik modal ± 2,5 tahun setelah peluncuran penuh | ± awal 2030 |

#### 3.0 Situasi saat ini dan pernyataan masalah/peluang

**Masalah (sisi UMKM).** Untuk berjualan daring, UMKM harus memakai beberapa layanan terpisah: satu aplikasi untuk berjualan, layanan lain untuk mengirim barang, dan layanan lain lagi untuk menerima pembayaran. Akibatnya:
- pencatatan pesanan, pengiriman, dan uang masuk tidak menyatu;
- potongan biaya di tiap layanan menumpuk;
- UMKM tidak punya bantuan berbasis data untuk mengetahui produk apa yang sebaiknya ditawarkan.

**Peluang (sisi PT ND).** Masalah tersebut adalah peluang bisnis: satu platform yang menyatukan jual, kirim, dan bayar dengan biaya yang lebih rendah dapat menarik UMKM untuk pindah, dan membuka sumber pendapatan baru bagi PT ND di pasar belanja daring.

**Pertimbangan waktu.** Rilis 1 jatuh setelah musim belanja Ramadan 2027 (± Februari–Maret), sehingga peluang musim ramai itu terlewat. Tanggal rilis sengaja tidak dimajukan. Meluncur terburu-buru dengan aplikasi pembayaran yang belum lolos uji keamanan dan perizinan lebih berbahaya daripada kehilangan satu musim ramai.

> **[CEK]** Bila bagian ini memakai data statistik (misalnya jumlah UMKM di Indonesia atau di DIY, atau porsi UMKM yang sudah berjualan daring), cantumkan sumber resminya.

#### 4.0 Asumsi kritis dan kendala

**Asumsi** (dianggap benar sebagai dasar perencanaan):
1. Paguyuban UMKM Barokah Yogyakarta bersedia menjadi mitra percontohan Rilis 1.
2. Kontrak dengan mitra kurir dan mitra pembayaran ditandatangani paling lambat akhir Januari 2027 (sebelum M2).
3. Tim proyek ± 50 orang tersedia sejak awal proyek.
4. Izin dan pendaftaran yang dipersyaratkan regulator dapat diselesaikan sebelum Rilis 1.
5. Rata-rata nilai penjualan setiap UMKM aktif Rp 10 juta per bulan.

**Kendala** (batas yang tidak bisa diubah tim proyek):
1. **Waktu:** 6 bulan, berakhir 30 Juni 2027; ada cuti bersama Idulfitri (± 9–10 Maret 2027 **[CEK]**) tepat sebelum Rilis 1.
2. **Biaya:** total Rp 15 miliar, termasuk cadangan risiko 10%.
3. **Regulasi:** ketentuan sistem pembayaran (Bank Indonesia) serta pendaftaran sistem elektronik dan pelindungan data pribadi (Kementerian Komunikasi dan Digital) **[CEK]**.
4. **Prinsip tanpa riba** (kebijakan perusahaan; data induk Bagian 8): modal sendiri tanpa pinjaman berbunga (P1); *wallet* tanpa *paylater* dan cicilan berbunga (P2); dana saldo pengguna di bank syariah (P3 **[CEK]**); pendapatan berupa upah jasa yang ditetapkan terbuka, tanpa denda keterlambatan (P4).

#### 5.0 Analisis opsi dan rekomendasi

| Opsi | Uraian | Kelebihan | Kekurangan |
|---|---|---|---|
| 1. Tidak berbuat apa-apa | PT ND tidak masuk ke pasar ini | Tidak ada biaya dan risiko pelaksanaan | Peluang hilang; pesaing makin kuat |
| 2. Beli/sewa platform jadi (*white-label*) | Memakai aplikasi buatan pihak lain yang diberi merek Nusantara Express | Paling cepat diluncurkan | Kendali atas data dan fitur AI terbatas; ada biaya lisensi dan bagi hasil terus-menerus; fitur bawaan (misalnya *paylater*) belum tentu sesuai prinsip tanpa riba |
| 3. Bangun sendiri, bermitra untuk pengiriman dan pembayaran | Bagian inti (*marketplace*, data, AI) dibangun sendiri; pengiriman dan pembayaran memakai mitra berizin | Kendali penuh atas data dan pengembangan; sesuai prinsip perusahaan | Lebih lama dan lebih mahal di awal; risiko pelaksanaan lebih tinggi |

Ketiga opsi dibandingkan dengan ***Weighted Scoring Model***, yaitu penilaian berbobot atas beberapa kriteria (slide 07 hlm 13). Skor 1–10; makin tinggi makin baik. Untuk kriteria biaya dan risiko, skor tinggi berarti biayanya rendah atau risikonya rendah.

**Tabel 2.3 Weighted Scoring Model**

| Kriteria | Bobot | Opsi 1 | Opsi 2 | Opsi 3 |
|---|---|---|---|---|
| Kesesuaian dengan strategi perusahaan | 25% | 1 | 6 | 9 |
| Kendali atas data dan pengembangan AI | 20% | 1 | 3 | 9 |
| Kesesuaian dengan prinsip tanpa riba | 15% | 10 | 5 | 9 |
| Kecepatan masuk pasar | 15% | 1 | 9 | 5 |
| Biaya selama 3 tahun | 15% | 10 | 6 | 5 |
| Risiko pelaksanaan | 10% | 5 | 6 | 5 |
| **Skor tertimbang** | **100%** | **4,1** | **5,7** | **7,4** |

**Rekomendasi: Opsi 3.** Opsi 3 unggul pada kriteria berbobot terbesar (strategi dan kendali data/AI), dan tetap sesuai prinsip perusahaan. Kelemahannya, yaitu waktu dan biaya, dikendalikan dengan rilis dua tahap dan keputusan lanjut/berhenti di M4.

#### 6.0 Kebutuhan awal proyek

| Modul | Rilis 1 (M3) | Rilis 2 (M5) |
|---|---|---|
| *Marketplace* | Pendaftaran UMKM, katalog produk, keranjang, pemesanan, ulasan | Promosi berbayar untuk UMKM |
| Pengiriman dan *tracking* | Integrasi dengan mitra kurir, pelacakan *real-time*, notifikasi status | Perluasan wilayah layanan |
| *Digital wallet* | Isi saldo, pembayaran, pencairan dana penjual; **tanpa *paylater* dan cicilan berbunga** | — |
| Rekomendasi AI | — | Rekomendasi produk dan saran stok untuk UMKM |
| Pendukung | Dasbor penjualan UMKM, panel admin, keamanan (enkripsi, verifikasi dua langkah), pemenuhan izin | Laporan kinerja untuk manajemen |

#### 7.0 Estimasi anggaran dan analisis keuangan

**Tabel 2.4 Rincian anggaran proyek**

| Pos | Rp (miliar) |
|---|---|
| Tenaga kerja (± 50 orang × 6 bulan × Rp 25 juta) | 7,5 |
| *Cloud* dan infrastruktur | 1,2 |
| Lisensi perangkat lunak dan API (peta, SMS kode verifikasi, alat AI) | 0,8 |
| Uji keamanan (2 kali) dan audit kepatuhan | 0,6 |
| Perizinan dan legal | 0,4 |
| Perangkat kerja dan perangkat uji | 0,5 |
| Uji coba lapangan, pelatihan UMKM, sosialisasi di Yogyakarta | 1,5 |
| Manajemen proyek dan lain-lain | 1,0 |
| **Subtotal** | **13,5** |
| Cadangan risiko (10%) | 1,5 |
| **Total** | **15,0** |

**Asumsi pendapatan** (tiga tahun operasi, Juli 2027 – Juni 2030):

| Asumsi | Nilai |
|---|---|
| Rata-rata UMKM aktif (tahun 1 / 2 / 3) | 2.500 / 6.000 / 12.000 |
| Nilai penjualan per UMKM aktif | Rp 10 juta per bulan |
| Komisi transaksi | 2,5% dari nilai penjualan |
| Iklan/promosi | 10% UMKM membayar Rp 500 ribu per bulan |
| Selisih ongkos kirim | Rp 1.000 per pesanan (rata-rata belanja Rp 150 ribu) |
| Biaya operasional (tahun 1 / 2 / 3) | Rp 15 / 20 / 28 miliar |

**Tabel 2.5 Arus kas skenario dasar (Rp miliar)**

| | Masa proyek (Jan–Jun 2027) | Tahun 1 | Tahun 2 | Tahun 3 | Total |
|---|---|---|---|---|---|
| Pendapatan | 0 | 11,0 | 26,4 | 52,8 | 90,2 |
| Biaya | 15,0 | 15,0 | 20,0 | 28,0 | 78,0 |
| Arus kas bersih | −15,0 | −4,0 | 6,4 | 24,8 | 12,2 |
| Kumulatif | −15,0 | −19,0 | −12,6 | 12,2 | |

Rincian pendapatan tahun 1 / 2 / 3: komisi 7,5 / 18,0 / 36,0; iklan 1,5 / 3,6 / 7,2; selisih ongkos kirim 2,0 / 4,8 / 9,6.

**Ukuran kelayakan:**
- **ROI** (*Return on Investment*: keuntungan bersih dibandingkan total biaya) = 12,2 ÷ 78,0 = **15,6%** selama tiga tahun.
- ***Payback period*** (lama sampai modal kembali) = 2 tahun + (12,6 ÷ 24,8) ≈ **2,5 tahun** setelah peluncuran, yaitu sekitar awal 2030.

> **Mengapa tidak memakai NPV?** NPV (*Net Present Value*) mengubah uang masa depan menjadi nilai hari ini dengan potongan persentase per tahun, yang dalam praktik sering disamakan dengan bunga. Sesuai prinsip tanpa riba perusahaan (data induk Bagian 8), kelayakan finansial dinilai dengan **ROI** dan ***payback period***, dua cara penilaian yang juga diakui di materi kuliah (slide 05 hlm 9; slide 07 hlm 11–12).

**Tabel 2.6 Analisis sensitivitas terhadap adopsi UMKM**

Biaya dianggap tetap; yang berubah hanya jumlah UMKM aktif.

| Skenario | Total pendapatan 3 tahun | ROI | Balik modal |
|---|---|---|---|
| Pesimis (adopsi −20%) | Rp 72,2 M | **−7,5%** | Tidak tercapai dalam 3 tahun |
| **Dasar** | **Rp 90,2 M** | **+15,6%** | **± 2,5 tahun** |
| Optimis (adopsi +20%) | Rp 108,2 M | +38,8% | ± 2,1 tahun |

**Temuan:** penurunan adopsi 20% saja sudah membuat proyek merugi dalam tiga tahun. Jadi **risiko terbesar proyek ini adalah adopsi UMKM**, bukan teknologi. Karena itu, keputusan lanjut/berhenti di M4 (30 April 2027) memakai data adopsi Rilis 1 sebagai dasar sebelum dana Rilis 2 digunakan sepenuhnya.

#### 8.0 Estimasi jadwal

| Kode | Milestone | Tanggal |
|---|---|---|
| M0 | Project Charter disahkan | 4 Jan 2027 |
| M1 | Kick-off meeting | 6 Jan 2027 |
| M2 | Lingkup dan desain disetujui | 29 Jan 2027 |
| M3 | Rilis 1 di Yogyakarta | 31 Mar 2027 |
| M4 | Evaluasi Rilis 1 dan keputusan lanjut ke Rilis 2 | 30 Apr 2027 |
| M5 | Rilis 2 | 15 Jun 2027 |
| M6 | Penutupan proyek dan serah terima | 30 Jun 2027 |

#### 9.0 Risiko potensial

Rincian probabilitas, dampak, dan mitigasi ada di Risk Register (Bagian 2.3).

1. **Adopsi UMKM dan pembeli di bawah target** (risiko utama; lihat Tabel 2.6). Penjual menunggu pembeli, pembeli menunggu barang.
2. Izin pembayaran atau pendaftaran sistem elektronik belum selesai saat Rilis 1.
3. Mitra kurir atau mitra pembayaran mundur atau terlambat integrasi.
4. Kebocoran data atau gangguan keamanan transaksi.
5. *Force majeure* di kota percontohan (gempa bumi, erupsi Merapi) atau gangguan pusat data/*cloud* berskala besar.
6. Cuti bersama Idulfitri memotong waktu kerja menjelang Rilis 1.
7. Ketentuan penempatan dana saldo pengguna di bank syariah tidak bisa dipenuhi.

---

## 2.2 Inisiasi

### 2.2.1 Project Charter

*Project Charter* adalah dokumen resmi yang **mengesahkan** dimulainya proyek dan memberi wewenang kepada Project Manager untuk memakai sumber daya organisasi. Dokumen ini dihasilkan proses 4.1 *Develop Project Charter* (PMBOK 4 hlm 73), dengan Business Case sebagai salah satu masukannya. Komponen mengikuti slide 05 hlm 18; format mengikuti contoh JWD (slide Minggu 04 slide 77).

> Keputusan pengguna (13 Nov 2026): wewenang PM opsi B, kriteria keberhasilan opsi B, susunan Komite Pengarah, dan daftar di luar lingkup sesuai usulan.

**Tabel 2.7 Identitas proyek**

| Unsur | Isi |
|---|---|
| Judul proyek | Pengembangan Platform "Smart Retails & Delivery Super App" (Nusantara Express) |
| Tanggal mulai | 4 Januari 2027 |
| Tanggal selesai | 30 Juni 2027 |
| Sponsor | Ahmad Fauzan Hakim, Direktur Utama PT Nusantara Digital Indonesia |
| Project Manager | Eka Putra Kurnia |
| Anggaran | Rp 15 miliar, termasuk cadangan risiko Rp 1,5 miliar. Sumber dana: modal sendiri perusahaan, tanpa pinjaman berbunga |

#### Tujuan proyek

Membangun dan meluncurkan *super app* Nusantara Express yang menyatukan *marketplace*, pengiriman dengan pelacakan *real-time*, pembayaran *digital wallet*, dan rekomendasi produk berbasis AI untuk UMKM. Peluncuran dilakukan dalam dua rilis: Rilis 1 di Yogyakarta pada 31 Maret 2027, lalu Rilis 2 (rekomendasi AI dan perluasan wilayah) pada 15 Juni 2027.

#### Kriteria keberhasilan

**Kriteria keberhasilan proyek** (tanggung jawab Project Manager):
1. Rilis 1 beroperasi paling lambat 31 Maret 2027 dan Rilis 2 paling lambat 15 Juni 2027.
2. Total biaya tidak melebihi Rp 15 miliar.
3. Setiap rilis lolos uji keamanan dan memenuhi persyaratan izin sebelum diluncurkan.
4. Sistem beserta dokumentasinya diserahterimakan kepada Operations & Logistics paling lambat 30 Juni 2027.
5. Prinsip tanpa riba P1–P4 terpenuhi di seluruh fitur dan kontrak.

**Indikator manfaat awal** (dipantau di M4 dan M6; tanggung jawab Kepala Business Development dan Sponsor):
- 1.000 UMKM aktif per 30 Juni 2027.
- 20.000 pembeli aktif per 30 Juni 2027.

> Pemisahan ini disengaja: PM dapat menjamin produk selesai tepat waktu, tepat biaya, dan sesuai mutu, tetapi tidak dapat menjamin UMKM dan pembeli mau memakainya. Target adopsi tetap dicantumkan karena menjadi dasar keputusan lanjut/berhenti di M4 (lihat Business Case Tabel 2.6).

#### Ringkasan lingkup

| Termasuk | Tidak termasuk |
|---|---|
| Empat modul (*marketplace*, pengiriman dan *tracking*, *digital wallet*, rekomendasi AI) dalam dua rilis | Fitur *paylater* dan cicilan berbunga (prinsip P2) |
| Dasbor penjualan UMKM dan panel admin | Armada kurir milik sendiri (pengiriman memakai mitra kurir) |
| Integrasi dengan mitra kurir dan mitra pembayaran | Izin uang elektronik atas nama PT ND sendiri (*wallet* memakai izin mitra pembayaran S15) |
| Uji keamanan, pemenuhan izin dan pendaftaran sistem elektronik | Layanan di luar Indonesia |
| Uji coba lapangan dan pelatihan UMKM di Yogyakarta | Toko fisik atau mesin kasir untuk UMKM |

Rincian lingkup ada di Project Scope Statement (Bagian 2.3).

#### Milestone

| Kode | Milestone | Tanggal |
|---|---|---|
| M0 | Project Charter disahkan | 4 Jan 2027 |
| M1 | Kick-off meeting | 6 Jan 2027 |
| M2 | Lingkup dan desain disetujui | 29 Jan 2027 |
| M3 | Rilis 1 di Yogyakarta | 31 Mar 2027 |
| M4 | Evaluasi Rilis 1 dan keputusan lanjut ke Rilis 2 | 30 Apr 2027 |
| M5 | Rilis 2 | 15 Jun 2027 |
| M6 | Penutupan proyek dan serah terima | 30 Jun 2027 |

#### Pendekatan

1. Produk dikembangkan dan diluncurkan dalam **dua rilis**. Rilis 1 menguji pasar di satu kota percontohan sebelum perluasan.
2. Pada **M4**, Komite Pengarah memutuskan lanjut, menyesuaikan, atau menghentikan Rilis 2 berdasarkan data adopsi dan kinerja Rilis 1.
3. Bagian inti (*marketplace*, data, AI) dibangun sendiri. Pengiriman dan pembayaran memakai mitra berizin.
4. **Komite Pengarah** bersidang setiap bulan dan di setiap *milestone*.

#### Wewenang Project Manager

| Keputusan | Wewenang |
|---|---|
| Perubahan biaya sampai Rp 250 juta per perubahan | PM memutuskan sendiri, lalu melaporkannya ke Komite Pengarah |
| Pergeseran jadwal aktivitas sampai 1 minggu yang tidak menggeser *milestone* | PM memutuskan sendiri |
| Perubahan di atas batas tersebut, perubahan *milestone*, atau perubahan lingkup | Persetujuan Komite Pengarah |
| Pemakaian dana cadangan risiko (Rp 1,5 miliar) | Persetujuan Komite Pengarah |
| Penugasan dan pengaturan kerja anggota tim proyek | PM, berkoordinasi dengan kepala divisi |

#### Peran dan tanggung jawab

| Nama | Jabatan | Peran di proyek |
|---|---|---|
| Ahmad Fauzan Hakim | Direktur Utama | Sponsor; Ketua Komite Pengarah; pengambil keputusan di M4 |
| Muhammad Fadhil | Direktur Keuangan | Anggota Komite Pengarah; menyetujui pencairan dana bertahap |
| Eka Putra Kurnia | Project Manager | Memimpin proyek; Sekretaris Komite Pengarah |
| Ibrahim Hanif | Kepala Legal & Compliance | Anggota Komite Pengarah; izin, kontrak mitra, kepatuhan prinsip P1–P4 |
| Hasan Arifin | Kepala Infrastructure & Cybersecurity | Anggota Komite Pengarah; infrastruktur dan persetujuan keamanan sebelum rilis |
| Zaki Farhan Maulana | Kepala Software Engineering | Pengembangan aplikasi |
| Ali Akbar Ramadhan | Kepala UI/UX | Desain antarmuka dan pengalaman pengguna |
| Yusuf Kamil Hidayat | Kepala Business Development | Kemitraan UMKM, kurir, dan pembayaran; penanggung jawab indikator adopsi |
| Umar Hamzah | Kepala Operations & Logistics | Kesiapan operasional; penerima serah terima di M6 |

Daftar seluruh stakeholder ada di Stakeholder Register (Tabel 2.1).

#### Asumsi, kendala, dan risiko utama

- **Asumsi dan kendala:** sesuai Business Case bagian 4.0. Kendala utama: waktu 6 bulan, biaya Rp 15 miliar, regulasi, dan prinsip tanpa riba.
- **Risiko utama:** (1) adopsi UMKM dan pembeli di bawah target; (2) keterlambatan izin atau integrasi mitra pembayaran; (3) gangguan keamanan data. Rincian ada di Risk Register.

#### Persetujuan

| | Sponsor | Project Manager |
|---|---|---|
| Nama | Ahmad Fauzan Hakim | Eka Putra Kurnia |
| Jabatan | Direktur Utama | Project Manager |
| Tanda tangan | *(tanda tangan simulasi)* | *(tanda tangan simulasi)* |
| Tanggal | 4 Januari 2027 | 4 Januari 2027 |

### 2.2.2 Agenda Kick-off Meeting

*Kick-off meeting* adalah rapat resmi pertama antara tim proyek dan stakeholder kunci, diadakan setelah Charter disahkan, untuk menyamakan pemahaman tentang tujuan, lingkup, jadwal, dan peran (slide 05 hlm 22–24). Susunan acara mengikuti pola lima sesi di slide 05 hlm 24; format mengikuti contoh JWD (slide Minggu 04 slide 78).

> Keputusan pengguna (13 Nov 2026): rapat campuran (*hybrid*); peserta internal ditambah tiga mitra kunci.

**Tabel 2.8 Agenda Kick-off Meeting**

| Unsur | Isi |
|---|---|
| Judul rapat | Kick-off Meeting Proyek Super App Nusantara Express |
| Tanggal dan waktu | Rabu, 6 Januari 2027, 09.00–10.30 WIB (M1) |
| Tempat | Ruang rapat kantor PT Nusantara Digital Indonesia, dengan tautan rapat daring untuk peserta eksternal |
| Pimpinan rapat | Eka Putra Kurnia (Project Manager) |
| Tujuan rapat | Memulai proyek secara resmi, menyamakan pemahaman tentang tujuan, lingkup, jadwal, dan anggaran, serta menyepakati peran dan cara berkomunikasi |
| Peserta luring (internal) | Ahmad Fauzan Hakim (Direktur Utama, Sponsor); Muhammad Fadhil (Direktur Keuangan); Eka Putra Kurnia (PM); Zaki Farhan Maulana (Software Engineering); Ali Akbar Ramadhan (UI/UX); Hasan Arifin (Infrastructure & Cybersecurity); Yusuf Kamil Hidayat (Business Development); Umar Hamzah (Operations & Logistics); Ibrahim Hanif (Legal & Compliance) |
| Peserta daring (eksternal) | Perwakilan Paguyuban UMKM Barokah Yogyakarta; perwakilan PT Berkah Pay Indonesia; perwakilan PT Amanah Ekspres Logistik (semuanya fiktif) |
| Bahan yang dibagikan sebelum rapat | Internal: Business Case, Project Charter, Stakeholder Register. Eksternal: ringkasan Charter (tujuan, lingkup, *milestone*) |

> Stakeholder Management Strategy **tidak** dibagikan kepada peserta eksternal, karena berisi penilaian pengaruh dan strategi terhadap masing-masing pihak.

**Susunan acara**

| Waktu | Sesi | Isi | Penyaji |
|---|---|---|---|
| 09.00–09.15 | 1. Pembukaan dan perkenalan | Sambutan sponsor; perkenalan PM, kepala divisi, dan perwakilan mitra; penjelasan agenda | Ahmad Fauzan Hakim; Eka Putra Kurnia |
| 09.15–09.35 | 2. Latar belakang dan tujuan proyek | Ringkasan Business Case: masalah UMKM dan peluang perusahaan, tujuan T1–T5, anggaran Rp 15 miliar, risiko utama adopsi | Eka Putra Kurnia; Muhammad Fadhil (anggaran) |
| 09.35–09.55 | 3. Lingkup dan deliverable | Empat modul dalam dua rilis; hal-hal di luar lingkup; prinsip tanpa riba P1–P4 | Eka Putra Kurnia; Zaki Farhan Maulana; Ibrahim Hanif (prinsip dan izin) |
| 09.55–10.10 | 4. Jadwal dan milestone | Milestone M0–M6; Rilis 1 pada 31 Maret di Yogyakarta; keputusan lanjut/berhenti di M4; dampak cuti bersama Idulfitri | Eka Putra Kurnia |
| 10.10–10.30 | 5. Peran, komunikasi, dan tanya jawab | Komite Pengarah dan wewenang PM; ritme rapat (tim mingguan, Komite Pengarah bulanan); peran mitra di Rilis 1; tanya jawab; penetapan *action items* | Eka Putra Kurnia; semua peserta |

**Tindak lanjut yang diharapkan dari rapat** (dilengkapi dan disahkan saat rapat)

| No | Tindakan | Penanggung jawab | Tenggat |
|---|---|---|---|
| 1 | Menyepakati dan menandatangani Team Contract | Eka Putra Kurnia dan para kepala divisi | 8 Jan 2027 |
| 2 | Menyelesaikan kontrak dengan mitra pembayaran dan mitra kurir | Yusuf Kamil Hidayat; Ibrahim Hanif | 29 Jan 2027 |
| 3 | Menunjuk perwakilan tetap Paguyuban UMKM untuk penyusunan kebutuhan dan uji coba | Yusuf Kamil Hidayat | 13 Jan 2027 |
| 4 | Menyusun Project Scope Statement dan desain awal untuk disetujui | Eka Putra Kurnia; Zaki Farhan Maulana; Ali Akbar Ramadhan | 29 Jan 2027 (M2) |
| 5 | Memetakan seluruh izin dan pendaftaran beserta jadwalnya | Ibrahim Hanif | 15 Jan 2027 |
| … | *(diisi saat rapat)* | | |

**Rapat berikutnya:** Rapat Komite Pengarah, Jumat, 29 Januari 2027, 09.00 WIB (M2: persetujuan lingkup dan desain).

---

## 2.3 Planning

### 2.3.1 Team Contract

*Team Contract* adalah kesepakatan bersama tim proyek tentang cara bekerja sama, dibuat untuk mencegah salah paham dan konflik (slide 07 hlm 29). Dokumen ini berasal dari Schwalbe. Padanannya di PMBOK 4 adalah ***ground rules*** (aturan dasar perilaku tim) dalam proses 9.3 *Develop Project Team* (hlm 233), yang membantu pengelolaan konflik pada proses 9.4 (hlm 239).

> Keputusan pengguna (13 Nov 2026): musyawarah dengan batas 2 hari kerja; penyelesaian konflik bertingkat; pola rapat dan jam inti kerja sesuai usulan.
> Rincian lain di bawah ini: **[USULAN]**.

**Tabel 2.9 Team Contract Proyek Super App Nusantara Express**

| Unsur | Kesepakatan |
|---|---|
| **1. Etika kerja** | Jujur dan amanah dalam melaporkan kemajuan dan masalah. Menjaga kerahasiaan data pengguna dan data mitra. Menghormati waktu dan pendapat rekan kerja. Mematuhi prinsip tanpa riba P1–P4 dalam setiap rancangan fitur dan kesepakatan dengan mitra. |
| **2. Partisipasi** | Hadir di rapat yang menjadi kewajibannya, atau memberi kabar sebelum rapat dimulai. Menyelesaikan tugas sesuai tenggat. Memberi tahu PM paling lambat **2 hari kerja** sebelum tenggat bila tugas berisiko terlambat. |
| **3. Komunikasi** | Grup pesan proyek untuk hal cepat, dibalas paling lambat 2 jam pada jam inti kerja. Surel untuk keputusan dan persetujuan resmi. Aplikasi manajemen tugas proyek untuk pembagian tugas dan status pekerjaan. Masalah yang menghambat pekerjaan disampaikan di rapat harian, tidak menunggu rapat mingguan. |
| **4. Jam kerja dan rapat** | Jam inti kerja **09.00–15.00 WIB**, saat semua anggota tim dapat dihubungi. **Rapat harian** 15 menit pukul 09.00 (luring atau daring). **Rapat tim mingguan** setiap Senin, 10.00–11.00 WIB. **Rapat Komite Pengarah** bulanan dan di setiap *milestone*. Agenda dikirim paling lambat 1 hari sebelum rapat mingguan. Toleransi keterlambatan 5 menit. Notulen dicatat bergiliran antardivisi. **Tidak ada rapat pada waktu salat Zuhur dan Asar, dan pada hari Jumat pukul 11.30–13.00 WIB.** |
| **5. Pengambilan keputusan** | Keputusan tim diambil dengan **musyawarah untuk mufakat**. Bila dalam **2 hari kerja** belum tercapai mufakat, **PM memutuskan** sesuai wewenangnya di Charter. Keputusan di luar wewenang PM dibawa ke Komite Pengarah. Setiap keputusan dicatat di notulen beserta alasannya. |
| **6. Penyelesaian konflik** | Bertingkat, masing-masing paling lama 2 hari kerja sebelum naik ke tingkat berikutnya: (1) dibicarakan langsung antaranggota; (2) dibawa ke kepala divisi masing-masing; (3) dibawa ke PM; (4) dibawa ke Komite Pengarah. Konflik dibahas berdasarkan masalah dan data, bukan pribadi. |
| **7. Pelanggaran kesepakatan** | Pelanggaran dibicarakan lebih dulu secara pribadi oleh PM dengan anggota yang bersangkutan. Bila berulang, dibawa ke kepala divisinya. Tidak ada sanksi denda. |

**Persetujuan** (sesuai tindak lanjut kick-off no. 1, tenggat 8 Januari 2027)

| Nama | Jabatan | Tanda tangan |
|---|---|---|
| Eka Putra Kurnia | Project Manager | *(simulasi)* |
| Zaki Farhan Maulana | Kepala Software Engineering | *(simulasi)* |
| Ali Akbar Ramadhan | Kepala UI/UX | *(simulasi)* |
| Hasan Arifin | Kepala Infrastructure & Cybersecurity | *(simulasi)* |
| Yusuf Kamil Hidayat | Kepala Business Development | *(simulasi)* |
| Umar Hamzah | Kepala Operations & Logistics | *(simulasi)* |
| Ibrahim Hanif | Kepala Legal & Compliance | *(simulasi)* |

Kepala divisi menandatangani atas nama anggota timnya masing-masing.

### 2.3.2 Project Scope Statement

*Project Scope Statement* adalah dokumen formal yang menetapkan batas proyek: apa yang dikerjakan, apa yang **tidak** dikerjakan, dan kapan sebuah hasil dinyatakan diterima (slide 06 hlm 6–8). Dokumen ini dihasilkan proses 5.2 *Define Scope* (PMBOK 4 hlm 112) dan menjadi dasar penyusunan WBS. Format mengikuti contoh JWD (slide Minggu 04 slide 80).

> Keputusan pengguna (13 Nov 2026): platform opsi A, wilayah perluasan seluruh DIY, kriteria penerimaan teknis sesuai usulan.

**Tabel 2.10 Project Scope Statement**

| Unsur | Isi |
|---|---|
| **Judul proyek** | Pengembangan Platform "Smart Retails & Delivery Super App" (Nusantara Express) |
| **Justifikasi proyek** | UMKM harus memakai layanan terpisah untuk berjualan, mengirim, dan menerima pembayaran. Satu platform terpadu dengan biaya rendah membuka peluang pendapatan baru bagi PT ND. Proyek diharapkan balik modal ± 2,5 tahun setelah peluncuran (Business Case bagian 7.0) |
| **Tujuan proyek** | Rilis 1 beroperasi di Kota Yogyakarta pada 31 Maret 2027; Rilis 2 beroperasi di seluruh DIY pada 15 Juni 2027; biaya ≤ Rp 15 miliar; serah terima ke tim operasional pada 30 Juni 2027 (Charter, kriteria keberhasilan) |

**Karakteristik dan kebutuhan produk**

| Modul | Rilis 1 (M3, Kota Yogyakarta) | Rilis 2 (M5, seluruh DIY) |
|---|---|---|
| Platform | Aplikasi Android; dasbor web untuk UMKM | Aplikasi iOS |
| *Marketplace* | Pendaftaran dan verifikasi UMKM, katalog produk, pencarian, keranjang, pemesanan, ulasan | Promosi berbayar untuk UMKM |
| Pengiriman dan *tracking* | Integrasi dengan mitra kurir, pelacakan *real-time*, notifikasi status pesanan | Perluasan wilayah layanan ke seluruh DIY |
| *Digital wallet* | Isi saldo, pembayaran, pencairan dana penjual, riwayat transaksi; berjalan di bawah izin mitra pembayaran | — |
| Rekomendasi AI | — | Rekomendasi produk untuk pembeli; saran produk dan stok untuk UMKM |
| Pendukung | Panel admin; keamanan (enkripsi data, verifikasi dua langkah); pemenuhan izin dan pendaftaran sistem elektronik | Laporan kinerja untuk manajemen |

**Deliverable**

*Deliverable* adalah hasil kerja yang harus diserahkan.

| Jenis | Deliverable |
|---|---|
| Produk | Aplikasi Rilis 1 (Android + dasbor web); aplikasi Rilis 2 (+ iOS, rekomendasi AI, cakupan DIY); integrasi mitra kurir dan mitra pembayaran; laporan uji keamanan per rilis; laporan UAT per rilis; materi pelatihan UMKM; dokumentasi teknis dan panduan operasional |
| Manajemen proyek | Business Case; Project Charter; Team Contract; Scope Statement; WBS; jadwal proyek; Risk Register; laporan kemajuan bulanan; laporan evaluasi Rilis 1 untuk keputusan M4; berita acara serah terima (M6); laporan akhir dan *lessons learned* (pelajaran yang dicatat untuk proyek berikutnya) |

**Di luar lingkup**

| No | Hal yang tidak dikerjakan | Alasan |
|---|---|---|
| L1 | Fitur *paylater*, cicilan berbunga, dan layanan pinjaman modal untuk UMKM | Prinsip tanpa riba (P1, P2) |
| L2 | Armada kurir milik sendiri | Pengiriman memakai mitra kurir |
| L3 | Izin uang elektronik atas nama PT ND | *Wallet* memakai izin mitra pembayaran (S15) |
| L4 | Aplikasi iOS pada Rilis 1 | Dijadwalkan pada Rilis 2 |
| L5 | Layanan di luar DIY dan di luar Indonesia | Perluasan lebih lanjut diputuskan setelah proyek selesai |
| L6 | Toko fisik atau mesin kasir untuk UMKM | Bukan bagian dari platform daring |
| L7 | Kampanye pemasaran berskala nasional | Proyek hanya mencakup sosialisasi dan pelatihan di DIY |
| L8 | Operasional harian setelah 30 Juni 2027 | Menjadi tanggung jawab Operations & Logistics setelah serah terima |

**Kendala dan asumsi:** sesuai Business Case bagian 4.0 (waktu 6 bulan, biaya Rp 15 miliar, regulasi, prinsip tanpa riba P1–P4, cuti bersama Idulfitri; asumsi kesediaan paguyuban, kontrak mitra paling lambat 29 Januari 2027, ketersediaan tim, dan penyelesaian izin sebelum Rilis 1).

**Kriteria penerimaan**

Setiap rilis dinyatakan **diterima** bila semua kriteria berikut terpenuhi:

| No | Kriteria | Ukuran | Pemeriksa |
|---|---|---|---|
| K1 | Ketersediaan sistem | Aplikasi hidup ≥ 99,5% dari waktu selama masa uji coba | Kepala Infrastructure & Cybersecurity |
| K2 | Kecepatan | Halaman terbuka ≤ 3 detik | Kepala Software Engineering |
| K3 | Kapasitas | Melayani ≥ 2.000 pengguna bersamaan | Kepala Infrastructure & Cybersecurity |
| K4 | Keamanan | Uji keamanan tidak menemukan celah berkategori kritis atau tinggi | Kepala Infrastructure & Cybersecurity, berdasarkan laporan konsultan keamanan |
| K5 | Penerimaan pengguna | ≥ 80% skenario lulus dalam UAT (*User Acceptance Test*, uji penerimaan oleh perwakilan pengguna) bersama perwakilan Paguyuban UMKM | Kepala Business Development |
| K6 | Kepatuhan | Izin dan pendaftaran terpenuhi; fitur sesuai prinsip P1–P4 | Kepala Legal & Compliance |
| K7 | Pengesahan | Komite Pengarah menyetujui peluncuran berdasarkan hasil K1–K6 | Komite Pengarah |

**Pengendalian perubahan lingkup**

Untuk mencegah ***scope creep***, yaitu penambahan pekerjaan diam-diam tanpa persetujuan (slide 06 hlm 8), setiap permintaan perubahan lingkup:
1. diajukan tertulis kepada PM;
2. dinilai dampaknya terhadap biaya, jadwal, dan risiko;
3. diputuskan PM bila masih dalam wewenangnya (Charter), atau dibawa ke Komite Pengarah bila melampauinya, termasuk **setiap** perubahan lingkup produk;
4. dicatat beserta keputusannya, lalu dokumen terkait (Scope Statement, WBS, jadwal) diperbarui.

### 2.3.3 Work Breakdown Structure (WBS)

*Work Breakdown Structure* (WBS) adalah pemecahan **seluruh** pekerjaan proyek secara bertingkat menjadi bagian-bagian kecil yang bisa dikelola (slide 06 hlm 13–15). Bagian paling bawah disebut ***work package*** (paket kerja): unit kerja yang bisa diberi penanggung jawab, diperkirakan durasi dan biayanya, lalu dipantau. WBS dihasilkan proses 5.3 *Create WBS* (PMBOK 4 hlm 116), dengan Scope Statement sebagai masukan utamanya.

> Keputusan pengguna (13 Nov 2026): level 2 disusun **per rilis** (opsi B); tiga level; disajikan sebagai diagram pohon dan tabel berkode.

**Dasar penyusunan**

- **Level 2 per rilis.** PMBOK 4 membolehkan fase siklus hidup sebagai tingkat pertama penguraian, dengan *deliverable* produk di bawahnya (hlm 118; Gambar 5-9 hlm 119). Di sini, fase = rilis, sehingga WBS sejalan langsung dengan *milestone* dan gerbang keputusan M4. Modul produk muncul di level 3.
- **Aturan 100%** (*100% rule*, PMBOK 4 hlm 121). Jumlah pekerjaan di level bawah harus sama dengan pekerjaan di level atasnya. Tidak ada yang terlewat dan tidak ada pekerjaan di luar lingkup. Karena itu manajemen proyek dan serah terima ikut masuk WBS, sementara butir L1–L8 di Scope Statement tidak muncul sama sekali.
- **Berisi hasil kerja, bukan langkah.** Nama paket kerja adalah kata benda (misalnya "Modul *digital wallet*"), bukan kegiatan ("membuat kode").
- ***Milestone* tidak dimasukkan ke WBS.** *Milestone* adalah penanda waktu, bukan pekerjaan. M0–M6 ditempatkan di jadwal (Bagian 2.3.4).
- **Kode WBS** (1.3.2, dst.) dipakai lagi di jadwal dan Risk Register.

**Gambar 2.2 Diagram pohon WBS** (level 1–2, dengan cabang 1.3 sampai level 3; diagram rapi dibuat saat laporan dirakit)

```
1  Super App Nusantara Express
├── 1.1  Manajemen proyek
├── 1.2  Persiapan dan desain ........................ (sampai M2, 29 Jan)
├── 1.3  Rilis 1: Kota Yogyakarta, Android + web ..... (sampai M3, 31 Mar)
│   ├── 1.3.1   Modul marketplace
│   ├── 1.3.2   Modul pengiriman dan tracking
│   ├── 1.3.3   Modul digital wallet
│   ├── 1.3.4   Dasbor web UMKM dan panel admin
│   ├── 1.3.5   Fitur keamanan aplikasi
│   ├── 1.3.6   Infrastruktur produksi
│   ├── 1.3.7   Pengujian fungsi dan integrasi
│   ├── 1.3.8   Uji keamanan pertama
│   ├── 1.3.9   UAT Rilis 1
│   ├── 1.3.10  Pemenuhan izin dan pendaftaran sistem elektronik
│   ├── 1.3.11  Pelatihan dan pendaftaran UMKM Kota Yogyakarta
│   ├── 1.3.12  Kesiapan operasional
│   └── 1.3.13  Peluncuran Rilis 1
├── 1.4  Rilis 2: seluruh DIY, + iOS dan AI .......... (sampai M5, 15 Jun)
└── 1.5  Serah terima dan penutupan .................. (sampai M6, 30 Jun)
```

**Tabel 2.11 WBS berkode**

Singkatan penanggung jawab: PM = Project Manager; SE = Software Engineering; UX = UI/UX; IC = Infrastructure & Cybersecurity; BD = Business Development; OL = Operations & Logistics; LC = Legal & Compliance. Penanggung jawab pertama adalah pemilik paket kerja.

| Kode | Paket kerja | Hasil kerja | PJ |
|---|---|---|---|
| **1** | **Super App Nusantara Express** | Seluruh pekerjaan proyek | PM |
| **1.1** | **Manajemen proyek** | | PM |
| 1.1.1 | Dokumen inisiasi | Stakeholder Register, Stakeholder Management Strategy, Business Case, Project Charter | PM |
| 1.1.2 | Kick-off meeting dan Team Contract | Notulen kick-off, Team Contract bertanda tangan | PM |
| 1.1.3 | Rencana proyek | Scope Statement, WBS, jadwal, Risk Register | PM |
| 1.1.4 | Komunikasi dan laporan kemajuan | Notulen rapat harian, mingguan, dan Komite Pengarah; laporan kemajuan bulanan; kabar berkala untuk stakeholder sesuai Tabel 2.2 | PM |
| 1.1.5 | Pengendalian perubahan dan risiko | Catatan permintaan perubahan beserta keputusannya; Risk Register yang diperbarui | PM |
| 1.1.6 | Laporan evaluasi Rilis 1 | Data adopsi, kinerja sistem, dan masukan pengguna sebagai dasar keputusan M4 | PM, BD |
| **1.2** | **Persiapan dan desain** | | PM |
| 1.2.1 | Kebutuhan pengguna | Daftar kebutuhan UMKM, pembeli, dan kurir, disusun bersama perwakilan Paguyuban UMKM | BD, UX |
| 1.2.2 | Arsitektur sistem dan rancangan data | Dokumen arsitektur, rancangan basis data, rancangan integrasi dengan mitra | SE |
| 1.2.3 | Desain antarmuka dan prototipe | Rancangan tampilan Android dan dasbor web; prototipe yang diuji ke perwakilan UMKM | UX |
| 1.2.4 | Kontrak mitra | Kontrak dengan mitra kurir, mitra pembayaran, penyedia *cloud*, dan konsultan keamanan, sesuai prinsip P1–P4 | BD, LC |
| 1.2.5 | Peta izin dan kepatuhan | Daftar izin dan pendaftaran beserta jadwalnya; daftar periksa perlindungan data pribadi dan prinsip P1–P4 | LC |
| 1.2.6 | Lingkungan pengembangan | Server pengembangan dan pengujian di *cloud*, alat kerja tim | IC |
| **1.3** | **Rilis 1 (Kota Yogyakarta; Android + dasbor web)** | | SE |
| 1.3.1 | Modul *marketplace* | Pendaftaran dan verifikasi UMKM, katalog produk, pencarian, keranjang, pemesanan, ulasan | SE |
| 1.3.2 | Modul pengiriman dan *tracking* | Integrasi dengan mitra kurir, pelacakan *real-time*, notifikasi status pesanan | SE |
| 1.3.3 | Modul *digital wallet* | Isi saldo, pembayaran, pencairan dana penjual, riwayat transaksi; terhubung ke mitra pembayaran; tanpa *paylater* dan cicilan | SE |
| 1.3.4 | Dasbor web UMKM dan panel admin | Dasbor penjualan untuk UMKM; panel admin untuk verifikasi dan pengaduan | SE, UX |
| 1.3.5 | Fitur keamanan aplikasi | Enkripsi data, verifikasi dua langkah, pencatatan akses | IC |
| 1.3.6 | Infrastruktur produksi | Server produksi di *cloud*, pemantauan sistem, cadangan data | IC |
| 1.3.7 | Pengujian fungsi dan integrasi | Laporan uji fungsi, uji integrasi mitra, dan uji beban (K1–K3) | SE |
| 1.3.8 | Uji keamanan pertama | Laporan uji keamanan dari konsultan dan bukti perbaikannya (K4) | IC |
| 1.3.9 | UAT Rilis 1 | Laporan UAT bersama perwakilan Paguyuban UMKM (K5) | BD |
| 1.3.10 | Pemenuhan izin dan pendaftaran sistem elektronik | Bukti pendaftaran dan izin yang dibutuhkan Rilis 1 (K6) | LC |
| 1.3.11 | Pelatihan dan pendaftaran UMKM Kota Yogyakarta | Materi pelatihan, daftar hadir, UMKM terdaftar dengan katalog terisi | BD, OL |
| 1.3.12 | Kesiapan operasional | Prosedur layanan pelanggan, penanganan pengaduan, dan koordinasi kurir | OL |
| 1.3.13 | Peluncuran Rilis 1 | Aplikasi tersedia di toko aplikasi; sosialisasi di Kota Yogyakarta | BD |
| **1.4** | **Rilis 2 (seluruh DIY; + iOS dan rekomendasi AI)** | | SE |
| 1.4.1 | Desain Rilis 2 | Rancangan fitur Rilis 2 dan daftar perbaikan dari evaluasi Rilis 1 | UX, SE |
| 1.4.2 | Modul rekomendasi AI | Rekomendasi produk untuk pembeli; saran produk dan stok untuk UMKM | SE |
| 1.4.3 | Aplikasi iOS | Aplikasi iOS dengan fitur setara Android | SE |
| 1.4.4 | Fitur promosi berbayar UMKM | Promosi produk dengan tarif tetap yang diumumkan terbuka, tanpa denda (P4) | SE, BD |
| 1.4.5 | Laporan kinerja untuk manajemen | Dasbor kinerja penjualan dan adopsi untuk manajemen PT ND | SE |
| 1.4.6 | Perluasan layanan ke seluruh DIY | Area layanan kurir di Sleman, Bantul, Kulon Progo, dan Gunungkidul | OL, BD |
| 1.4.7 | Penambahan kapasitas infrastruktur | Kapasitas server untuk pengguna seluruh DIY | IC |
| 1.4.8 | Pengujian fungsi dan integrasi | Laporan uji fungsi, uji integrasi, dan uji beban Rilis 2 (K1–K3) | SE |
| 1.4.9 | Uji keamanan kedua | Laporan uji keamanan dari konsultan dan bukti perbaikannya (K4) | IC |
| 1.4.10 | UAT Rilis 2 | Laporan UAT bersama perwakilan UMKM dari kabupaten baru (K5) | BD |
| 1.4.11 | Pelatihan UMKM empat kabupaten | Materi pelatihan, daftar hadir, UMKM terdaftar | BD, OL |
| 1.4.12 | Peluncuran Rilis 2 | Rilis 2 tersedia di toko aplikasi Android dan iOS; sosialisasi di seluruh DIY | BD |
| **1.5** | **Serah terima dan penutupan** | | PM |
| 1.5.1 | Dokumentasi teknis dan panduan operasional | Dokumentasi sistem, panduan admin, panduan penanganan gangguan | SE, IC |
| 1.5.2 | Alih pengetahuan ke tim operasional | Pelatihan tim Operations & Logistics untuk menjalankan sistem | SE, OL |
| 1.5.3 | Berita acara serah terima | Berita acara bertanda tangan PM dan Kepala Operations & Logistics | PM, OL |
| 1.5.4 | Penutupan kontrak proyek | Penyelesaian kontrak yang khusus untuk proyek (misalnya konsultan keamanan) | LC, BD |
| 1.5.5 | Laporan akhir dan *lessons learned* | Laporan akhir proyek dan catatan pelajaran untuk proyek berikutnya | PM |

Jumlah: 5 paket di level 2 dan 42 *work package* di level 3.

> **Catatan untuk jadwal:** 1.1.6 dan 1.4.1 dikerjakan pada April 2027, sebelum keputusan M4. Desain Rilis 2 dimulai lebih awal oleh tim kecil agar Rilis 2 tetap sempat selesai pada 15 Juni. Pembangunan 1.4.2–1.4.12, yang memakan sebagian besar dana Rilis 2, baru dimulai setelah Komite Pengarah memutuskan lanjut di M4.

**Pemeriksaan aturan 100%: *deliverable* Scope Statement → kode WBS**

| *Deliverable* di Scope Statement (Bagian 2.3.2) | Kode WBS |
|---|---|
| Aplikasi Rilis 1 (Android + dasbor web) | 1.3.1–1.3.6, 1.3.13 |
| Aplikasi Rilis 2 (+ iOS, rekomendasi AI, cakupan DIY) | 1.4.1–1.4.7, 1.4.12 |
| Integrasi mitra kurir dan mitra pembayaran | 1.2.4, 1.3.2, 1.3.3 |
| Laporan uji keamanan per rilis | 1.3.8, 1.4.9 |
| Laporan UAT per rilis | 1.3.9, 1.4.10 |
| Materi pelatihan UMKM | 1.3.11, 1.4.11 |
| Dokumentasi teknis dan panduan operasional | 1.5.1 |
| Business Case, Charter, Team Contract, Scope Statement, WBS, jadwal, Risk Register | 1.1.1–1.1.3 |
| Laporan kemajuan bulanan | 1.1.4 |
| Laporan evaluasi Rilis 1 (keputusan M4) | 1.1.6 |
| Berita acara serah terima (M6) | 1.5.3 |
| Laporan akhir dan *lessons learned* | 1.5.5 |

Semua *deliverable* di Scope Statement punya paket kerja. Sebaliknya, setiap paket kerja di WBS menghasilkan salah satu *deliverable* di atas atau pekerjaan pendukungnya (pengujian, izin, kesiapan operasional), sehingga tidak ada pekerjaan di luar lingkup.

### 2.3.4 Jadwal Proyek (Gantt Chart dan Milestone)

Jadwal proyek menetapkan **kapan** setiap paket kerja dikerjakan. Penyusunannya melalui empat langkah: menetapkan aktivitas, mengurutkan, memperkirakan durasi, dan menyusun jadwal (slide 06 hlm 18; PMBOK 4 proses 6.1–6.5, hlm 131–152). ***Gantt chart*** menampilkan setiap pekerjaan sebagai batang mendatar di sepanjang garis waktu, sehingga mudah dibaca oleh pihak nonteknis (slide 06 hlm 19; PMBOK 4 Gambar 6-14 hlm 158).

> Keputusan pengguna (13 Nov 2026): Gantt dibuat di **ClickUp**; satu batang untuk setiap paket kerja level 3; jalur kritis ditandai; pekan cuti bersama Idulfitri dikosongkan.
> Tanggal dan durasi rinci di bawah ini: **[USULAN]**.

**Dasar penyusunan**

- **Satuan durasi: hari kerja** (Senin–Jumat). Hari yang tidak dihitung: cuti bersama Idulfitri 8–12 Maret 2027 [CEK], Wafat Isa Almasih (Jumat Agung) 26 Maret, Kenaikan Isa Almasih 6 Mei, dan Hari Lahir Pancasila 1 Juni 2027. Hari libur nasional lain menyesuaikan SKB (Surat Keputusan Bersama) Menteri tentang libur nasional dan cuti bersama 2027 setelah terbit [CEK].
- **Teknik estimasi:** *expert judgment* (penilaian kepala divisi berdasarkan pengalaman) dan *analogous estimation* (berdasarkan proyek serupa), dua teknik di slide 06 hlm 21.
- **Pendahulu** (*predecessor*) adalah pekerjaan yang harus selesai sebelum pekerjaan lain bisa dimulai. Semua hubungan memakai pola *finish-to-start* (selesai lalu mulai), kecuali disebut lain.
- **Jalur kritis** (*critical path*) adalah rangkaian pekerjaan terpanjang yang saling bergantung. Pekerjaan di jalur ini tidak punya *float* (waktu longgar), sehingga keterlambatan sehari pun menggeser *milestone* (slide 06 hlm 20; PMBOK 4 hlm 138). Di tabel, pekerjaan ini diberi tanda ●.
- **Gerbang M4.** Hanya 1.1.6 dan 1.4.1 yang berjalan pada April. Pembangunan Rilis 2 (1.4.2 dst.) baru mulai Senin 3 Mei 2027, setelah Komite Pengarah memutuskan lanjut pada 30 April.

**Tabel 2.12 Daftar milestone**

| Kode | Milestone | Tanggal | Syarat tercapai |
|---|---|---|---|
| M0 | Project Charter disahkan | Sen, 4 Jan 2027 | 1.1.1 selesai |
| M1 | Kick-off meeting | Rab, 6 Jan 2027 | Rapat terlaksana (1.1.2) |
| M2 | Lingkup dan desain disetujui | Jum, 29 Jan 2027 | 1.1.3 dan 1.2.1–1.2.6 selesai; disetujui Komite Pengarah |
| M3 | Rilis 1 di Kota Yogyakarta | Rab, 31 Mar 2027 | Kriteria penerimaan K1–K7 terpenuhi; 1.3.13 selesai |
| M4 | Evaluasi Rilis 1 dan keputusan lanjut | Jum, 30 Apr 2027 | 1.1.6 selesai; keputusan Komite Pengarah |
| M5 | Rilis 2 | Sel, 15 Jun 2027 | Kriteria penerimaan K1–K7 terpenuhi; 1.4.12 selesai |
| M6 | Penutupan proyek dan serah terima | Rab, 30 Jun 2027 | 1.5.3 dan 1.5.5 selesai |

**Gambar 2.3 Ringkasan Gantt per level 2** (sketsa per minggu; Gantt lengkap 42 batang dibuat di ClickUp)

```
                            Jan     Feb     Mar       Apr     Mei       Jun
Minggu ke-                  1       5       9       13      17      21      25
1.1 Manajemen proyek        ████████████████████████████████████████████████████
1.2 Persiapan dan desain    ████████············································
1.3 Rilis 1                 ········██████████░░██████··························
1.1.6 Evaluasi Rilis 1      ··························▒▒▒▒▒▒▒▒··················
1.4 Rilis 2                 ··························▒▒▒▒▒▒··██████████████····
1.5 Serah terima, penutupan ······································██████████████
Milestone                   ◆     ◆                 ◆       ◆             ◆   ◆
                            M0/M1 M2                M3      M4            M5  M6

█ = dikerjakan   ░ = cuti bersama Idulfitri   ▒ = tim kecil, sebelum keputusan M4
```

**Tabel 2.13 Jadwal paket kerja**

| Kode | Paket kerja | Mulai | Selesai | Hari kerja | Pendahulu | Kritis |
|---|---|---|---|---|---|---|
| **1.1** | **Manajemen proyek** | **4 Jan** | **30 Jun** | | | |
| 1.1.1 | Dokumen inisiasi | — | 4 Jan | 1 | — (Stakeholder Register dan Business Case disusun sebelum proyek dimulai) | |
| 1.1.2 | Kick-off meeting dan Team Contract | 6 Jan | 8 Jan | 3 | 1.1.1 (M0) | |
| 1.1.3 | Rencana proyek | 7 Jan | 29 Jan | 17 | 1.1.2 (mulai sehari setelah kick-off) | |
| 1.1.4 | Komunikasi dan laporan kemajuan | 4 Jan | 30 Jun | 120 | — (berjalan sepanjang proyek) | |
| 1.1.5 | Pengendalian perubahan dan risiko | 4 Jan | 30 Jun | 120 | — (berjalan sepanjang proyek) | |
| 1.1.6 | Laporan evaluasi Rilis 1 | 1 Apr | 29 Apr | 21 | 1.3.13 (M3) | ● |
| **1.2** | **Persiapan dan desain** | **7 Jan** | **29 Jan** | | | |
| 1.2.1 | Kebutuhan pengguna | 7 Jan | 22 Jan | 12 | 1.1.2 (M1) | |
| 1.2.2 | Arsitektur sistem dan rancangan data | 11 Jan | 29 Jan | 15 | 1.2.1 (mulai 2 hari kemudian) | |
| 1.2.3 | Desain antarmuka dan prototipe | 11 Jan | 29 Jan | 15 | 1.2.1 (mulai 2 hari kemudian) | |
| 1.2.4 | Kontrak mitra | 7 Jan | 29 Jan | 17 | 1.1.2 (M1) | ● |
| 1.2.5 | Peta izin dan kepatuhan | 7 Jan | 15 Jan | 7 | 1.1.2 (M1) | |
| 1.2.6 | Lingkungan pengembangan | 18 Jan | 29 Jan | 10 | 1.2.4 (kontrak *cloud* lebih dulu, paling lambat 15 Jan) | |
| **1.3** | **Rilis 1** | **18 Jan** | **31 Mar** | | | |
| 1.3.1 | Modul *marketplace* | 1 Feb | 5 Mar | 25 | 1.2.2, 1.2.3 (M2) | |
| 1.3.2 | Modul pengiriman dan *tracking* | 1 Feb | 5 Mar | 25 | 1.2.2, 1.2.4 (M2) | |
| 1.3.3 | Modul *digital wallet* | 1 Feb | 5 Mar | 25 | 1.2.2, 1.2.4 (M2) | ● |
| 1.3.4 | Dasbor web UMKM dan panel admin | 8 Feb | 5 Mar | 20 | 1.2.3 | |
| 1.3.5 | Fitur keamanan aplikasi | 8 Feb | 5 Mar | 20 | 1.2.2 | |
| 1.3.6 | Infrastruktur produksi | 1 Feb | 5 Mar | 25 | 1.2.6 | |
| 1.3.7 | Pengujian fungsi dan integrasi | 15 Mar | 19 Mar | 5 | 1.3.1–1.3.6 | ● |
| 1.3.8 | Uji keamanan pertama | 15 Mar | 24 Mar | 8 | 1.3.5, 1.3.6 | |
| 1.3.9 | UAT Rilis 1 | 22 Mar | 25 Mar | 4 | 1.3.7 | ● |
| 1.3.10 | Pemenuhan izin dan pendaftaran sistem elektronik | 18 Jan | 19 Mar | 40 | 1.2.5 | |
| 1.3.11 | Pelatihan dan pendaftaran UMKM Kota Yogyakarta | 15 Mar | 30 Mar | 11 | 1.3.4 | |
| 1.3.12 | Kesiapan operasional | 1 Mar | 25 Mar | 14 | 1.2.1 | |
| 1.3.13 | Peluncuran Rilis 1 | 29 Mar | 31 Mar | 3 | 1.3.8–1.3.10, 1.3.12; disetujui Komite (K7) | ● |
| **1.4** | **Rilis 2** | **5 Apr** | **15 Jun** | | | |
| 1.4.1 | Desain Rilis 2 | 5 Apr | 23 Apr | 15 | 1.3.13 (M3) | |
| 1.4.2 | Modul rekomendasi AI | 3 Mei | 28 Mei | 19 | 1.4.1; keputusan lanjut (M4) | ● |
| 1.4.3 | Aplikasi iOS | 3 Mei | 28 Mei | 19 | 1.4.1; keputusan lanjut (M4) | ● |
| 1.4.4 | Fitur promosi berbayar UMKM | 3 Mei | 21 Mei | 14 | 1.4.1; M4 | |
| 1.4.5 | Laporan kinerja untuk manajemen | 10 Mei | 28 Mei | 15 | 1.4.1; M4 | |
| 1.4.6 | Perluasan layanan ke seluruh DIY | 3 Mei | 4 Jun | 23 | M4 | |
| 1.4.7 | Penambahan kapasitas infrastruktur | 17 Mei | 28 Mei | 10 | M4 | |
| 1.4.8 | Pengujian fungsi dan integrasi | 31 Mei | 8 Jun | 6 | 1.4.2–1.4.5, 1.4.7 | ● |
| 1.4.9 | Uji keamanan kedua | 31 Mei | 9 Jun | 7 | 1.4.2–1.4.5, 1.4.7 | |
| 1.4.10 | UAT Rilis 2 | 7 Jun | 10 Jun | 4 | 1.4.8 (mulai sebelum 1.4.8 selesai) | ● |
| 1.4.11 | Pelatihan UMKM empat kabupaten | 17 Mei | 11 Jun | 19 | 1.4.6 (mulai bersamaan); memakai aplikasi Rilis 1 | |
| 1.4.12 | Peluncuran Rilis 2 | 14 Jun | 15 Jun | 2 | 1.4.6, 1.4.9–1.4.11; disetujui Komite (K7) | ● |
| **1.5** | **Serah terima dan penutupan** | **17 Mei** | **30 Jun** | | | |
| 1.5.1 | Dokumentasi teknis dan panduan operasional | 17 Mei | 25 Jun | 29 | 1.3.13 | |
| 1.5.2 | Alih pengetahuan ke tim operasional | 16 Jun | 25 Jun | 8 | 1.4.12 (M5) | ● |
| 1.5.3 | Berita acara serah terima | 28 Jun | 30 Jun | 3 | 1.5.1, 1.5.2 | ● |
| 1.5.4 | Penutupan kontrak proyek | 21 Jun | 29 Jun | 7 | 1.4.12 (M5) | |
| 1.5.5 | Laporan akhir dan *lessons learned* | 21 Jun | 30 Jun | 8 | 1.4.12 (M5) | |

Semua tanggal dalam tahun 2027.

**Jalur kritis**

M1 → 1.2.4 Kontrak mitra → 1.3.3 Modul *digital wallet* → 1.3.7 Pengujian → 1.3.9 UAT → 1.3.13 Peluncuran Rilis 1 (M3) → 1.1.6 Evaluasi → **M4** → 1.4.2/1.4.3 AI dan iOS → 1.4.8 Pengujian → 1.4.10 UAT → 1.4.12 Peluncuran Rilis 2 (M5) → 1.5.2 Alih pengetahuan → 1.5.3 Serah terima (M6).

Catatan:
1. **Kontrak mitra pembayaran menjadi titik paling rawan.** Modul *wallet* tidak bisa dibangun dan diuji tanpa akses ke sistem mitra pembayaran. Bila kontrak mundur dari 29 Januari, Rilis 1 ikut mundur. Hal ini dicatat di Risk Register.
2. **Pekerjaan yang punya waktu longgar** (contoh): 1.3.10 Izin (selesai 19 Mar, peluncuran 29 Mar, longgar 4 hari kerja); 1.4.6 Perluasan layanan DIY (selesai 4 Jun, peluncuran 14 Jun, longgar 5 hari kerja); 1.4.4 Promosi berbayar (selesai 21 Mei, pengujian 31 Mei, longgar 5 hari kerja).
3. **Waktu efektif Rilis 1 sempit.** Pembangunan berlangsung 25 hari kerja (1 Feb–5 Mar), bertepatan dengan bulan Ramadan (± 8 Feb–9 Mar 2027 [CEK]), lalu langsung disusul cuti bersama. Pengujian sampai peluncuran hanya 12 hari kerja (15–31 Mar).
4. **Waktu Rilis 2 juga sempit.** Setelah M4, AI dan iOS hanya punya 19 hari kerja. Ini harga yang dibayar karena dana Rilis 2 ditahan sampai ada keputusan di M4. Desain Rilis 2 (1.4.1) yang dikerjakan pada April mengurangi tekanan ini.

**Pemindahan ke ClickUp:** setiap baris Tabel 2.13 menjadi satu *task* dengan kode WBS di awal namanya, dikelompokkan per level 2 (*list*). Pendahulu diisi sebagai *dependency* (*waiting on*), dan M0–M6 dibuat sebagai *milestone*. Tangkapan layar tampilan Gantt dimasukkan ke laporan, ditambah tautan publik seperti di Tugas 2.

### 2.3.5 Risk Register

*Risk Register* adalah dokumen hidup yang mencatat semua risiko proyek beserta analisis dan rencana responsnya, dan diperbarui sepanjang proyek (slide 06 hlm 30). Dokumen ini dihasilkan proses 11.2 *Identify Risks* (PMBOK 4 hlm 282). Isinya kemudian dilengkapi lewat 11.3 *Perform Qualitative Risk Analysis* (hlm 289) dan 11.5 *Plan Risk Responses* (hlm 301). Di proyek ini, risiko yang dicatat adalah **ancaman** (*threat*), yaitu kejadian tidak pasti yang merugikan proyek bila terjadi.

> Keputusan pengguna (13 Nov 2026): skala 1–5, sekitar 12 risiko, empat strategi respons PMBOK 4 tanpa mitigasi berupa pinjaman, kolom sesuai panduan ditambah pemicu.
> Isi risiko, nilai, dan respons di bawah ini: **[USULAN]**.

**Dasar penyusunan**

- **Sumber risiko:** bahan Risk Register di data induk Bagian 9, risiko potensial di Business Case bagian 9.0, temuan jadwal (Bagian 2.3.4), dan contoh risiko umum proyek TI di slide 06 hlm 31.
- **Rumusan risiko** mengikuti pola PMBOK 4 hlm 288: *karena [penyebab], [kejadian] bisa terjadi, sehingga [akibat]*.
- **Skor = Probabilitas (P) × Dampak (D)**, dibaca dengan matriks probabilitas dan dampak (PMBOK 4 Gambar 11-10 hlm 292).
- **Pemicu** (*trigger*) adalah tanda awal bahwa risiko mulai terjadi. Bila pemicu muncul, pemilik risiko menjalankan respons dan melapor ke PM.
- **Peninjauan:** Risk Register dibahas di rapat tim mingguan dan di setiap rapat Komite Pengarah (WBS 1.1.5).

**Tabel 2.14 Skala penilaian**

| Nilai | Probabilitas | Dampak |
|---|---|---|
| 1 | Sangat kecil (< 10%) | Sangat kecil: biaya tambahan < Rp 50 juta; tidak menggeser jadwal |
| 2 | Kecil (10–30%) | Kecil: biaya ≤ Rp 250 juta atau aktivitas bergeser ≤ 1 minggu tanpa menggeser *milestone* (masih dalam wewenang PM) |
| 3 | Sedang (30–50%) | Sedang: biaya ≤ Rp 750 juta atau *milestone* bergeser ≤ 2 minggu |
| 4 | Besar (50–70%) | Besar: biaya ≤ Rp 1,5 miliar (memakai dana cadangan) atau *milestone* bergeser > 2 minggu |
| 5 | Sangat besar (> 70%) | Sangat besar: rilis gagal atau proyek dihentikan; biaya melebihi dana cadangan; pelanggaran hukum atau kebocoran data pengguna |

Tingkat risiko menurut skor: **Rendah** 1–4 · **Sedang** 5–9 · **Tinggi** 10–16 · **Sangat tinggi** 20–25.

Batas dampak 2 sengaja disamakan dengan wewenang PM di Charter (Rp 250 juta, 1 minggu). Artinya, risiko berdampak 3 ke atas otomatis harus dilaporkan ke Komite Pengarah bila terjadi.

**Tabel 2.15 Daftar risiko dan penilaiannya**

| No | Risiko | Kategori | Kode WBS | P | D | Skor | Tingkat | Pemilik |
|---|---|---|---|---|---|---|---|---|
| R01 | Karena UMKM menunggu pembeli dan pembeli menunggu barang ("ayam dan telur"), **adopsi UMKM dan pembeli di bawah target**, sehingga pendapatan tidak menutup biaya (adopsi −20% membuat ROI tiga tahun −7,5%) | Pasar | 1.3.11, 1.4.11, 1.1.6 | 4 | 5 | 20 | Sangat tinggi | Yusuf Kamil Hidayat (BD) |
| R02 | Karena negosiasi atau proses internal mitra pembayaran lambat, **kontrak dan akses sistem mitra pembayaran terlambat**, sehingga modul *wallet* (jalur kritis) dan Rilis 1 mundur | Mitra | 1.2.4, 1.3.3 | 3 | 5 | 15 | Tinggi | Yusuf Kamil Hidayat (BD) |
| R03 | Karena mitra kurir mengubah prioritas bisnisnya, **mitra kurir mundur atau integrasinya terlambat**, sehingga pengiriman dan *tracking* tidak siap | Mitra | 1.2.4, 1.3.2, 1.4.6 | 2 | 4 | 8 | Sedang | Umar Hamzah (OL) |
| R04 | Karena proses perizinan di luar kendali perusahaan, **pendaftaran sistem elektronik atau persyaratan izin belum selesai saat Rilis 1**, sehingga peluncuran tertunda | Regulasi | 1.2.5, 1.3.10 | 3 | 5 | 15 | Tinggi | Ibrahim Hanif (LC) |
| R05 | Karena aplikasi menyimpan data pribadi dan transaksi, **terjadi serangan siber atau kebocoran data**, sehingga pengguna dirugikan, kepercayaan hilang, dan ada sanksi menurut UU PDP | Keamanan | 1.3.5, 1.3.8, 1.4.9 | 3 | 5 | 15 | Tinggi | Hasan Arifin (IC) |
| R06 | Karena gangguan besar di pusat data penyedia *cloud* (contoh nasional: PDNS 2, 2024), **layanan berhenti berjam-jam atau data hilang**, sehingga transaksi terhenti | Teknis | 1.3.6, 1.4.7 | 2 | 5 | 10 | Tinggi | Hasan Arifin (IC) |
| R07 | Karena DIY berada di wilayah rawan bencana, **terjadi *force majeure*** (gempa bumi seperti tahun 2006, erupsi Merapi), sehingga kegiatan lapangan dan tim terganggu | Eksternal | 1.3.11, 1.4.6, 1.4.11 | 1 | 5 | 5 | Sedang | Eka Putra Kurnia (PM) |
| R08 | Karena masa pembangunan Rilis 1 bertepatan dengan Ramadan lalu langsung disusul cuti Idulfitri, **produktivitas tim turun**, sehingga pembangunan modul tidak selesai 5 Maret | Jadwal | 1.3.1–1.3.7 | 4 | 3 | 12 | Tinggi | Zaki Farhan Maulana (SE) |
| R09 | Karena dana Rilis 2 ditahan sampai keputusan M4, **waktu pembangunan Rilis 2 hanya 19 hari kerja**, sehingga AI atau iOS tidak siap 15 Juni | Jadwal | 1.4.1–1.4.3 | 3 | 4 | 12 | Tinggi | Zaki Farhan Maulana (SE) |
| R10 | Karena SKB libur dan cuti bersama 2027 belum terbit, **tanggal libur berbeda dari perkiraan** (misalnya Isra Mikraj jatuh pada 6 Januari, hari kick-off), sehingga beberapa aktivitas bergeser | Jadwal | 1.1.2, Tabel 2.13 | 3 | 2 | 6 | Sedang | Eka Putra Kurnia (PM) |
| R11 | Karena belum semua mitra pembayaran menempatkan dana saldo di bank syariah, **prinsip P3 tidak bisa dipenuhi** oleh mitra terpilih, sehingga *wallet* tidak sesuai prinsip perusahaan | Kepatuhan prinsip | 1.2.4, 1.3.3 | 2 | 4 | 8 | Sedang | Ibrahim Hanif (LC) |
| R12 | Karena UMKM dan manajemen terus mengusulkan fitur baru selama uji coba, **terjadi *scope creep***, sehingga biaya dan jadwal membengkak | Lingkup | 1.1.5 | 3 | 3 | 9 | Sedang | Eka Putra Kurnia (PM) |

**Tabel 2.16 Respons risiko**

Empat strategi untuk ancaman (PMBOK 4 hlm 303–304):
- ***Avoid*** (hindari): mengubah rencana agar ancaman hilang.
- ***Transfer*** (alihkan): memindahkan tanggung jawab atas akibatnya ke pihak lain, misalnya lewat kontrak.
- ***Mitigate*** (kurangi): menurunkan probabilitas atau dampaknya.
- ***Accept*** (terima): tidak bertindak dulu, tetapi menyiapkan dana atau waktu cadangan bila terjadi.

Sesuai prinsip tanpa riba (P1), **tidak ada respons yang berupa pinjaman berbunga**. Biaya tak terduga ditutup dari dana cadangan Rp 1,5 miliar (modal sendiri) dengan persetujuan Komite Pengarah.

| No | Strategi | Tindakan respons | Pemicu |
|---|---|---|---|
| R01 | *Mitigate* | Bersama Paguyuban UMKM, mendaftarkan dan mengisi katalog UMKM **sebelum** peluncuran, agar pembeli pertama langsung menemukan barang (1.3.11). Promosi pembeli awal yang biayanya sudah ada di anggaran sosialisasi. Gerbang M4: dana Rilis 2 baru dipakai penuh bila data adopsi April memadai | UMKM terdaftar dengan katalog terisi < 300 pada 25 Maret; UMKM aktif pada April di bawah 50% lintasan menuju 1.000 per 30 Juni |
| R02 | *Mitigate* | Negosiasi dimulai segera setelah kick-off. Meminta akses lingkungan uji (*sandbox*) mitra sejak Januari lewat nota kesepahaman, sebelum kontrak final. Menyiapkan daftar pendek mitra pembayaran cadangan | Kontrak belum ditandatangani pada 22 Januari; akses *sandbox* belum ada pada 1 Februari |
| R03 | *Mitigate* | Kontrak mencantumkan jadwal dan kewajiban integrasi. Integrasi dirancang dengan antarmuka standar agar mitra kurir bisa diganti. Menyiapkan kurir cadangan | Uji integrasi kurir gagal pada akhir Februari; mitra tidak menanggapi dalam 5 hari kerja |
| R04 | *Mitigate* | Peta izin selesai 15 Januari (1.2.5). Pengajuan dimulai 18 Januari. Konsultasi awal dengan regulator. Bila belum selesai pada 19 Maret, Komite Pengarah memutuskan apakah Rilis 1 berjalan sebagai uji coba tertutup sampai izin terbit | Ada persyaratan yang belum diajukan pada 15 Februari; izin belum terbit pada 12 Maret |
| R05 | *Mitigate* + *Transfer* | Enkripsi data, verifikasi dua langkah, dan pencatatan akses (1.3.5). Uji keamanan oleh konsultan di setiap rilis (1.3.8, 1.4.9). Rencana tanggap insiden. Pemrosesan dana dan keamanan transaksi *wallet* menjadi tanggung jawab mitra pembayaran berizin sesuai kontrak | Uji keamanan menemukan celah kritis atau tinggi; ada pola akses atau login mencurigakan |
| R06 | *Mitigate* + *Transfer* | Cadangan data harian di lokasi pusat data yang berbeda; rencana pemulihan bencana yang diuji sebelum Rilis 1. Kontrak *cloud* memuat jaminan tingkat layanan (*SLA*, *Service Level Agreement*) dan kewajiban pemulihan | Ketersediaan sistem turun di bawah 99,5% (K1); penyedia *cloud* mengumumkan gangguan |
| R07 | *Accept* (aktif) | Server berada di *cloud* di luar DIY, dan tim bisa bekerja jarak jauh. Rencana kelangsungan kerja: kegiatan lapangan dipindah jadwalnya. Biaya pemulihan dari dana cadangan dengan persetujuan Komite | Peringatan dini BMKG; status Merapi naik ke Siaga |
| R08 | *Mitigate* | Pekan cuti sudah dikosongkan di jadwal. Jam kerja selama Ramadan disesuaikan tanpa memotong jam inti. Fitur wajib Rilis 1 dikerjakan lebih dulu, fitur pelengkap belakangan. Kemajuan dipantau di rapat harian | Kemajuan pembangunan < 70% pada 26 Februari |
| R09 | *Mitigate* | Desain Rilis 2 dikerjakan pada April (1.4.1). Data transaksi Rilis 1 disiapkan sebagai bahan AI. Fitur AI dibatasi pada rekomendasi dasar. Bila tetap tidak sempat, penundaan saran stok UMKM diajukan sebagai perubahan lingkup ke Komite | 1.4.1 belum selesai 23 April; kemajuan AI atau iOS < 50% pada 17 Mei |
| R10 | *Accept* | Jadwal disesuaikan setelah SKB terbit. Pergeseran ≤ 1 minggu yang tidak menggeser *milestone* diputuskan PM sendiri | SKB libur nasional dan cuti bersama 2027 terbit |
| R11 | *Avoid* | Penempatan dana saldo di bank syariah dijadikan **syarat** dalam pemilihan mitra pembayaran (1.2.4). Bila tidak ada mitra yang memenuhi, Komite Pengarah memutuskan apakah *wallet* ditunda | Calon mitra tidak bisa menunjukkan rekening penampungan di bank syariah saat negosiasi |
| R12 | *Mitigate* | Setiap usulan fitur baru lewat prosedur pengendalian perubahan lingkup (Scope Statement). Usulan yang ditolak dicatat sebagai bahan pengembangan setelah proyek | Usulan perubahan lebih dari 3 per bulan; ada pekerjaan yang tidak punya kode WBS |

**Gambar 2.4 Matriks probabilitas dan dampak** (diagram berwarna dibuat saat laporan dirakit)

| P \ D | 1 Sangat kecil | 2 Kecil | 3 Sedang | 4 Besar | 5 Sangat besar |
|---|---|---|---|---|---|
| **5 Sangat besar** | | | | | |
| **4 Besar** | | | R08 (12) | | **R01 (20)** |
| **3 Sedang** | | R10 (6) | R12 (9) | R09 (12) | R02, R04, R05 (15) |
| **2 Kecil** | | | | R03, R11 (8) | R06 (10) |
| **1 Sangat kecil** | | | | | R07 (5) |

**Ringkasan:** 1 risiko sangat tinggi, 6 tinggi, 5 sedang, 0 rendah.

**Temuan:**
1. **Risiko terbesar adalah pasar, bukan teknologi (R01).** Hasil ini sama dengan analisis sensitivitas Business Case. Karena itu respons utamanya bersifat bisnis (UMKM masuk sebelum peluncuran, gerbang M4), bukan teknis.
2. **Tiga risiko tinggi berdampak 5 dan berkaitan dengan pihak luar** (mitra pembayaran, regulator, penyerang siber). Risiko seperti ini tidak bisa dihapus, hanya dikurangi atau dialihkan. Karena itu pemicunya dibuat jelas dan diberi tanggal.
3. **Dua risiko lahir dari keputusan proyek sendiri.** R09 adalah akibat menahan dana sampai M4, dan R11 akibat prinsip P3. Keduanya ditanggung secara sadar demi tujuan yang lebih besar, yaitu menjaga modal dan memegang prinsip perusahaan.
