<!-- SAMPUL
judul: Rencana Proyek Sistem Peringatan Dini Cuaca Publik Berbasis IoT (Audio-Visual) Terintegrasi Data BMKG
subjudul: Work Breakdown Structure, Jadwal Proyek, dan Risk Register
jenis: Tugas Kelompok — IT Project Management
anggota: EKA PUTRA KURNIA|25.55.2927; ERLISNAWATI|25.55.2882; SRI REJEKI|25.55.2906
prodi: Program Studi S2 Informatika
kampus: Universitas Amikom Yogyakarta
dosen: Dosen Pengampu: Melwin Syafrizal, S.Kom., M.Eng., Ph.D.
waktu: Semester Ganjil 2026/2027 — November 2026
logo: ../../tugas1/sumber/logo_amikom.png
header: Rencana Proyek SPDC — Tugas Kelompok IT Project Management
-->

<!--
Draf laporan Tugas 2 (berkas sumber). Dokumen .docx dan .pdf dibuat dari berkas ini oleh buat_laporan.py.
Tabel lampiran, Risk Register, dan respons rinci diambil dari draf Tahap 1–3 (wbs_, jadwal_, risiko_peringatan_dini.md).
Penanda khusus untuk skrip: LANDSCAPE / PORTRAIT (ganti orientasi halaman), GANTT, MATRIKS_AWAL, MATRIKS_RESIDUAL,
"tabel: judul | lebar: persen,..." (judul dan lebar kolom tabel berikutnya).
-->

# 1. Pendahuluan

## 1.1 Latar belakang

Badan Meteorologi, Klimatologi, dan Geofisika (BMKG) menerbitkan **peringatan dini cuaca** di situs resminya, yaitu peringatan cuaca ekstrem untuk 0–6 jam ke depan, disusun per provinsi. Informasi ini baru sampai kepada warga yang sedang membuka situs atau media sosial BMKG. Warga di tempat umum, seperti pasar, terminal, sekolah, dan bantaran sungai, sering tidak menerimanya tepat waktu.

Dokumen ini merencanakan proyek **Sistem Peringatan Dini Cuaca Publik (SPDC)**, yaitu sistem yang membaca halaman peringatan dini BMKG secara berkala dan, bila wilayah sasaran disebut, otomatis menyalakan perangkat peringatan audio-visual di wilayah tersebut: panel LED bertuliskan pesan peringatan, lampu rotari (lampu putar), dan sirene. Sistem **tidak membuat prakiraan cuaca sendiri**; sistem hanya meneruskan peringatan resmi BMKG.

Dokumen ini disusun untuk memenuhi Tugas Kelompok mata kuliah IT Project Management, yaitu menyusun satu artefak perencanaan proyek yang memadukan seluruh *knowledge area* (bidang pengetahuan manajemen proyek) dalam PMBOK. Isinya tiga bagian utama yang saling terhubung: *Work Breakdown Structure* (WBS), jadwal proyek dalam bentuk Gantt Chart, dan Risk Register.

## 1.2 Cara kerja sistem

1. Server membuka halaman peringatan dini BMKG untuk provinsi yang relevan **setiap 5 menit** dengan Playwright, yaitu pustaka Python untuk mengendalikan peramban web secara otomatis.
2. Server mencari **nama wilayah sasaran** di teks halaman, per kata utuh, tanpa bergantung pada bentuk elemen HTML halaman.
3. Bila nama wilayah ditemukan, status wilayah menjadi **AKTIF**. Bila nama tidak muncul lagi pada **3 pengecekan berturut-turut**, status menjadi **SELESAI**. Bila halaman **gagal dimuat**, status tidak diubah dan admin diberi tanda.
4. Server mengirim perintah lewat **MQTT** (protokol kirim pesan ringan untuk perangkat IoT) ke semua perangkat yang terdaftar di wilayah tersebut.
5. Perangkat IoT berbasis **ESP32** (firmware C++) menyalakan panel LED, lampu rotari (melalui *relay*, yaitu sakelar listrik yang dikendalikan papan elektronik), dan sirene.
6. Setiap perangkat mengirim ***heartbeat*** (sinyal "masih hidup") dan data diagnosa ke server. Admin memantau semuanya melalui **dasbor**, termasuk menyalakan peringatan secara manual bila pembacaan otomatis terganggu.

## 1.3 Ringkasan lingkup (*Project Scope Statement*)

<!-- tabel: Tabel 1.1 Ringkasan lingkup proyek | lebar: 22,78 -->
| Komponen | Isi |
|---|---|
| Tujuan (SMART) | Dalam **±4 bulan**, memasang dan mengoperasikan **6 perangkat** peringatan audio-visual di **3 wilayah percontohan** DIY (Kota Yogyakarta, Kab. Sleman, Kab. Bantul) yang menyala **paling lambat 10 menit** setelah wilayahnya muncul di halaman peringatan dini BMKG |
| Hasil yang diserahkan (*deliverables*) | Server (modul pemantau BMKG, pencocok wilayah, pengelola status, MQTT *broker*, dasbor admin); 6 unit perangkat IoT terpasang; daftar wilayah dan variasi nama; dokumen kebutuhan, desain, laporan uji, manual operator, dan SOP; pelatihan operator dan sosialisasi warga |
| Di luar lingkup | Prakiraan cuaca sendiri; sensor cuaca; aplikasi HP warga; peringatan gempa dan tsunami; perawatan setelah serah terima |
| Batasan (*constraints*) | Durasi ±4 bulan; tim proyek 5 orang; sumber data hanya halaman publik BMKG; anggaran tidak dirinci dalam dokumen ini |
| Asumsi (*assumptions*) | Halaman BMKG tetap dapat diakses publik; lokasi pemasangan memiliki listrik dan sinyal; BPBD bersedia menjadi sponsor dan operator; izin pemasangan dapat diperoleh |
| *Sponsor* | BPBD (Badan Penanggulangan Bencana Daerah), sebagai pendana, pemilik sistem, dan operator |

*SMART*: tujuan yang Spesifik, Terukur (*Measurable*), Dapat dicapai (*Achievable*), Relevan, dan Berbatas waktu (*Time-bound*). *Deliverable*: hasil kerja yang diserahkan. *SOP*: prosedur kerja baku.

<!-- tabel: Tabel 1.2 Pemangku kepentingan | lebar: 30,70 -->
| Pihak | Peran |
|---|---|
| BPBD | *Sponsor*, pemilik sistem, dan operator |
| Warga di sekitar perangkat | Pengguna akhir penerima peringatan |
| Pemilik lokasi pemasangan | Pemberi izin dan penyedia listrik |
| BMKG | Sumber data; **bukan** pihak dalam proyek |
| Pemasok komponen | Penyedia board ESP32, panel LED, lampu, audio, dan *enclosure* (kotak pelindung) |
| Tim proyek | Pelaksana (5 orang, lihat Bagian 1.5) |

<!-- tabel: Tabel 1.3 Kriteria penerimaan | lebar: 6,64,30 -->
| No | Kriteria | Target |
|---|---|---|
| 1 | Waktu dari wilayah muncul di BMKG sampai perangkat menyala | ≤ 10 menit |
| 2 | Salah cocok pada daftar uji nama wilayah yang mirip | 0 kasus |
| 3 | Perangkat mati otomatis setelah wilayah hilang dari halaman | Setelah 3 pengecekan berturut-turut |
| 4 | Halaman BMKG gagal dimuat | Status tidak berubah; admin menerima tanda |
| 5 | Perangkat mati atau terputus terdeteksi di dasbor | ≤ 5 menit |
| 6 | Perangkat tetap bekerja saat listrik padam | ≥ 4 jam dengan baterai cadangan |
| 7 | Pesan panel LED terbaca di siang hari | Dari jarak 20 m |

## 1.4 Pendekatan pengerjaan

Proyek memakai pendekatan **prediktif** (*Waterfall*, tahap demi tahap). Pengadaan komponen, perakitan, dan pemasangan perangkat keras harus berurutan dan sulit diubah di tengah jalan, sehingga rencana lengkap perlu disusun di awal. Pengembangan perangkat lunak server tetap boleh dikerjakan bertahap di dalam fasenya.

## 1.5 Tim proyek dalam skenario

Tim proyek dalam dokumen ini adalah **simulasi skenario** dan berbeda dengan kelompok mahasiswa penyusun dokumen. Tim terdiri atas **5 orang untuk 6 peran**. Engineer IoT merangkap Teknisi Lapangan karena pekerjaan keduanya tidak pernah bertabrakan di jadwal: Teknisi Lapangan bekerja pada hari kerja ke-11–16 dan ke-71–75, sedangkan Engineer IoT pada hari ke-25–70.

<!-- tabel: Tabel 1.4 Peran dalam tim proyek | lebar: 10,30,60 -->
| Kode | Peran | Tanggung jawab utama |
|---|---|---|
| MP | Manajer Proyek | Perencanaan, pengadaan, izin, hubungan dengan sponsor, pemantauan risiko |
| AS | Analis Sistem | Kebutuhan, desain sistem, sosialisasi, pelatihan operator |
| PS | Programmer Server | Modul server, MQTT, dasbor, *deploy* |
| EI | Engineer IoT | Rangkaian perangkat keras, firmware ESP32, perakitan |
| QA | Penguji | Seluruh pengujian dan pencatatan *bug* |
| TL | Teknisi Lapangan | Survei lokasi dan pemasangan (dirangkap EI) |

# 2. Metodologi

## 2.1 Proses PMBOK yang dipakai

Dokumen ini merupakan hasil kelompok proses *Planning* (perencanaan) dalam PMBOK. Tabel 2.1 memetakan setiap *knowledge area* ke proses perencanaan PMBOK, teknik yang dipakai, dan letak hasilnya dalam dokumen ini. Pemetaan mengikuti Tabel 3-7 (proses perencanaan dan keluarannya) pada materi Pertemuan 4, ditambah *Stakeholder Management* dari PMBOK edisi ke-5 ke atas.

<!-- tabel: Tabel 2.1 Pemetaan knowledge area ke dokumen ini | lebar: 18,30,27,25 -->
| *Knowledge area* | Proses perencanaan PMBOK | Teknik yang dipakai | Letak dalam dokumen |
|---|---|---|---|
| *Integration* | *Develop project management plan* | Penyatuan rencana; keterkaitan antar-dokumen | Seluruh dokumen; Bab 6 |
| *Scope* | *Define scope*; *Create WBS* | *Scope statement*; dekomposisi; aturan 100% | Bagian 1.3; Bab 3; Lampiran A |
| *Time / Schedule* | *Define activities*; *Sequence activities*; *Estimate activity durations*; *Develop schedule* | PDM (hubungan FS); *three-point estimation* (PERT); *Critical Path Method* | Bab 4; Lampiran B |
| *Cost* | *Estimate costs*; *Determine budget* | Daftar komponen (BOM); cadangan waktu | WBS 1.1.1 dan 1.4.1 (tidak dirinci; di luar permintaan tugas) |
| *Quality* | *Plan quality* | Kriteria penerimaan terukur; pengujian bertahap; tinjauan kode | Tabel 1.3; fase 1.7; Bagian 4.5 |
| *Human Resource* | *Develop human resource plan* | Peran dan penanggung jawab per *work package* | Bagian 1.5; Lampiran A |
| *Communications* | *Plan communications* | Rapat dan laporan mingguan; sosialisasi; notifikasi admin | WBS 1.1.2, 1.8.4, 1.5.6 |
| *Risk* | *Plan risk management*; *Identify risks*; *Perform qualitative risk analysis*; *Plan risk responses* | RBS; Probability-Impact Matrix; lima strategi respons | Bab 5 |
| *Procurement* | *Plan procurements* | Fase pengadaan; pemilihan pemasok dalam negeri | Fase 1.4; risiko R-01 |
| *Stakeholder* | *Identify stakeholders* | Daftar pemangku kepentingan; sosialisasi | Tabel 1.2; WBS 1.8.4 |

## 2.2 Alat

<!-- tabel: Tabel 2.2 Alat yang dipakai | lebar: 25,45,30 -->
| Alat | Fungsi | Dipakai oleh |
|---|---|---|
| ClickUp | Menyusun WBS dan jadwal (Gantt) secara digital | Penyusun rencana |
| VS Code + PlatformIO | Editor kode; kompilasi dan *upload* firmware ESP32 | Tim proyek (skenario) |
| Python + Playwright | Modul pemantau halaman BMKG | Tim proyek (skenario) |
| Claude Code | Asisten pemrograman AI; seluruh kodenya wajib ditinjau anggota tim lain | Tim proyek (skenario) |
| Git | Penyimpan riwayat versi kode bersama | Tim proyek (skenario) |

# 3. Work Breakdown Structure (WBS)

## 3.1 Struktur

WBS adalah pemecahan **seluruh** pekerjaan proyek secara bertingkat menjadi bagian yang makin kecil. Elemen terbawahnya disebut *work package* (paket kerja), yaitu pekerjaan yang dapat ditugaskan, diperkirakan durasinya, dan dipantau. WBS proyek SPDC terdiri atas **3 level, 8 fase, dan 43 *work package*** dan disusun per fase, mengikuti pola PMBOK edisi ke-4 Gambar 5-9.

WBS disusun dengan **aturan 100%** (PMBOK 4, Bagian 5.3): semua pekerjaan yang diperlukan masuk ke WBS, termasuk pekerjaan yang sering terlupa, seperti manajemen proyek (1.1), pengadaan dan izin (1.4), *deploy* server (1.8.2), sosialisasi warga (1.8.4), dan pelatihan operator (1.8.5). Milestone tidak dimasukkan ke WBS karena bukan pekerjaan, melainkan penanda waktu di jadwal. Uraian, hasil, dan penanggung jawab setiap *work package* dimuat dalam kamus WBS (Lampiran A).

<!-- tabel: Tabel 3.1 Struktur WBS (3 level) | lebar: 12,10,78 -->
| Kode | Level | Elemen WBS |
|---|---|---|
| **1** | **1** | **Sistem Peringatan Dini Cuaca Publik (SPDC)** |
| **1.1** | **2** | **Manajemen Proyek** |
| 1.1.1 | 3 | Project charter dan rencana proyek |
| 1.1.2 | 3 | Rapat dan laporan kemajuan |
| 1.1.3 | 3 | Pengendalian perubahan dan pemantauan risiko |
| 1.1.4 | 3 | Penutupan proyek dan lessons learned |
| **1.2** | **2** | **Analisis Kebutuhan** |
| 1.2.1 | 3 | Kebutuhan pemangku kepentingan |
| 1.2.2 | 3 | Studi halaman peringatan dini BMKG |
| 1.2.3 | 3 | Daftar wilayah sasaran dan variasi nama |
| 1.2.4 | 3 | Survei lokasi pemasangan |
| 1.2.5 | 3 | Spesifikasi kebutuhan sistem (SRS) |
| **1.3** | **2** | **Desain Sistem** |
| 1.3.1 | 3 | Arsitektur sistem |
| 1.3.2 | 3 | Desain logika status peringatan |
| 1.3.3 | 3 | Desain database wilayah dan perangkat |
| 1.3.4 | 3 | Desain rangkaian perangkat keras |
| 1.3.5 | 3 | Desain pesan LED dan pola audio-lampu |
| 1.3.6 | 3 | Desain dasbor admin |
| **1.4** | **2** | **Pengadaan** |
| 1.4.1 | 3 | Daftar komponen (BOM) |
| 1.4.2 | 3 | Pemilihan pemasok dan pembelian komponen |
| 1.4.3 | 3 | Sewa server (VPS) dan domain |
| 1.4.4 | 3 | Izin pemasangan |
| 1.4.5 | 3 | Penyiapan alat pengembangan |
| **1.5** | **2** | **Pengembangan Perangkat Lunak Server** |
| 1.5.1 | 3 | Modul pemantau BMKG (Playwright) |
| 1.5.2 | 3 | Modul pencocokan nama wilayah |
| 1.5.3 | 3 | Modul pengelola status peringatan |
| 1.5.4 | 3 | Layanan pengirim perintah (MQTT) |
| 1.5.5 | 3 | Dasbor admin |
| 1.5.6 | 3 | Pemantauan heartbeat dan notifikasi admin |
| **1.6** | **2** | **Pengembangan Perangkat IoT** |
| 1.6.1 | 3 | Perakitan prototipe |
| 1.6.2 | 3 | Firmware C++ |
| 1.6.3 | 3 | Fitur heartbeat dan sambung ulang otomatis |
| 1.6.4 | 3 | Fitur diagnosa jarak jauh |
| 1.6.5 | 3 | Perakitan unit produksi |
| **1.7** | **2** | **Pengujian** |
| 1.7.1 | 3 | Uji unit perangkat lunak |
| 1.7.2 | 3 | Uji pencocokan nama wilayah |
| 1.7.3 | 3 | Uji perangkat keras |
| 1.7.4 | 3 | Uji integrasi ujung ke ujung |
| 1.7.5 | 3 | Uji kegagalan |
| 1.7.6 | 3 | Uji coba lapangan dan UAT |
| **1.8** | **2** | **Pemasangan dan Peluncuran** |
| 1.8.1 | 3 | Pemasangan perangkat di lokasi |
| 1.8.2 | 3 | Deploy perangkat lunak server dan pengamanan dasar |
| 1.8.3 | 3 | Konfigurasi wilayah dan pendaftaran perangkat |
| 1.8.4 | 3 | Sosialisasi ke warga |
| 1.8.5 | 3 | Pelatihan operator |
| 1.8.6 | 3 | Serah terima dan dokumentasi |

## 3.2 Keputusan desain yang tercermin di WBS

- Playwright mencari teks nama wilayah tanpa bergantung pada bentuk elemen HTML (1.5.1, 1.5.2); tautan halaman per provinsi sudah tersedia (1.2.2).
- Peringatan dianggap selesai bila wilayah tidak muncul lagi pada 3 pengecekan berturut-turut; halaman yang gagal dimuat tidak mengubah status (1.3.2, 1.5.3).
- Pencocokan per kata utuh dengan daftar variasi nama dan daftar nama mirip yang harus ditolak (1.2.3, 1.5.2, 1.7.2).
- MQTT untuk perintah server ke perangkat (1.5.4, 1.6.2); board ESP32 dengan relay, audio, panel LED *outdoor*, baterai cadangan, modem 4G, serta sensor arus dan tegangan (1.3.4, 1.4.1).
- *Heartbeat* dan diagnosa jarak jauh (1.5.6, 1.6.3, 1.6.4); dasbor admin dengan aktivasi peringatan manual (1.3.6, 1.5.5).
- *Debugging* saat menulis kode termasuk dalam 1.5.x dan 1.6.x; perbaikan *bug* hasil pengujian termasuk dalam 1.7.x dengan pola uji → perbaiki → uji ulang.

# 4. Jadwal Proyek (Gantt Chart & Schedule)

## 4.1 Dasar penyusunan

Jadwal disusun melalui empat proses PMBOK:

- ***Define activities***: setiap *work package* menjadi satu aktivitas dengan kode yang sama dengan WBS.
- ***Sequence activities***: urutan disusun dengan *Precedence Diagramming Method* (PMBOK 4, Bagian 6.2.2.1). Semua hubungan berjenis **FS** (*Finish-to-Start*): aktivitas berikut mulai setelah pendahulunya selesai.
- ***Estimate activity durations***: durasi diperkirakan dengan ***three-point estimation*** (PERT; PMBOK 4, Bagian 6.4.2.4), yaitu (Optimis + 4 × Paling mungkin + Pesimis) / 6, lalu dibulatkan ke hari terdekat.
- ***Develop schedule***: jalur kritis dihitung dengan ***Critical Path Method*** (CPM; PMBOK 4, Bagian 6.5.2.2) melalui hitung maju dan hitung mundur. *Float* (kelonggaran) adalah selisih waktu mulai paling lambat dan paling awal; aktivitas dengan *float* 0 berada di jalur kritis.

Satuan waktu adalah **hari kerja** (5 hari per minggu). Pekerjaan 1.1.2 (rapat dan laporan kemajuan) dan 1.1.3 (pengendalian perubahan dan pemantauan risiko) berjalan sepanjang proyek sehingga tidak dihitung dalam jalur kritis. Tabel aktivitas lengkap beserta nilai O, M, P, ES, EF, LS, LF, dan *float* dimuat di Lampiran B.

## 4.2 Ringkasan hasil

<!-- tabel: Tabel 4.1 Ringkasan jadwal | lebar: 28,72 -->
| Hal | Hasil |
|---|---|
| Durasi proyek | **92 hari kerja ≈ 18,4 minggu ≈ 4,2 bulan** (sesuai target ±4 bulan) |
| Jumlah aktivitas | 43 *work package* + 6 milestone |
| Jalur kritis | Melalui perangkat keras dan pengujian akhir |
| Waktu pengujian | 31 hari kerja aktivitas uji, termasuk perbaikan *bug* dan uji ulang |
| Cadangan waktu | 5 hari kerja dipegang manajer proyek (*contingency reserve*, PMBOK 4, Bagian 6.4.2.5); batas selesai terburuk hari ke-97 |

## 4.3 Milestone

<!-- tabel: Tabel 4.2 Daftar milestone | lebar: 8,44,14,12,22 -->
| Kode | Milestone | Hari kerja ke- | Minggu ke- | Disetujui oleh |
|---|---|---|---|---|
| M1 | Proyek disahkan (project charter ditandatangani) | 5 | 1 | Sponsor (BPBD) |
| M2 | Kebutuhan disetujui (SRS ditandatangani) | 21 | 5 | Sponsor |
| M3 | Desain disetujui | 29 | 6 | Manajer proyek + sponsor |
| M4 | UAT disetujui | 86 | 18 | Sponsor |
| M5 | Sistem diserahterimakan | 89 | 18 | Sponsor |
| M6 | Proyek ditutup | 92 | 19 | Manajer proyek |

## 4.4 Jalur kritis

**1.1.1 → M1 → 1.2.1 → 1.2.4 → 1.2.5 → M2 → 1.3.1 → 1.3.4 → 1.4.1 → 1.4.2 → 1.6.1 → 1.6.2 → 1.6.3 → 1.6.4 → 1.7.3 → [cabang A atau B] → 1.7.6 → M4 → 1.8.6 → M5 → 1.1.4 → M6 = 92 hari kerja**

Setelah uji perangkat keras (1.7.3), jalur kritis bercabang dua dengan panjang sama (12 hari) dan bertemu kembali di uji lapangan/UAT (1.7.6):

- **Cabang A:** 1.6.5 Perakitan unit produksi → 1.8.1 Pemasangan → 1.8.3 Konfigurasi wilayah dan perangkat.
- **Cabang B:** 1.7.4 Uji integrasi ujung ke ujung → 1.7.5 Uji kegagalan.

Beberapa hal yang terbaca dari hasil ini:

1. **Lama proyek ditentukan oleh perangkat keras dan pengujian akhir**, bukan oleh perangkat lunak server. Pekerjaan perangkat lunak server masih memiliki *float* 10 hari.
2. **Pembelian komponen (1.4.2) adalah titik paling rawan.** Perkiraan pesimisnya 20 hari (perkiraan paling mungkin 10 hari), dan setiap keterlambatan langsung menunda proyek (risiko R-01).
3. **Izin pemasangan (1.4.4) tidak kritis tetapi paling tidak pasti.** *Float*-nya 37 hari, dengan rentang perkiraan 10–30 hari (risiko R-02).
4. **Uji integrasi dan uji kegagalan menjadi kritis** karena durasinya sudah memasukkan waktu perbaikan *bug* (risiko R-06).

## 4.5 Lama waktu pengujian

<!-- tabel: Tabel 4.3 Lama waktu pengujian | lebar: 9,37,10,16,13,15 -->
| Kode | Pengujian | Durasi | Hari kerja ke- | Minggu ke- | Kritis? |
|---|---|---|---|---|---|
| 1.7.2 | Uji pencocokan nama wilayah | 2 | 39–40 | 8 | Tidak |
| 1.7.1 | Uji unit perangkat lunak | 3 | 50–52 | 10–11 | Tidak |
| 1.7.3 | Uji perangkat keras | 4 | 61–64 | 13 | **Ya** |
| 1.7.4 | Uji integrasi ujung ke ujung | 7 | 65–71 | 13–15 | **Ya** |
| 1.7.5 | Uji kegagalan | 5 | 72–76 | 15–16 | **Ya** |
| 1.7.6 | Uji coba lapangan dan UAT | 10 | 77–86 | 16–18 | **Ya** |
| | **Jumlah** | **31 hari kerja** | | | |

Perbaikan *bug* (*debugging*) termasuk dalam periode pengujian dengan pola **uji → perbaiki → uji ulang**: penguji mencatat *bug*, Programmer Server atau Engineer IoT memperbaikinya, lalu penguji menguji ulang. Pengujian tidak ditumpuk di akhir proyek: uji pencocokan nama dan uji unit dijalankan pada minggu 8–11, jauh sebelum uji integrasi. UAT (*User Acceptance Testing*, uji penerimaan oleh sponsor) berlangsung 10 hari kerja agar perangkat dapat diamati di lokasi dalam beberapa kondisi cuaca; bila selama masa itu BMKG tidak mengeluarkan peringatan untuk wilayah percontohan, pengujian memakai mode uji dari dasbor.

## 4.6 Catatan sumber daya dan pilihan pemendekan jadwal

CPM menghitung jadwal tanpa memperhitungkan jumlah orang. Dari pengecekan per peran, beberapa pekerjaan dalam satu peran bertumpang tindih (misalnya 1.5.1 dan 1.5.4 pada Programmer Server), tetapi semuanya dapat digeser dalam *float* masing-masing tanpa memundurkan proyek; perhitungan ulang dengan CPM untuk skenario satu Programmer Server tetap menghasilkan 92 hari kerja.

Bila sponsor meminta proyek dipercepat, tersedia pilihan ***fast tracking*** (PMBOK 4, Bagian 6.5.2.7): komponen untuk satu prototipe dibeli lebih dulu tanpa menunggu pembelian komponen produksi. Hasil perhitungan ulang CPM: **88 hari kerja** dengan satu Programmer Server, atau **82 hari kerja** dengan dua programmer. Risikonya, bila prototipe menunjukkan komponen yang salah, sebagian pembelian harus diulang. Pilihan ini **tidak diterapkan** karena durasi 92 hari sudah sesuai target.

<!-- LANDSCAPE -->

## 4.7 Gantt Chart

<!-- GANTT -->

<!-- PORTRAIT -->

# 5. Risk Register

## 5.1 Proses dan skala penilaian

Risiko dikelola melalui proses PMBOK *Identify risks*, *Perform qualitative risk analysis*, dan *Plan risk responses*. Risiko dicari dengan menelusuri WBS, jalur kritis jadwal, dan *Risk Breakdown Structure* (RBS; PMBOK 4, Gambar 11-4), yaitu pohon kategori risiko: teknis, eksternal, organisasi, dan manajemen proyek. Setiap risiko ditulis dengan pola **sebab → kejadian → akibat**, dinilai Kemungkinan (K) dan Dampak (D) dengan skala 1–5, lalu dipetakan ke **Probability-Impact Matrix**.

<!-- tabel: Tabel 5.1 Skala kemungkinan (dari contoh Risk Register dosen) | lebar: 15,35,50 -->
| Nilai | Tipe | Peluang terjadi |
|---|---|---|
| 5 | Sangat sering | 50% |
| 4 | Sering | 20% |
| 3 | Sedang | 10% |
| 2 | Jarang | 5% |
| 1 | Hampir tidak pernah | 2% |

<!-- tabel: Tabel 5.2 Skala dampak (PMBOK 4, Gambar 11-5; waktu dihitung dari 92 hari kerja) | lebar: 8,14,26,26,26 -->
| Nilai | Tipe | Waktu | Lingkup | Mutu |
|---|---|---|---|---|
| 5 | Serius | Mundur > 20% (> 18 hari) | Hasil akhir praktis tidak berguna | Hasil akhir praktis tidak berguna |
| 4 | Tinggi | Mundur 10–20% (± 10–18 hari) | Pengurangan lingkup tidak dapat diterima sponsor | Penurunan mutu tidak dapat diterima sponsor |
| 3 | Sedang | Mundur 5–10% (± 5–9 hari) | Bagian utama lingkup terdampak | Penurunan mutu perlu persetujuan sponsor |
| 2 | Rendah | Mundur < 5% (< 5 hari) | Bagian kecil lingkup terdampak | Hanya fungsi yang sangat menuntut yang terdampak |
| 1 | Sangat rendah | Tidak berarti | Nyaris tak terasa | Nyaris tak terasa |

Bila satu risiko mengenai beberapa sasaran, dipakai nilai tertinggi. Nilai risiko = K × D, dengan level: **Kritikal** 20–25, **Tinggi** 13–19, **Sedang** 6–12, dan **Rendah** 1–5 (mengikuti contoh Risk Register dosen).

<!-- LANDSCAPE -->

## 5.2 Daftar risiko

<!-- tabel: Tabel 5.3 Risk Register | lebar: 4,9,34,8,3,3,4,6,12,6,11 -->
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

## 5.3 Probability-Impact Matrix

<!-- MATRIKS_AWAL -->

<!-- MATRIKS_RESIDUAL -->

Sebelum respons terdapat 2 risiko Tinggi (R-01 dan R-03) dan 8 risiko Sedang. Setelah respons, tidak ada lagi risiko Tinggi: 6 risiko Sedang dan 4 risiko Rendah. Kelima strategi respons PMBOK dipakai: *Avoid* (menghindari), *Mitigate* (mengurangi), *Transfer* (mengalihkan ke pihak ketiga), *Accept* aktif (menerima dengan cadangan atau rencana darurat), dan *Escalate* (menyerahkan ke pihak yang lebih berwenang; PMBOK edisi ke-7).

## 5.4 Rencana respons rinci

<!-- tabel: Tabel 5.4 Rencana respons rinci | lebar: 5,13,40,15,6,10,11 -->
| ID | Strategi | Tindakan | Pemicu | Pemilik | Batas waktu | Residual |
|---|---|---|---|---|---|---|
| **R-01** | ***Avoid***: menghilangkan ketergantungan pada barang impor. ***Mitigate***: mengurangi kemungkinan dan dampak keterlambatan | 1) Saat menyusun BOM (1.4.1), utamakan komponen yang **tersedia di pemasok dalam negeri**; board ESP32 dipilih antara lain karena mudah didapat di toko elektronik lokal. 2) Siapkan **minimal dua pemasok** untuk setiap komponen utama. 3) Pesan **segera** setelah BOM disetujui. 4) Beli **1 unit komponen cadangan** untuk setiap jenis. 5) Bila perlu, gunakan *fast tracking* (jadwal Tahap 2, Bagian 8): komponen prototipe dibeli lebih dulu | Pemasok belum mengonfirmasi stok dalam 2 hari kerja setelah pesanan, atau nomor resi belum ada di hari ke-5 | MP | Daftar pemasok siap sebelum 1.4.2 dimulai (minggu 7) | K 2 × D 3 = **6 (Sedang)**: keterlambatan masih mungkin, tetapi dengan pemasok cadangan diperkirakan < 9 hari |
| **R-02** | ***Escalate***: izin dari pemda dan pemilik lokasi berada **di luar wewenang tim proyek**, sehingga diserahkan ke sponsor (BPBD) yang punya jalur antarinstansi. ***Mitigate***: mempercepat pengurusan | 1) Ajukan izin **langsung setelah survei lokasi** (1.2.4) selesai. 2) Minta **surat dukungan dari BPBD** untuk dilampirkan. 3) Saat survei, tetapkan **satu lokasi cadangan** untuk setiap wilayah | Belum ada jawaban 10 hari kerja setelah pengajuan | MP (eskalasi ke sponsor) | Pengajuan izin di minggu 4 | K 1 × D 4 = **4 (Rendah)**: dengan dukungan BPBD dan lokasi cadangan, kemungkinannya kecil |
| **R-03** | ***Mitigate***: membuat pembacaan tahan terhadap perubahan. ***Accept* aktif**: menyiapkan rencana darurat bila tetap terjadi | 1) Playwright mencari **teks nama wilayah tanpa bergantung pada bentuk elemen HTML** (keputusan desain). 2) Pengecekan **setiap 5 menit dan hanya halaman provinsi yang relevan**, supaya tidak membebani server BMKG. 3) Status **"gagal muat"** dan notifikasi ke admin (1.5.3, 1.5.6). 4) Saat studi halaman (1.2.2), periksa apakah BMKG menyediakan *feed* RSS/CAP sebagai **sumber cadangan**. 5) **Rencana darurat**: admin dapat menyalakan peringatan secara manual dari dasbor (1.5.5) bila pembacaan otomatis terganggu | Modul pemantau mencatat "gagal muat" 3 kali berturut-turut, atau teks penanda halaman tidak ditemukan | PS | Studi halaman di minggu 2; modul pemantau di minggu 6–7 | K 2 × D 3 = **6 (Sedang)**: bila terjadi, sistem tetap bisa dipakai lewat sumber cadangan atau mode manual |
| **R-04** | ***Mitigate*** | 1) Pencocokan **per kata utuh** (keputusan desain). 2) Susun **daftar variasi nama** dan **daftar nama mirip yang harus ditolak** (1.2.3). 3) Uji khusus pencocokan nama (1.7.2) dengan target **0 salah cocok** (kriteria penerimaan 2) | Uji 1.7.2 menemukan satu atau lebih salah cocok, atau muncul penulisan nama wilayah baru di halaman BMKG | AS | Daftar nama di minggu 3; uji di minggu 8 | K 1 × D 4 = **4 (Rendah)** |
| **R-05** | ***Mitigate*** | 1) Baterai cadangan/UPS untuk **≥ 4 jam** (kriteria penerimaan 6). 2) **Modem 4G** sebagai jalur internet bila Wi-Fi tidak tersedia. 3) Fitur **sambung ulang otomatis** dan **heartbeat** (1.6.3). 4) Saat survei (1.2.4), pilih titik dengan **sinyal baik**. 5) Uji kegagalan (1.7.5) mensimulasikan listrik padam dan internet putus | Uji baterai < 4 jam, atau heartbeat hilang > 5 menit saat pengujian | EI | Desain rangkaian di minggu 5–6; uji kegagalan di minggu 15–16 | K 2 × D 3 = **6 (Sedang)**: padam lebih lama dari kapasitas baterai tetap mungkin |
| **R-06** | ***Mitigate*** + ***Accept* aktif** | 1) **Uji dini**: uji pencocokan nama (minggu 8) dan uji unit (minggu 10–11) dijalankan jauh sebelum uji integrasi. 2) **Tinjauan kode** untuk setiap perubahan. 3) **Halaman uji tiruan**, supaya uji integrasi tidak perlu menunggu peringatan BMKG sungguhan. 4) **Cadangan waktu 5 hari kerja** dipegang manajer proyek (*contingency reserve*, PMBOK 4, Bagian 6.4.2.5, hlm. 150). Cadangan ini tidak dimasukkan ke jadwal sebagai aktivitas; bila terpakai seluruhnya, proyek selesai paling lambat di hari ke-97 | Masih ada *bug* berat yang belum diperbaiki di hari ke-5 uji integrasi | QA | Uji dini di minggu 8–11 | K 2 × D 2 = **4 (Rendah)** |
| **R-07** | ***Mitigate***: mengurangi ketergantungan pada satu orang | 1) Semua firmware disimpan di **Git** dengan catatan perubahan harian. 2) Firmware **ditinjau oleh PS**, sehingga ada orang kedua yang memahaminya. 3) Skema rangkaian (1.3.4) didokumentasikan lengkap | EI tidak hadir lebih dari 2 hari kerja selama minggu 9–12 | MP | Mulai minggu 9 (perakitan prototipe) | K 2 × D 3 = **6 (Sedang)**: pengganti tetap butuh waktu mempelajari, diperkirakan < 1 minggu |
| **R-08** | ***Mitigate*** | 1) **Tinjauan kode wajib** oleh anggota lain sebelum kode digabungkan (aturan di Tahap 1, Bagian 1.11). 2) Kata sandi dan kunci akses **disimpan di berkas konfigurasi terpisah yang tidak ikut ke repositori**, dan tidak pernah dimasukkan ke percakapan dengan AI. 3) Pemeriksaan keamanan dasar saat *deploy* (1.8.2): *firewall*, HTTPS, dan memastikan tidak ada data rahasia di repositori | Tinjauan kode menemukan bagian yang tidak bisa dijelaskan penulisnya, atau ada data rahasia terdeteksi di repositori | PS | Aturan berlaku sejak penyiapan alat (minggu 2) | K 2 × D 3 = **6 (Sedang)** |
| **R-09** | ***Mitigate*** | 1) Pola bunyi, volume, dan jam senyap **disepakati bersama sponsor** saat desain (1.3.5). 2) **Sosialisasi** sebelum sistem dipakai (1.8.4): arti setiap bunyi dan lampu, serta tindakan yang harus dilakukan warga. 3) Tombol **senyapkan sementara** di dasbor untuk keadaan tertentu. 4) Volume diatur ulang saat uji lapangan | Ada keluhan warga selama uji lapangan | AS | Desain di minggu 5; sosialisasi di minggu 16 | K 2 × D 3 = **6 (Sedang)** |
| **R-10** | ***Transfer***: mengalihkan beban kerugian ke pihak ketiga. ***Mitigate***: mempersulit pencurian | 1) **Asuransi perangkat**, atau **perjanjian dengan pemilik lokasi** yang mencantumkan tanggung jawab keamanan. 2) Pasang di **ketinggian** dengan *enclosure* **terkunci**. 3) Fitur diagnosa (1.6.4) segera memberi tahu admin bila perangkat mati tanpa sebab teknis | Perangkat terputus tanpa sebab teknis, atau ada laporan kerusakan fisik | TL | Perjanjian atau asuransi selesai sebelum pemasangan (minggu 14) | K 2 × D 2 = **4 (Rendah)** |

<!-- PORTRAIT -->

# 6. Keterkaitan Antar-Dokumen

Ketiga bagian rencana saling terhubung melalui **kode WBS** yang sama. Risiko diidentifikasi dari *work package* dan posisinya di jadwal, dan respons risiko yang menambah pekerjaan dikembalikan ke WBS dan jadwal.

<!-- tabel: Tabel 6.1 Keterkaitan risiko, WBS, jadwal, dan respons | lebar: 24,12,22,42 -->
| Risiko | WBS terkait | Posisi di jadwal | Respons kembali ke rencana |
|---|---|---|---|
| R-01 Pengiriman komponen terlambat | 1.4.2 | 1.4.2 **kritis** | Pemasok dalam negeri, dua pemasok, dan unit cadangan dalam 1.4.1–1.4.2; pilihan *fast tracking* (Bagian 4.6) |
| R-02 Izin pemasangan terlambat | 1.4.4, 1.8.1 | 1.4.4 *float* 37; 1.8.1 **kritis** | Izin diajukan segera setelah 1.2.4 (minggu 4); eskalasi ke BPBD; lokasi cadangan ditetapkan di 1.2.4 |
| R-03 Halaman BMKG berubah/diblokir | 1.2.2, 1.5.1 | 1.2.2 *float* 5; 1.5.1 *float* 10 | Aktivasi peringatan manual **ditambahkan** ke 1.3.6 dan 1.5.5; sumber cadangan diperiksa di 1.2.2 |
| R-04 Salah cocok nama wilayah | 1.2.3, 1.5.2, 1.7.2 | 1.2.3 *float* 3; 1.5.2 *float* 10; 1.7.2 *float* 22 | Daftar nama mirip di 1.2.3; uji khusus 1.7.2 dengan target 0 salah cocok |
| R-05 Listrik/internet putus | 1.3.4, 1.6.3, 1.7.5 | 1.3.4 **kritis**; 1.6.3 **kritis**; 1.7.5 **kritis** | Baterai cadangan dan modem 4G di BOM (1.4.1); simulasi padam di 1.7.5 |
| R-06 *Bug* lebih banyak | 1.7.4, 1.7.5 | 1.7.4 **kritis**; 1.7.5 **kritis** | Uji dini 1.7.1–1.7.2; **cadangan waktu 5 hari** di luar jadwal (batas hari ke-97) |
| R-07 Engineer IoT berhalangan | 1.6.1, 1.6.2, 1.6.3, 1.6.4 | 1.6.1 **kritis**; 1.6.2 **kritis**; 1.6.3 **kritis**; 1.6.4 **kritis** | Firmware di Git dan ditinjau PS selama 1.6.x |
| R-08 Kesalahan/kebocoran dari Claude Code | 1.4.5, 1.5.5, 1.8.2 | 1.4.5 *float* 32; 1.5.5 *float* 10; 1.8.2 *float* 10 | Aturan tinjauan kode (Bagian 2.2); pemeriksaan keamanan saat 1.8.2 |
| R-09 Keluhan warga terhadap sirene | 1.3.5, 1.8.4 | 1.3.5 *float* 16; 1.8.4 *float* 8 | Pola bunyi disepakati di 1.3.5; sosialisasi di 1.8.4 |
| R-10 Perangkat dicuri/dirusak | 1.8.1 | 1.8.1 **kritis** | Asuransi atau perjanjian lokasi masuk anggaran (1.1.1) dan izin (1.4.4) |

Risk Register ditinjau dalam rapat mingguan (WBS 1.1.2) dan diperbarui melalui pekerjaan 1.1.3 (pengendalian perubahan dan pemantauan risiko) sepanjang proyek.

# 7. Kesimpulan

Rencana proyek SPDC terdiri atas WBS 3 level dengan 43 *work package*, jadwal 92 hari kerja (sekitar 4,2 bulan) yang disusun dengan estimasi PERT dan *Critical Path Method*, serta Risk Register berisi 10 risiko proyek yang dianalisis dengan Probability-Impact Matrix dan diberi rencana respons rinci.

Analisis jalur kritis menunjukkan bahwa keberhasilan jadwal paling ditentukan oleh rantai perangkat keras, yaitu pembelian komponen, prototipe, firmware, perakitan, dan pemasangan, serta pengujian akhir. Temuan ini sejalan dengan Risk Register: dua risiko teratas adalah keterlambatan pengiriman komponen (R-01) dan perubahan atau pembatasan akses halaman BMKG (R-03). Dengan respons yang direncanakan, seluruh risiko turun ke level Sedang atau Rendah, dan cadangan waktu 5 hari tersedia untuk menghadapi *bug* yang lebih banyak dari perkiraan.

# Glosarium

<!-- tabel: | lebar: 28,72 -->
| Istilah | Penjelasan |
|---|---|
| *Accept* aktif | Strategi respons: risiko diterima, tetapi disiapkan cadangan atau rencana darurat |
| *Acceptance criteria* | Kriteria penerimaan; syarat hasil dinyatakan selesai dan diterima |
| *Assumptions* | Asumsi; hal yang dianggap benar sebagai dasar perencanaan |
| *Avoid* | Strategi respons: mengubah rencana supaya ancaman hilang |
| *Backup* | Salinan data cadangan |
| BMKG | Badan Meteorologi, Klimatologi, dan Geofisika |
| BOM (*Bill of Materials*) | Daftar komponen beserta jumlah dan spesifikasinya |
| BPBD | Badan Penanggulangan Bencana Daerah |
| *Bug* | Kesalahan dalam program |
| *Change log* | Catatan semua permintaan perubahan dan keputusannya |
| Claude Code | Asisten pemrograman berbasis AI yang membantu menulis dan memeriksa kode |
| *Code review* (tinjauan kode) | Pemeriksaan kode oleh anggota tim lain sebelum kode dipakai |
| *Constraints* | Batasan proyek: waktu, biaya, jumlah orang |
| *Contingency reserve* | Cadangan waktu atau biaya untuk menghadapi risiko |
| *Critical Path Method* (CPM) | Teknik menghitung jalur terpanjang dalam jadwal untuk menemukan jalur kritis |
| Dampak (D) | Seberapa parah akibat risiko bila terjadi |
| *Debugging* | Mencari dan memperbaiki *bug* |
| *Deliverable* | Hasil kerja yang diserahkan |
| *Deploy* | Memasang program ke server sungguhan agar bisa dipakai |
| Ekstensi | Tambahan fitur yang dipasang ke dalam aplikasi |
| *Enclosure* | Kotak pelindung perangkat, misalnya tahan air |
| *Escalate* | Strategi respons: risiko di luar wewenang tim diserahkan ke pihak yang lebih berwenang |
| ES / EF | *Early Start* / *Early Finish*: mulai / selesai paling awal |
| ESP32 | Papan mikrokontroler dengan Wi-Fi bawaan, diprogram dengan C++ |
| *Fast tracking* | Teknik memperpendek jadwal dengan mengerjakan paralel aktivitas yang biasanya berurutan |
| *Firewall* | Penyaring akses jaringan; hanya akses yang diizinkan yang bisa masuk |
| *Firmware* | Program yang tertanam di papan elektronik |
| *Float* | Kelonggaran; berapa hari aktivitas boleh terlambat tanpa menunda proyek |
| FS (*Finish-to-Start*) | Hubungan ketergantungan: aktivitas berikut mulai setelah pendahulunya selesai |
| Gantt Chart | Jadwal berbentuk batang mendatar di atas garis waktu |
| Git | Alat penyimpan riwayat versi kode |
| *Heartbeat* | Sinyal berkala dari perangkat yang menandakan perangkat masih hidup |
| HTTPS | Sambungan web terenkripsi |
| IoT (*Internet of Things*) | Perangkat fisik yang tersambung ke internet |
| Jalur kritis | Rangkaian aktivitas dengan *float* nol; keterlambatannya langsung menunda proyek |
| Kemungkinan (K) | Seberapa besar peluang risiko terjadi |
| *Knowledge area* | Bidang pengetahuan manajemen proyek dalam PMBOK, misalnya lingkup, jadwal, dan risiko |
| Lampu rotari | Lampu putar seperti pada kendaraan patroli |
| *Lessons learned* | Catatan pelajaran dari proyek untuk proyek berikutnya |
| *Library* | Kumpulan kode siap pakai |
| LS / LF | *Late Start* / *Late Finish*: mulai / selesai paling lambat tanpa menunda proyek |
| Milestone | Titik pencapaian penting berdurasi nol |
| *Mitigate* | Strategi respons: menurunkan kemungkinan dan/atau dampak |
| *Mockup* | Gambar rancangan tampilan sebelum dibuat |
| MQTT | Protokol kirim pesan ringan untuk IoT, berbasis topik |
| MQTT *broker* | Program server yang menerima dan meneruskan pesan MQTT |
| Panel LED matrix | Papan tampilan yang tersusun dari banyak titik LED untuk menampilkan teks |
| Pemicu (*trigger*) | Tanda bahwa sebuah risiko mulai terjadi |
| Pemilik risiko (*risk owner*) | Orang yang bertanggung jawab memantau dan menangani satu risiko |
| PERT / *three-point estimation* | Estimasi durasi dari tiga perkiraan: (Optimis + 4 × Paling mungkin + Pesimis) / 6 |
| PlatformIO | Ekstensi VS Code untuk menulis, mengompilasi, dan meng-*upload* firmware ke board IoT |
| *Playwright* | Pustaka untuk mengendalikan peramban web secara otomatis |
| PMBOK | *Project Management Body of Knowledge*; buku standar manajemen proyek dari Project Management Institute (PMI) |
| *Precedence Diagramming Method* (PDM) | Metode menyusun urutan aktivitas dengan kotak dan panah ketergantungan |
| Prediktif / *Waterfall* | Pendekatan proyek tahap demi tahap secara berurutan |
| Probability-Impact Matrix | Matriks kemungkinan × dampak untuk menentukan prioritas risiko |
| *Project charter* | Piagam proyek; dokumen resmi yang mengesahkan dimulainya proyek |
| RBS (*Risk Breakdown Structure*) | Pohon kategori risiko untuk membantu menemukan risiko |
| *Relay* | Sakelar listrik yang dikendalikan oleh papan elektronik |
| Repositori | Tempat penyimpanan kode bersama beserta riwayat perubahannya |
| *Residual risk* | Risiko sisa; nilai risiko setelah respons dijalankan |
| *Rework* | Pekerjaan ulang karena hasil sebelumnya harus diperbaiki |
| Risk Register | Daftar risiko beserta nilai dan rencana responsnya |
| SMART | Tujuan yang Spesifik, Terukur, Dapat dicapai, Relevan, dan Berbatas waktu |
| SOP | *Standard Operating Procedure*; prosedur kerja baku |
| SPDC | Sistem Peringatan Dini Cuaca Publik; nama proyek dalam dokumen ini |
| *Sponsor* | Pihak yang mendanai dan mengesahkan proyek |
| SRS | *Software Requirements Specification*; dokumen spesifikasi kebutuhan sistem |
| *Stakeholder* | Pihak yang terdampak atau berkepentingan dengan proyek |
| *Transfer* | Strategi respons: mengalihkan dampak dan penanganan risiko ke pihak ketiga |
| UAT | *User Acceptance Testing*; uji penerimaan oleh pengguna atau sponsor |
| Uji ulang | Menguji kembali setelah *bug* diperbaiki, untuk memastikan perbaikan berhasil dan tidak merusak bagian lain |
| UPS | Catu daya cadangan berbaterai |
| VPS | *Virtual Private Server*; server sewaan di internet |
| VS Code | *Visual Studio Code*; aplikasi editor kode gratis |
| WBS | *Work Breakdown Structure*; pemecahan seluruh pekerjaan proyek secara bertingkat |
| *WBS Dictionary* | Kamus WBS; penjelasan rinci setiap elemen WBS |
| *Work package* | Elemen terbawah WBS yang bisa ditugaskan, diestimasi, dan dipantau |

# Daftar Pustaka

Badan Meteorologi, Klimatologi, dan Geofisika. (2026). *Peringatan dini cuaca*. Diakses 27 Oktober 2026, dari https://www.bmkg.go.id/cuaca/peringatan-dini-cuaca

Luthfi, E. T. (2026). *IT project management: Pertemuan 4* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Project Management Institute. (2008). *A guide to the project management body of knowledge (PMBOK® Guide)* (4th ed.). Project Management Institute.

Project Management Institute. (2021). *A guide to the project management body of knowledge (PMBOK® Guide)* (7th ed.). Project Management Institute.

Syafrizal, M. (2026a). *Project planning (core PMBOK): Pertemuan 6* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026b). *IT project management: Integrasi project plan* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

Syafrizal, M. (2026c). *Contoh usulan risk register (FIK 2026)* [Berkas spreadsheet]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.

<!-- LANDSCAPE -->

# Lampiran A. Kamus WBS

<!-- tabel: Tabel A.1 Kamus WBS | lebar: 6,18,44,24,8 -->
| Kode | Work package | Uraian | Hasil | PJ |
|---|---|---|---|---|
| **1.1** | **Manajemen Proyek** | | | |
| 1.1.1 | Project charter dan rencana proyek | Menyusun piagam proyek, WBS, jadwal, anggaran, Risk Register, dan rencana komunikasi | Project charter; rencana manajemen proyek | MP |
| 1.1.2 | Rapat dan laporan kemajuan | Rapat mingguan tim dan laporan kemajuan ke sponsor | Notulen; laporan mingguan | MP |
| 1.1.3 | Pengendalian perubahan dan pemantauan risiko | Menilai setiap permintaan perubahan; memperbarui Risk Register | *Change log*; Risk Register terbaru | MP |
| 1.1.4 | Penutupan proyek dan lessons learned | Evaluasi akhir dan pencatatan pelajaran | Laporan penutupan; dokumen lessons learned | MP |
| **1.2** | **Analisis Kebutuhan** | | | |
| 1.2.1 | Kebutuhan pemangku kepentingan | Wawancara BPBD/pemda dan perwakilan warga: wilayah prioritas, jam operasi, bentuk pesan | Catatan kebutuhan | AS |
| 1.2.2 | Studi halaman peringatan dini BMKG | Mengamati halaman per provinsi: cara penulisan wilayah, frekuensi pembaruan, tampilan saat tidak ada peringatan, tampilan peringatan yang belum mulai berlaku | Laporan studi halaman; daftar tautan provinsi | AS |
| 1.2.3 | Daftar wilayah sasaran dan variasi nama | Mendata wilayah sasaran, ejaan yang mungkin muncul, dan nama mirip yang harus ditolak | Daftar wilayah; daftar nama mirip | AS |
| 1.2.4 | Survei lokasi pemasangan | Mengecek listrik, sinyal, ketinggian pasang, keamanan, dan jarak pandang | Laporan survei per lokasi | TL |
| 1.2.5 | Spesifikasi kebutuhan sistem (SRS) | Merumuskan kebutuhan fungsional dan nonfungsional, termasuk kriteria penerimaan | Dokumen SRS | AS |
| **1.3** | **Desain Sistem** | | | |
| 1.3.1 | Arsitektur sistem | Rancangan hubungan server, MQTT broker, database, dasbor, dan perangkat | Diagram arsitektur | AS |
| 1.3.2 | Desain logika status peringatan | Aturan AKTIF / SELESAI / GAGAL MUAT, aturan 3 pengecekan, interval pengecekan | Diagram status dan aturannya | AS |
| 1.3.3 | Desain database wilayah dan perangkat | Struktur data wilayah, variasi nama, perangkat, riwayat status | Skema database | PS |
| 1.3.4 | Desain rangkaian perangkat keras | Skema board IoT, relay, panel LED, audio, catu daya, dan baterai cadangan | Skema rangkaian | EI |
| 1.3.5 | Desain pesan LED dan pola audio-lampu | Teks pesan, pola kedip lampu, pola bunyi sirene, dan jam senyap bila disepakati | Spesifikasi pesan dan pola | AS |
| 1.3.6 | Desain dasbor admin | Rancangan tampilan: status wilayah, status perangkat, mode uji, aktivasi peringatan manual, riwayat | *Mockup* dasbor | PS |
| **1.4** | **Pengadaan** | | | |
| 1.4.1 | Daftar komponen (BOM) | Board IoT **ESP32** (diprogram dengan C++ melalui PlatformIO), panel LED *outdoor*, lampu rotari, relay, speaker/amplifier, catu daya, baterai/UPS, modem 4G, *enclosure* tahan air, sensor arus dan tegangan | BOM dengan spesifikasi dan perkiraan harga | EI |
| 1.4.2 | Pemilihan pemasok dan pembelian komponen | Membandingkan pemasok, memesan, dan memeriksa barang datang | Komponen diterima; bukti pembelian | MP |
| 1.4.3 | Sewa server (VPS) dan domain | Memilih penyedia, menyewa, dan menyiapkan akses | Server siap pakai | PS |
| 1.4.4 | Izin pemasangan | Mengurus izin dari pemilik lokasi, kelurahan, atau pemda | Surat izin per lokasi | MP |
| 1.4.5 | Penyiapan alat pengembangan | Berlangganan Claude Code; memasang VS Code, PlatformIO, dan Python + Playwright di komputer tim; membuat repositori Git bersama | Alat siap pakai; repositori kode | PS |
| **1.5** | **Pengembangan Perangkat Lunak Server** | | | |
| 1.5.1 | Modul pemantau BMKG (Playwright) | Membuka halaman provinsi yang relevan secara berkala, mengambil teks halaman, dan memastikan halaman berhasil dimuat | Modul Python | PS |
| 1.5.2 | Modul pencocokan nama wilayah | Mencocokkan per kata utuh dengan variasi nama, menolak nama mirip | Modul Python | PS |
| 1.5.3 | Modul pengelola status peringatan | Menerapkan aturan AKTIF / SELESAI / GAGAL MUAT dan menyimpan riwayat | Modul Python | PS |
| 1.5.4 | Layanan pengirim perintah (MQTT) | Memasang MQTT broker; mengirim perintah nyala/mati ke topik wilayah | Broker dan modul pengirim | PS |
| 1.5.5 | Dasbor admin | Mengelola wilayah dan perangkat, melihat status, menyalakan mode uji, dan menyalakan peringatan secara manual bila pembacaan BMKG terganggu (rencana darurat risiko R-03) | Aplikasi web dasbor | PS |
| 1.5.6 | Pemantauan heartbeat dan notifikasi admin | Mendeteksi perangkat yang tidak mengirim heartbeat; memberi tahu admin | Modul pemantau dan notifikasi | PS |
| **1.6** | **Pengembangan Perangkat IoT** | | | |
| 1.6.1 | Perakitan prototipe | Merakit satu unit uji di meja kerja | 1 unit prototipe | EI |
| 1.6.2 | Firmware C++ | Koneksi jaringan, berlangganan topik MQTT, kendali panel LED, relay lampu, dan audio | Firmware versi 1 | EI |
| 1.6.3 | Fitur heartbeat dan sambung ulang otomatis | Mengirim heartbeat; menyambung ulang otomatis saat jaringan putus | Firmware versi akhir | EI |
| 1.6.4 | Fitur diagnosa jarak jauh | Perangkat melaporkan kondisi daya, koneksi, dan keluaran; admin dapat menjalankan uji diri dari dasbor | Firmware dengan fitur diagnosa | EI |
| 1.6.5 | Perakitan unit produksi | Merakit **6** unit di dalam *enclosure* tahan air | Unit siap pasang | EI |
| **1.7** | **Pengujian** | | | |
| 1.7.1 | Uji unit perangkat lunak | Menguji setiap modul server secara terpisah | Laporan uji unit | QA |
| 1.7.2 | Uji pencocokan nama wilayah | Menguji dengan daftar nama mirip (misalnya "Batu" vs "Batubara") dan nama di luar daftar peringatan | Laporan uji; 0 salah cocok | QA |
| 1.7.3 | Uji perangkat keras | Uji tahan air, panas, baterai cadangan ≥ 4 jam, dan keterbacaan LED di siang hari | Laporan uji perangkat keras | QA |
| 1.7.4 | Uji integrasi ujung ke ujung | Alur lengkap BMKG → server → perangkat, dengan halaman uji tiruan; memperbaiki *bug* yang ditemukan dan menguji ulang | Laporan uji; waktu ≤ 10 menit | QA |
| 1.7.5 | Uji kegagalan | Halaman BMKG tidak bisa diakses, internet perangkat putus, listrik padam; memperbaiki *bug* yang ditemukan dan menguji ulang | Laporan uji kegagalan | QA |
| 1.7.6 | Uji coba lapangan dan UAT | Menjalankan sistem di lokasi percontohan; diuji dan disetujui sponsor; termasuk perbaikan kecil yang diminta sponsor | Berita acara UAT | QA |
| **1.8** | **Pemasangan dan Peluncuran** | | | |
| 1.8.1 | Pemasangan perangkat di lokasi | Memasang unit, menyambung listrik dan jaringan, uji nyala di tempat | Unit terpasang dan berfungsi | TL |
| 1.8.2 | Deploy perangkat lunak server dan pengamanan dasar | Memasang semua modul ke server produksi; mengatur *firewall*, HTTPS, dan *backup* berkala | Server produksi berjalan dan aman | PS |
| 1.8.3 | Konfigurasi wilayah dan pendaftaran perangkat | Mendaftarkan setiap unit ke wilayah dan topiknya di dasbor | Data perangkat lengkap | PS |
| 1.8.4 | Sosialisasi ke warga | Menjelaskan arti pesan, lampu, dan bunyi; tindakan yang harus dilakukan warga | Materi sosialisasi; daftar hadir | MP |
| 1.8.5 | Pelatihan operator | Melatih petugas memakai dasbor, membaca tanda gangguan, dan mode uji | Daftar hadir; manual operator | AS |
| 1.8.6 | Serah terima dan dokumentasi | Menyerahkan sistem, kode, manual, dan SOP kepada sponsor | Berita acara serah terima | MP |

# Lampiran B. Tabel Aktivitas Jadwal

Baris tebal menandai aktivitas di jalur kritis. O = optimis, M = paling mungkin, P = pesimis; ES/EF = mulai/selesai paling awal; LS/LF = mulai/selesai paling lambat (hari kerja ke-).

<!-- tabel: Tabel B.1 Aktivitas, durasi, ketergantungan, dan float | lebar: 6,30,4,4,4,6,6,14,5,5,5,5,6 -->
| Kode | Aktivitas | O | M | P | PERT | Durasi | Pendahulu | ES | EF | LS | LF | Float |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1.1.1** | **Project charter dan rencana proyek** | 3 | 5 | 8 | 5,17 | **5** | – | 0 | 5 | 0 | 5 | **0** |
| **M1** | **◆ Proyek disahkan** | | | | | **0** | 1.1.1 | 5 | 5 | 5 | 5 | **0** |
| 1.4.5 | Penyiapan alat pengembangan | 1 | 2 | 3 | 2,00 | 2 | M1 | 5 | 7 | 37 | 39 | 32 |
| **1.2.1** | **Kebutuhan pemangku kepentingan** | 3 | 5 | 8 | 5,17 | **5** | M1 | 5 | 10 | 5 | 10 | **0** |
| 1.2.2 | Studi halaman peringatan dini BMKG | 2 | 3 | 5 | 3,17 | 3 | M1 | 5 | 8 | 10 | 13 | 5 |
| 1.2.3 | Daftar wilayah dan variasi nama | 2 | 3 | 4 | 3,00 | 3 | 1.2.1, 1.2.2 | 10 | 13 | 13 | 16 | 3 |
| **1.2.4** | **Survei lokasi pemasangan** | 3 | 5 | 10 | 5,50 | **6** | 1.2.1 | 10 | 16 | 10 | 16 | **0** |
| **1.2.5** | **Spesifikasi kebutuhan sistem (SRS)** | 3 | 5 | 7 | 5,00 | **5** | 1.2.3, 1.2.4 | 16 | 21 | 16 | 21 | **0** |
| **M2** | **◆ Kebutuhan disetujui sponsor** | | | | | **0** | 1.2.5 | 21 | 21 | 21 | 21 | **0** |
| 1.4.4 | Izin pemasangan | 10 | 15 | 30 | 16,67 | 17 | 1.2.4 | 16 | 33 | 53 | 70 | 37 |
| **1.3.1** | **Arsitektur sistem** | 2 | 3 | 5 | 3,17 | **3** | M2 | 21 | 24 | 21 | 24 | **0** |
| 1.3.2 | Desain logika status peringatan | 1 | 2 | 4 | 2,17 | 2 | 1.3.1 | 24 | 26 | 37 | 39 | 13 |
| 1.3.3 | Desain database | 1 | 2 | 3 | 2,00 | 2 | 1.3.1 | 24 | 26 | 34 | 36 | 10 |
| **1.3.4** | **Desain rangkaian perangkat keras** | 3 | 5 | 8 | 5,17 | **5** | 1.3.1 | 24 | 29 | 24 | 29 | **0** |
| 1.3.5 | Desain pesan LED dan pola audio-lampu | 1 | 2 | 3 | 2,00 | 2 | M2 | 21 | 23 | 37 | 39 | 16 |
| 1.3.6 | Desain dasbor admin | 2 | 3 | 5 | 3,17 | 3 | 1.3.3 | 26 | 29 | 36 | 39 | 10 |
| M3 | ◆ Desain disetujui | | | | | 0 | 1.3.2, 1.3.4, 1.3.5, 1.3.6 | 29 | 29 | 39 | 39 | 10 |
| **1.4.1** | **Daftar komponen (BOM)** | 1 | 2 | 3 | 2,00 | **2** | 1.3.4 | 29 | 31 | 29 | 31 | **0** |
| **1.4.2** | **Pemilihan pemasok dan pembelian komponen** | 7 | 10 | 20 | 11,17 | **11** | 1.4.1 | 31 | 42 | 31 | 42 | **0** |
| 1.4.3 | Sewa server (VPS) dan domain | 1 | 1 | 2 | 1,17 | 1 | 1.3.1 | 24 | 25 | 41 | 42 | 17 |
| 1.5.1 | Modul pemantau BMKG | 3 | 5 | 8 | 5,17 | 5 | M3, 1.4.5 | 29 | 34 | 39 | 44 | 10 |
| 1.5.2 | Modul pencocokan nama wilayah | 2 | 4 | 7 | 4,17 | 4 | 1.5.1 | 34 | 38 | 44 | 48 | 10 |
| 1.5.3 | Modul pengelola status peringatan | 2 | 3 | 5 | 3,17 | 3 | 1.5.2 | 38 | 41 | 48 | 51 | 10 |
| 1.5.4 | Layanan pengirim perintah (MQTT) | 2 | 3 | 5 | 3,17 | 3 | M3, 1.4.3 | 29 | 32 | 42 | 45 | 13 |
| 1.5.5 | Dasbor admin | 5 | 8 | 12 | 8,17 | 8 | 1.5.3, 1.5.4 | 41 | 49 | 51 | 59 | 10 |
| 1.5.6 | Pemantauan heartbeat dan notifikasi admin | 2 | 3 | 5 | 3,17 | 3 | 1.5.4 | 32 | 35 | 56 | 59 | 24 |
| **1.6.1** | **Perakitan prototipe** | 2 | 3 | 5 | 3,17 | **3** | 1.4.2, M3 | 42 | 45 | 42 | 45 | **0** |
| **1.6.2** | **Firmware C++** | 5 | 8 | 12 | 8,17 | **8** | 1.6.1, 1.5.4 | 45 | 53 | 45 | 53 | **0** |
| **1.6.3** | **Fitur heartbeat dan sambung ulang otomatis** | 2 | 3 | 5 | 3,17 | **3** | 1.6.2 | 53 | 56 | 53 | 56 | **0** |
| **1.6.4** | **Fitur diagnosa jarak jauh** | 3 | 4 | 7 | 4,33 | **4** | 1.6.3 | 56 | 60 | 56 | 60 | **0** |
| 1.7.1 | Uji unit perangkat lunak | 2 | 3 | 5 | 3,17 | 3 | 1.5.5, 1.5.6 | 49 | 52 | 59 | 62 | 10 |
| 1.7.2 | Uji pencocokan nama wilayah | 1 | 2 | 4 | 2,17 | 2 | 1.5.2 | 38 | 40 | 60 | 62 | 22 |
| **1.7.3** | **Uji perangkat keras** | 3 | 4 | 6 | 4,17 | **4** | 1.6.4 | 60 | 64 | 60 | 64 | **0** |
| **1.6.5** | **Perakitan unit produksi** | 4 | 6 | 9 | 6,17 | **6** | 1.7.3 | 64 | 70 | 64 | 70 | **0** |
| 1.8.2 | Deploy perangkat lunak server dan pengamanan dasar | 1 | 2 | 4 | 2,17 | 2 | 1.7.1, 1.7.2, 1.4.3 | 52 | 54 | 62 | 64 | 10 |
| **1.7.4** | **Uji integrasi ujung ke ujung** | 4 | 7 | 12 | 7,33 | **7** | 1.8.2, 1.7.3 | 64 | 71 | 64 | 71 | **0** |
| **1.7.5** | **Uji kegagalan** | 3 | 4 | 8 | 4,50 | **5** | 1.7.4 | 71 | 76 | 71 | 76 | **0** |
| **1.8.1** | **Pemasangan perangkat di lokasi** | 3 | 5 | 8 | 5,17 | **5** | 1.6.5, 1.4.4 | 70 | 75 | 70 | 75 | **0** |
| **1.8.3** | **Konfigurasi wilayah dan pendaftaran perangkat** | 1 | 1 | 2 | 1,17 | **1** | 1.8.1, 1.8.2 | 75 | 76 | 75 | 76 | **0** |
| **1.7.6** | **Uji coba lapangan dan UAT** | 5 | 10 | 15 | 10,00 | **10** | 1.8.3, 1.7.5 | 76 | 86 | 76 | 86 | **0** |
| **M4** | **◆ UAT disetujui sponsor** | | | | | **0** | 1.7.6 | 86 | 86 | 86 | 86 | **0** |
| 1.8.4 | Sosialisasi ke warga | 2 | 3 | 5 | 3,17 | 3 | 1.8.1 | 75 | 78 | 83 | 86 | 8 |
| 1.8.5 | Pelatihan operator | 1 | 2 | 3 | 2,00 | 2 | 1.8.3 | 76 | 78 | 84 | 86 | 8 |
| **1.8.6** | **Serah terima dan dokumentasi** | 2 | 3 | 5 | 3,17 | **3** | M4, 1.8.4, 1.8.5 | 86 | 89 | 86 | 89 | **0** |
| **M5** | **◆ Sistem diserahterimakan** | | | | | **0** | 1.8.6 | 89 | 89 | 89 | 89 | **0** |
| **1.1.4** | **Penutupan proyek dan lessons learned** | 2 | 3 | 4 | 3,00 | **3** | M5 | 89 | 92 | 89 | 92 | **0** |
| **M6** | **◆ Proyek ditutup** | | | | | **0** | 1.1.4 | 92 | 92 | 92 | 92 | **0** |
