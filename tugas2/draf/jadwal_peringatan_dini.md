# Draf Tugas 2 — Tahap 2: Jadwal (Gantt Chart & Schedule)
## Sistem Peringatan Dini Cuaca Publik Berbasis IoT (Audio-Visual) Terintegrasi Data BMKG

> Berkas kerja (draf), disusun bertahap:
> Tahap 1: lingkup + WBS (`wbs_peringatan_dini.md`) → **Tahap 2: jadwal (berkas ini)** → Tahap 3: Risk Register → Tahap 4: penyatuan ke PDF dan ClickUp.
> Dasar: keputusan 28 Oktober 2026, yaitu 6 perangkat di 3 wilayah DIY, durasi target ±4 bulan, sponsor BPBD, dan tim 4–5 orang.
> **[USULAN]** Semua angka durasi (O, M, P) adalah perkiraan awal dari Claude. Kelompok boleh mengubahnya; jadwal lalu dihitung ulang.

---

## 1. Ringkasan

| Hal | Hasil |
|---|---|
| Durasi proyek | **92 hari kerja ≈ 18,4 minggu ≈ 4,2 bulan** (sesuai target ±4 bulan) |
| Jumlah aktivitas | 43 *work package* dari WBS + 6 milestone |
| Jalur kritis | Lewat **perangkat keras dan pengujian akhir**: pengadaan → prototipe → firmware → uji → produksi/uji integrasi → pemasangan → UAT |
| Cadangan waktu (*contingency reserve*) | **5 hari kerja**, dipegang manajer proyek untuk risiko R-06 (*bug* lebih banyak dari perkiraan). Tidak dimasukkan ke jadwal sebagai aktivitas; bila terpakai seluruhnya, proyek selesai paling lambat di **hari ke-97** (PMBOK 4, Bagian 6.4.2.5, hlm. 150) |
| Waktu pengujian | Total 31 hari kerja aktivitas uji, **sudah termasuk perbaikan *bug* dan uji ulang**; pengujian akhir berlangsung di minggu 13–18 (lihat Bagian 6) |

---

## 2. Dasar penyusunan (metodologi PMBOK)

Jadwal disusun melalui empat proses PMBOK (slide 06, hlm. 18):

| Proses PMBOK | Yang dilakukan di sini |
|---|---|
| *Define Activities* | Setiap *work package* WBS menjadi satu aktivitas dengan **kode yang sama** |
| *Sequence Activities* | Urutan ditentukan dengan *Precedence Diagramming Method* (PMBOK 4, Bagian 6.2.2.1). Semua hubungan memakai jenis **FS** (*Finish-to-Start*: aktivitas berikut mulai setelah pendahulunya selesai) |
| *Estimate Activity Durations* | ***Three-point estimation* / PERT** (PMBOK 4, Bagian 6.4.2.4, hlm. 149; slide 06, hlm. 21). Durasi = **(O + 4M + P) / 6**, lalu dibulatkan ke hari terdekat (0,5 dibulatkan ke atas) |
| *Develop Schedule* | Jalur kritis dihitung dengan ***Critical Path Method*** (PMBOK 4, Bagian 6.5.2.2, hlm. 153): hitung maju, hitung mundur, lalu *float* |

Keterangan:
- **O** = optimis (perkiraan tercepat), **M** = paling mungkin, **P** = pesimis (perkiraan terlama).
- Satuan waktu: **hari kerja**, 5 hari per minggu.
- **ES/EF** = mulai/selesai paling awal; **LS/LF** = mulai/selesai paling lambat. ES = 0 artinya mulai di awal hari kerja ke-1.
- ***Float*** = LS − ES, yaitu berapa hari aktivitas boleh terlambat tanpa menunda proyek. *Float* = 0 berarti aktivitas berada di **jalur kritis**.
- **1.1.2 Rapat dan laporan kemajuan** dan **1.1.3 Pengendalian perubahan dan pemantauan risiko** berjalan terus sepanjang proyek (minggu 2–18), sehingga tidak dimasukkan ke perhitungan jalur kritis.

---

## 3. Tabel aktivitas

Baris **tebal** = jalur kritis.

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

---

## 4. Daftar milestone

| Kode | Milestone | Hari kerja ke- | Minggu ke- | Disetujui oleh |
|---|---|---|---|---|
| M1 | Proyek disahkan (project charter ditandatangani) | 5 | 1 | Sponsor (BPBD) |
| M2 | Kebutuhan disetujui (SRS ditandatangani) | 21 | 5 | Sponsor |
| M3 | Desain disetujui | 29 | 6 | Manajer proyek + sponsor |
| M4 | UAT disetujui | 86 | 18 | Sponsor |
| M5 | Sistem diserahterimakan | 89 | 18 | Sponsor |
| M6 | Proyek ditutup | 92 | 19 | Manajer proyek |

Milestone berdurasi 0 dan tidak dimasukkan ke WBS (lihat Tahap 1).

---

## 5. Jalur kritis

**1.1.1 → M1 → 1.2.1 → 1.2.4 → 1.2.5 → M2 → 1.3.1 → 1.3.4 → 1.4.1 → 1.4.2 → 1.6.1 → 1.6.2 → 1.6.3 → 1.6.4 → 1.7.3 → [cabang A atau B] → 1.7.6 → M4 → 1.8.6 → M5 → 1.1.4 → M6 = 92 hari kerja**

Setelah uji perangkat keras (1.7.3), jalur kritis **bercabang dua**. Kedua cabang sama panjang (12 hari) dan bertemu lagi di uji lapangan/UAT (1.7.6):
- **Cabang A:** 1.6.5 Perakitan unit produksi (6) → 1.8.1 Pemasangan (5) → 1.8.3 Konfigurasi (1)
- **Cabang B:** 1.7.4 Uji integrasi (7) → 1.7.5 Uji kegagalan (5)

Artinya, keterlambatan di **salah satu** cabang langsung menunda proyek.

Yang bisa dibaca dari hasil ini:

1. **Penentu lama proyek adalah perangkat keras dan pengujian akhir, bukan perangkat lunak server.** Rantai pembelian komponen → prototipe → firmware → uji → perakitan/uji integrasi → pemasangan tidak punya kelonggaran. Perangkat lunak server punya *float* 10 hari.
2. **Pembelian komponen (1.4.2) paling rawan.** Perkiraan pesimisnya 20 hari (O = 7, M = 10). Karena berada di jalur kritis, setiap hari keterlambatan pengiriman langsung menunda proyek. Ini menjadi bahan Risk Register (Tahap 3).
3. **Izin pemasangan (1.4.4) tidak kritis, tetapi paling tidak pasti.** *Float*-nya 37 hari, tetapi rentang perkiraannya paling lebar (10–30 hari). Izin perlu diurus sejak survei lokasi selesai (minggu 4). Ini juga bahan Risk Register.
4. **Uji lapangan dan UAT (1.7.6) adalah aktivitas kritis terpanjang di akhir proyek** (10 hari). Kalau sponsor menunda persetujuan, serah terima ikut mundur.
5. **Uji integrasi dan uji kegagalan menjadi kritis** karena durasinya sudah memasukkan waktu perbaikan *bug*. Kalau *bug* yang ditemukan lebih banyak dari perkiraan, proyek langsung mundur. Ini juga bahan Risk Register.

### Catatan sumber daya

CPM menghitung jadwal **tanpa memperhitungkan jumlah orang** (PMBOK 4, Bagian 6.5.2.2). Dari pengecekan per peran, ada beberapa pekerjaan satu peran yang tumpang tindih. Contohnya, Programmer Server mengerjakan 1.5.1 dan 1.5.4 pada hari yang sama, dan Analis Sistem mengerjakan 1.2.1 dan 1.2.2 bersamaan. Semua tumpang tindih ini **bisa digeser memakai *float*-nya masing-masing** tanpa memundurkan tanggal selesai proyek. Rangkaian pekerjaan Programmer Server, kalau dikerjakan berurutan, selesai di hari ke-55; batasnya hari ke-59. Hasil ini sudah dihitung ulang dengan CPM untuk skenario satu programmer: durasi proyek tetap 92 hari.

---

## 6. Lama waktu pengujian

| Kode | Pengujian | Durasi | Hari kerja ke- | Minggu ke- | Kritis? |
|---|---|---|---|---|---|
| 1.7.2 | Uji pencocokan nama wilayah | 2 | 39–40 | 8 | Tidak |
| 1.7.1 | Uji unit perangkat lunak | 3 | 50–52 | 10–11 | Tidak |
| 1.7.3 | Uji perangkat keras | 4 | 61–64 | 13 | **Ya** |
| 1.7.4 | Uji integrasi ujung ke ujung | 7 | 65–71 | 13–15 | **Ya** |
| 1.7.5 | Uji kegagalan | 5 | 72–76 | 15–16 | **Ya** |
| 1.7.6 | Uji coba lapangan dan UAT | 10 | 77–86 | 16–18 | **Ya** |
| | **Jumlah** | **31 hari kerja** | | | |

- **Perbaikan *bug* (*debugging*) termasuk di dalam periode pengujian.** Setiap pengujian berjalan dengan pola **uji → perbaiki → uji ulang**. Durasi uji integrasi (1.7.4) dan uji kegagalan (1.7.5) sengaja dibuat lebih panjang, karena di sanalah *bug* paling banyak ditemukan: server, MQTT, dan perangkat pertama kali dijalankan bersama. *Debugging* saat menulis kode sudah termasuk di durasi 1.5.x dan 1.6.x.
- Jumlah durasi seluruh aktivitas uji adalah **31 hari kerja**, setara **sekitar 34%** dari durasi proyek (92 hari). Sebagian pengujian berjalan bersamaan dengan pekerjaan lain.
- Pengujian **tidak ditumpuk di akhir proyek**. Modul yang selesai lebih dulu langsung diuji: uji pencocokan nama di minggu 8, uji unit di minggu 10–11.
- Rangkaian **pengujian akhir** berlangsung dari uji perangkat keras (minggu 13) sampai UAT disetujui (minggu 18), sekitar **5 minggu**.
- **UAT 10 hari (2 minggu)**, karena perangkat perlu diamati di lokasi dalam beberapa kondisi cuaca. Bila selama masa itu BMKG tidak mengeluarkan peringatan untuk wilayah percontohan, pengujian memakai mode uji dari dasbor.

---

## 7. Gantt Chart (per minggu)

█ = aktivitas di jalur kritis, ░ = aktivitas dengan *float*, ◆ = milestone. Satu kolom = satu minggu (5 hari kerja).

```
Minggu                                      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19
1.1.1 Project charter dan rencana proyek    ███
M1    ◆ Proyek disahkan                      ◆
1.4.5 Penyiapan alat pengembangan              ░░░
1.2.1 Kebutuhan pemangku kepentingan           ███
1.2.2 Studi halaman peringatan dini BMKG       ░░░
1.2.3 Daftar wilayah dan variasi nama             ░░░
1.2.4 Survei lokasi pemasangan                    ██████
1.2.5 Spesifikasi kebutuhan sistem (SRS)             ██████
M2    ◆ Kebutuhan disetujui sponsor                      ◆
1.4.4 Izin pemasangan                                ░░░░░░░░░░░░
1.3.1 Arsitektur sistem                                 ███
1.3.2 Desain logika status peringatan                   ░░░░░░
1.3.3 Desain database                                   ░░░░░░
1.3.4 Desain rangkaian perangkat keras                  ██████
1.3.5 Desain pesan LED dan pola audio-lampu             ░░░
1.3.6 Desain dasbor admin                                  ░░░
M3    ◆ Desain disetujui                                    ◆
1.4.1 Daftar komponen (BOM)                                ██████
1.4.2 Pemilihan pemasok dan pembelian                         █████████
1.4.3 Sewa server (VPS) dan domain                      ░░░
1.5.1 Modul pemantau BMKG                                  ░░░░░░
1.5.2 Modul pencocokan nama wilayah                           ░░░░░░
1.5.3 Modul pengelola status                                     ░░░░░░
1.5.4 Layanan MQTT                                         ░░░░░░
1.5.5 Dasbor admin                                                  ░░░░░░
1.5.6 Heartbeat dan notifikasi admin                          ░░░
1.6.1 Perakitan prototipe                                           ███
1.6.2 Firmware C++                                                     ██████
1.6.3 Heartbeat dan sambung ulang                                         ██████
1.6.4 Fitur diagnosa jarak jauh                                              ███
1.7.1 Uji unit perangkat lunak                                         ░░░░░░
1.7.2 Uji pencocokan nama wilayah                                ░░░
1.7.3 Uji perangkat keras                                                       ███
1.6.5 Perakitan unit produksi                                                   ██████
1.8.2 Deploy server dan pengamanan                                        ░░░
1.7.4 Uji integrasi ujung ke ujung                                              █████████
1.7.5 Uji kegagalan                                                                   ██████
1.8.1 Pemasangan perangkat di lokasi                                                  ███
1.8.3 Konfigurasi wilayah dan perangkat                                                  ███
1.7.6 Uji lapangan dan UAT                                                               █████████
M4    ◆ UAT disetujui sponsor                                                                   ◆
1.8.4 Sosialisasi ke warga                                                               ░░░
1.8.5 Pelatihan operator                                                                 ░░░
1.8.6 Serah terima dan dokumentasi                                                             ███
M5    ◆ Sistem diserahterimakan                                                                 ◆
1.1.4 Penutupan dan lessons learned                                                            ██████
M6    ◆ Proyek ditutup                                                                             ◆
```

Satu kolom mewakili seminggu penuh. Aktivitas pendek yang melewati pergantian minggu tampil di dua kolom; contohnya, 1.4.1 (2 hari, hari ke-30–31) tampil di minggu 6 dan 7. Gantt versi harian dibuat di ClickUp pada Tahap 4.

---

## 8. [USULAN] Pilihan memperpendek jadwal

Durasi 92 hari kerja sudah sesuai target ±4 bulan, jadi **tidak wajib** diperpendek. Pilihan ini dicatat sebagai bahan diskusi dan untuk menunjukkan pemahaman teknik PMBOK.

**Fast tracking** (PMBOK 4, Bagian 6.5.2.7, hlm. 155–156): mengerjakan secara paralel aktivitas yang biasanya berurutan.
- **Caranya:** komponen untuk **satu prototipe** dibeli lebih dulu, langsung setelah desain rangkaian (1.3.4) selesai, tanpa menunggu pembelian semua komponen produksi (1.4.2).
- **Perkiraan hasil:** ada tambahan satu *work package* kecil, yaitu "pembelian komponen prototipe" (3 hari).

| Skenario | Durasi proyek |
|---|---|
| Jadwal sekarang (tanpa *fast tracking*) | 92 hari kerja |
| *Fast tracking*, **satu** Programmer Server | **88 hari kerja** (hemat 4 hari) |
| *Fast tracking*, **dua** programmer | **82 hari kerja** (hemat 10 hari) |

- **Kenapa hasilnya berbeda:** dengan *fast tracking*, pekerjaan perangkat lunak server ikut masuk jalur kritis. Satu programmer tidak bisa mengerjakan modul-modulnya secara paralel, sehingga sebagian penghematan hilang.
- **Risikonya** (sesuai PMBOK): bila prototipe menunjukkan komponen yang salah, sebagian pembelian produksi harus diulang (*rework*).

Ketiga angka di atas sudah dihitung ulang dengan CPM, bukan perkiraan kasar.

Belum diterapkan. Kelompok yang memutuskan.

---

## Glosarium

| Istilah | Penjelasan |
|---|---|
| *Bug* | Kesalahan dalam program |
| *Critical Path Method* (CPM) | Teknik menghitung jalur terpanjang dalam jadwal untuk menemukan jalur kritis |
| *Debugging* | Mencari dan memperbaiki *bug* |
| ES / EF | *Early Start* / *Early Finish*: mulai / selesai paling awal |
| *Fast tracking* | Teknik memperpendek jadwal dengan mengerjakan paralel aktivitas yang biasanya berurutan |
| FS (*Finish-to-Start*) | Hubungan ketergantungan: aktivitas berikut mulai setelah pendahulunya selesai |
| *Float* | Kelonggaran; berapa hari aktivitas boleh terlambat tanpa menunda proyek |
| Gantt Chart | Jadwal berbentuk batang mendatar di atas garis waktu |
| Jalur kritis | Rangkaian aktivitas dengan *float* nol; keterlambatannya langsung menunda proyek |
| LS / LF | *Late Start* / *Late Finish*: mulai / selesai paling lambat tanpa menunda proyek |
| Milestone | Titik pencapaian penting berdurasi nol |
| PERT / *three-point estimation* | Estimasi durasi dari tiga perkiraan: (Optimis + 4 × Paling mungkin + Pesimis) / 6 |
| *Precedence Diagramming Method* (PDM) | Metode menyusun urutan aktivitas dengan kotak dan panah ketergantungan |
| *Rework* | Pekerjaan ulang karena hasil sebelumnya harus diperbaiki |
| UAT | *User Acceptance Testing*; uji penerimaan oleh pengguna atau sponsor |
