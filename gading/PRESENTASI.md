# Panduan Presentasi: Struktur Data Majemuk Linear
> **Topik:** Stack, Queue, Linked List, & Dynamic Array List
> **Bahasa Pemrograman:** Python
> **Pembuat:** Gading Nst

---

## 📌 Slide 1: Pendahuluan
### Apa itu Struktur Data Majemuk Linear?
Struktur data **linear** adalah cara penyimpanan dan pengorganisasian data di mana elemen-elemen data disusun secara **berurutan (sekuensial)**. 

Setiap elemen (kecuali elemen pertama dan terakhir) memiliki:
1. **Predecessor** (elemen sebelum).
2. **Successor** (elemen sesudah).

> [!NOTE]
> **Mengapa disebut "Majemuk"?** Karena struktur data ini menampung lebih dari satu elemen data (koleksi data) yang bertipe homogen (sama) atau heterogen, berbeda dengan variabel primitif (seperti integer atau float) yang hanya dapat menampung satu nilai tunggal.

---

## 📌 Slide 2: Stack (Tumpukan)
### "Last In, First Out" (LIFO)

Stack adalah struktur data linear di mana penambahan dan pengambilan elemen hanya dapat dilakukan pada satu ujung yang sama, yang disebut **TOP** (Puncak).

```
          [ Piring C ]  <─── TOP (Terakhir Masuk, Pertama Keluar)
          [ Piring B ]
          [ Piring A ]  <─── BASE
```

### 🍳 Analogi Dunia Nyata
*   **Tumpukan piring di restoran:** Piring yang terakhir dicuci diletakkan di paling atas, dan merupakan piring pertama yang diambil oleh pelanggan.
*   **Fitur Undo/Redo (Ctrl+Z) di Text Editor:** Riwayat perubahan disimpan dalam Stack. Perubahan terakhir adalah yang pertama kali dibatalkan.
*   **Tombol Back pada Web Browser:** Halaman web terakhir yang Anda buka ditumpuk di atas halaman sebelumnya.

### ⚙️ Operasi Utama
*   `push(item)`: Memasukkan elemen ke puncak stack.
*   `pop()`: Mengambil dan menghapus elemen dari puncak stack.
*   `peek()` / `top()`: Melihat elemen teratas tanpa menghapusnya.

---

## 📌 Slide 3: Queue (Antrean)
### "First In, First Out" (FIFO)

Queue adalah struktur data linear di mana elemen masuk dari ujung belakang (**REAR/TAIL**) dan keluar dari ujung depan (**FRONT/HEAD**).

```
   [ KELUAR / EXIT ]                                      [ MASUK / ENTER ]
         ▲                                                      ▲
         │    [ FRONT: Elemen A ] <─── [ Elemen B ] <─── [ REAR: Elemen C ]
```

### 👥 Analogi Dunia Nyata
*   **Antrean pembelian tiket bioskop:** Orang pertama yang datang akan dilayani pertama kali dan keluar dari antrean pertama kali.
*   **Antrean print dokumen (Print Spooler):** Dokumen yang pertama kali dikirim ke printer akan dicetak terlebih dahulu.
*   **Buffering Video:** Data paket internet yang tiba pertama kali didecode dan ditampilkan di layar terlebih dahulu.

### ⚙️ Operasi Utama
*   `enqueue(item)`: Memasukkan elemen ke ujung belakang antrean.
*   `dequeue()`: Mengeluarkan dan menghapus elemen dari ujung depan antrean.
*   `front()`: Melihat elemen terdepan tanpa menghapusnya.

---

## 📌 Slide 4: Linked List (Senarai Berantai)
### Alokasi Memori Dinamis Non-Kontigu

Linked List adalah sekumpulan **Node** (simpul) dinamis yang saling terhubung menggunakan **Pointer** (penunjuk alamat memori berikutnya). Berbeda dengan array, data di Linked List tidak disimpan berdampingan secara fisik di dalam RAM.

```
   Head ──► [ Data: A | Next ] ──► [ Data: B | Next ] ──► [ Data: C | Next ] ──► NULL
```

### 🚂 Analogi Dunia Nyata
*   **Kereta Api / Gerbong Barang:** Setiap gerbong berisi muatan (Data) dan rantai penghubung (Pointer) ke gerbong di belakangnya. Jika Anda ingin menambah gerbong di tengah, Anda hanya perlu memutuskan satu rantai dan menyambungkan rantai baru.
*   **Permainan Berburu Harta Karun:** Petunjuk pertama menunjuk lokasi petunjuk kedua, petunjuk kedua menunjuk lokasi petunjuk ketiga, dan seterusnya.

### ⚙️ Operasi Utama
*   `insert_at_beginning(data)`: Menyisipkan Node baru di awal (mengganti Head).
*   `insert_at_end(data)`: Berjalan hingga akhir rantai lalu menyambungkan Node baru.
*   `delete_value(value)`: Mencari Node bernilai tertentu, lalu memutus hubungan pointernya agar dilewati (di-bypass).

---

## 📌 Slide 5: Array List / Dynamic Array
### Blok Memori Fisik Berurutan (Kontigu) dengan Resizing Otomatis

Array List adalah struktur data berbasis array biasa yang memiliki kemampuan **Resizing Otomatis** saat kapasitasnya sudah penuh. Elemen disimpan secara berdampingan di memori fisik RAM, memungkinkan akses langsung menggunakan indeks.

```
       Kapasitas Fisik Awal = 4
       +───────────+───────────+───────────+───────────+
       |   Data 1  |   Data 2  |   Data 3  |  [EMPTY]  |
       +───────────+───────────+───────────+───────────+
         indeks 0    indeks 1    indeks 2    indeks 3
         
       Ketika diisi elemen ke-5 (Penuh), sistem akan:
       1. Membuat blok memori baru dengan kapasitas ganda (8).
       2. Menyalin seluruh elemen lama ke memori baru.
       3. Menghapus blok memori lama.
```

### 💺 Analogi Dunia Nyata
*   **Barisan Kursi Bioskop Pesanan Rombongan:** Rombongan memesan 4 kursi berdampingan. Ketika ada orang ke-5 yang ingin bergabung dan tidak ada kursi kosong di sebelahnya, seluruh rombongan harus pindah ke barisan baru yang memiliki 8 kursi berdampingan kosong.

### ⚙️ Operasi Utama
*   `get(index)` / `__getitem__`: Akses langsung elemen secara instan ($O(1)$) menggunakan alamat memori dasar + (indeks * ukuran tipe data).
*   `append(item)`: Menambah elemen di akhir array.
*   `insert(index, item)`: Menyisipkan elemen pada indeks tertentu dan menggeser elemen di kanannya ke kanan.

---

## 📊 Slide 6: Analisis Kompleksitas (Big-O)

Berikut adalah tabel ringkasan efisiensi performa (Waktu) untuk keempat struktur data:

| Struktur Data | Akses Indeks / Random Access | Pencarian (Search) | Penyisipan di Ujung (Insert End) | Penyisipan di Tengah / Awal | Penghapusan (Delete) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Stack** | N/A (Hanya TOP) | $O(N)$ | $O(1)$ | N/A | $O(1)$ |
| **Queue** | N/A (Hanya FRONT) | $O(N)$ | $O(1)$ | N/A | $O(1)$ |
| **Linked List** | $O(N)$ (Harus urut) | $O(N)$ | $O(N)$ atau $O(1)$* | $O(1)$ (Jika pointer diketahui) | $O(1)$ atau $O(N)$ |
| **Array List** | $O(1)$ *(Sangat Cepat!)* | $O(N)$ | $O(1)$ *(Amortized)* | $O(N)$ *(Harus geser elemen)* | $O(N)$ *(Harus geser elemen)* |

*\* Keterangan:*
*   Linked List memiliki kompleksitas penyisipan di akhir $O(1)$ jika kita menyimpan variabel pointer penunjuk akhir (`tail`). Jika tidak, kita harus menelusuri dari `head` sehingga menjadi $O(N)$.
*   Penyisipan Array List di akhir bernilai $O(1)$ *Amortized* karena sesekali terjadi proses resizing yang memakan waktu $O(N)$, namun rata-rata operasi append biasa hanya $O(1)$.

---

## 💻 Slide 7: Panduan Demo Live Aplikasi (`main.py`)

Saat presentasi di depan kelas atau dosen, jalankan terminal dan ikuti skenario demo interaktif berikut:

### 1. Persiapan
Buka terminal pada folder proyek Anda dan jalankan perintah:
```bash
python main.py
```

### 2. Skenario Demo Stack (Pilih Menu 1)
*   **Tunjukkan Kondisi Awal:** Stack terisi dengan `Piring 1`, `Piring 2`, `Piring 3`.
*   **Lakukan Push:** Tambahkan `'Piring 4'`. Tunjukkan bahwa `'Piring 4'` berada di posisi **TOP** paling atas.
*   **Lakukan Pop:** Klik opsi Pop. Tunjukkan bahwa `'Piring 4'` keluar terlebih dahulu, sesuai prinsip **LIFO** (Last In First Out).

### 3. Skenario Demo Queue (Pilih Menu 2)
*   **Tunjukkan Aliran Data:** Tunjukkan data mengalir horizontal dengan tanda panah ` <=== `.
*   **Lakukan Enqueue:** Masukkan `'Pelanggan baru'`. Tunjukkan bahwa dia masuk di sebelah kanan (**REAR**).
*   **Lakukan Dequeue:** Keluarkan elemen. Tunjukkan bahwa elemen terdepan sebelah kiri (**FRONT**) yang keluar terlebih dahulu (**FIFO**).

### 4. Skenario Demo Linked List (Pilih Menu 3)
*   **Tunjukkan Rantai Node:** Jelaskan format `[ Data | • ] ──► [ Data | • ]` di mana titik (`•`) adalah representasi pointer penunjuk alamat memori Node berikutnya di RAM.
*   **Tunjukkan Insert Beginning:** Masukkan data di awal dan tunjukkan bagaimana `Head` langsung berubah menunjuk ke Node baru secara instan.

### 5. Skenario Demo Array List (Pilih Menu 4)
> 🔥 **BAGIAN TERBAIK UNTUK MEMIKAT DOSEN!**
*   **Tunjukkan Kapasitas Awal:** Array terisi 3 elemen (`Data 1`, `Data 2`, `Data 3`), dengan 1 slot cadangan bertuliskan `[RESERVE]`. Kapasitas Fisik = 4.
*   **Lakukan Append 1 Elemen:** Masukkan `'Data 4'`. Sekarang kapasitas penuh 4/4.
*   **Picu Resizing secara Live:** Masukkan `'Data 5'`. Perhatikan terminal akan mencetak:
    `[ SYSTEM INFO ] Memori Penuh! Me-resize kapasitas: 4 ──► 8...`
*   Jelaskan pada audiens bahwa array di RAM telah digandakan kapasitas fisiknya menjadi 8 dengan 3 slot `[RESERVE]` baru untuk efisiensi!

---

## 🙋‍♂️ Slide 8: Antisipasi Pertanyaan Dosen (Q&A)

Saat sesi tanya jawab, dosen sering kali menanyakan pertanyaan kritis untuk menguji pemahaman Anda. Berikut adalah rangkuman pertanyaan terpopuler beserta kunci jawaban akademis terbaik:

#### 💬 **Pertanyaan 1:**
> *"Mengapa kita membutuhkan Linked List jika kita sudah memiliki Array List yang jauh lebih mudah diakses?"*
*   **Kunci Jawaban:** 
    "Array List menyimpan data di memori secara berurutan (kontigu), sehingga untuk menyisipkan atau menghapus elemen di tengah, kita harus menggeser seluruh elemen di kanannya ($O(N)$). Sedangkan **Linked List** dialokasikan secara dinamis di memori non-kontigu. Untuk menyisipkan atau menghapus elemen, kita hanya perlu mengubah referensi pointer Node tetangganya ($O(1)$) tanpa perlu menggeser memori fisik sama sekali. Linked List sangat efisien untuk aplikasi dengan frekuensi insert dan delete yang tinggi."

#### 💬 **Pertanyaan 2:**
> *"Pada Array List kustom yang Anda buat, mengapa saat kapasitas penuh ukuran barunya dilipatgandakan menjadi 2x lipat (misal dari 4 menjadi 8), bukan ditambah 1 saja?"*
*   **Kunci Jawaban:**
    "Jika kita hanya menambah kapasitas sebesar 1 setiap kali penuh, maka setiap kali kita melakukan operasi `append()`, kita harus melakukan pengalokasian memori baru dan penyalinan elemen ($O(N)$). Ini sangat tidak efisien. Dengan melipatgandakan kapasitas secara geometris (faktor pengali 2 atau 1.5), kita memastikan bahwa rata-rata (amortized) biaya operasi `append()` tetap sangat murah, yaitu $O(1)$."

#### 💬 **Pertanyaan 3:**
> *"Apa perbedaan utama antara Stack dan Queue dalam hal aksesibilitas data?"*
*   **Kunci Jawaban:**
    "Perbedaan utamanya terletak pada titik akses (access points). **Stack** adalah struktur data satu ujung (*Single-ended*) di mana operasi penambahan dan penghapusan terjadi di ujung yang sama (Top). Sedangkan **Queue** adalah struktur data dua ujung (*Double-ended*) di mana penambahan terjadi di satu ujung (Rear/Back) dan penghapusan terjadi di ujung yang berlawanan (Front/Forward)."
