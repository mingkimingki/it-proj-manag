# Petunjuk: Memasukkan WBS dan Jadwal Tugas 2 ke ClickUp

> Tujuan: memenuhi syarat soal "file tools digital (Jira/ClickUp/MS Project)".
> Isi yang dimasukkan sama persis dengan laporan PDF: 8 fase, 43 *work package*, 6 milestone, dan 65 ketergantungan.
> Jadwal dimulai **Senin, 4 Januari 2027** dan selesai **Selasa, 11 Mei 2027** (92 hari kerja, Senin–Jumat; hari libur nasional tidak dihitung).
> Nama tombol dan menu ClickUp bisa sedikit berbeda karena aplikasinya sering diperbarui.

---

## Langkah 1. Siapkan akun dan List (wajib untuk pilihan A dan B)

1. Buka **clickup.com**, daftar dengan email atau akun Google, lalu pilih paket **Free**.
2. Buat satu ***Space*** (area kerja), misalnya "Tugas 2 ITPM".
3. Di dalam Space itu, buat satu ***List*** (daftar tugas) bernama **SPDC - Sistem Peringatan Dini Cuaca Publik**. List ini adalah **level 1 WBS** (proyek).
4. **Untuk pilihan B:** buka List itu, lalu lihat alamat web di browser. Angka setelah `/li/` adalah **List ID**. Contoh: `https://app.clickup.com/9012345/v/li/901234567` → List ID = `901234567`.

Kalau ingin anggota kelompok lain ikut melihat, undang mereka lewat tombol **Invite**.

---

## Langkah 2A. Pilihan A: impor CSV, lalu buat ketergantungan manual

1. Di List tadi, buka menu **Import** (biasanya lewat ikon ⋯ atau **Settings → Import/Export**), lalu pilih **Spreadsheet / CSV**.
2. Unggah berkas **`clickup_import_spdc.csv`**.
3. Saat diminta mencocokkan kolom (*mapping*), pasangkan:

| Kolom di CSV | Bidang ClickUp |
|---|---|
| Task ID | Task ID |
| Task Name | Task Name |
| Description | Description |
| Start Date | Start Date (format tahun-bulan-tanggal, misalnya 2027-01-04) |
| Due Date | Due Date |
| Tags | Tags (pemisah: koma) |
| Subtask IDs | Subtask IDs (pemisah: koma, tanpa spasi) |

4. Jalankan impor. Hasilnya: 8 fase sebagai *task*, 43 *work package* sebagai *subtask*, dan 6 milestone.
5. **Ketergantungan tidak ikut terimpor lewat CSV.** Buat manual di tampilan Gantt (Langkah 3) mengikuti daftar di **`ketergantungan.md`**: 65 baris, sudah diurutkan dari tugas paling awal, dengan kotak centang.

---

## Langkah 2B. Pilihan B: skrip otomatis lewat API

*API* (*Application Programming Interface*) adalah jalur bagi program untuk mengisi ClickUp tanpa diklik manual. Skrip ini membuat semua tugas, subtask, tanggal, **dan ke-65 ketergantungan** sekaligus.

1. **Buat API token pribadi:** klik foto profil (pojok kiri bawah) → **Settings** → **Apps** → **API Token** → **Generate**. Salin token yang diawali `pk_`.
   **Jaga kerahasiaan token** ini seperti kata sandi. Jangan simpan di berkas proyek, jangan di-commit ke Git, dan jangan ditempel ke percakapan dengan AI.
2. Buka terminal di folder ini (`tugas2/clickup/`), lalu jalankan:

   ```
   export CLICKUP_TOKEN="pk_tempel_token_anda_di_sini"
   python3 buat_clickup.py --uji 901234567
   ```

   Ganti `901234567` dengan List ID Anda. Mode `--uji` **hanya menampilkan rencana**; belum ada yang dikirim ke ClickUp.
3. Kalau tampilannya wajar, jalankan tanpa `--uji`:

   ```
   python3 buat_clickup.py 901234567
   ```

   Prosesnya sekitar 2–3 menit (122 permintaan, dengan jeda supaya tidak melampaui batas paket gratis).
4. **Kalau berhenti di tengah jalan** (misalnya internet putus atau muncul pesan gagal), jalankan ulang perintah yang sama. Tugas yang sudah dibuat tercatat di `clickup_id.json` dan tidak akan dibuat dua kali.
5. Kalau muncul pesan gagal yang tidak jelas, salin pesannya (tanpa token) dan tanyakan.

Skrip ini **belum pernah diuji langsung ke ClickUp**, karena penyusunnya tidak memiliki akses. Bila gagal, pilihan A tetap bisa dipakai.

---

## Langkah 3. Tampilkan Gantt Chart dan jalur kritis

1. Di bagian atas List, klik **+ View** → pilih **Gantt**.
2. Di pengaturan tampilan Gantt, tampilkan *subtask* (misalnya **Subtasks → Expanded**) supaya *work package* terlihat.
3. Aktifkan **Show critical path** di pengaturan Gantt (ikon roda gigi). Tugas di jalur kritis akan berwarna merah.
   **Bila pilihan ini tidak tersedia di paket gratis**, tidak masalah: tugas di jalur kritis sudah diberi *tag* **jalur-kritis**, dan perhitungan lengkapnya ada di laporan (Bab 4.4 dan Lampiran B).
4. Atur skala tampilan ke **Week** atau **Month** supaya seluruh proyek (Januari–Mei 2027) terlihat.

---

## Langkah 4. Ambil bukti untuk dikumpulkan

1. **Tangkapan layar:**
   - tampilan **List** (memperlihatkan WBS bertingkat: fase dan *subtask*),
   - tampilan **Gantt** (memperlihatkan batang, panah ketergantungan, dan milestone; satu gambar untuk keseluruhan dan satu gambar diperbesar bila perlu).
2. **Tautan berbagi:** di tampilan Gantt, pilih **Share** → aktifkan **public link** (tautan publik) → salin tautannya.
3. **Bentuk "file tools digital" yang diminta dosen belum jelas**: tautan, berkas ekspor, atau tangkapan layar. Sebaiknya tanyakan ke dosen. Sambil menunggu, siapkan ketiganya.

---

## Isi folder ini

| Berkas | Fungsi |
|---|---|
| `clickup_import_spdc.csv` | Berkas impor untuk pilihan A |
| `ketergantungan.md` | Daftar 65 ketergantungan untuk dibuat manual (pilihan A) |
| `buat_clickup.py` | Skrip API untuk pilihan B |
| `siapkan_clickup.py` | Pembuat CSV dan daftar ketergantungan dari `../draf/laporan_tugas2.md`. Jalankan ulang (`python3 siapkan_clickup.py`) bila isi laporan berubah |
| `clickup_id.json` | Dibuat otomatis oleh `buat_clickup.py`; catatan tugas yang sudah dibuat. Tidak berisi token |

## Istilah

| Istilah | Penjelasan |
|---|---|
| *Space* | Area kerja di ClickUp yang berisi beberapa *List* |
| *List* | Daftar tugas; di sini mewakili proyek (level 1 WBS) |
| *Task* / *Subtask* | Tugas / tugas di dalam tugas lain; di sini fase (level 2) dan *work package* (level 3) |
| *Tag* | Label pada tugas, misalnya peran penanggung jawab (mp, as, ps, ei, qa, tl) atau "jalur-kritis" |
| API | Jalur bagi program untuk berkomunikasi dengan aplikasi lain secara otomatis |
| API token | Kunci rahasia yang memberi izin kepada program untuk mengakses akun ClickUp Anda |
| List ID | Nomor unik sebuah *List*, terlihat di alamat web |
| *Mapping* | Mencocokkan kolom di berkas CSV dengan bidang di ClickUp saat impor |
