# Draf RTM#1 Literature Review — IT Project Management

> Berkas kerja. Bukan untuk dikumpulkan. Hasil akhir dibuat dalam .docx sesuai template.
> "Hal." = nomor halaman PDF (sesuai penampil PDF) di folder `article-pdf/`.

## Topik

**Manajemen Risiko dan Verifikasi Kesiapan pada Transisi Observasi Meteorologi Manual ke Automatic Weather Station (AWS)**

---

## Tabel Literature Review

### Paper 1 — `article-pdf/P1-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 1 |
| **Title** | Continuity of daily temperature time series in the transition from conventional to automated stations for the Colombian coffee network |
| **Author** | Ramírez Carabalí, Sarmiento Herrera, Imbachi Quinchua, & García López (2022) |
| **Quartile** | Q2 |
| **Field/industries** | Meteorologi/agroklimatologi — jaringan stasiun cuaca perkebunan kopi, Kolombia |
| **Method** | Data paralel stasiun konvensional (CWS) dan AWS di 36 lokasi, 2014–2019. QC data 5 menit (filter lonjakan, uji rentang, konsistensi temporal dan spasial). Uji homogenitas SNHT ditambah analisis metadata. Koreksi bias dengan *quantile mapping* dan konstanta aditif. (hal. 1, 3–6) |
| **Result** | Data AWS umumnya lebih tinggi dari CWS untuk Tmean dan Tmax; bias Tmax terbesar 1,7 °C. Sebanyak 75% titik patahan (*changepoint*) disebabkan kerusakan instrumen, 12,5% oleh pembaruan *software*, dan 12,5% tidak tercatat di metadata. Tanpa penyesuaian, hanya 11 stasiun yang dapat melanjutkan seri historis untuk Tmean, 12 stasiun untuk Tmin, dan 1 stasiun untuk Tmax; sisanya diperlakukan sebagai seri baru yang terpisah. (hal. 7, 9, 16) |
| **Knowledge gaps** | Kriteria kontinuitas ditentukan dengan *expert judgement* (±0,5 °C pada <20–30% hari), belum ada standar yang baku. Metadata perawatan tidak lengkap. Hanya variabel suhu yang dikaji. Kontinuitas data AWS terganggu oleh kegagalan catu daya dan instrumen yang "tidak mudah diatasi". (hal. 6, 7, 16) |
| **Validasi dan Evaluasi Method** | Bias, indeks kesesuaian Willmott (dr > 0,8 = baik), PR05 (% hari dengan selisih dalam ±0,5 °C). Pemisahan seri kalibrasi dan validasi. (hal. 5–6) |
| **Weakness/opportunity** | *Quantile mapping* bekerja baik pada seri kalibrasi tetapi tidak pada seri validasi; di 6 stasiun bias justru memburuk sampai 1,25 °C. **Peluang:** rekomendasi penulis (paralel minimal 2 tahun, sensor cadangan, pencatatan metadata) bisa dirumuskan menjadi kriteria kesiapan transisi yang formal. (hal. 14–16) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As both a professional and a researcher. Sebagai praktisi (teknisi/observer), temuan bahwa 75% patahan data berasal dari kerusakan instrumen dan 12,5% dari pembaruan *software* menunjukkan pentingnya manajemen perubahan dan pencatatan metadata perawatan di stasiun. |

### Paper 2 — `article-pdf/P2-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 2 |
| **Title** | Bias of automatic weather parameter measurement in monsoon area, a case study in Makassar Coast |
| **Author** | Sunusi & Giarno (2023) |
| **Quartile** | Q3 |
| **Field/industries** | Meteorologi maritim — BMKG Stamar Paotere, Makassar, Indonesia |
| **Method** | Uji paralel AWS (Vaisala) dan observasi manual untuk suhu, tekanan, kelembapan, curah hujan, serta arah dan kecepatan angin. Data Januari 2020 (musim hujan) dan Juni 2020 (musim kemarau). Uji homogenitas varians (uji F), korelasi, RMSE, MAE, boxplot, dan *wind rose*. (hal. 1, 3–6) |
| **Result** | Musim hujan: hanya suhu dan tekanan yang homogen. Musim kemarau: kelembapan dan kecepatan angin ikut homogen. Curah hujan tidak homogen di kedua bulan. Korelasi suhu, tekanan, dan kelembapan >0,9; angin 0,76–0,81; curah hujan sangat lemah. Pada hujan berintensitas tinggi, AWS mencatat lebih rendah dari manual. (hal. 1, 6, 10, 12) |
| **Knowledge gaps** | Latar belakang: BMKG menetapkan sejak 2014 bahwa observasi akan beralih dari manual ke otomatis, dan WMO mewajibkan uji paralel. Penulis menyarankan pengujian lebih lama dengan memperhitungkan musim, data hilang/salah, berbagai metode homogenitas, dan dampaknya pada prakiraan. (hal. 1–2) |
| **Validasi dan Evaluasi Method** | Uji F (homogenitas varians), korelasi Pearson, RMSE, MAE, dan visual (boxplot, *wind rose*). (hal. 4–5) |
| **Weakness/opportunity** | Sampel hanya 2 bulan; hanya homogenitas varians yang diuji; sensor AWS dan manual berbeda lokasi (±10 m, AWS lebih dekat ke laut, ada sekat penghalang angin); penulis menduga gangguan arus listrik memengaruhi pencatatan hujan. **Peluang:** kajian paralel yang lebih panjang di stasiun BMKG dengan kriteria evaluasi yang terstruktur. (hal. 3, 12) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As a professional. Sebagai praktisi BMKG, paper ini paling dekat dengan kondisi kerja saya. Masalah teknis yang disebut (posisi sensor, catu daya, *tipping bucket*) sering ditemui di lapangan. |

### Paper 3 — `article-pdf/P3-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 3 |
| **Title** | Continuity of long-term climate data series after the transition from manual to automatic weather station |
| **Author** | Lukasová, Varšová, Onderka, Bilčík, Buchholcerová, & Nejedlík (2024) |
| **Quartile** | Q3 |
| **Field/industries** | Klimatologi pegunungan — Observatorium Skalnaté Pleso (1778 mdpl), Slovakia |
| **Method** | AWS dipasang 2014. Data paralel 2017–2022 dipakai untuk menurunkan koreksi (dua tahun pertama dibuang karena banyak data kosong); koreksi diuji pada data 2023. Dua pendekatan: regresi bulanan (MR) dan *quantile mapping* (distribusi GEV, Gauss, Gamma). Parameter: curah hujan bulanan, Tmax, Tmin, Tmean. (hal. 1, 4–7) |
| **Result** | AWS mencatat curah hujan lebih rendah (MBE −6,8 mm; RMSE 20,0 mm), setelah koreksi MR menjadi 1,5 mm dan 11,1 mm. Suhu AWS lebih tinggi 0,1–0,3 °C, setelah koreksi MBE 0,0 °C. Selisih terbesar pada salju di musim dingin. Data AWS hilang ±12% pada 2022 karena kerusakan alat, sedangkan data manual tidak pernah kosong karena ada observer. (hal. 1, 7, 13–14) |
| **Knowledge gaps** | Koreksi perlu disempurnakan dengan periode paralel lebih panjang **sebelum implementasi penuh**. Kerusakan AWS di lokasi terpencil sulit segera diperbaiki. Belum ada panduan kapan observasi manual aman dihentikan. (hal. 14–15) |
| **Validasi dan Evaluasi Method** | Seri kalibrasi 2017–2022 dan validasi independen 2023. Metrik: MBE, RMSE, simpangan baku selisih. (hal. 5–8) |
| **Weakness/opportunity** | Hanya satu stasiun, hanya data bulanan (bukan harian), validasi hanya satu tahun. **Peluang:** temuan bahwa observer 24/7 menjamin kelengkapan data bisa menjadi argumen manajemen risiko, yaitu kapan observer masih dibutuhkan setelah otomatisasi. (hal. 14) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As a professional. Sebagai observer, temuan ini relevan dengan peran saya: data manual lengkap karena ada observer yang menangani gangguan kecil, sedangkan AWS kehilangan ±12% data ketika rusak. |

### Paper 4 — `article-pdf/P4-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 4 |
| **Title** | Developing a statistical approach of evaluating daily maximum and minimum temperature observations from third-party automatic weather stations in Australia |
| **Author** | Li, Shao, Dabrowski, Rahman, Powell, Henderson, Hussain, & Steinle (2024) |
| **Quartile** | Q1 |
| **Field/industries** | Meteorologi operasional — kendali mutu data AWS pihak ketiga, Australia (CSIRO dan Bureau of Meteorology) |
| **Method** | Setiap observasi Tmax/Tmin dibandingkan dengan tiga data acuan: stasiun resmi terdekat (*spatial regression test*), data grid AGCD, dan model NWP. Hasil ketiga uji digabung dengan *Gaussian mixture model* menjadi satu skor kepercayaan berbasis *p-value*. (hal. 1, 4–8) |
| **Result** | Mendeteksi galat lebih dari 2 °C. Uji gabungan menghasilkan *false alarm* lebih rendah daripada uji tunggal. Diterapkan pada 184 AWS milik DPIRD (Australia Barat) tahun 2019: 2,3% data Tmax dan 4,4% data Tmin terindikasi salah. Kinerja menurun di wilayah dengan jaringan stasiun yang jarang. (hal. 1, 12–13, 15–16) |
| **Knowledge gaps** | Tidak dapat mendeteksi **bias sistematis** karena mengasumsikan galat berupa *outlier*. Belum berlaku untuk curah hujan. Bergantung pada data acuan khas Australia (AGCD). Tidak menjelaskan penyebab galat. (hal. 16–17) |
| **Validasi dan Evaluasi Method** | Dataset sintetis dari 100 stasiun berkualitas tinggi (ACORN-SAT, 2017–2018) yang disisipi galat acak (±2,7% data). Metrik: *hit rate* dan *false alarm rate*. (hal. 8–9, 13) |
| **Weakness/opportunity** | Penerapan di negara lain butuh data acuan pengganti. **Peluang:** skor kepercayaan per observasi bisa dipakai sebagai indikator kuantitatif untuk menilai **kelayakan/kesiapan** sebuah AWS sebelum datanya dipakai resmi. (hal. 16) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As both a professional and a researcher. Sebagai peneliti, pendekatan ini menarik karena otomatis dan dapat ditelusuri (*interpretable*). Sebagai teknisi, keterbatasannya pada bias sistematis justru menunjukkan pentingnya kalibrasi dan uji paralel. Paper ini relevan dengan riset saya tentang deteksi anomali dan *data drift* pada data AWOS Stasiun Meteorologi Biak menggunakan Isolation Forest, ADWIN, dan aturan (*rules*). |

### Paper 5 — `article-pdf/P5-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 5 |
| **Title** | Automatic quality control of telemetric rain gauge data providing quantitative quality information (RainGaugeQC) |
| **Author** | Ośródka, Otop, & Szturc (2022) |
| **Quartile** | Q1 |
| **Field/industries** | Hidrometeorologi operasional — layanan meteorologi nasional Polandia (IMGW), 503 stasiun hujan telemetri |
| **Method** | Rangkaian pemeriksaan otomatis untuk data hujan 10 menit: *gross error*, uji rentang, kesesuaian dengan radar cuaca, konsistensi sensor berpemanas vs tanpa pemanas, dan konsistensi spasial dengan stasiun tetangga. Setiap data diberi **Quality Index (QI)** 0,0–1,0. (hal. 1–2, 4) |
| **Result** | Kurang dari 1,5% data mengalami penurunan QI. Data yang ditolak (QI = 0) ±0,4% di musim panas dan 0,10–0,23% di musim lain. Sensor *tipping bucket* rata-rata mencatat 8–20% lebih rendah. Skema ini dipakai secara operasional oleh IMGW. (hal. 2, 11–13) |
| **Knowledge gaps** | Parameter algoritma bersifat empiris dan bergantung pada kondisi lokal; setiap perubahan konfigurasi jaringan mengharuskan kalibrasi ulang. Efektivitas turun jika stasiun hanya punya satu sensor. (hal. 13) |
| **Validasi dan Evaluasi Method** | Studi kasus, penyisipan nilai salah buatan (10 mm/10 menit), perbandingan dengan radar, dan statistik penurunan QI per musim. Tidak ada metrik akurasi formal seperti *hit rate*. (hal. 8–12) |
| **Weakness/opportunity** | Evaluasi lebih deskriptif daripada kuantitatif; hanya untuk curah hujan. **Peluang:** konsep QI per observasi bisa diadopsi sebagai ukuran mutu ketika memverifikasi AWS baru. (hal. 12–13) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As a professional. Sebagai teknisi, masalah *tipping bucket* yang dibahas (tersumbat, embun terbaca sebagai hujan, *double tip*) sesuai dengan pengalaman lapangan pada ARG/AWS. Konsep *Quality Index* per observasi dapat diadaptasi pada riset saya tentang deteksi anomali data AWOS (suhu, tekanan, kelembapan) menggunakan Isolation Forest, ADWIN, dan aturan (*rules*). |

### Paper 6 — `article-pdf/P6-...pdf`

| Kolom | Isi |
|---|---|
| **No** | 6 |
| **Title** | Analysis of 105 IT Project Risks |
| **Author** | Nikolaenko & Sidorov (2023) |
| **Quartile** | Q2 |
| **Field/industries** | Manajemen proyek TI — manajemen risiko (Rusia) |
| **Method** | Analisis 105 risiko universal proyek TI (5 komersial, 45 kepatuhan, 55 proyek) dengan metode 5Why (akar penyebab), SWIFT (*Structured What-If Technique*), dan koefisien Harrington (probabilitas dan dampak). (hal. 1, 3–4) |
| **Result** | Sumber risiko: manajer proyek 43%, tim proyek 36%, pelanggan 15%, pengguna/subkontraktor/pesaing masing-masing 2%. Memetakan hubungan sebab-akibat antarrisiko dan menyusun kriteria kematangan manajemen kontraktor proyek TI. (hal. 1, 15–16, 18) |
| **Knowledge gaps** | Risiko khusus (*special risks*) yang unik per proyek tidak dicakup. Model kematangan kontraktor baru direncanakan untuk penelitian berikutnya. Belum ada penerapan pada proyek sektor tertentu. (hal. 18) |
| **Validasi dan Evaluasi Method** | Penilaian kualitatif dengan skala Harrington dan perbandingan dengan daftar risiko peneliti lain (Addison & Vallabh, Stevens & Fowell, Sumner). Tidak ada data empiris dari proyek nyata ("*Data Availability: Not applicable*"). (hal. 4, 16–18) |
| **Weakness/opportunity** | Validasi empiris lemah. **Peluang:** daftar risiko dan metode 5Why/SWIFT bisa diterapkan pada proyek transisi AWS (risiko teknologi baru, kompetensi tim, kepatuhan pada standar WMO). (hal. 16–18) |
| **Other Descriptions** | *[USULAN — sesuaikan]* As a researcher. Paper ini dipakai sebagai kerangka manajemen risiko proyek TI: transisi observasi manual ke AWS diperlakukan sebagai proyek TI, sehingga risiko seperti pengenalan teknologi baru, kompetensi tim, dan kepatuhan pada standar WMO dapat dianalisis dengan metode 5Why dan SWIFT. Paper-paper meteorologi dalam tabel ini belum membahas aspek tersebut. |

---

## Problem Statement and Research Problem

### Problem Statement

1. Data AWS memiliki bias sistematis terhadap observasi manual. Besarnya bergantung pada jenis instrumen, pelindung radiasi, lokasi sensor, dan musim, sehingga data AWS tidak dapat langsung dianggap sebagai lanjutan seri data historis observasi manual (Ramírez Carabalí et al., 2022; Sunusi & Giarno, 2023; Lukasová et al., 2024).
2. Kesesuaian AWS dengan observasi manual berbeda per parameter dan per musim. Suhu dan tekanan homogen pada musim hujan maupun kemarau, kelembapan hanya homogen pada musim kemarau, sedangkan curah hujan tidak homogen pada kedua musim (Sunusi & Giarno, 2023).
3. Kerusakan instrumen, gangguan catu daya, dan pembaruan *software* menyebabkan patahan dan kekosongan data AWS. Sebanyak 75% titik patahan data disebabkan kerusakan instrumen dan 12,5% oleh pembaruan *software* (Ramírez Carabalí et al., 2022), dan data AWS dapat hilang hingga sekitar 12% dalam setahun ketika terjadi kerusakan, sedangkan data manual tetap lengkap karena ada observer (Lukasová et al., 2024).
4. Lama periode observasi paralel dan kriteria kesiapan AWS untuk menggantikan observasi manual belum baku. Kriteria kontinuitas masih ditetapkan berdasarkan *expert judgement*, dan para peneliti menyatakan perlunya periode paralel yang lebih panjang sebelum implementasi penuh (Ramírez Carabalí et al., 2022; Sunusi & Giarno, 2023; Lukasová et al., 2024).
5. Metode kendali mutu otomatis telah menyediakan ukuran mutu kuantitatif per observasi, tetapi tidak dapat mendeteksi bias sistematis dan parameternya bergantung pada kondisi lokal, sehingga belum cukup untuk menjadi dasar tunggal keputusan transisi (Li et al., 2024; Ośródka et al., 2022).
6. Sebagian besar sumber risiko proyek TI berasal dari manajer proyek dan tim proyek (79%), termasuk risiko pengenalan teknologi baru dan risiko kepatuhan (Nikolaenko & Sidorov, 2023). Namun, kajian-kajian transisi ke AWS di atas berfokus pada aspek teknis data dan belum membahas transisi tersebut sebagai proyek TI yang risikonya dikelola secara terstruktur.

### Research Problem

Transisi observasi meteorologi manual ke AWS menimbulkan bias data yang sistematis dan risiko terputusnya kontinuitas data akibat kegagalan perangkat, sementara belum tersedia kriteria verifikasi kesiapan yang terukur maupun kerangka manajemen risiko proyek untuk mengambil keputusan penghentian observasi manual, sehingga transisi berisiko menurunkan kualitas dan kontinuitas data meteorologi.

## Dataset

Berdasarkan pada literatur yang ada, maka dataset yang digunakan adalah:

1. **Data observasi paralel AWOS (*Automated Weather Observing System*, jenis AWS yang digunakan di stasiun bandara) dan observasi manual (sinoptik)** di Stasiun Meteorologi Biak, periode Desember 2012 – Juli 2026, dengan parameter suhu udara, tekanan udara, dan kelembapan relatif. Jenis data ini digunakan oleh Ramírez Carabalí et al. (2022), Sunusi dan Giarno (2023), dan Lukasová et al. (2024); periodenya jauh melampaui rekomendasi paralel minimal 2 tahun (Ramírez Carabalí et al., 2022) dan mencakup masa sebelum dan sesudah penetapan peralihan observasi BMKG ke sistem otomatis pada 2014 (Sunusi & Giarno, 2023).
   - *Alasan pemilihan parameter:* suhu, tekanan, dan kelembapan menunjukkan kesesuaian AWS–manual paling tinggi (korelasi > 0,9) dan saling terkait secara fisis, misalnya perbedaan suhu memengaruhi kerapatan udara dan tekanan (Sunusi & Giarno, 2023). Curah hujan tidak digunakan karena perbedaannya didominasi karakteristik alat ukur *tipping bucket* (Ośródka et al., 2022; Lukasová et al., 2024).
2. **Metadata stasiun**, yaitu catatan perawatan, kerusakan, kalibrasi, penggantian sensor, dan pembaruan *software* AWS selama periode yang sama. Metadata digunakan untuk menjelaskan penyebab patahan data, sebagaimana dilakukan Ramírez Carabalí et al. (2022).
3. **Data risiko proyek transisi**, diperoleh melalui wawancara atau kuesioner kepada observer, teknisi, dan pengelola stasiun, lalu dianalisis dengan metode 5Why dan SWIFT serta dinilai probabilitas dan dampaknya mengikuti Nikolaenko dan Sidorov (2023).

*Catatan: penggunaan data internal stasiun memerlukan izin instansi. Alternatif data publik: BMKG Data Online (dataonline.bmkg.go.id).*

---

## References (acuan — daftar final dibuat dari Mendeley, APA 7)

1. Ramírez Carabalí, C., Sarmiento Herrera, N. G., Imbachi Quinchua, L. C., & García López, J. C. (2022). Continuity of daily temperature time series in the transition from conventional to automated stations for the Colombian coffee network. *Meteorological Applications, 29*(3), e2054. https://doi.org/10.1002/met.2054
2. Sunusi, N., & Giarno. (2023). Bias of automatic weather parameter measurement in monsoon area, a case study in Makassar Coast. *AIMS Environmental Science, 10*(1), 1–15. https://doi.org/10.3934/environsci.2023001
3. Lukasová, V., Varšová, S., Onderka, M., Bilčík, D., Buchholcerová, A., & Nejedlík, P. (2024). Continuity of long-term climate data series after the transition from manual to automatic weather station. *Contributions to Geophysics and Geodesy, 54*(3), 251–266. https://doi.org/10.31577/congeo.2024.54.3.2
4. Li, M., Shao, Q., Dabrowski, J. J., Rahman, A., Powell, A., Henderson, B., Hussain, Z., & Steinle, P. (2024). Developing a statistical approach of evaluating daily maximum and minimum temperature observations from third-party automatic weather stations in Australia. *Quarterly Journal of the Royal Meteorological Society, 150*(760), 1624–1642. https://doi.org/10.1002/qj.4662
5. Ośródka, K., Otop, I., & Szturc, J. (2022). Automatic quality control of telemetric rain gauge data providing quantitative quality information (RainGaugeQC). *Atmospheric Measurement Techniques, 15*(19), 5581–5597. https://doi.org/10.5194/amt-15-5581-2022
6. Nikolaenko, V., & Sidorov, A. (2023). Analysis of 105 IT project risks. *Journal of Risk and Financial Management, 16*(1), 33. https://doi.org/10.3390/jrfm16010033
