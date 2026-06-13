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

## 4. Analisis Kamus Data & Spesifikasi Proses

### A. Kamus Data (Data Dictionary)
Kamus data mendefinisikan struktur elemen data yang mengalir dalam sistem maupun yang disimpan di dalam *data store*:
* **Struktur Penyimpanan (Data Store):**
  * `Anggota` = `@Kd-anggota` + `nm-anggota` + `tgl-lahir` + `tgl_daftar`
  * `Buku` = `@Kd-buku` + `judul` + `penerbit` + `pengarang` + `stok`
  * `Pinjaman` = `@no-pinjam` + `tgl_pinjam` + `tgl_kembali` + `kd-anggota` + `kd_buku`
* **Aliran Data Utama:**
  * `Id-anggota` = `nm_anggota` + `tgl_lahir` + `no_identitas` (input pendaftaran)
  * `Kartu Anggota` = `@Kd-anggota` + `nm-anggota` + `tgl-lahir` + `tgl_daftar` + `masa_berlaku`
  * `Bukti-pinjaman` = `no-bukti` + `kd-anggota` + `nm_anggota` + `tgl_pinjam` + `{kd_buku + judul + pengarang + penerbit}` + `tgl_hrs_kembali` + `nm_petugas`

### B. Spesifikasi Proses (Process Specification)
Logika proses krusial digambarkan dengan menggunakan *Structured English* / *Pseudocode*. Contoh logika pemrosesan data:
* **Proses 4.3 (Update Buku):** Mengurangi jumlah stok buku ketika transaksi peminjaman berhasil direkam.
* **Proses 1.1 (Cari Data Anggota):** Melakukan perulangan pencarian sekuensial (*sequential search*) pada tabel anggota berdasarkan *input* ID anggota hingga ditemukan atau mencapai akhir file (*EOF*).

---

## 5. Analisis Kritis: Temuan Kesalahan (*Logic Defects*) & Inkonsistensi Desain
Setelah menelaah dokumen studi kasus secara saksama, ditemukan beberapa kesalahan perancangan yang cukup krusial. Temuan ini sangat penting karena dapat menyebabkan kegagalan sistem (*system failure*) atau ketidaksesuaian implementasi jika langsung diserahkan kepada tim pengembang (*programmer*).

Berikut adalah daftar temuan defect beserta penjelasannya:

### 1. Kesalahan Aliran Data pada Diagram Konteks (Halaman 2)
* **Temuan:** Aliran data dari sistem ke entitas **Pimpinan** tertulis **"Laporan Penjualan"**.
* **Analisis Cacat:** Studi kasus ini membahas tentang **Sistem Peminjaman Buku Perpustakaan**, bukan sistem penjualan ritel atau e-commerce. Pimpinan perpustakaan seharusnya menerima **"Laporan Peminjaman"** sesuai dengan deskripsi kebutuhan bisnis yang tertera di halaman 1.

### 2. Cacat Logika Aliran Data pada DFD Level-0 (Halaman 3)
* **Temuan:** Proses **`3.0 cari & tampilkan status bku`** tidak terhubung ke *Data Store* mana pun.
* **Analisis Cacat:** Di dalam diagram, proses 3.0 menerima input `Info Status Buku` dari Anggota, lalu mengeluarkan output `Info Status Buku` kembali ke Anggota. Namun, proses ini **tidak membaca data dari Data Store `Buku`**. Secara prinsip Rekayasa Perangkat Lunak, sebuah proses pencarian status buku mustahil mengembalikan informasi valid tanpa melakukan query/pembacaan data ke penyimpanan data (tabel Buku). Ini adalah pelanggaran aturan dasar DFD (*Black Hole / Miracle Process*).

### 3. Kesalahan Penulisan Objek (*Copy-Paste Error*) pada Spesifikasi Proses 4.3 (Halaman 7)
* **Temuan:** Pada deskripsi algoritma proses **`4.3 Update buku`**, baris ke-4 tertulis: `"Search ke table barang"`.
* **Analisis Cacat:** Di dalam database sistem perpustakaan ini hanya didefinisikan tiga tabel, yaitu `Anggota`, `Buku`, dan `Peminjaman`. Tidak ada tabel bernama **`barang`**. Istilah "barang" biasanya merujuk pada sistem inventori toko. Hal ini mengindikasikan adanya kelalaian penulisan akibat menyalin (*copy-paste*) template pseudocode sistem inventori barang tanpa menyesuaikan variabel dengan domain studi kasus perpustakaan.

### 4. Inkonsistensi Penamaan Aliran Data & Typo
* **Temuan & Analisis:**
  * Di DFD Level-0 (Halaman 3), aliran data ke Pimpinan tertulis **`Lapoan Pemianjaman`** (Typo: kurang huruf 'r' pada Laporan dan kelebihan huruf 'i' pada Peminjaman).
  * Di Kamus Data Aliran Data (Halaman 5), definisi `Id-anggota` menggunakan field `tgl_lahit` dan `no_identitas`, padahal di *Data Store* Anggota menggunakan field `tgl-lahir`. Penggunaan karakter penghubung (underscore `_` vs dash `-`) tidak konsisten.

---

## 6. Rekomendasi Perbaikan Desain Sistem

Untuk menghasilkan perancangan perangkat lunak yang valid dan siap diimplementasikan, berikut adalah usulan perbaikan terhadap rancangan sistem:

1. **Perbaikan Diagram Konteks:** Mengubah nama aliran data dari sistem ke Pimpinan menjadi **"Laporan Peminjaman"** guna menjaga konsistensi domain perpustakaan.
2. **Perbaikan DFD Level-0:** Menambahkan aliran data bertipe *read* (panah satu arah dari *Data Store* ke proses) antara *Data Store* **`Buku`** dengan proses **`3.0 cari & tampilkan status bku`**.
3. **Perbaikan Spesifikasi Proses 4.3:** Mengubah baris algoritma menjadi `"Search ke table buku"` (menggantikan kata "barang") agar sesuai dengan skema database yang telah didefinisikan pada Kamus Data.
4. **Standardisasi Kamus Data:** Menyelaraskan penulisan variabel (misalnya, secara konsisten menggunakan gaya penulisan *snake_case* atau *kebab-case* di seluruh diagram dan spesifikasi proses).
