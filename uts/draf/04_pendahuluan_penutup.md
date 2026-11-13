<!-- SAMPUL
judul: Comparative Project Management Simulation: PMBOK 4th dan 7th Edition
subjudul: Studi Kasus Pengembangan Platform "Smart Retails & Delivery Super App" (Nusantara Express)
jenis: Ujian Tengah Semester — IT Project Management (PJ059)
anggota: EKA PUTRA KURNIA|25.55.2927
dosen: Dosen Pengampu: Robert Marco, S.T., M.T., Ph.D. · Emha Taufiq Luthfi, S.T., M.Kom., Ph.D. · Dr. Kumara Ari Yuana, S.T., M.T.
prodi: Program Studi S2 PJJ Informatika, Fakultas Ilmu Komputer
kampus: Universitas Amikom Yogyakarta
waktu: Semester Ganjil 2026/2027 — November 2026
logo: ../../tugas1/sumber/logo_amikom.png
header: UTS IT Project Management — Eka Putra Kurnia (25.55.2927)
-->

> Berkas kerja UTS: Bab 1, Bab 6, glosarium, daftar pustaka, dan lampiran. Isi **[USULAN]** (13 Nov 2026), perlu ditinjau penulis.
> Bab 2–5 diambil skrip perakitan dari 01_pmbok4.md, 02_pmbok7.md, 03_komparatif_refleksi.md, dan 05_refleksi.md, lalu disisipkan di tempat penanda di bawah.

# Bab 1 — Pendahuluan

## 1.1 Latar belakang

PT Nusantara Digital Indonesia (PT ND) berencana merancang dan meluncurkan *super app* Nusantara Express. *Super app* adalah satu aplikasi yang menyatukan banyak layanan. Nusantara Express memadukan empat layanan untuk UMKM (Usaha Mikro, Kecil, dan Menengah):
- *marketplace*, yaitu pasar daring;
- pengiriman dengan pelacakan *real-time*;
- pembayaran *digital wallet* (dompet digital);
- rekomendasi produk berbasis AI.

Proyek ini ditargetkan selesai dalam enam bulan dan melibatkan enam divisi: Software Engineering, UI/UX, Infrastructure & Cybersecurity, Business Development, Operations & Logistics, serta Legal & Compliance.

Dalam simulasi ini penulis berperan sebagai Project Manager. Tugasnya menyusun dokumen manajemen proyek dengan dua edisi panduan PMI, lalu membandingkan keduanya:
- **PMBOK edisi ke-4 (2008)** berbasis proses: 5 *process group* dan 9 *knowledge area*.
- **PMBOK edisi ke-7 (2021)** berbasis prinsip: 12 prinsip dan 8 *performance domain*, dengan nilai (*value*) sebagai ukuran keberhasilan (slide 04 hlm 5).

## 1.2 Tujuan laporan

1. Menyusun sepuluh dokumen manajemen proyek berbasis proses PMBOK 4 untuk Nusantara Express, dari Stakeholder Register sampai Risk Register (Bab 2).
2. Menerapkan prinsip dan *performance domain* PMBOK 7 pada kasus yang sama: penciptaan nilai, stakeholder dan tim, serta perencanaan adaptif dan ketidakpastian (Bab 3).
3. Membandingkan kedua edisi berdasarkan dokumen yang dihasilkan, lalu merumuskan rekomendasi pendekatan untuk proyek ini (Bab 4).
4. Merefleksikan pelajaran manajerial dari penyusunan kedua versi (Bab 5).

## 1.3 Asumsi simulasi

Soal hanya memberi gambaran umum kasus. Karena itu, penulis menetapkan sejumlah asumsi, dan semua dokumen di laporan ini memakai asumsi yang sama.

**Tabel 1.1 Asumsi utama simulasi**

| Aspek | Asumsi |
|---|---|
| Periode proyek | Senin, 4 Januari 2027 sampai Rabu, 30 Juni 2027 (± 25,5 minggu), dengan tujuh *milestone* M0–M6 |
| Lingkup | Dua rilis. **Rilis 1** (31 Maret 2027): Kota Yogyakarta, aplikasi Android dan dasbor web, tanpa AI. **Rilis 2** (15 Juni 2027): seluruh DIY, ditambah aplikasi iOS dan rekomendasi AI. Keputusan lanjut atau berhenti diambil pada **M4** (30 April 2027) |
| Anggaran | Rp 15 miliar, termasuk cadangan risiko Rp 1,5 miliar; dibiayai modal sendiri perusahaan |
| Organisasi | Sponsor: Direktur Utama. Project Manager: penulis. Komite Pengarah: Direktur Utama, Direktur Keuangan, Kepala Legal & Compliance, Kepala Infrastructure & Cybersecurity, dan PM. Tim proyek ± 50 orang dari enam divisi |
| Mitra | Mitra kurir, mitra pembayaran berizin (*wallet* berjalan di bawah izin uang elektronik milik mitra ini), penyedia *cloud*, konsultan keamanan, dan paguyuban UMKM di Yogyakarta |
| Prinsip tanpa riba | Kebijakan perusahaan: (P1) modal sendiri tanpa pinjaman berbunga; (P2) *wallet* tanpa *paylater* dan cicilan berbunga; (P3) dana saldo pengguna ditempatkan di bank syariah; (P4) pendapatan berupa upah jasa (*ujrah*) yang besarnya terbuka sejak awal, tanpa denda |
| Asumsi teknis | Aplikasi lintas platform; arsitektur modular; *cloud* dengan pusat data di Indonesia dan cadangan di lokasi lain; integrasi mitra diuji di *sandbox*; AI memakai data Rilis 1 yang dianonimkan (rinciannya di Scope Statement, Bagian 2.3.2) |
| Kalender | Hari kerja Senin–Jumat. Tanggal hari libur dan cuti bersama 2027 (antara lain Idulfitri ± 9–10 Maret 2027 dengan cuti bersama ± 8–12 Maret) masih **perkiraan**, menunggu penetapan resmi pemerintah |
| Nama | Semua nama orang, perusahaan, mitra, dan paguyuban adalah **fiktif**. Bank Indonesia, Kementerian Komunikasi dan Digital, serta Dinas Koperasi dan UKM DIY adalah lembaga nyata yang disebut sesuai perannya |

## 1.4 Metode dan sumber

Laporan ini memakai **satu kasus dan satu set data** yang dikerjakan dua kali:
- **Bab 2** dengan cara PMBOK 4. Bentuk dokumennya mengikuti contoh proyek JWD Consulting dari Schwalbe (2010) yang dibahas dalam slide perkuliahan.
- **Bab 3** dengan cara PMBOK 7.

Dengan begitu, perbedaan di Bab 4 berasal dari **cara berpikir** kedua edisi, bukan dari perbedaan kasus.

**Sumber utama:**
- PMBOK 4 (PMI, 2008) dan PMBOK 7 (PMI, 2021). Halaman yang dirujuk adalah nomor halaman buku. Untuk PMBOK 7, *Standard* dan *Guide* adalah dua bagian buku dengan penomoran halaman sendiri.
- Slide perkuliahan. "Slide 04" sampai "slide 08" adalah slide pertemuan 4–8 oleh Syafrizal (2026a–2026e). "Slide Minggu 04" adalah slide pertemuan 4 oleh Luthfi (2026).

**Alat bantu:**
- Jadwal proyek dimasukkan ke **ClickUp**, lengkap dengan ketergantungan antartugas. Tampilan Gantt-nya dapat dibuka di https://sharing.clickup.com/1100310000031077/g/h/z8q7hb3nb5-618/c5be485d10fbe8c
- **Pernyataan penggunaan AI.** Penyusunan laporan ini dibantu AI (Claude, Anthropic) untuk menelusuri rujukan dalam materi kuliah, menyusun draf, dan memeriksa konsistensi data antardokumen. Keputusan-keputusan proyek dan sikap dalam analisis komparatif ditetapkan penulis, dan isi refleksi manajerial (Bab 5) berasal dari pendapat penulis sendiri.

## 1.5 Sistematika laporan

- **Bab 2** berisi sepuluh dokumen PMBOK 4 dalam tiga tahap:
  - pra-inisiasi: Stakeholder Register, Stakeholder Management Strategy, Business Case;
  - inisiasi: Project Charter, Agenda Kick-off Meeting;
  - perencanaan: Team Contract, Project Scope Statement, WBS, jadwal, Risk Register.
- **Bab 3** menerapkan PMBOK 7: lima prinsip dan *Value Delivery System*, domain Stakeholder dan Team, serta domain Planning beserta ketidakpastian.
- **Bab 4** membandingkan kedua edisi dalam sembilan dimensi, lalu merumuskan sintesis dan rekomendasi.
- **Bab 5** memuat refleksi manajerial penulis.
- **Bab 6** berisi kesimpulan.

Laporan ditutup dengan glosarium, daftar pustaka, dan lampiran.

<!-- SISIPKAN: BAB 2-5 -->

# Bab 6 — Kesimpulan

1. **PMBOK 4 menghasilkan alat kendali yang lengkap dan saling terhubung.** Kesepuluh dokumen di Bab 2 memakai data yang sama, mulai dari Stakeholder Register sampai Risk Register. Kode WBS menghubungkan lingkup, jadwal, dan risiko. Penyusunan dokumen ini memunculkan tiga temuan penting:
   - risiko terbesar proyek adalah **adopsi UMKM**: adopsi 20% di bawah perkiraan membuat ROI tiga tahun menjadi −7,5%;
   - **kontrak mitra pembayaran** berada di jalur kritis;
   - **24 dari 42 paket kerja** tidak punya waktu longgar.
2. **PMBOK 7 memperlihatkan hal yang tidak terlihat dari dokumen PMBOK 4.** Hanya *output* yang terjadi selama proyek. *Outcome*, *benefit*, dan *value* sebagian besar baru terwujud setelah proyek ditutup. Karena itu proyek ini membutuhkan:
   - gerbang keputusan di M4;
   - pemantauan manfaat sampai Juni 2030;
   - pendekatan *hybrid* yang dipilih per komponen;
   - penanganan ketidakpastian lewat cara kerja: MVP, eksperimen satu kota, dan keterlibatan paguyuban.
3. **Kedua edisi saling melengkapi, bukan saling menggantikan.** PMBOK 4 paling tepat untuk bagian yang mengurus **uang dan aturan**: pembayaran, keamanan, izin, *milestone*, dan anggaran. PMBOK 7 paling tepat untuk bagian yang mengurus **manusia dan hal yang belum pasti**: keterlibatan UMKM, fitur *marketplace*, dan AI. PMBOK 7 tidak sama dengan Agile, karena PMBOK 7 sendiri menyarankan pendekatan prediktif untuk bagian yang berisiko tinggi dan diatur ketat.
4. **Rekomendasi untuk PT ND:**
   - jalankan proyek dengan pendekatan *hybrid*;
   - kunci kontrak dan akses *sandbox* mitra pembayaran sejak Januari;
   - jalankan gerbang M4 dengan sungguh-sungguh berdasarkan dasbor adopsi;
   - jadikan fitur pelengkap sebagai penyangga waktu;
   - pilah cadangan biaya menjadi cadangan kontingensi dan cadangan manajemen;
   - tetapkan penanggung jawab pemantauan manfaat setelah proyek selesai.
5. **Saran.** Simulasi ini memakai data fiktif dan perkiraan. Langkah berikutnya yang berguna:
   - menguji asumsi adopsi dan biaya dengan data pasar nyata;
   - menyusun ulang perbandingan dengan PMBOK edisi ke-8 (2025), yang memadukan kembali proses dan prinsip.

# Glosarium

| Istilah | Penjelasan |
|---|---|
| *Accept* (terima) | Strategi respons risiko: tidak bertindak lebih dulu, tetapi menyiapkan dana atau waktu cadangan bila risiko terjadi |
| Ambang risiko (*risk threshold*) | Batas penyimpangan yang masih dapat diterima organisasi; di proyek ini dituangkan dalam skala dampak Risk Register |
| Ambiguitas | Keadaan ketika belum jelas apa yang terjadi atau apa yang dibutuhkan; salah satu jenis ketidakpastian di PMBOK 7 |
| API (*Application Programming Interface*) | Antarmuka standar yang memungkinkan dua sistem atau program saling bertukar data |
| *Avoid* (hindari) | Strategi respons risiko: mengubah rencana agar ancaman hilang |
| *Benefit* (manfaat) | Keuntungan terukur yang diterima organisasi dari *outcome* proyek |
| Business Case | Dokumen yang menjelaskan alasan bisnis sebuah proyek: masalah atau peluang, pilihan solusi, biaya, manfaat, dan risiko |
| Cadangan kontingensi (*contingency reserve*) | Dana atau waktu yang disisihkan untuk risiko yang sudah teridentifikasi |
| Cadangan manajemen (*management reserve*) | Dana yang disisihkan untuk kejadian tak terduga yang masih dalam lingkup proyek |
| *Cloud* | Layanan server dan penyimpanan data yang disewa dari penyedia dan diakses lewat internet |
| Definisi selesai | Syarat yang harus dipenuhi sebelum suatu pekerjaan dianggap selesai |
| *Deliverable* | Hasil kerja yang harus diserahkan proyek |
| *Digital wallet* (dompet digital) | Layanan untuk menyimpan saldo dan membayar secara elektronik |
| *Enhance* (perbesar) | Strategi untuk peluang: menaikkan probabilitas atau dampak positifnya |
| *Exploit* (manfaatkan) | Strategi untuk peluang: memastikan peluang benar-benar terwujud |
| *Float* (waktu longgar) | Lama suatu pekerjaan boleh terlambat tanpa menggeser *milestone* atau akhir proyek |
| Gantt Chart | Diagram jadwal yang menampilkan pekerjaan sebagai batang mendatar di sepanjang garis waktu |
| *Ground rules* | Aturan dasar perilaku tim dalam PMBOK 4; padanan Team Contract |
| *Hybrid* | Pendekatan campuran: sebagian pekerjaan direncanakan rinci di awal (prediktif), sebagian disesuaikan bertahap (adaptif) |
| Jalur kritis (*critical path*) | Rangkaian pekerjaan yang tidak punya waktu longgar; keterlambatannya langsung menggeser *milestone* |
| *Kick-off meeting* | Rapat resmi pertama tim proyek dan stakeholder kunci untuk menyamakan pemahaman tentang tujuan, lingkup, jadwal, dan peran |
| Komite Pengarah | Forum pengambil keputusan proyek di atas PM; di proyek ini diketuai Direktur Utama |
| Kompleksitas | Keadaan ketika banyak unsur saling memengaruhi sehingga hasil sulit diramalkan |
| Kriteria penerimaan | Syarat terukur agar hasil proyek dinyatakan diterima (K1–K7) |
| *Lessons learned* | Pelajaran dari proyek yang dicatat untuk proyek berikutnya |
| Lintas platform | Satu kode program yang dapat dijalankan di Android dan iOS |
| *Milestone* | Penanda waktu bagi pencapaian penting proyek; bukan pekerjaan dan tidak punya durasi |
| *Mitigate* (kurangi) | Strategi respons risiko: menurunkan probabilitas atau dampak ancaman |
| MVP (*Minimum Viable Product*) | Versi produk paling sederhana yang sudah berguna, dirilis untuk menguji pasar dengan investasi kecil |
| NPV (*Net Present Value*) | Ukuran kelayakan yang mengubah uang masa depan menjadi nilai hari ini dengan potongan persentase per tahun; tidak dipakai di proyek ini |
| *Outcome* (hasil) | Perubahan perilaku atau kondisi akibat *output* proyek |
| *Output* (keluaran) | Hasil kerja langsung proyek, misalnya aplikasi yang selesai dibangun |
| *Payback period* | Lama waktu sampai modal proyek kembali |
| Pemicu (*trigger*) | Tanda awal bahwa suatu risiko mulai terjadi |
| Pendahulu (*predecessor*) | Pekerjaan yang harus selesai sebelum pekerjaan lain dimulai |
| *Penetration test* | Uji keamanan dengan mencoba membobol sistem secara sah untuk menemukan celah |
| *Performance domain* | Bidang kinerja di PMBOK 7, yaitu kelompok kegiatan yang saling terkait untuk mencapai hasil proyek |
| Portofolio | Kumpulan proyek dan program yang dikelola terpusat untuk mencapai tujuan strategis organisasi |
| *Power-Interest Grid* | Matriks empat kotak untuk memetakan stakeholder menurut pengaruh dan kepentingannya |
| Prinsip tanpa riba | Kebijakan perusahaan dalam simulasi ini: tanpa pinjaman berbunga, tanpa *paylater*, dana saldo di bank syariah, dan pendapatan tanpa denda |
| *Process group* | Kelompok proses di PMBOK 4: Initiating, Planning, Executing, Monitoring & Controlling, Closing |
| *Product Owner* | Orang yang menentukan urutan prioritas kebutuhan sebuah produk atau modul |
| Program | Sekelompok proyek yang saling terkait dan dikelola bersama untuk manfaat yang lebih besar |
| *Progressive elaboration* | Perencanaan yang makin rinci seiring bertambahnya informasi |
| Project Charter | Dokumen resmi yang mengesahkan proyek dan memberi wewenang kepada PM |
| Project Scope Statement | Dokumen yang menetapkan batas proyek: yang dikerjakan, yang tidak dikerjakan, dan syarat penerimaan |
| RACI | Matriks pembagian tanggung jawab: *Responsible*, *Accountable*, *Consulted*, *Informed* |
| Risk Register | Daftar risiko proyek beserta penilaian, respons, pemicu, dan pemiliknya |
| ROI (*Return on Investment*) | Perbandingan keuntungan bersih dengan total biaya |
| *Rolling wave planning* | Perencanaan rinci untuk pekerjaan yang dekat, dan garis besar untuk pekerjaan yang jauh |
| *Sandbox* | Sistem uji milik mitra yang meniru sistem sungguhan tanpa memakai uang atau data nyata |
| *Scope creep* | Penambahan pekerjaan secara diam-diam tanpa persetujuan |
| *Servant leadership* | Gaya kepemimpinan yang melayani tim dan menyingkirkan hambatan kerjanya |
| SLA (*Service Level Agreement*) | Jaminan tingkat layanan dalam kontrak, misalnya ketersediaan sistem |
| *Sprint* | Putaran kerja dengan waktu tetap (*timebox*), diakhiri dengan demo hasil kerja |
| Stakeholder | Orang, kelompok, atau lembaga yang terlibat, terdampak, atau dapat memengaruhi proyek |
| *Stakeholder Engagement Assessment Matrix* | Matriks yang membandingkan tingkat keterlibatan stakeholder saat ini dengan yang diinginkan |
| *Stewardship* | Prinsip PMBOK 7: mengelola amanah dengan integritas, kepedulian, dan kepatuhan |
| *Tailoring* | Penyesuaian pendekatan, proses, dan dokumen dengan konteks proyek |
| Team Contract / *team charter* | Kesepakatan tim tentang cara bekerja sama; *team charter* adalah istilah PMBOK 7 |
| *Transfer* (alihkan) | Strategi respons risiko: memindahkan tanggung jawab atas akibat ancaman ke pihak lain, misalnya lewat kontrak |
| UAT (*User Acceptance Test*) | Uji penerimaan oleh perwakilan pengguna |
| *Ujrah* | Upah atas jasa dalam muamalah syariah; besarnya disepakati terbuka sejak awal |
| UMKM | Usaha Mikro, Kecil, dan Menengah |
| *Uptime* | Persentase waktu sistem dapat dipakai |
| *Value* (nilai) | Arti penting, manfaat, atau kegunaan hasil proyek bagi stakeholder; indikator keberhasilan tertinggi di PMBOK 7 |
| *Value Delivery System* | Cara PMBOK 7 memandang proyek sebagai bagian dari sistem organisasi (portofolio, program, proyek, produk, operasional) yang bersama-sama menciptakan nilai |
| Volatilitas | Kondisi yang berubah cepat dan tidak terduga |
| WBS (*Work Breakdown Structure*) | Pemecahan seluruh pekerjaan proyek secara bertingkat menjadi paket kerja |
| *Weighted Scoring Model* | Cara memilih opsi dengan memberi bobot pada setiap kriteria lalu menjumlahkan skornya |
| *Work package* (paket kerja) | Tingkat terendah WBS yang dapat dijadwalkan, dianggarkan, dan diberi penanggung jawab |

# Daftar Pustaka

Luthfi, E. T. (2026). *IT project management: Pertemuan 4* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Project Management Institute. (2008). *A guide to the project management body of knowledge (PMBOK® Guide)* (4th ed.). Project Management Institute.

Project Management Institute. (2021). *The standard for project management and a guide to the project management body of knowledge (PMBOK® Guide)* (7th ed.). Project Management Institute.

Republik Indonesia. (2022). *Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*.

Schwalbe, K. (2010). *Managing information technology projects* (6th ed.). Course Technology, Cengage Learning.

Syafrizal, M. (2026a). *Metodologi manajemen proyek: Pertemuan 4* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026b). *Project initiation in IT project management: Pertemuan 5* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026c). *Project planning (core PMBOK): Pertemuan 6* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026d). *IT project management: Integrasi project plan: Pertemuan 7* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026e). *IT project management: Value delivery system (PMBOK 7): Pertemuan 8* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

# Lampiran A. Gantt Chart Utuh di ClickUp

Gambar berikut adalah seluruh tampilan Gantt proyek di ClickUp, disusun sesuai urutan gulir layar:
- **daftar bertingkat**: akar proyek, 5 cabang level 2, dan 42 paket kerja;
- **daftar kedua**: 42 paket kerja yang sama, ditampilkan ulang tanpa induk oleh opsi *Separate* di ClickUp;
- tujuh *milestone* M0–M6.

Batang merah adalah jalur kritis menurut perhitungan ClickUp. Perhitungan itu tidak memakai kalender libur proyek, sehingga dapat sedikit berbeda dengan tanda ● di Tabel 2.13 (lihat catatan 6 di Bagian 2.3.4). Tampilan aslinya dapat dibuka di https://sharing.clickup.com/1100310000031077/g/h/z8q7hb3nb5-618/c5be485d10fbe8c

<!-- GAMBAR_HALAMAN_BESAR: Gambar A.1 Tampilan Gantt ClickUp lengkap (97 baris) | ../clickup/gantt_clickup_utuh.png -->
