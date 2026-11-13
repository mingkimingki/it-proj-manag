# Petunjuk: Memasukkan WBS dan Jadwal UTS ke ClickUp

> Tujuan: Gantt Chart UTS (Bab 2.3.4) dibuat di alat digital, lalu tangkapan layarnya masuk laporan PDF.
> Isinya sama dengan draf: **5 cabang level 2, 42 paket kerja, 7 milestone, 84 ketergantungan**.
> Jadwal: **Senin, 4 Januari 2027** sampai **Rabu, 30 Juni 2027**. Tanggal diambil langsung dari Tabel 2.13 dan 2.12.
> Cara kerjanya sama dengan Tugas 2 (`tugas2/clickup/`), yang skrip API-nya sudah berhasil dijalankan (57 tugas, 65 ketergantungan).

---

## Langkah 1. Siapkan Space dan List

1. Masuk ke ClickUp (akun yang sama dengan Tugas 2 boleh).
2. Buat ***Space*** baru, misalnya **UTS ITPM**.
3. Di dalamnya, buat ***List*** kosong bernama **Super App Nusantara Express (UTS ITPM)**. List ini adalah **level 1 WBS**.
4. Buka List itu dan lihat alamat web di browser. Angka setelah `/li/` adalah **List ID**.
   Contoh: `https://app.clickup.com/9012345/v/li/901234567` → List ID = `901234567`.

---

## Langkah 2. Isi lewat skrip API (cara utama)

1. **API token:** pakai token dari Tugas 2, atau buat baru lewat foto profil → **Settings** → **Apps** → **API Token** → **Generate**. Token diawali `pk_`.
   **Jaga kerahasiaan token** seperti kata sandi. Jangan simpan di berkas proyek, jangan di-*commit* ke Git, dan jangan ditempel ke percakapan dengan AI.
2. Buka terminal di folder ini (`uts/clickup/`), lalu jalankan:

   ```
   export CLICKUP_TOKEN="pk_tempel_token_di_sini"
   python3 buat_clickup.py --uji 901234567
   ```

   Ganti `901234567` dengan List ID. Mode `--uji` **hanya menampilkan rencana**; belum ada yang dikirim.
3. Kalau tampilannya wajar, jalankan tanpa `--uji`:

   ```
   python3 buat_clickup.py 901234567
   ```

   Prosesnya sekitar 2–3 menit (54 tugas + 84 ketergantungan = 138 permintaan, dengan jeda agar tidak melampaui batas paket gratis).
4. **Bila berhenti di tengah jalan**, jalankan ulang perintah yang sama. Yang sudah dibuat tercatat di `clickup_id.json` dan tidak dibuat dua kali.
5. **Bila muncul pesan gagal**, salin pesannya (tanpa token) dan tanyakan.

### Cadangan: impor CSV

Bila skrip tidak bisa dipakai, impor **`clickup_import_uts.csv`** lewat menu **Import → Spreadsheet/CSV**. Pemetaan kolomnya sama dengan Tugas 2 (lihat `tugas2/clickup/PETUNJUK_CLICKUP.md`, Langkah 2A). Ketergantungan tidak ikut terimpor; buat manual mengikuti **`ketergantungan.md` bagian A**.

---

## Langkah 3. Tampilkan Gantt

1. Di bagian atas List, klik **+ View** → **Gantt**.
2. Tampilkan *subtask* (**Subtasks → Expanded**) supaya 42 paket kerja terlihat.
3. Aktifkan **Show critical path** bila tersedia. Bila tidak tersedia di paket gratis, tidak masalah: tugas di jalur kritis sudah diberi *tag* **jalur-kritis**.
4. Atur skala ke **Week** atau **Month** supaya Januari–Juni 2027 terlihat.

**Catatan:** ada **6 hubungan** di Tabel 2.13 yang sengaja **tidak** dibuat sebagai ketergantungan, misalnya "mulai bersamaan" (1.4.6 dan 1.4.11) dan "mulai sebelum pendahulu selesai" (UAT 1.4.10 mulai sebelum pengujian 1.4.8 selesai). ClickUp hanya mengenal pola "selesai lalu mulai". Daftarnya ada di `ketergantungan.md` bagian B dan dijelaskan di laporan.

---

## Langkah 4. Ambil bukti

Simpan tangkapan layar di folder **`uts/clickup/bukti/`** dengan nama berikut, supaya bisa langsung dipakai skrip perakitan laporan:

| Berkas | Isi |
|---|---|
| `01_list.png` | Tampilan **List**: WBS bertingkat (level 2 dan *subtask*) |
| `02_gantt.png` | Tampilan **Gantt** keseluruhan: batang, panah ketergantungan, dan milestone |
| `03_gantt_rilis1.png` (opsional) | Gantt diperbesar di sekitar Rilis 1 (Februari–Maret) agar tulisan terbaca |

Lalu buat **tautan publik**: di tampilan Gantt, **Share** → aktifkan **public link** → salin tautannya dan berikan ke Claude untuk dicantumkan di laporan.

---

## Isi folder ini

| Berkas | Fungsi |
|---|---|
| `siapkan_clickup.py` | Membaca Tabel 2.11–2.13 dari `../draf/01_pmbok4.md`, lalu membuat CSV dan daftar ketergantungan. Jalankan ulang (`python3 siapkan_clickup.py`) bila jadwal di draf berubah |
| `buat_clickup.py` | Skrip API (cara utama) |
| `perbarui_tag.py` | Menyesuaikan *tag* "jalur-kritis" dan deskripsi tugas bila jalur kritis di Tabel 2.13 berubah (`python3 perbarui_tag.py --uji`, lalu tanpa `--uji`) |
| `clickup_import_uts.csv` | Berkas impor CSV (cadangan) |
| `ketergantungan.md` | Bagian A: 84 ketergantungan yang dibuat. Bagian B: 6 hubungan yang tidak dibuat |
| `clickup_id.json` | Dibuat otomatis saat skrip dijalankan; catatan tugas yang sudah dibuat. Tidak berisi token |
| `bukti/` | Tangkapan layar untuk laporan |

## Istilah

| Istilah | Penjelasan |
|---|---|
| *Space* | Area kerja di ClickUp yang berisi beberapa *List* |
| *List* | Daftar tugas; di sini mewakili proyek (level 1 WBS) |
| *Task* / *Subtask* | Tugas / tugas di dalam tugas lain; di sini level 2 dan level 3 WBS |
| *Tag* | Label pada tugas: penanggung jawab (pm, se, ux, ic, bd, ol, lc) dan "jalur-kritis" |
| API | Jalur bagi program untuk berkomunikasi dengan aplikasi lain secara otomatis |
| API token | Kunci rahasia yang memberi izin kepada program untuk mengakses akun ClickUp |
| List ID | Nomor unik sebuah *List*, terlihat di alamat web |
| *Finish-to-Start* | Jenis ketergantungan: tugas baru mulai setelah pendahulunya selesai |
