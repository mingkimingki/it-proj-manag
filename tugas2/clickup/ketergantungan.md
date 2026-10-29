# Daftar ketergantungan (untuk dibuat manual di Gantt ClickUp)

Semua hubungan berjenis **Finish-to-Start**: tugas di kolom kanan baru boleh mulai setelah tugas di kolom kiri selesai. Jumlah: **65 ketergantungan**. Urutan mengikuti tanggal mulai, jadi bisa dikerjakan dari atas ke bawah.

Cara membuat di Gantt ClickUp: arahkan kursor ke batang tugas di kolom **Pendahulu**, tarik titik di ujung kanannya ke batang tugas di kolom **Tugas**. Centang kolom terakhir setelah selesai.

| No | Pendahulu (selesai dulu) | Tugas (mulai sesudahnya) | ✓ |
|---|---|---|---|
| 1 | 1.1.1 Project charter dan rencana proyek | ◆ M1 Proyek disahkan | ☐ |
| 2 | ◆ M1 Proyek disahkan | 1.2.1 Kebutuhan pemangku kepentingan | ☐ |
| 3 | ◆ M1 Proyek disahkan | 1.2.2 Studi halaman peringatan dini BMKG | ☐ |
| 4 | ◆ M1 Proyek disahkan | 1.4.5 Penyiapan alat pengembangan | ☐ |
| 5 | 1.2.1 Kebutuhan pemangku kepentingan | 1.2.3 Daftar wilayah sasaran dan variasi nama | ☐ |
| 6 | 1.2.2 Studi halaman peringatan dini BMKG | 1.2.3 Daftar wilayah sasaran dan variasi nama | ☐ |
| 7 | 1.2.1 Kebutuhan pemangku kepentingan | 1.2.4 Survei lokasi pemasangan | ☐ |
| 8 | 1.2.3 Daftar wilayah sasaran dan variasi nama | 1.2.5 Spesifikasi kebutuhan sistem (SRS) | ☐ |
| 9 | 1.2.4 Survei lokasi pemasangan | 1.2.5 Spesifikasi kebutuhan sistem (SRS) | ☐ |
| 10 | 1.2.4 Survei lokasi pemasangan | 1.4.4 Izin pemasangan | ☐ |
| 11 | 1.2.5 Spesifikasi kebutuhan sistem (SRS) | ◆ M2 Kebutuhan disetujui sponsor | ☐ |
| 12 | ◆ M2 Kebutuhan disetujui sponsor | 1.3.1 Arsitektur sistem | ☐ |
| 13 | ◆ M2 Kebutuhan disetujui sponsor | 1.3.5 Desain pesan LED dan pola audio-lampu | ☐ |
| 14 | 1.3.1 Arsitektur sistem | 1.3.2 Desain logika status peringatan | ☐ |
| 15 | 1.3.1 Arsitektur sistem | 1.3.3 Desain database wilayah dan perangkat | ☐ |
| 16 | 1.3.1 Arsitektur sistem | 1.3.4 Desain rangkaian perangkat keras | ☐ |
| 17 | 1.3.1 Arsitektur sistem | 1.4.3 Sewa server (VPS) dan domain | ☐ |
| 18 | 1.3.3 Desain database wilayah dan perangkat | 1.3.6 Desain dasbor admin | ☐ |
| 19 | 1.3.2 Desain logika status peringatan | ◆ M3 Desain disetujui | ☐ |
| 20 | 1.3.4 Desain rangkaian perangkat keras | ◆ M3 Desain disetujui | ☐ |
| 21 | 1.3.5 Desain pesan LED dan pola audio-lampu | ◆ M3 Desain disetujui | ☐ |
| 22 | 1.3.6 Desain dasbor admin | ◆ M3 Desain disetujui | ☐ |
| 23 | 1.3.4 Desain rangkaian perangkat keras | 1.4.1 Daftar komponen (BOM) | ☐ |
| 24 | ◆ M3 Desain disetujui | 1.5.1 Modul pemantau BMKG (Playwright) | ☐ |
| 25 | 1.4.5 Penyiapan alat pengembangan | 1.5.1 Modul pemantau BMKG (Playwright) | ☐ |
| 26 | ◆ M3 Desain disetujui | 1.5.4 Layanan pengirim perintah (MQTT) | ☐ |
| 27 | 1.4.3 Sewa server (VPS) dan domain | 1.5.4 Layanan pengirim perintah (MQTT) | ☐ |
| 28 | 1.4.1 Daftar komponen (BOM) | 1.4.2 Pemilihan pemasok dan pembelian komponen | ☐ |
| 29 | 1.5.4 Layanan pengirim perintah (MQTT) | 1.5.6 Pemantauan heartbeat dan notifikasi admin | ☐ |
| 30 | 1.5.1 Modul pemantau BMKG (Playwright) | 1.5.2 Modul pencocokan nama wilayah | ☐ |
| 31 | 1.5.2 Modul pencocokan nama wilayah | 1.5.3 Modul pengelola status peringatan | ☐ |
| 32 | 1.5.2 Modul pencocokan nama wilayah | 1.7.2 Uji pencocokan nama wilayah | ☐ |
| 33 | 1.5.3 Modul pengelola status peringatan | 1.5.5 Dasbor admin | ☐ |
| 34 | 1.5.4 Layanan pengirim perintah (MQTT) | 1.5.5 Dasbor admin | ☐ |
| 35 | 1.4.2 Pemilihan pemasok dan pembelian komponen | 1.6.1 Perakitan prototipe | ☐ |
| 36 | ◆ M3 Desain disetujui | 1.6.1 Perakitan prototipe | ☐ |
| 37 | 1.6.1 Perakitan prototipe | 1.6.2 Firmware C++ | ☐ |
| 38 | 1.5.4 Layanan pengirim perintah (MQTT) | 1.6.2 Firmware C++ | ☐ |
| 39 | 1.5.5 Dasbor admin | 1.7.1 Uji unit perangkat lunak | ☐ |
| 40 | 1.5.6 Pemantauan heartbeat dan notifikasi admin | 1.7.1 Uji unit perangkat lunak | ☐ |
| 41 | 1.7.1 Uji unit perangkat lunak | 1.8.2 Deploy perangkat lunak server dan pengamanan dasar | ☐ |
| 42 | 1.7.2 Uji pencocokan nama wilayah | 1.8.2 Deploy perangkat lunak server dan pengamanan dasar | ☐ |
| 43 | 1.4.3 Sewa server (VPS) dan domain | 1.8.2 Deploy perangkat lunak server dan pengamanan dasar | ☐ |
| 44 | 1.6.2 Firmware C++ | 1.6.3 Fitur heartbeat dan sambung ulang otomatis | ☐ |
| 45 | 1.6.3 Fitur heartbeat dan sambung ulang otomatis | 1.6.4 Fitur diagnosa jarak jauh | ☐ |
| 46 | 1.6.4 Fitur diagnosa jarak jauh | 1.7.3 Uji perangkat keras | ☐ |
| 47 | 1.7.3 Uji perangkat keras | 1.6.5 Perakitan unit produksi | ☐ |
| 48 | 1.8.2 Deploy perangkat lunak server dan pengamanan dasar | 1.7.4 Uji integrasi ujung ke ujung | ☐ |
| 49 | 1.7.3 Uji perangkat keras | 1.7.4 Uji integrasi ujung ke ujung | ☐ |
| 50 | 1.6.5 Perakitan unit produksi | 1.8.1 Pemasangan perangkat di lokasi | ☐ |
| 51 | 1.4.4 Izin pemasangan | 1.8.1 Pemasangan perangkat di lokasi | ☐ |
| 52 | 1.7.4 Uji integrasi ujung ke ujung | 1.7.5 Uji kegagalan | ☐ |
| 53 | 1.8.1 Pemasangan perangkat di lokasi | 1.8.3 Konfigurasi wilayah dan pendaftaran perangkat | ☐ |
| 54 | 1.8.2 Deploy perangkat lunak server dan pengamanan dasar | 1.8.3 Konfigurasi wilayah dan pendaftaran perangkat | ☐ |
| 55 | 1.8.1 Pemasangan perangkat di lokasi | 1.8.4 Sosialisasi ke warga | ☐ |
| 56 | 1.8.3 Konfigurasi wilayah dan pendaftaran perangkat | 1.7.6 Uji coba lapangan dan UAT | ☐ |
| 57 | 1.7.5 Uji kegagalan | 1.7.6 Uji coba lapangan dan UAT | ☐ |
| 58 | 1.8.3 Konfigurasi wilayah dan pendaftaran perangkat | 1.8.5 Pelatihan operator | ☐ |
| 59 | 1.7.6 Uji coba lapangan dan UAT | ◆ M4 UAT disetujui sponsor | ☐ |
| 60 | ◆ M4 UAT disetujui sponsor | 1.8.6 Serah terima dan dokumentasi | ☐ |
| 61 | 1.8.4 Sosialisasi ke warga | 1.8.6 Serah terima dan dokumentasi | ☐ |
| 62 | 1.8.5 Pelatihan operator | 1.8.6 Serah terima dan dokumentasi | ☐ |
| 63 | 1.8.6 Serah terima dan dokumentasi | ◆ M5 Sistem diserahterimakan | ☐ |
| 64 | ◆ M5 Sistem diserahterimakan | 1.1.4 Penutupan proyek dan lessons learned | ☐ |
| 65 | 1.1.4 Penutupan proyek dan lessons learned | ◆ M6 Proyek ditutup | ☐ |
