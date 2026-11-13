# Daftar ketergantungan jadwal UTS (Tabel 2.13 dan 2.12)

**A. Finish-to-Start (84 hubungan)**: dibuat otomatis oleh buat_clickup.py, atau dibuat manual di Gantt ClickUp bila memakai impor CSV. Tugas di kolom kanan baru mulai setelah tugas di kolom kiri selesai.

Cara manual di Gantt ClickUp: arahkan kursor ke batang di kolom **Pendahulu**, tarik titik di ujung kanannya ke batang di kolom **Tugas**.

| No | Pendahulu (selesai dulu) | Tugas (mulai sesudahnya) | ✓ |
|---|---|---|---|
| 1 | 1.1.1 Dokumen inisiasi | ◆ M0 Project Charter disahkan | ☐ |
| 2 | 1.1.1 Dokumen inisiasi | 1.1.2 Kick-off meeting dan Team Contract | ☐ |
| 3 | ◆ M0 Project Charter disahkan | 1.1.2 Kick-off meeting dan Team Contract | ☐ |
| 4 | ◆ M1 Kick-off meeting | 1.1.3 Rencana proyek | ☐ |
| 5 | ◆ M1 Kick-off meeting | 1.2.1 Kebutuhan pengguna | ☐ |
| 6 | ◆ M1 Kick-off meeting | 1.2.4 Kontrak mitra | ☐ |
| 7 | ◆ M1 Kick-off meeting | 1.2.5 Peta izin dan kepatuhan | ☐ |
| 8 | 1.2.5 Peta izin dan kepatuhan | 1.3.10 Pemenuhan izin dan pendaftaran sistem elektronik | ☐ |
| 9 | 1.2.1 Kebutuhan pengguna | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 10 | 1.2.2 Arsitektur sistem dan rancangan data | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 11 | 1.2.3 Desain antarmuka dan prototipe | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 12 | 1.2.4 Kontrak mitra | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 13 | 1.2.5 Peta izin dan kepatuhan | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 14 | 1.2.6 Lingkungan pengembangan | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 15 | 1.1.3 Rencana proyek | ◆ M2 Lingkup dan desain disetujui | ☐ |
| 16 | 1.2.2 Arsitektur sistem dan rancangan data | 1.3.1 Modul marketplace | ☐ |
| 17 | 1.2.3 Desain antarmuka dan prototipe | 1.3.1 Modul marketplace | ☐ |
| 18 | ◆ M2 Lingkup dan desain disetujui | 1.3.1 Modul marketplace | ☐ |
| 19 | 1.2.2 Arsitektur sistem dan rancangan data | 1.3.2 Modul pengiriman dan tracking | ☐ |
| 20 | 1.2.4 Kontrak mitra | 1.3.2 Modul pengiriman dan tracking | ☐ |
| 21 | ◆ M2 Lingkup dan desain disetujui | 1.3.2 Modul pengiriman dan tracking | ☐ |
| 22 | 1.2.2 Arsitektur sistem dan rancangan data | 1.3.3 Modul digital wallet | ☐ |
| 23 | 1.2.4 Kontrak mitra | 1.3.3 Modul digital wallet | ☐ |
| 24 | ◆ M2 Lingkup dan desain disetujui | 1.3.3 Modul digital wallet | ☐ |
| 25 | 1.2.6 Lingkungan pengembangan | 1.3.6 Infrastruktur produksi | ☐ |
| 26 | 1.2.3 Desain antarmuka dan prototipe | 1.3.4 Dasbor web UMKM dan panel admin | ☐ |
| 27 | 1.2.2 Arsitektur sistem dan rancangan data | 1.3.5 Fitur keamanan aplikasi | ☐ |
| 28 | 1.2.1 Kebutuhan pengguna | 1.3.12 Kesiapan operasional | ☐ |
| 29 | 1.3.4 Dasbor web UMKM dan panel admin | 1.3.11 Pelatihan dan pendaftaran UMKM Kota Yogyakarta | ☐ |
| 30 | 1.3.1 Modul marketplace | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 31 | 1.3.2 Modul pengiriman dan tracking | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 32 | 1.3.3 Modul digital wallet | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 33 | 1.3.4 Dasbor web UMKM dan panel admin | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 34 | 1.3.5 Fitur keamanan aplikasi | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 35 | 1.3.6 Infrastruktur produksi | 1.3.7 Pengujian fungsi dan integrasi | ☐ |
| 36 | 1.3.5 Fitur keamanan aplikasi | 1.3.8 Uji keamanan pertama | ☐ |
| 37 | 1.3.6 Infrastruktur produksi | 1.3.8 Uji keamanan pertama | ☐ |
| 38 | 1.3.7 Pengujian fungsi dan integrasi | 1.3.9 UAT Rilis 1 | ☐ |
| 39 | 1.3.8 Uji keamanan pertama | 1.3.13 Peluncuran Rilis 1 | ☐ |
| 40 | 1.3.9 UAT Rilis 1 | 1.3.13 Peluncuran Rilis 1 | ☐ |
| 41 | 1.3.10 Pemenuhan izin dan pendaftaran sistem elektronik | 1.3.13 Peluncuran Rilis 1 | ☐ |
| 42 | 1.3.12 Kesiapan operasional | 1.3.13 Peluncuran Rilis 1 | ☐ |
| 43 | 1.3.13 Peluncuran Rilis 1 | ◆ M3 Rilis 1 di Kota Yogyakarta | ☐ |
| 44 | 1.3.13 Peluncuran Rilis 1 | 1.1.6 Laporan evaluasi Rilis 1 | ☐ |
| 45 | ◆ M3 Rilis 1 di Kota Yogyakarta | 1.1.6 Laporan evaluasi Rilis 1 | ☐ |
| 46 | 1.3.13 Peluncuran Rilis 1 | 1.4.1 Desain Rilis 2 | ☐ |
| 47 | ◆ M3 Rilis 1 di Kota Yogyakarta | 1.4.1 Desain Rilis 2 | ☐ |
| 48 | 1.1.6 Laporan evaluasi Rilis 1 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | ☐ |
| 49 | 1.4.1 Desain Rilis 2 | 1.4.2 Modul rekomendasi AI | ☐ |
| 50 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.2 Modul rekomendasi AI | ☐ |
| 51 | 1.4.1 Desain Rilis 2 | 1.4.3 Aplikasi iOS | ☐ |
| 52 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.3 Aplikasi iOS | ☐ |
| 53 | 1.4.1 Desain Rilis 2 | 1.4.4 Fitur promosi berbayar UMKM | ☐ |
| 54 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.4 Fitur promosi berbayar UMKM | ☐ |
| 55 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.6 Perluasan layanan ke seluruh DIY | ☐ |
| 56 | 1.4.1 Desain Rilis 2 | 1.4.5 Laporan kinerja untuk manajemen | ☐ |
| 57 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.5 Laporan kinerja untuk manajemen | ☐ |
| 58 | ◆ M4 Evaluasi Rilis 1 dan keputusan lanjut | 1.4.7 Penambahan kapasitas infrastruktur | ☐ |
| 59 | 1.3.13 Peluncuran Rilis 1 | 1.5.1 Dokumentasi teknis dan panduan operasional | ☐ |
| 60 | 1.4.2 Modul rekomendasi AI | 1.4.8 Pengujian fungsi dan integrasi | ☐ |
| 61 | 1.4.3 Aplikasi iOS | 1.4.8 Pengujian fungsi dan integrasi | ☐ |
| 62 | 1.4.4 Fitur promosi berbayar UMKM | 1.4.8 Pengujian fungsi dan integrasi | ☐ |
| 63 | 1.4.5 Laporan kinerja untuk manajemen | 1.4.8 Pengujian fungsi dan integrasi | ☐ |
| 64 | 1.4.7 Penambahan kapasitas infrastruktur | 1.4.8 Pengujian fungsi dan integrasi | ☐ |
| 65 | 1.4.2 Modul rekomendasi AI | 1.4.9 Uji keamanan kedua | ☐ |
| 66 | 1.4.3 Aplikasi iOS | 1.4.9 Uji keamanan kedua | ☐ |
| 67 | 1.4.4 Fitur promosi berbayar UMKM | 1.4.9 Uji keamanan kedua | ☐ |
| 68 | 1.4.5 Laporan kinerja untuk manajemen | 1.4.9 Uji keamanan kedua | ☐ |
| 69 | 1.4.7 Penambahan kapasitas infrastruktur | 1.4.9 Uji keamanan kedua | ☐ |
| 70 | 1.4.9 Uji keamanan kedua | 1.4.12 Peluncuran Rilis 2 | ☐ |
| 71 | 1.4.10 UAT Rilis 2 | 1.4.12 Peluncuran Rilis 2 | ☐ |
| 72 | 1.4.11 Pelatihan UMKM empat kabupaten | 1.4.12 Peluncuran Rilis 2 | ☐ |
| 73 | 1.4.6 Perluasan layanan ke seluruh DIY | 1.4.12 Peluncuran Rilis 2 | ☐ |
| 74 | 1.4.12 Peluncuran Rilis 2 | ◆ M5 Rilis 2 | ☐ |
| 75 | 1.4.12 Peluncuran Rilis 2 | 1.5.2 Alih pengetahuan ke tim operasional | ☐ |
| 76 | ◆ M5 Rilis 2 | 1.5.2 Alih pengetahuan ke tim operasional | ☐ |
| 77 | 1.4.12 Peluncuran Rilis 2 | 1.5.4 Penutupan kontrak proyek | ☐ |
| 78 | ◆ M5 Rilis 2 | 1.5.4 Penutupan kontrak proyek | ☐ |
| 79 | 1.4.12 Peluncuran Rilis 2 | 1.5.5 Laporan akhir dan lessons learned | ☐ |
| 80 | ◆ M5 Rilis 2 | 1.5.5 Laporan akhir dan lessons learned | ☐ |
| 81 | 1.5.1 Dokumentasi teknis dan panduan operasional | 1.5.3 Berita acara serah terima | ☐ |
| 82 | 1.5.2 Alih pengetahuan ke tim operasional | 1.5.3 Berita acara serah terima | ☐ |
| 83 | 1.5.3 Berita acara serah terima | ◆ M6 Penutupan proyek dan serah terima | ☐ |
| 84 | 1.5.5 Laporan akhir dan lessons learned | ◆ M6 Penutupan proyek dan serah terima | ☐ |

**B. Hubungan lain (6 hubungan)**: TIDAK dibuat di ClickUp, karena pendahulu belum selesai ketika tugas dimulai (pola "mulai bersamaan" atau "mulai sebelum pendahulu selesai" di Tabel 2.13). ClickUp hanya mengenal Finish-to-Start, jadi hubungan ini cukup dijelaskan di laporan.

| No | Pendahulu | Tugas | Pendahulu selesai | Tugas mulai |
|---|---|---|---|---|
| 1 | 1.1.2 Kick-off meeting dan Team Contract | ◆ M1 Kick-off meeting | 08 Jan | 06 Jan |
| 2 | 1.2.1 Kebutuhan pengguna | 1.2.2 Arsitektur sistem dan rancangan data | 22 Jan | 11 Jan |
| 3 | 1.2.1 Kebutuhan pengguna | 1.2.3 Desain antarmuka dan prototipe | 22 Jan | 11 Jan |
| 4 | 1.2.4 Kontrak mitra | 1.2.6 Lingkungan pengembangan | 29 Jan | 18 Jan |
| 5 | 1.4.6 Perluasan layanan ke seluruh DIY | 1.4.11 Pelatihan UMKM empat kabupaten | 04 Jun | 17 May |
| 6 | 1.4.8 Pengujian fungsi dan integrasi | 1.4.10 UAT Rilis 2 | 08 Jun | 07 Jun |
