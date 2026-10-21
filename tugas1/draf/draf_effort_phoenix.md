# Draf Laporan — Analisis Distribusi Effort Proyek: Phoenix Pay System (Kanada)

> Berkas kerja (draf). Hasil akhir: laporan .docx (min. 1000 kata) + diagram + slide.
> Status: Bagian 1–6 terisi (draf lengkap). Berikutnya: diagram → laporan .docx (dipadatkan ke ±1.500–2.000 kata) → slide.
> Aturan penulisan: setiap istilah asing/teknis dijelaskan singkat saat pertama kali muncul, lalu dikumpulkan di Glosarium.
> Rujukan "OAG 1.xx" = nomor paragraf laporan Auditor General Kanada (2018).

---

## 1. Pendahuluan

Laporan ini menganalisis bagaimana tenaga dan waktu (*effort*) sebuah proyek teknologi informasi (TI) yang nyata terbagi ke dalam lima kelompok proses manajemen proyek, lalu menilai apakah pembagian itu ikut menentukan keberhasilan atau kegagalan proyek.

Kasus yang dipilih adalah **Phoenix Pay System**, sistem penggajian (*payroll*, yaitu sistem yang menghitung dan membayarkan gaji pegawai) milik Pemerintah Kanada yang mulai dipakai pada 2016. Kasus ini dipilih karena tiga alasan:

1. **Terdokumentasi resmi dan independen.** Kantor Auditor General Kanada (OAG), lembaga pemeriksa keuangan negara yang setara dengan BPK di Indonesia, menerbitkan laporan audit lengkap tentang proyek ini pada 2018.
2. **Diperiksa memakai kerangka yang sama dengan materi kuliah.** OAG mencantumkan *PMBOK Guide* (buku panduan standar manajemen proyek dari Project Management Institute) sebagai salah satu kriteria audit.
3. **Memuat data konkret** tentang pemangkasan lingkup pekerjaan, pengujian, jadwal, dan jumlah staf, yang menjadi bahan utama analisis *effort*.

---

## 2. Landasan Teori

### 2.1 Lima kelompok proses (*process group*) — PMBOK edisi ke-4

PMBOK edisi ke-4 (PMI, 2008) mengelompokkan kegiatan manajemen proyek ke dalam lima *process group* (kelompok proses):

| Process group | Arti |
|---|---|
| **Initiating** (inisiasi) | Memutuskan dan mengesahkan dimulainya proyek: tujuan, kebutuhan awal, dan pihak-pihak yang berkepentingan (*stakeholder*, yaitu semua orang atau organisasi yang terdampak proyek). |
| **Planning** (perencanaan) | Menyusun rencana lingkup, jadwal, biaya, mutu, risiko, dan pengadaan. |
| **Executing** (pelaksanaan) | Mengerjakan pekerjaan sesuai rencana. |
| **Monitoring & Controlling** (pemantauan dan pengendalian) | Memantau kemajuan, menguji hasil, mengendalikan perubahan dan risiko, serta mengambil tindakan perbaikan. |
| **Closing** (penutupan) | Menyerahkan hasil, menutup kontrak, dan mencatat pelajaran (*lessons learned*). |

Hal penting dari PMBOK dan materi kuliah Pertemuan 4: kelima kelompok ini **bukan tahap berurutan**. Mereka tumpang tindih sepanjang proyek, dan *Monitoring & Controlling* berlangsung dari awal sampai akhir, bukan baru dimulai setelah *Executing* selesai (PMBOK 4, Gambar 3-2; slide Pertemuan 4).

PMBOK juga menjelaskan bahwa biaya untuk mengubah rancangan atau memperbaiki kesalahan **makin mahal menjelang akhir proyek** (PMBOK 4, Gambar 2-2). Karena itu, kelemahan yang baru ditemukan setelah sistem dipakai menimbulkan kerugian paling besar.

### 2.2 Patokan distribusi waktu: Crowe (2006)

Materi kuliah Pertemuan 4 menyajikan data survei Crowe (2006) tentang persentase waktu yang dipakai manajer proyek untuk setiap *process group*. "Manajer proyek Alpha" adalah sekitar 2% manajer proyek terbaik menurut penilaian para *stakeholder*.

| Process group | Manajer proyek Alpha | Manajer proyek lain |
|---|---|---|
| Initiating | 2% | 1% |
| Planning | 21% | 11% |
| Executing | 69% | 82% |
| Monitoring & Controlling | 5% | 4% |
| Closing | 3% | 2% |

**Catatan kritis** (sebagian juga dicatat di slide dosen):
- Data ini hasil survei, sehingga hanya menunjukkan **hubungan**, bukan bukti sebab-akibat.
- Data ini mengukur **waktu manajer proyek**, bukan *effort* seluruh tim proyek. Dalam laporan ini, data Crowe dipakai sebagai **pembanding pola** (misalnya porsi *Planning* yang tipis), bukan sebagai angka pasti.

### 2.3 Pendekatan pengembangan: *predictive*, *hybrid*, *adaptive* — PMBOK edisi ke-7

PMBOK edisi ke-7 (PMI, 2021) menggambarkan cara mengerjakan proyek sebagai sebuah **spektrum**:

- **Predictive** (dikenal juga sebagai **Waterfall**): proyek dikerjakan tahap demi tahap secara berurutan (analisis kebutuhan → desain → pembangunan → pengujian → peluncuran). Rencana lengkap dibuat di awal, perubahan sulit, dan pengguna baru melihat hasilnya di akhir. Cocok bila kebutuhan jelas dan stabil, regulasinya ketat, atau risikonya tinggi.
- **Adaptive** (dikenal juga sebagai **Agile**): proyek dibagi menjadi siklus pendek 1–4 minggu (disebut iterasi atau *sprint*). Di setiap siklus, sebagian fitur dirancang, dibuat, diuji, lalu ditunjukkan kepada pengguna untuk mendapat masukan. Cocok bila kebutuhan belum jelas atau sering berubah.
- **Hybrid** (campuran): sebagian pekerjaan dikerjakan secara *predictive*, sebagian lagi secara *adaptive* atau bertahap. Contohnya, infrastruktur direncanakan lengkap di awal, sedangkan fitur diluncurkan bertahap.

PMBOK 7 (Bagian 2.3.4) menyebut faktor-faktor untuk memilih pendekatan, antara lain kepastian kebutuhan, stabilitas lingkup, **opsi pengiriman** (apakah hasil bisa diserahkan bertahap), risiko, regulasi, keterlibatan *stakeholder*, serta ukuran dan lokasi tim.

---

## 3. Studi Kasus: Phoenix Pay System

### 3.1 Latar belakang

- Pada 2009, Pemerintah Kanada memulai inisiatif untuk mengganti sistem penggajian berusia 40 tahun yang membayar sekitar **290.000 pegawai di 101 instansi**, dengan total gaji sekitar $22 miliar per tahun (OAG 1.1).
- Inisiatif ini terdiri dari dua proyek: memusatkan petugas penggajian 46 instansi ke satu **Pay Centre** (pusat layanan gaji) di Miramichi, dan mengganti *software* (perangkat lunak) gaji untuk seluruh instansi (OAG 1.2).
- Anggaran inisiatif $310 juta, termasuk **$155 juta** untuk membangun dan menerapkan *software* baru. Pemerintah berharap menghemat sekitar **$70 juta per tahun** mulai tahun anggaran 2016–2017, terutama dengan mengurangi sekitar 1.200 posisi petugas gaji menjadi 550 posisi di Miramichi (OAG 1.2–1.3).
- Penanggung jawab proyek adalah Kementerian Public Services and Procurement Canada (PSPC). Pada Juni 2011, PSPC mengontrak **IBM** sebagai kontraktor (perusahaan yang dibayar untuk merancang dan membangun sistem). Sistemnya dibangun dari **PeopleSoft**, *software* penggajian siap pakai yang dikustomisasi, yaitu diubah supaya sesuai aturan gaji pemerintah Kanada. Sistem ini diberi nama Phoenix (OAG 1.5).

### 3.2 Lini waktu (OAG Exhibit 1.1)

| Waktu | Peristiwa |
|---|---|
| Musim semi 2009 | PSPC menyusun usulan awal dan *business case* (dokumen yang menjelaskan alasan, biaya, dan manfaat proyek) |
| Juni–Oktober 2010 | Tender terbuka (*request for proposals*) untuk mencari kontraktor |
| Juni 2011 | Kontrak dengan IBM |
| Musim semi 2012 | Setelah tahap perencanaan, IBM memperkirakan biaya **$274 juta**, hampir dua kali anggaran $155 juta (OAG 1.32) |
| Desember 2012 | Pendanaan disetujui, tahap implementasi (pembangunan sistem) dimulai |
| Juni 2015 | **Uji coba (*pilot*) dengan satu instansi dibatalkan** |
| 27 Januari 2016 | Tinjauan kesiapan oleh konsultan S.i. Systems selesai |
| 29 Januari 2016 | Penjelasan kesiapan kepada lebih dari 30 deputi menteri |
| 11 Februari 2016 | Laporan Gartner (perusahaan konsultan TI) tentang kesiapan instansi selesai |
| 15 Februari 2016 | Rencana kontinjensi (rencana cadangan bila sistem bermasalah) dibagikan ke instansi |
| 18 Februari 2016 | Wakil menteri PSPC diberi penjelasan bahwa sistem siap |
| 24 Februari 2016 | **Gelombang 1**: 34 instansi mulai memakai Phoenix |
| 21 April 2016 | **Gelombang 2**: 67 instansi sisanya |

### 3.3 Apa yang terjadi

- Sejak diluncurkan, banyak pegawai tidak menerima gaji dengan benar atau tepat waktu. Pada 30 Juni 2017, nilai gaji yang salah atau tertunda **lebih dari $520 juta**. Sekitar **51% pegawai** menerima slip gaji yang salah pada April 2017, dan permintaan perbaikan gaji yang belum diproses mencapai **lebih dari 494.500** (OAG 1.7).
- OAG menyimpulkan bahwa pembangunan dan penerapan Phoenix adalah "*an incomprehensible failure of project management and oversight*", yaitu kegagalan manajemen proyek dan pengawasan yang sulit dipahami (OAG 1.24, 1.105).

### 3.4 Temuan utama audit

1. **Lingkup dipangkas supaya muat anggaran.** Ketika perkiraan biaya hampir dua kali anggaran, PSPC tidak meminta tambahan dana. Sebagai gantinya, PSPC menghapus atau menunda **lebih dari 100 fungsi gaji penting** (misalnya pembayaran gaji rapel, yaitu selisih gaji yang dibayar mundur), mengurangi pengujian, **memadatkan jarak antargelombang dari 7 bulan menjadi 2 bulan**, dan mengurangi jumlah staf IBM dan PSPC (OAG 1.32–1.33). Manfaat yang dijanjikan tidak dihitung ulang (OAG 1.35).
2. **Pengujian tidak lengkap.** Dari 111 fungsi yang diperiksa auditor, 30 tidak ada saat peluncuran. Dari 81 sisanya, **20% gagal uji dan tidak diuji ulang**. Sistem juga tidak pernah diuji secara utuh (OAG 1.36–1.38).
3. **Uji coba dibatalkan.** Uji coba dengan satu instansi dibatalkan pada Juni 2015 karena cacat besar, dan tidak dijadwalkan ulang supaya tanggal peluncuran tetap. Dampak pembatalannya tidak dinilai (OAG 1.39–1.40).
4. **Asumsi produktivitas tidak diuji.** Penghematan $70 juta bergantung pada asumsi bahwa setiap petugas gaji mampu menangani 200 berkas, lalu 400 berkas setelah Phoenix. Pada Juli 2015 sudah diketahui mereka hanya mampu sekitar 150 berkas, tetapi asumsi tidak diubah (OAG 1.69–1.72).
5. **Peringatan diabaikan.** Laporan Gartner menilai risiko kritis bahwa gaji tidak bisa dibayar akurat, dan menyarankan **peluncuran bertahap mulai dari instansi yang sederhana serta menjalankan sistem lama dan baru secara paralel**. Saran ini tidak dipertimbangkan sebelum peluncuran (OAG 1.76–1.78).
6. **Tinjauan kesiapan tidak independen.** Tinjauan oleh S.i. Systems dilakukan sebelum pengujian selesai, daftar narasumbernya disetujui tim proyek sendiri, dan kesimpulannya ("siap") bertentangan dengan temuannya sendiri (OAG 1.80–1.82).
7. **Tidak ada pengawasan independen.** Informasi ke wakil menteri hanya datang dari tiga eksekutif proyek. Audit internal yang sudah direncanakan empat kali tidak pernah dilakukan (OAG 1.84–1.95).
8. **Keputusan peluncuran tidak didokumentasikan.** Para eksekutif sudah mengetahui masalah serius, tetapi tidak menyampaikannya kepada wakil menteri, dan keputusan *go-live* (mulai memakai sistem secara resmi) tidak pernah dicatat (OAG 1.97–1.102).
9. **Rencana cadangan lemah.** Rencana kontinjensi disusun kurang dari dua minggu sebelum peluncuran, tidak diuji, dan instansi diminta membuat rencana sendiri kurang dari seminggu sebelum peluncuran (OAG 1.46–1.47). Tidak ada rencana pembaruan PeopleSoft (OAG 1.45).

---

## 4. Analisis Distribusi Effort

### 4.1 Cara memperkirakan

Tidak ada dokumen resmi yang mencatat jumlah jam kerja proyek Phoenix per *process group*. Karena itu, distribusi *effort* diperkirakan dengan tiga langkah:

1. **Memetakan setiap temuan audit OAG ke *process group*-nya**, memakai Tabel 3-1 PMBOK 4. Contoh: pengujian termasuk proses *Perform Quality Control*, sehingga masuk *Monitoring & Controlling*.
2. **Mencatat indikator kuantitatif**, yaitu angka dari laporan OAG yang menunjukkan apakah sebuah *process group* ditambah atau dikurangi.
3. **Membandingkan polanya dengan data Crowe (2006)** dari slide dosen.

Supaya bisa dibandingkan dengan Crowe, perkiraan ini memakai sudut pandang yang sama, yaitu **porsi perhatian dan waktu manajemen proyek**, bukan total jam kerja seluruh *programmer* (pembuat program) dan penguji.

### 4.2 Indikator kuantitatif dari laporan OAG

| Indikator | Nilai | Process group terdampak |
|---|---|---|
| Selisih perkiraan biaya vs anggaran | $274 juta vs $155 juta (+77%); **tidak ada perencanaan ulang**, lingkup dipangkas (OAG 1.32) | Planning |
| Fungsi gaji yang dihapus/ditunda | **Lebih dari 100** (OAG 1.33) | Planning (lingkup), Executing |
| Fungsi gagal uji yang tidak diuji ulang | **20%** dari 81 fungsi yang diperiksa (OAG 1.37) | Monitoring & Controlling |
| Pengujian sistem secara utuh | **Tidak dilakukan** (OAG 1.38) | Monitoring & Controlling |
| Uji coba (*pilot*) | **Dibatalkan**, tidak dijadwalkan ulang (OAG 1.40) | Monitoring & Controlling |
| Menjalankan sistem lama dan baru bersamaan (*parallel run*) | **Tidak dilakukan**, padahal disarankan Gartner (OAG 1.77) | Monitoring & Controlling |
| Jarak gelombang 1 ke gelombang 2 | **Dipadatkan dari 7 menjadi 2 bulan** (−71%) (OAG 1.32) | Closing fase 1, Monitoring & Controlling |
| Audit internal | **0 dari 4** yang direncanakan (OAG 1.95) | Monitoring & Controlling |
| Pengawasan independen di luar tim proyek | **Tidak ada** (OAG 1.84–1.91) | Monitoring & Controlling |
| Rencana kontinjensi | Disusun **< 2 minggu** sebelum peluncuran, tidak diuji (OAG 1.46) | Planning |
| Keputusan *go-live* | **Tidak didokumentasikan** (OAG 1.102) | Closing / *phase gate* |

### 4.3 Estimasi distribusi effort Phoenix

| Process group | Crowe: PM Alpha | Crowe: PM lain | **Phoenix (estimasi)** | Alasan |
|---|---|---|---|---|
| Initiating | 2% | 1% | **2%** | *Business case* ada sejak 2009. Masalahnya pada **mutu**, bukan jumlah: penghematan $70 juta bertumpu pada asumsi produktivitas yang tidak pernah diuji, dan instansi pengguna tidak dilibatkan. |
| Planning | 21% | 11% | **~8%** | Ada tahap perencanaan (2011–2012), tetapi ketika biaya 77% di atas anggaran, rencana **tidak disusun ulang**; lingkup dipangkas. Manfaat tidak dihitung ulang, rencana kontinjensi dibuat di menit terakhir, tidak ada rencana pembaruan *software*. |
| Executing | 69% | 82% | **~86%** | *Effort* terpusat pada membangun dan mengkustomisasi sistem, memindahkan data, dan memusatkan petugas gaji ke Miramichi. Jadwal dan anggaran dipertahankan dengan mengorbankan proses lain. |
| Monitoring & Controlling | 5% | 4% | **~3%** | Uji coba dibatalkan, pengujian tidak utuh, *parallel run* tidak dilakukan, audit internal tidak pernah dilakukan, tinjauan kesiapan tidak independen, informasi ke atasan hanya dari tim proyek. |
| Closing | 3% | 2% | **~1%** | Tidak ada evaluasi akhir fase (*phase-end review*) yang berarti antara gelombang 1 dan 2; gelombang 2 tetap berjalan dua bulan kemudian walaupun masalah sudah muncul. Keputusan *go-live* tidak dicatat. |

**Catatan kejujuran:** angka Phoenix adalah **estimasi penulis**, bukan data terukur. Yang dapat dipertanggungjawabkan adalah **arah dan polanya**, yang didukung bukti di 4.2. Bila setiap angka digeser ±3 poin, kesimpulannya tetap: *Planning* dan *Monitoring & Controlling* jauh di bawah pola manajer proyek terbaik.

### 4.4 Apakah distribusinya timpang? Ya, dalam tiga hal

**1. Planning terlalu kecil dan hanya di awal.** PMBOK menyatakan *process group* berulang; ketika kondisi berubah (biaya naik 77%), perencanaan seharusnya diulang. Di Phoenix, satu-satunya respons adalah memangkas lingkup. Pola ini mirip "PM lain" di data Crowe (Planning 11%), bahkan lebih rendah.

**2. Monitoring & Controlling dipangkas tepat ketika paling dibutuhkan.** Dari tiga kendala proyek (*triple constraint*: lingkup, waktu, biaya), waktu dan biaya dikunci, sehingga yang dikorbankan adalah lingkup dan **mutu**. Mutu dijaga oleh proses *Monitoring & Controlling*: pengujian, uji coba, dan pengawasan. Menurut PMBOK 4 Gambar 2-2, biaya memperbaiki kesalahan makin mahal menjelang akhir proyek, dan kesalahan yang lolos ke peluncuran paling mahal. Phoenix membuktikannya: lebih dari $520 juta gaji salah atau tertunda dalam setahun.

**3. Closing antarfase tidak berfungsi sebagai titik kendali.** PMBOK 4 Bab 2.1 menyebut akhir fase sebagai *phase gate* atau *kill point*, yaitu titik untuk memutuskan lanjut, menunda, atau berhenti. Memadatkan jarak antargelombang dari 7 menjadi 2 bulan menghapus kesempatan itu.

**Kesimpulan:** ketimpangan distribusi *effort* (*Executing* terlalu dominan) adalah salah satu faktor utama kegagalan Phoenix. Yang lebih penting dari persentasenya adalah **waktu dan mutu** *effort* itu: *Planning* tidak diulang saat dibutuhkan, dan *Monitoring & Controlling* dipangkas tepat sebelum peluncuran.

### 4.5 Diagram

1. **Diagram 1 — grafik batang berkelompok:** lima *process group* × tiga data (PM Alpha, PM lain, Phoenix estimasi).
2. **Diagram 2 — lini waktu proyek 2009–2016:** tonggak utama (Exhibit 1.1 OAG) dan tanda pada titik kendali yang dihilangkan: perencanaan ulang 2012 (tidak dilakukan), uji coba Juni 2015 (dibatalkan), *parallel run* (tidak dilakukan), jarak antargelombang 2016 (7 → 2 bulan), keputusan *go-live* (tidak dicatat).
## 5. Perbandingan Waterfall vs Agile

### 5.1 Pendekatan yang dipakai Phoenix

Phoenix dikerjakan dengan pendekatan **predictive (Waterfall)**: *business case* dan anggaran ditetapkan di awal, IBM dikontrak, sistem dibangun lengkap, lalu diluncurkan ke 101 instansi dalam **dua gelombang besar**. Pembagian dua gelombang itu sebenarnya sudah merupakan peluncuran bertahap, tetapi tanpa jeda dan evaluasi yang memadai di antaranya.

### 5.2 Perbedaan distribusi effort

| Process group | Phoenix (aktual) | Waterfall yang dijalankan dengan benar | Agile |
|---|---|---|---|
| **Initiating** | Sekali di awal; asumsi tidak diuji | Sekali di awal; **asumsi manfaat diuji** sebelum proyek disahkan | Visi produk di awal, lalu ditinjau berkala |
| **Planning** | Di awal saja; tidak diulang saat biaya naik 77% | **Besar di awal** (±21% seperti PM Alpha) dan **diulang** bila kondisi berubah besar | **Kecil di awal, lalu sedikit-sedikit di setiap siklus**; daftar kebutuhan (*backlog*) diprioritaskan ulang terus |
| **Executing** | Dominan (~86%) | Besar di tengah proyek (±69%) | Tersebar di setiap siklus |
| **Monitoring & Controlling** | Dipangkas di akhir (~3%) | Pengujian lengkap, uji coba, dan *parallel run* sebelum peluncuran | **Di setiap siklus**: pengujian dan demo ke pengguna setiap 1–4 minggu |
| **Closing** | Hampir tidak ada antargelombang | *Phase gate* formal di akhir setiap fase | Evaluasi kecil di setiap siklus (*retrospective*) + penutupan akhir |

Kolom Waterfall dan Agile sengaja tidak diberi persentase selain patokan Crowe, karena tidak ada data pendukung untuk angka Agile.

**Intinya:** Waterfall **menumpuk** *Planning* di awal dan *Monitoring & Controlling* menjelang peluncuran. Karena menumpuk di akhir, *Monitoring & Controlling* menjadi bagian yang paling mudah dipangkas ketika jadwal terdesak, dan itulah yang terjadi di Phoenix. Agile **menyebar** keduanya di setiap siklus, sehingga tidak ada satu titik besar yang bisa dipangkas sekaligus.

### 5.3 Mana yang lebih cocok? Faktor PMBOK 7 (Bagian 2.3.4)

| Faktor | Kondisi Phoenix | Arah pendekatan |
|---|---|---|
| Kepastian kebutuhan | Aturan gaji pemerintah banyak dan rumit; instansi pengguna tidak diajak menyusun kebutuhan (OAG 1.54) | Adaptive |
| Kemudahan perubahan | Setelah gaji dibayar dengan sistem baru, kesalahan sulit dan mahal diperbaiki | Predictive |
| **Opsi pengiriman** | Bisa diluncurkan **per instansi**, mulai dari yang aturan gajinya sederhana (saran Gartner, OAG 1.77) | **Bertahap (*incremental*)** |
| Risiko | Sangat tinggi: gaji 290.000 orang | Perencanaan matang di awal **dan** peluncuran bertahap |
| Regulasi | Kebijakan keamanan, privasi, dan pengelolaan proyek pemerintah | Predictive (butuh dokumentasi) |
| Keterlibatan *stakeholder* | 101 instansi; Agile menuntut pengguna terlibat terus | Adaptive memaksa pelibatan yang justru tidak ada di Phoenix |
| Struktur dan budaya organisasi | Birokrasi pemerintah yang hierarkis | Predictive |
| Ukuran dan lokasi tim | Besar: PSPC, IBM, Shared Services Canada | Predictive, atau Agile yang diperbesar skalanya |

**Kesimpulan:** faktor-faktornya tidak menunjuk ke satu ujung spektrum. Pendekatan paling tepat untuk Phoenix adalah **hybrid**:

- **Predictive** untuk fondasi: aturan gaji inti, integrasi dengan sistem kepegawaian, keamanan, dan privasi, direncanakan lengkap bersama instansi pengguna.
- **Bertahap (*incremental*)** untuk peluncuran: mulai dari beberapa instansi dengan aturan gaji sederhana, disertai *parallel run* dengan sistem lama, dan *phase gate* sebelum setiap gelombang berikutnya.
- **Adaptive** untuk fungsi yang kebutuhannya paling tidak pasti (misalnya gaji rapel dan tunjangan jabatan sementara), dikembangkan dalam siklus pendek bersama petugas gaji sebagai pengguna.

Pilihan ini sejalan dengan contoh *hybrid* pada slide dosen (sistem informasi rumah sakit) dan dengan rekomendasi Gartner yang diabaikan.

### 5.4 Catatan kritis: Agile bukan obat untuk semua masalah Phoenix

Beberapa masalah terbesar Phoenix adalah masalah **tata kelola** (*governance*, yaitu siapa yang mengawasi dan siapa yang berwenang memutuskan), yang tidak otomatis selesai dengan mengganti pendekatan: wakil menteri hanya menerima informasi dari tim proyek (OAG 1.84–1.91), audit internal tidak pernah dilakukan (OAG 1.95), dan keputusan *go-live* tidak dicatat (OAG 1.102). Proyek Agile pun dapat gagal bila hasil setiap siklus dilaporkan keliru ke atasan. Pilihan pendekatan perlu dibarengi **pengawasan independen**.

## 6. Rekomendasi

Rekomendasi disusun per *process group* agar terlihat bagian distribusi *effort* mana yang diperbaiki. Setiap rekomendasi dibuat konkret dan dapat diperiksa.

### 6.1 Rekomendasi per *process group*

| No | Process group | Rekomendasi | Masalah Phoenix yang dijawab |
|---|---|---|---|
| 1 | **Initiating** | **Uji asumsi manfaat sebelum proyek disahkan.** Angka penghematan harus didasarkan pada data nyata, misalnya produktivitas petugas gaji yang diukur langsung, bukan perkiraan. | Asumsi 200 → 400 berkas per petugas tidak pernah diuji (OAG 1.69–1.72) |
| 2 | **Initiating** | **Libatkan instansi pengguna dalam komite pengarah** (*steering committee*, yaitu komite pimpinan yang mengarahkan dan mengawasi proyek) sejak awal. | Deputi menteri instansi lain tidak punya peran dalam tata kelola (OAG 1.92) |
| 3 | **Planning** | **Tetapkan aturan perencanaan ulang.** Bila perkiraan biaya atau jadwal menyimpang melebihi batas tertentu (sebagai contoh, 10–20%; batas pastinya ditetapkan organisasi), rencana wajib disusun ulang dan dilaporkan ke pihak yang menyetujui anggaran, bukan diatasi diam-diam dengan memangkas lingkup. | Biaya +77% diatasi dengan memangkas lebih dari 100 fungsi tanpa melapor ke Treasury Board (OAG 1.25, 1.32) |
| 4 | **Planning** | **Siapkan dan uji rencana kontinjensi serta rencana pemulihan berbulan-bulan sebelum peluncuran.** | Rencana kontinjensi dibuat < 2 minggu sebelum peluncuran dan tidak diuji (OAG 1.46) |
| 5 | **Executing** | **Latih pengguna dengan sistem yang sesungguhnya**, bukan presentasi umum. | Pelatihan generik, tanpa versi demo sistem (OAG 1.59) |
| 6 | **Monitoring & Controlling** | **Jadikan pengujian utuh, uji coba, dan *parallel run* syarat yang tidak boleh dipangkas** tanpa persetujuan pihak independen. | Uji coba dibatalkan, pengujian tidak utuh, *parallel run* tidak dilakukan (OAG 1.38–1.40, 1.77) |
| 7 | **Monitoring & Controlling** | **Adakan pengawasan independen yang melapor langsung ke pimpinan**: audit internal dan tinjauan kesiapan oleh pihak yang tidak berada di bawah tim proyek. | Informasi hanya dari tim proyek; 0 dari 4 audit internal; tinjauan kesiapan tidak independen (OAG 1.81–1.95) |
| 8 | **Closing (*phase gate*)** | **Catat keputusan *go/no-go* secara tertulis** dengan kriteria yang jelas dan nama pengambil keputusan; beri **masa stabilisasi minimum** dan evaluasi sebelum gelombang berikutnya. | Keputusan *go-live* tidak dicatat; jarak antargelombang dipadatkan 7 → 2 bulan (OAG 1.32, 1.102) |

### 6.2 Rekomendasi untuk distribusi effort

- **Lindungi porsi *Planning* dan *Monitoring & Controlling* dalam anggaran dan jadwal**, dengan alokasi tersendiri yang tidak boleh dipakai untuk menutup kekurangan *Executing*.
- **Jadikan pola manajer proyek Alpha sebagai acuan**: porsi *Planning* sekitar 20% lebih dekat dengan pola manajer proyek terbaik menurut Crowe (2006) dibanding 8–11%, dengan catatan bahwa data Crowe bersifat korelasional.
- **Sebarkan *Monitoring & Controlling* sepanjang proyek** melalui pendekatan *hybrid* (Bagian 5.3), sehingga tidak menumpuk di akhir dan mudah dipangkas.

### 6.3 Pola serupa di kasus lain

- **TSB Bank (Inggris, 2018).** Menurut *Final Notice* regulator FCA (2022), jadwal migrasi disusun mundur dari tanggal target (*right-to-left planning*), tahap pengujian dipadatkan, dan surat kesiapan dari pemasok berisi niat, bukan bukti.
- **Coretax DJP (Indonesia, 2025).** Materi kuliah Pertemuan 4 mencatat kendala *login* dan penerbitan faktur pajak pada minggu pertama, ketika banyak wajib pajak langsung bertransaksi nyata secara serentak. Hal ini menunjukkan pentingnya uji beban (*load testing*) dan peluncuran bertahap untuk sistem nasional.

Bagi proyek TI pemerintah di Indonesia, misalnya modernisasi layanan publik atau peralihan sistem observasi di BMKG, pelajarannya sama: **tanggal peluncuran tidak boleh lebih kuat daripada bukti kesiapan.**

---

## Glosarium

| Istilah | Penjelasan |
|---|---|
| *Effort* | Jumlah tenaga dan waktu yang dicurahkan untuk suatu pekerjaan |
| *Process group* | Kelompok proses manajemen proyek menurut PMBOK: Initiating, Planning, Executing, Monitoring & Controlling, Closing |
| PMBOK Guide | *A Guide to the Project Management Body of Knowledge*, buku panduan standar manajemen proyek dari Project Management Institute (PMI) |
| *Stakeholder* | Orang atau organisasi yang terdampak atau berkepentingan dengan proyek |
| *Payroll* | Sistem yang menghitung dan membayarkan gaji pegawai |
| *Software* | Perangkat lunak, yaitu program komputer |
| Kustomisasi | Mengubah *software* siap pakai supaya sesuai kebutuhan khusus |
| Kontraktor | Perusahaan yang dibayar untuk mengerjakan bagian proyek |
| *Business case* | Dokumen yang menjelaskan alasan, biaya, dan manfaat sebuah proyek |
| Tender (*request for proposals*) | Proses terbuka untuk memilih kontraktor berdasarkan penawaran |
| Uji coba (*pilot*) | Menjalankan sistem baru di lingkungan terbatas sebelum dipakai seluruhnya |
| Rencana kontinjensi | Rencana cadangan bila sistem bermasalah |
| *Go-live* | Saat sistem baru mulai dipakai secara resmi |
| Gaji rapel | Selisih gaji yang dibayarkan mundur, misalnya setelah kenaikan pangkat |
| Auditor General (OAG) | Lembaga pemeriksa keuangan dan kinerja pemerintah Kanada, setara BPK di Indonesia |
| Predictive / Waterfall | Pendekatan proyek berurutan dengan rencana lengkap di awal |
| Adaptive / Agile | Pendekatan proyek dalam siklus pendek dengan umpan balik pengguna di setiap siklus |
| Hybrid | Campuran pendekatan *predictive* dan *adaptive* |
| Iterasi / *sprint* | Satu siklus kerja pendek (1–4 minggu) dalam pendekatan Agile |
| *Lessons learned* | Catatan pelajaran dari proyek untuk dipakai di proyek berikutnya |
| *Programmer* | Orang yang menulis program komputer |
| *Triple constraint* | Tiga kendala utama proyek yang saling memengaruhi: lingkup, waktu, dan biaya; mengunci dua di antaranya membuat yang ketiga (atau mutu) yang dikorbankan |
| *Phase gate* / *kill point* | Titik evaluasi di akhir sebuah fase untuk memutuskan proyek lanjut, ditunda, atau dihentikan |
| *Parallel run* | Menjalankan sistem lama dan sistem baru bersamaan untuk sementara, lalu membandingkan hasilnya sebelum sistem lama dimatikan |
| Audit internal | Pemeriksaan oleh unit pemeriksa di dalam organisasi sendiri yang melapor langsung ke pimpinan, terpisah dari tim proyek |
| *Backlog* | Daftar kebutuhan atau fitur yang diurutkan berdasarkan prioritas dalam pendekatan Agile |
| *Retrospective* | Evaluasi cara kerja tim di akhir setiap siklus Agile |
| *Incremental* (bertahap) | Hasil proyek diserahkan sedikit demi sedikit, setiap tahap menambah fungsi atau pengguna |
| Tata kelola (*governance*) | Pengaturan siapa yang mengawasi proyek dan siapa yang berwenang mengambil keputusan |
| *Steering committee* (komite pengarah) | Komite pimpinan yang mengarahkan dan mengawasi proyek |
| Keputusan *go/no-go* | Keputusan resmi apakah sistem boleh mulai dipakai (*go*) atau ditunda (*no-go*) |
| *Right-to-left planning* | Menyusun jadwal mundur dari tanggal target yang sudah ditetapkan, bukan dari perkiraan pekerjaan yang dibutuhkan |
| Uji beban (*load testing*) | Pengujian apakah sistem tetap berjalan saat dipakai banyak pengguna sekaligus |
| *Perform Quality Control* | Proses dalam PMBOK 4 untuk memeriksa apakah hasil pekerjaan memenuhi standar mutu, misalnya melalui pengujian |

---

## Daftar Pustaka (sementara — final lewat Mendeley, APA 7)

- Crowe, A. (2006). *Alpha project managers: What the top 2% know that everyone else does not*. Velociteach. *(dikutip melalui slide Pertemuan 4)*
- Office of the Auditor General of Canada. (2018). *Report 1—Building and implementing the Phoenix pay system* (2018 Spring Reports of the Auditor General of Canada). https://www.oag-bvg.gc.ca/internet/English/parl_oag_201805_01_e_43033.html
- Project Management Institute. (2008). *A guide to the project management body of knowledge (PMBOK® Guide)* (4th ed.). Project Management Institute.
- Project Management Institute. (2021). *A guide to the project management body of knowledge (PMBOK® Guide)* (7th ed.). Project Management Institute.
- Luthfi, E. T. (2026). *IT project management: Pertemuan 4* [Slide perkuliahan]. Program Studi S2 Informatika, Universitas Amikom Yogyakarta.
