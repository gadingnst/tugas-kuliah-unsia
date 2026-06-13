# Analisis Sistem Informasi Peminjaman Buku Perpustakaan
**Mata Kuliah:** Rekayasa Perangkat Lunak (IF603)  
**Tugas:** Ujian Tengah Semester (UTS)  
**Mahasiswa:** Sutan Gading Fadhillah Nasution  
**NIM:** 250401020159  
**Dosen Pengampu:** Cian Ramadhona Hassolthine, S.Kom., M.Kom  

---

## 1. Pendahuluan
Dokumen ini merupakan hasil analisis mendalam terhadap spesifikasi kebutuhan dan perancangan terstruktur (*Structured Analysis*) untuk Sistem Informasi Peminjaman Buku di Perpustakaan berdasarkan dokumen studi kasus yang diberikan. 

Tujuan dari analisis ini adalah untuk membedah alur proses bisnis sistem, memverifikasi kesesuaian diagram aliran data (DFD), memetakan struktur data melalui Kamus Data, serta mengidentifikasi kesalahan logis (*logic defect*) atau inkonsistensi perancangan yang terdapat pada dokumen studi kasus asli demi memberikan rekomendasi perbaikan yang tepat.

---

## 2. Deskripsi Alur Bisnis Sistem
Berdasarkan dokumen studi kasus, sistem peminjaman buku perpustakaan memiliki alur operasional sebagai berikut:
1. **Pendaftaran Anggota:** Calon anggota menyerahkan identitas diri ke petugas perpustakaan. Petugas memeriksa dan mencatat data tersebut ke dalam sistem (jika belum terdaftar), lalu mencetak Kartu Anggota untuk diserahkan ke peminjam.
2. **Proses Peminjaman:** Anggota menyerahkan kode buku yang ingin dipinjam beserta Kartu Anggota ke petugas administrasi.
3. **Validasi & Pencatatan Buku:** Petugas memeriksa ketersediaan buku di sistem. Jika buku tersedia, petugas mencatat peminjaman tersebut ke catatan peminjaman, menyimpan kartu buku, lalu mencetak Bukti Peminjaman Buku.
4. **Penyerahan Buku:** Anggota menerima buku fisik beserta Bukti Peminjaman Buku.
5. **Penyediaan Buku:** Stok buku fisik yang tersedia di perpustakaan diperoleh dan disuplai oleh Bagian Pengadaan.
6. **Pelaporan:** Sistem secara periodik menghasilkan output berupa:
   * **Laporan Peminjaman** yang ditujukan kepada Pimpinan.
   * **Daftar Pengeluaran Buku** yang ditujukan kepada Bagian Pengadaan.

*Analisis Kritis:
* **Temuan Typo pada Deskripsi Kasus:** Pada dokumen studi kasus asli halaman 1, terdapat kesalahan penulisan *"...lalu dibuatkan kartu anggoa"*.
* **Analisis & Solusi:** Istilah yang benar adalah **"anggota"**. Kesalahan tik ini sebaiknya dikoreksi pada dokumentasi sistem agar bersifat formal dan tidak menimbulkan ambiguitas bagi pengembang.

---

## 3. Komponen Perancangan Terstruktur

### A. Entitas Luar (External Entities)
Sistem berinteraksi dengan 3 entitas luar utama:
1. **Anggota:** Aktor yang melakukan pendaftaran dan melakukan peminjaman buku.
2. **Bagian Pengadaan:** Aktor yang menyuplai buku ke perpustakaan serta menerima daftar pengeluaran buku untuk analisis stok/pengadaan baru.
3. **Pimpinan:** Aktor yang menerima laporan pertanggungjawaban peminjaman buku.

### B. Kebutuhan Fungsional (Requirements Mapping)
Sistem dibagi menjadi beberapa fungsi utama yang dikelompokkan ke dalam proses level atas:
* **Proses 1.0 (Pendaftaran):**
  * `1.1` Cari data anggota
  * `1.2` Rekam data anggota
  * `1.3` Cetak kartu anggota
* **Proses 2.0:** Rekam data buku
* **Proses 3.0:** Cari dan tampilkan status buku
* **Proses 4.0 (Peminjaman):**
  * `4.1` Rekam peminjaman
  * `4.2` Cetak bukti peminjaman
  * `4.3` Update buku (stok)
* **Proses 5.0 (Pelaporan):**
  * `5.1` Cetak daftar pengeluaran buku (untuk Bagian Pengadaan)
  * `5.2` Cetak laporan peminjaman (untuk Pimpinan)

### C. Data Store (Penyimpanan Data)
Terdapat 3 penyimpanan data utama yang digunakan oleh sistem:
1. **Anggota:** Menyimpan data identitas anggota perpustakaan.
2. **Buku:** Menyimpan katalog buku beserta jumlah stok yang tersedia.
3. **Peminjaman:** Menyimpan riwayat transaksi peminjaman buku.

---

## 4. Penjelasan Diagram-Diagram dalam Studi Kasus

### A. Diagram Konteks (Halaman 2)
Diagram Konteks menggambarkan sistem **"Sistem Peminjaman Buku"** sebagai satu proses tunggal (*black box*) yang berinteraksi dengan tiga entitas luar. Berikut adalah rincian aliran data yang tergambar:

| Arah | Dari | Ke | Aliran Data |
|------|------|----|-------------|
| Masuk | Anggota | Sistem | `Id-anggota` (data identitas untuk pendaftaran) |
| Masuk | Anggota | Sistem | `Kd-Buku Pinjaman` (kode buku yang ingin dipinjam) |
| Masuk | Anggota | Sistem | `Info Status Buku` (permintaan cek status buku) |
| Keluar | Sistem | Anggota | `Kartu Anggota` (hasil pendaftaran) |
| Keluar | Sistem | Anggota | `Bukti Pinjaman` (bukti transaksi peminjaman) |
| Keluar | Sistem | Anggota | `Info Status Buku` (hasil pengecekan status) |
| Masuk | Bag. Pengadaan | Sistem | `Id-buku` (data buku baru yang disuplai) |
| Keluar | Sistem | Bag. Pengadaan | `Daftar Pengeluaran Buku` (laporan buku yang keluar/dipinjam) |
| Keluar | Sistem | Pimpinan | `Laporan Penjualan` |

Diagram Konteks ini berfungsi untuk memberikan gambaran umum (*high-level view*) tentang batasan sistem — apa saja yang masuk dan keluar dari sistem serta siapa aktor yang terlibat, tanpa menunjukkan detail proses internal.

*Analisis Kritis:
* **Temuan Kesalahan Aliran Data:** Aliran data dari sistem ke entitas **Pimpinan** bertuliskan **"Laporan Penjualan"**.
* **Analisis & Solusi:** Domain sistem ini adalah **Peminjaman Buku Perpustakaan**, bukan ritel atau e-commerce. Pimpinan perpustakaan seharusnya menerima **"Laporan Peminjaman"** sesuai dengan deskripsi kebutuhan bisnis. Rekomendasi perbaikannya adalah mengubah nama aliran data tersebut menjadi **"Laporan Peminjaman"** agar sesuai dengan proses bisnis perpustakaan.

### B. DFD Level-0 (Halaman 3)
DFD Level-0 memecah sistem menjadi **5 proses utama** beserta koneksinya ke Data Store dan entitas luar. Berikut penjelasan setiap proses yang tergambar:

**Proses-proses:**
1. **`1.0 Pendaftaran`** — Menerima `Id-anggota` dari entitas Anggota, memproses pendaftaran, lalu menghasilkan `Kartu Anggota` yang dikirim kembali ke Anggota. Proses ini terhubung ke Data Store `Anggota` untuk membaca dan menyimpan data anggota.
2. **`2.0 Rekam dt-buku`** — Menerima `Id-buku` dari entitas Bag. Pengadaan, lalu menyimpan data buku ke Data Store `Buku`. Proses ini berfungsi mencatat buku-buku baru yang masuk ke perpustakaan.
3. **`3.0 Cari & tampilkan status bku`** — Menerima `Info Status Buku` dari Anggota dan mengembalikan `Info Status Buku` ke Anggota.
4. **`4.0 Peminjaman`** — Menerima `Kd-Buku Pinjaman` dan `Kartu Anggota` dari Anggota. Proses ini terhubung ke Data Store `Peminjaman` (untuk menulis data peminjaman) dan Data Store `Buku` (membaca data buku via aliran `Dt Buku Ada`). Menghasilkan output berupa buku fisik dan bukti peminjaman.
5. **`5.0 Pelaporan`** — Membaca data dari Data Store `Peminjaman` dan `Buku`, kemudian menghasilkan dua output: `Lapoan Pemianjaman` ke Pimpinan, dan `Daftar Pengeluaran Buku` ke Bag. Pengadaan.

**Data Store yang tergambar:**
* `Anggota` — terhubung ke proses 1.0
* `Buku` — terhubung ke proses 2.0, 4.0, dan 5.0
* `Peminjaman` — terhubung ke proses 4.0 dan 5.0

*Analisis Kritis:
* **Temuan Cacat Logika (Black Hole / Miracle Process) pada Proses 3.0:** Proses `3.0 Cari & tampilkan status bku` menerima input dan menghasilkan output tetapi tidak terhubung ke *Data Store* manapun.
  * **Analisis & Solusi:** Secara prinsip RPL, proses pencarian status buku mustahil memberikan informasi status buku secara dinamis tanpa membaca data dari Data Store `Buku`. Ini melanggar aturan dasar perancangan DFD. Solusinya, tambahkan aliran data bertipe *read* (panah dari *Data Store* ke proses) antara Data Store `Buku` dengan proses `3.0`.
* **Temuan Typo Aliran Data:** Aliran data ke Pimpinan tertulis **`Lapoan Pemianjaman`**.
  * **Analisis & Solusi:** Terdapat kesalahan ketik (kurang huruf 'r' pada Laporan dan kelebihan huruf 'i' pada Peminjaman). Solusinya, ubah penulisan menjadi **"Laporan Peminjaman"** agar konsisten dengan standar dokumen formal.

### C. DFD Level-1 Proses 1.0: Pendaftaran (Halaman 3)
Diagram ini mendekomposisi proses `1.0 Pendaftaran` menjadi 3 sub-proses:

1. **`1.1 Cari dt Anggota`** — Menerima `Id anggota` dari entitas Anggota, lalu melakukan pencarian apakah anggota sudah terdaftar atau belum. Jika sudah terdaftar, data anggota diteruskan langsung.
2. **`1.2 Rekam data Anggota`** — Menerima `Data anggota` dari proses 1.1 (jika anggota belum terdaftar), lalu merekam data anggota baru ke dalam penyimpanan.
3. **`1.3 Cetak Kartu Anggota`** — Menerima data dari proses 1.2, kemudian mencetak `Kartu anggota` yang dikirimkan ke entitas Anggota.

**Aliran Data:**
* `Anggota` → *(Id anggota)* → `1.1` → *(Data anggota)* → `1.2` → `1.3` → *(Kartu anggota)* → `Anggota`

*Analisis Kritis:
* **Temuan Cacat DFD (Hilangnya Penyimpanan Data):** DFD Level-1 Proses 1.0 Pendaftaran ini sama sekali tidak menampilkan Data Store `Anggota`.
  * **Analisis & Solusi:** Sub-proses `1.1` memerlukan akses *read* dan sub-proses `1.2` memerlukan akses *write* ke Data Store `Anggota` agar pencarian dan perekaman data anggota dapat berjalan secara nyata. Ketiadaan Data Store ini menyebabkan proses-proses tersebut tergolong sebagai *Miracle Process*. Solusinya, munculkan Data Store `Anggota` di diagram DFD Level-1 ini, lalu buat aliran data bertipe *read* ke proses `1.1` dan aliran bertipe *write* dari proses `1.2` ke Data Store.

### D. DFD Level-1 Proses 4.0: Peminjaman (Halaman 4)
Diagram ini mendekomposisi proses `4.0 Peminjaman` menjadi 3 sub-proses:

1. **`4.1 Rekam Peminjaman`** — Mencatat transaksi peminjaman baru. Terhubung ke Data Store `Peminjam(an)` untuk menyimpan record peminjaman, dan membaca `Data buku ada` dari Data Store `Buku` untuk memvalidasi ketersediaan buku.
2. **`4.2 Cetak Bukti Peminajaman`** — Menerima data dari proses 4.1, kemudian mencetak bukti peminjaman yang diserahkan ke entitas Anggota.
3. **`4.3 Update Bukti Peminjaman`** — Memperbarui data di Data Store `Buku` setelah peminjaman berhasil direkam (mengurangi stok).

**Data Store yang tergambar:**
* `Buku` — terhubung ke proses 4.1 (read: `Data buku ada`) dan proses 4.3 (write: update stok)
* `Peminjam(an)` — terhubung ke proses 4.1 (write: rekam peminjaman)

**Aliran Data:**
* `Anggota` → `4.1` → `4.2` → *(Bukti Peminjaman)* → `Anggota`
* `4.1` → `4.3` → update Data Store `Buku`

*Analisis Kritis:
* **Temuan Kesalahan Label Proses 4.3:** Di DFD Level-1 Proses 4.0, proses `4.3` diberi label **"Update Bukti Peminjaman"**.
  * **Analisis & Solusi:** Berdasarkan daftar kebutuhan awal, fungsi proses 4.3 adalah memutakhirkan stok buku di database. Nama "Update Bukti Peminjaman" sangat menyesatkan karena mengindikasikan modifikasi terhadap arsip bukti transaksi, bukan pengurangan stok buku. Solusinya, ubah label proses 4.3 menjadi **"Update Buku"** agar selaras dengan kebutuhan fungsional sistem.
* **Temuan Aliran Data Masuk & Keluar Tidak Lengkap pada Proses 4.1:** Aliran data input dari entitas Anggota (`Kd-Buku Pinjaman` dan `Kartu Anggota`) serta aliran *write* ke Data Store `Peminjaman` tidak digambarkan secara eksplisit dan lengkap.
  * **Analisis & Solusi:** Tanpa aliran masukan yang jelas, diagram tidak menunjukkan dari mana data transaksi diperoleh oleh sub-proses 4.1. Solusinya, tambahkan visualisasi aliran data masukan dari entitas Anggota ke proses 4.1, dan pastikan panah aliran data dari proses 4.1 ke Data Store `Peminjaman` tergambar jelas.
* **Temuan Typo Label Proses 4.2:** Proses `4.2` berlabel **"Cetak Bukti Peminajaman"**.
  * **Analisis & Solusi:** Terjadi typo pada kata "Peminajaman" (kelebihan huruf 'a' sebelum 'j'). Solusinya, koreksi label menjadi **"Cetak Bukti Peminjaman"**.

### E. DFD Level-1 Proses 5.0: Pelaporan (Halaman 4)
Diagram ini mendekomposisi proses `5.0 Pelaporan` menjadi 2 sub-proses:

1. **`5.1 Cetak Laporan`** — Membaca data dari Data Store `Peminjaman`, kemudian menghasilkan `Lap. Peminjaman` yang ditujukan ke entitas Pimpinan.
2. **`5.2 Cetak Daftar Pengeluaran`** — Membaca data dari Data Store `Buku`, kemudian menghasilkan `Daftar Pengeluaran` yang ditujukan ke entitas Bag. Pengadaan.

**Data Store yang tergambar:**
* `Peminjaman` — terhubung ke proses 5.1 (read)
* `Buku` — terhubung ke proses 5.2 (read)

**Aliran Data:**
* Data Store `Peminjaman` → `5.1` → *(Lap. Peminjaman)* → `Pimpinan`
* Data Store `Buku` → `5.2` → *(Daftar Pengeluaran)* → `Bag. Pengadaan`

*Analisis Kritis:
* **Analisis Aliran Data:** Aliran data secara visual di DFD Level-1 Proses 5.0 sudah benar dan konsisten memecah proses 5.0 Level-0. Kesalahan yang berkaitan dengan bagian ini terletak pada penamaan label pada bagian detail Spesifikasi Proses (yang dibahas di bagian analisis Spesifikasi Proses).

### F. Diagram ER / Pemodelan Data (Halaman 5)
Diagram Entity-Relationship (ER) menggambarkan hubungan antar entitas data dalam sistem. Terdapat 3 entitas utama:

1. **Entitas `Anggota`**
   * Atribut: `Kd-anggota` (PK), `Nm-anggota`, `Tgl-lahir`, `Tgl-daftar`
   * Relasi: **Melakukan** → terhubung ke entitas `Peminjaman`

2. **Entitas `Peminjaman`**
   * Atribut: `No-pinjam` (PK), `Tgl-pinjam`, `Tgl-kembali`
   * Relasi: Merupakan entitas penghubung (*associative entity*) antara `Anggota` dan `Buku`

3. **Entitas `Buku`**
   * Atribut: `Kd-buku` (PK), `Judul`, `Penerbit`, `Pengarang`, `Stok`
   * Relasi: **Terdiri dr** → terhubung ke entitas `Peminjaman`

**Hubungan Relasi:**
* `Anggota` — *(Melakukan)* → `Peminjaman` — *(Terdiri dr)* → `Buku`
* Satu anggota dapat **melakukan** banyak peminjaman, dan satu peminjaman **terdiri dari** buku yang dipinjam. Diagram ini menunjukkan hubungan *many-to-many* antara Anggota dan Buku yang dijembatani oleh entitas Peminjaman.

*Analisis Kritis:
* **Analisis Struktur ER:** Pemodelan ER secara konseptual sudah tepat. Entitas `Peminjaman` berfungsi sebagai entitas asosiatif untuk memecah relasi *many-to-many* antara `Anggota` dan `Buku`. Atribut kunci utama (*Primary Key*) seperti `Kd-anggota`, `No-pinjam`, dan `Kd-buku` juga telah terpetakan dengan baik untuk menjamin integritas data.

---

## 5. Analisis Kamus Data & Spesifikasi Proses

### A. Kamus Data (Data Dictionary)
Kamus data mendefinisikan struktur elemen data yang mengalir dalam sistem maupun yang disimpan di dalam *data store*:
* **Struktur Penyimpanan (Data Store):**
  * `Anggota` = `@Kd-anggota` + `nm-anggota` + `tgl-lahir` + `tgl_daftar`
  * `Buku` = `@Kd-buku` + `judul` + `penerbit` + `pengarang` + `stok`
  * `Pinjaman` = `@no-pinjam` + `tgl_pinjam` + `tgl_kembali` + `kd-anggota` + `kd_buku`
* **Aliran Data Utama:**
  * `Id-anggota` = `nm_anggota` + `tgl_lahir` + `no_identitas` (input pendaftaran)
  * `Kartu Anggota` = `@Kd-anggota` + `nm-anggota` + `tgl-lahir` + `tgl_daftar` + `masa_berlaku`
  * `Bukti-pinjaman` = `no-bukti` + `kd-anggota` + `nm_anggota` + `tgl-pinjam` + `{kd_buku + judul + pengarang + penerbit}` + `tgl_hrs_kembali` + `nm_petugas`

*Analisis Kritis:
* **Temuan Ketidakkonsistenan Penulisan Variabel (Naming Convention) & Typo:**
  * Terjadi pencampuran karakter penghubung seperti dash `-` dan underscore `_` (contoh: `tgl-lahir` vs `tgl_daftar`).
  * Di Kamus Data Aliran Data (Halaman 5), terdapat field `tgl_lahit` (typo huruf 'r' menjadi 't') dan `no_identitas`, padahal di *Data Store* Anggota menggunakan field `tgl-lahir`.
  * **Analisis & Solusi:** Inkonsistensi penamaan ini akan menyulitkan developer saat melakukan mapping database fisik. Rekomendasi solusinya adalah menerapkan standardisasi penamaan secara konsisten (disarankan menggunakan *snake_case* secara menyeluruh, contoh: `kd_anggota`, `nm_anggota`, `tgl_lahir`, `tgl_daftar`), serta memperbaiki typo `tgl_lahit` menjadi `tgl_lahir`.

### B. Spesifikasi Proses (Process Specification)
Logika proses krusial digambarkan dengan menggunakan *Structured English* / *Pseudocode*. Contoh logika pemrosesan data:
* **Proses 4.3 (Update Buku):** Mengurangi jumlah stok buku ketika transaksi peminjaman berhasil direkam.
* **Proses 1.1 (Cari Data Anggota):** Melakukan perulangan pencarian sekuensial (*sequential search*) pada tabel anggota berdasarkan *input* ID anggota hingga ditemukan atau mencapai akhir file (*EOF*).

*Analisis Kritis:
* **Temuan Pertukaran Label Proses 5.1 dan 5.2:** Pada bagian Spesifikasi Proses (Halaman 6) di dokumen asli, deskripsi proses `5.1` berlabel **"Cetak laporan peminjaman"** (untuk Pimpinan).
  * **Analisis & Solusi:** Berdasarkan requirement di halaman 1, proses `5.1` adalah **"Cetak daftar pengeluaran buku"** (Bagian Pengadaan), sedangkan `5.2` adalah **"Cetak laporan peminjaman"** (Pimpinan). Penomoran ini tertukar dan membingungkan pengembang. Solusinya, tukar label spesifikasi proses agar `5.1` merujuk ke Daftar Pengeluaran Buku dan `5.2` merujuk ke Laporan Peminjaman.
* **Temuan Kesalahan Objek (Copy-Paste Error) pada Spesifikasi Proses 4.3:** Di deskripsi algoritma proses `4.3 Update buku` (Halaman 7), baris ke-4 tertulis: `"Search ke table barang"`.
  * **Analisis & Solusi:** Sistem perpustakaan ini tidak menggunakan tabel `barang`, melainkan tabel `Buku`. Hal ini merupakan indikasi kelalaian copy-paste dari template pseudocode sistem inventori toko. Rekomendasi solusinya adalah mengubah penulisan variabel tabel tersebut menjadi **"Search ke table buku"** agar selaras dengan skema database yang ada.
* **Temuan Cacat Logika Algoritma Pencarian pada Spesifikasi Proses 1.1:** Algoritma pencarian pada proses `1.1 Cari data anggota` (Halaman 7) menggunakan struktur `While not EOF` dengan percabangan `If-Else` di dalamnya yang langsung menampilkan pesan *"data tdk ada"* ketika satu record tidak cocok.
  * **Analisis & Solusi:** Logika tersebut salah secara fundamental. Program akan langsung menyimpulkan data tidak ada pada iterasi record pertama jika ID tidak cocok, meskipun data sebenarnya ada di record berikutnya. Solusinya, perbaiki algoritma menggunakan variabel bendera (*flag*) (misalnya `found = false`), cari di seluruh record, dan tampilkan pesan data tidak ada hanya jika pencarian selesai dan `found` masih bernilai `false`.
  * **Rekomendasi Algoritma yang Benar:**
    ```
    Begin
      Open table anggota
      Input id-anggota
      Set found = false
      While not EOF anggota
        If id-anggota = id_tabel_anggota
          Then tampilkan data anggota
          Set found = true
        Endif
      EndWhile
      If found = false
        Then tampilkan "data tidak ditemukan"
      Endif
      Close table anggota
    End
    ```
