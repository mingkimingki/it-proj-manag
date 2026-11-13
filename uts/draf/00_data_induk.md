# Data Induk Proyek: Super App Nusantara Express

> Berkas kerja UTS (Tahap 0). Semua dokumen PMBOK 4 dan PMBOK 7 **wajib** mengambil angka, nama, dan tanggal dari berkas ini. Kalau ada perubahan, ubah di sini dulu, baru di dokumen lain.
> Disepakati: 13 November 2026. Lihat [PANDUAN_UTS.md](../PANDUAN_UTS.md) Bagian 5.1.
> Butir yang masih terbuka diberi tanda **[USULAN]** atau **[CEK]**.

---

## 1. Identitas proyek

| Data | Isi | Dipakai di |
|---|---|---|
| Nama proyek | Pengembangan Platform "Smart Retails & Delivery Super App" (Nusantara Express) | Semua dokumen |
| Organisasi pelaksana | PT Nusantara Digital Indonesia | Semua dokumen |
| Sponsor | Ahmad Fauzan Hakim, Direktur Utama | Business Case, Charter (tanda tangan), Kick-off, Stakeholder Register |
| Project Manager | Eka Putra Kurnia | Semua dokumen |
| Kota percontohan | Yogyakarta | Scope Statement, WBS, Gantt, Risk Register, PMBOK 7 Planning |

## 2. Waktu

| Data | Isi | Dipakai di |
|---|---|---|
| Mulai | Senin, 4 Januari 2027 | Business Case, Charter, Gantt |
| Selesai | Rabu, 30 Juni 2027 | Business Case, Charter, Gantt |
| Durasi | ± 6 bulan (± 25,5 minggu) | Semua dokumen yang menyebut durasi |

### Milestone

*Milestone* adalah titik penting di jadwal yang tidak punya durasi. Charter membutuhkan minimal 4.

| Kode | Milestone | Tanggal | Dipakai di |
|---|---|---|---|
| M0 | Project Charter disahkan | Sen, 4 Jan 2027 | Charter, Gantt |
| M1 | Kick-off meeting | Rab, 6 Jan 2027 | Agenda Kick-off, Gantt |
| M2 | Lingkup dan desain disetujui | Jum, 29 Jan 2027 | Scope Statement, Gantt |
| M3 | **Rilis 1** di Yogyakarta | Rab, 31 Mar 2027 | Charter, WBS, Gantt, PMBOK 7 Planning |
| M4 | Evaluasi Rilis 1 dan keputusan lanjut ke Rilis 2 | Jum, 30 Apr 2027 | Charter, Gantt, PMBOK 7 Planning |
| M5 | **Rilis 2** | Sel, 15 Jun 2027 | Charter, WBS, Gantt, PMBOK 7 Planning |
| M6 | Penutupan proyek dan serah terima ke tim operasional | Rab, 30 Jun 2027 | Charter, Gantt |

### Kendala kalender

- **[CEK]** Idulfitri 1448 H diperkirakan sekitar 9–10 Maret 2027, sehingga ada cuti bersama tepat sebelum Rilis 1. Tanggal pastinya dicek di SKB cuti bersama 2027. Dipakai di: Scope Statement (kendala), Gantt, Risk Register.
- **[CEK]** Isra Mikraj 1448 H diperkirakan sekitar Selasa 5 Januari 2027. Bila ternyata jatuh pada Rabu 6 Januari, kick-off (M1) bentrok dengan hari libur. Keputusan pengguna (13 Nov 2026): tanggal M1 tetap, disesuaikan setelah SKB libur 2027 terbit (Risk Register R10).
- **[USULAN]** Rilis 1 jatuh setelah musim belanja Ramadan (± Februari–Maret 2027), jadi peluang itu terlewat. Tanggal rilis tidak dimajukan. Hal ini dibahas di Business Case sebagai pertimbangan (peluang yang terlewat versus risiko meluncur terburu-buru) dan menjadi bahan refleksi.

## 3. Lingkup rilis (keputusan: opsi B, dua tahap)

| Rilis | Waktu | Isi | Wilayah | Platform |
|---|---|---|---|---|
| Rilis 1 | Bulan ke-3 (M3) | *Marketplace*, *real-time tracking*, *digital wallet* dasar | Kota Yogyakarta | Aplikasi Android + dasbor web UMKM |
| Rilis 2 | Bulan ke-6 (M5) | Rekomendasi produk berbasis AI untuk UMKM, perluasan wilayah | Seluruh DIY (+ Sleman, Bantul, Kulon Progo, Gunungkidul) | + aplikasi iOS |

Wilayah perluasan dan platform: keputusan pengguna, 13 Nov 2026.

Dipakai di: Charter (ringkasan lingkup), Scope Statement, WBS (level 2), Gantt, PMBOK 7 Planning (pendekatan *incremental*), dan analisis komparatif.

## 4. Anggaran

| Data | Isi | Dipakai di |
|---|---|---|
| Total anggaran | ± **Rp 15 miliar** | Business Case, Charter |
| Cadangan risiko (*contingency reserve*, dana untuk risiko tak terduga) | 10% = Rp 1,5 miliar (sudah termasuk dalam total) | Business Case, Charter, Risk Register |
| Anggaran kerja tanpa cadangan | Rp 13,5 miliar | Business Case |
| Dasar perkiraan | ± 50 orang selama 6 bulan, *cloud*, audit keamanan, lisensi, uji coba lapangan | Business Case (rincian dihitung di sana) |

## 5. Tokoh internal PT Nusantara Digital Indonesia (fiktif)

| Jabatan | Nama | Dipakai di |
|---|---|---|
| Direktur Utama (Sponsor) | Ahmad Fauzan Hakim | Stakeholder Register, Charter, Kick-off |
| Direktur Keuangan | Muhammad Fadhil | Stakeholder Register, Business Case |
| Project Manager | Eka Putra Kurnia | Semua dokumen |
| Kepala Software Engineering | Zaki Farhan Maulana | Stakeholder Register, Team Contract, RACI |
| Kepala UI/UX | Ali Akbar Ramadhan | Stakeholder Register, Team Contract, RACI |
| Kepala Infrastructure & Cybersecurity | Hasan Arifin | Stakeholder Register, Team Contract, RACI |
| Kepala Business Development | Yusuf Kamil Hidayat | Stakeholder Register, Team Contract, RACI |
| Kepala Operations & Logistics | Umar Hamzah | Stakeholder Register, Team Contract, RACI |
| Kepala Legal & Compliance | Ibrahim Hanif | Stakeholder Register, Team Contract, RACI |

## 6. Mitra eksternal (fiktif)

Di laporan, setiap nama mitra diberi label **(fiktif)**.

| Peran | Nama | Dipakai di |
|---|---|---|
| Mitra kurir | PT Amanah Ekspres Logistik | Stakeholder Register, Risk Register |
| Mitra pembayaran | PT Berkah Pay Indonesia | Stakeholder Register, Risk Register |
| Penyedia *cloud* | PT Nur Awan Teknologi | Stakeholder Register, Risk Register |
| Konsultan uji keamanan | PT Al-Hifzh Keamanan Siber | Stakeholder Register, Risk Register |
| Asosiasi UMKM percontohan | Paguyuban UMKM Barokah Yogyakarta | Stakeholder Register, PMBOK 7 Stakeholder |

## 7. Regulator (lembaga sungguhan)

Regulator **tidak** diberi nama fiktif. Mereka disebut hanya sebagai pihak yang aturannya wajib dipatuhi, bukan sebagai mitra kerja sama.

| Lembaga | Kaitan | Status |
|---|---|---|
| Bank Indonesia | Ketentuan sistem pembayaran dan uang elektronik (*digital wallet*) | **[CEK]** aturan yang tepat sebelum dikutip |
| Kementerian Komunikasi dan Digital | Pendaftaran penyelenggara sistem elektronik; pelindungan data pribadi (UU No. 27 Tahun 2022) | **[CEK]** aturan yang tepat sebelum dikutip |

> Izin uang elektronik **tidak** diurus atas nama PT ND. *Wallet* berjalan di bawah izin mitra pembayaran PT Berkah Pay Indonesia (S15), sehingga pemenuhan ketentuan Bank Indonesia dan prinsip P3 menjadi kewajiban mitra tersebut (keputusan 13 Nov 2026).

## 8. Prinsip syariah proyek (keputusan pengguna: tanpa unsur riba)

Prinsip ini berlaku sebagai **kendala proyek** dan dicantumkan di Business Case (asumsi dan kendala), Charter, Scope Statement (di luar lingkup), serta PMBOK 7 (prinsip *Stewardship*).

| No | Prinsip | Dipakai di |
|---|---|---|
| P1 | **Sumber dana proyek berasal dari modal sendiri** PT Nusantara Digital Indonesia, tanpa pinjaman berbunga | Business Case, Charter |
| P2 | ***Digital wallet* tanpa fitur *paylater* dan tanpa cicilan berbunga** | Scope Statement (di luar lingkup), WBS |
| P3 | **Dana saldo pengguna (*float*) ditempatkan di bank syariah** **[CEK]** apakah ketentuan uang elektronik membolehkan | Business Case, Risk Register, Stakeholder (S15 mitra pembayaran) |
| P4 | **Pendapatan berupa upah jasa (*ujrah*)**: komisi, biaya iklan, dan selisih ongkos kirim, semuanya ditetapkan terbuka di awal. Tidak ada denda keterlambatan | Business Case (model pendapatan) |

## 9. Bahan Risk Register (dikumpulkan sejak awal)

| Ide risiko | Asal | Catatan |
|---|---|---|
| *Force majeure* (keadaan kahar): gempa bumi (Yogyakarta 2006), erupsi Merapi | Ide pengguna, 13 Nov 2026 | Kota percontohan Rilis 1 berada di wilayah rawan bencana |
| Gangguan pusat data atau layanan *cloud* skala besar (contoh nasional: PDNS 2 lumpuh karena *ransomware*, 2024) | Ide pengguna dikaitkan dengan slide Minggu 04 slide 32–34 | Kaitkan dengan S16 Penyedia *cloud* |
| Masalah "ayam dan telur": UMKM menunggu pembeli, pembeli menunggu barang | Jawaban pengguna saat menilai stakeholder | Juga bahan Business Case |
| Izin pembayaran atau pendaftaran sistem elektronik belum selesai saat Rilis 1 | Penilaian stakeholder S09, S18, S19 | Jalur kritis menuju M3 |
| Mitra kurir atau mitra pembayaran mundur atau terlambat integrasi | Penilaian stakeholder S14, S15 | — |
| Cuti bersama Idulfitri tepat sebelum Rilis 1 | Data induk Bagian 2 | — |
| **Adopsi UMKM di bawah target (risiko utama)**: adopsi 20% lebih rendah membuat ROI tiga tahun negatif (−7,5%) | Analisis sensitivitas Business Case | Kaitkan dengan keputusan lanjut/berhenti di M4 |
| Ketentuan penempatan dana *float* di bank syariah tidak bisa dipenuhi | Prinsip syariah P3 | — |

## 10. Tata kelola proyek

| Data | Isi | Dipakai di |
|---|---|---|
| Komite Pengarah | Direktur Utama (ketua), Direktur Keuangan, Kepala Legal & Compliance, Kepala Infrastructure & Cybersecurity, PM (sekretaris). Bersidang bulanan dan di setiap *milestone* | Charter, Stakeholder Strategy, Agenda Kick-off, Team Contract, PMBOK 7 |
| Wewenang PM | Perubahan biaya ≤ Rp 250 juta dan pergeseran jadwal ≤ 1 minggu (tanpa menggeser *milestone*). Di atas itu, perubahan lingkup, dan pemakaian dana cadangan memerlukan persetujuan Komite Pengarah | Charter, Risk Register |
| Kriteria keberhasilan | Kriteria proyek (tanggung jawab PM) dipisahkan dari indikator manfaat awal 1.000 UMKM / 20.000 pembeli (tanggung jawab Business Development dan Sponsor) | Charter, analisis komparatif |

## 11. Asumsi teknis (keputusan pengguna: opsi A, ringkas, tanpa merek atau produk)

Butir di bawah ini **bukan rancangan sistem**, melainkan asumsi teknis yang menopang keputusan manajerial. Rincian teknologinya menjadi wewenang Kepala Software Engineering dan Kepala Infrastructure & Cybersecurity.

| No | Asumsi | Menopang keputusan | Dipakai di |
|---|---|---|---|
| AT1 | Aplikasi seluler dibangun dengan **kerangka lintas platform**: satu kode program untuk Android dan iOS | Aplikasi iOS cukup 19 hari kerja di Rilis 2, karena sebagian besar kode Rilis 1 dipakai ulang | Scope Statement, Gantt (1.4.3), Risk Register (R09) |
| AT2 | **Arsitektur modular**: setiap modul (*marketplace*, pengiriman, *wallet*, AI) terpisah dan saling terhubung lewat antarmuka standar (API, *Application Programming Interface*) | Mitra kurir bisa diganti; tim bisa dibagi per modul; satu modul bermasalah tidak menghentikan modul lain | Risk Register (R03), Tabel 3.9, Tabel 3.15 (*decoupling*) |
| AT3 | Layanan *cloud* dengan **pusat data di Indonesia**, ditambah cadangan data di lokasi pusat data yang berbeda | Perlindungan data pribadi pengguna; pemulihan bila pusat data utama terganggu | Risk Register (R05, R06), kriteria K1 |
| AT4 | Integrasi pembayaran dan pengiriman memakai **sistem uji (*sandbox*) milik mitra** sebelum terhubung ke sistem sungguhan | Pembangunan *wallet* bisa dimulai sebelum kontrak final; pengujian tidak memakai uang sungguhan | Gantt (1.3.2, 1.3.3), Risk Register (R02) |
| AT5 | Rekomendasi AI di Rilis 2 memakai **data transaksi Rilis 1** yang sudah dianonimkan (identitas pengguna dihapus) | AI tidak dibangun di Rilis 1; perlindungan data pribadi tetap terjaga | Scope Statement, Tabel 3.13, analisis komparatif (9) |

---

## Catatan perubahan

| Tanggal | Perubahan |
|---|---|
| 13 Nov 2026 | Versi awal: keputusan pengguna (periode, opsi B, anggaran, PM, mitra, kota percontohan) dan rincian turunan yang disetujui (milestone, nama fiktif) |
| 13 Nov 2026 | Tambah regulator Kementerian Komunikasi dan Digital; tambah Bagian 8 "Bahan Risk Register" |
| 13 Nov 2026 | Tambah Bagian 8 "Prinsip syariah proyek" (Bahan Risk Register menjadi Bagian 9); tambah risiko adopsi UMKM dan risiko dana *float* |
| 13 Nov 2026 | Tambah Bagian 10 "Tata kelola proyek"; catatan bahwa *wallet* memakai izin mitra pembayaran |
| 13 Nov 2026 | Bagian 3: wilayah perluasan Rilis 2 (seluruh DIY) dan platform (Android + web; iOS di Rilis 2) diputuskan |
| 13 Nov 2026 | Bagian 2: tambah catatan Isra Mikraj dekat M1. Bagian 9: "NPV negatif" diganti "ROI negatif" (NPV tidak dipakai, sesuai prinsip tanpa riba) |
| 13 Nov 2026 | Tambah Bagian 11 "Asumsi teknis" (AT1–AT5) |
