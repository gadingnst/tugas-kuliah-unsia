# Panduan Ujian & Presentasi: Struktur Data Majemuk Linear
> **Pembuat:** Rina
> **Topik Khusus:** Stack (Rounded Box), Circular Queue (Modulo FIFO), Doubly Linked List (Two-Way Chain), & Dynamic Array (Pre-allocated List)
> **Bahasa Pemrograman:** Python

---

## 📌 Slide 1: Pendahuluan Struktur Data Linear
### Apa itu Struktur Data Majemuk Linear?
Struktur data linear adalah pengorganisasian elemen data secara beruntun dalam garis lurus sekuensial. Elemen-elemen terikat secara logis dari awal hingga akhir, di mana setiap elemen (kecuali elemen pertama dan terakhir) terhubung secara langsung dengan tepat satu elemen sebelum (**Predecessor**) dan satu elemen setelah (**Successor**).

> [!NOTE]
> **Mengapa Rina memilih struktur data ini?** 
> Karena merupakan fondasi paling esensial dalam pemrosesan memori komputer. Pembagian memori secara berurutan fisik (kontigu) seperti Array atau berurutan logis (pointer memori dinamis) seperti Linked List memberikan pemahaman mendalam tentang efisiensi komputasi RAM.

---

## 📌 Slide 2: Stack (Tumpukan CD)
### LIFO: "Last In, First Out"

Stack adalah struktur data linear satu arah di mana penambahan (Push) dan pengambilan (Pop) data dibatasi hanya pada satu pintu masuk/keluar yang sama, yang dikenal sebagai **Puncak Tumpukan (TOP)**.

```
      ╭───────────╮  ◄── [ TOP: Elemen C (Terakhir Masuk, Pertama Keluar) ]
      │  CD C     │
      ├───────────┤
      │  CD B     │
      ├───────────┤
      │  CD A     │  ◄── [ BASE: Elemen A (Terbawah) ]
      ╰───────────╯
```

### 💿 Analogi Dunia Nyata Rina
*   **Tumpukan CD Musik dalam Wadah:** CD terakhir yang Anda masukkan ke dalam tabung wadah adalah CD pertama yang harus Anda ambil untuk diputar.
*   **Tumpukan Kursi Plastik:** Kursi terakhir yang ditumpuk di atas adalah satu-satunya kursi yang bisa diangkat pertama kali secara aman.

### ⚙️ Operasi Utama
*   `push(element)`: Menaruh CD baru di puncak tumpukan.
*   `pop()`: Mengambil CD teratas dari wadah.
*   `peek()`: Mengintip label CD teratas tanpa merusak tumpukan.

---

## 📌 Slide 3: Circular Queue (Antrean Melingkar)
### Ring Buffer Sirkular FIFO (First In, First Out)

Circular Queue adalah bentuk optimal dari Antrean biasa. Pada antrean biasa, saat elemen terdepan dihapus (dequeue), terjadi pergeseran memori berbiaya $O(N)$ atau kapasitas memori tersisa terbuang sia-sia. Circular Queue memecahkan masalah ini dengan menyambungkan ujung akhir array kembali ke ujung awal menggunakan **aritmatika modulo (`%`)**, menciptakan ring buffer sirkular $O(1)$ dequeue tanpa pergeseran elemen memori fisik!

```
     Kapasitas Statis = 5 (Indeks 0 s.d 4)
     +─────────+─────────+─────────+─────────+─────────+
     |   Dewi  |  [None] |  [None] |   Rina  |   Budi  |
     +─────────+─────────+─────────+─────────+─────────+
       Idx 0     Idx 1     Idx 2     Idx 3     Idx 4
                 [REAR]              [FRONT]
     
     * Keterangan: Indeks REAR memutar kembali ke indeks 0 setelah indeks 4 (karena 5 % 5 = 0)!
```

### 🎠 Analogi Dunia Nyata Rina
*   **Komidi Putar / Bianglala (Carousel):** Kursi bianglala berputar secara melingkar. Penumpang naik dari pintu masuk dan turun dari pintu keluar, sementara kursi kosong terus berputar melingkar tanpa perlu dipindahkan posisinya secara fisik.
*   **Mekanisme Buffering Audio Player:** Ring buffer mengisi data musik baru secara berputar di memori RAM dan menghapusnya setelah dimainkan.

---

## 📌 Slide 4: Doubly Linked List (Senarai Berantai Ganda)
### Fleksibilitas Rantai Penunjuk Dua Arah (Two-Way Chain)

Doubly Linked List adalah kumpulan Node dinamis di mana setiap Node menyimpan data dan **dua pointer penunjuk arah**:
1.  `next` (menunjuk ke Node setelahnya).
2.  `prev` (menunjuk ke Node sebelumnya).

Hal ini memungkinkan kita untuk berjalan menyusuri memori baik maju (**Head to Tail**) maupun mundur (**Tail to Head**) dengan efisiensi tinggi.

```
   NULL ◄──► [ prev | Data A | next ] ◄──► [ prev | Data B | next ] ◄──► NULL
```

### ⚓ Analogi Dunia Nyata Rina
*   **Daftar Putar Musik (Playlist) Spotify:** Anda dapat menekan tombol *Next* untuk memutar lagu berikutnya (penunjuk `next`), atau menekan tombol *Previous* untuk memutar lagu sebelumnya (penunjuk `prev`).
*   **Rantai Jangkar Kapal:** Setiap mata rantai terikat kuat dengan mata rantai di depan dan di belakangnya.

---

## 📌 Slide 5: Dynamic Array (Larik Dinamis)
### Pra-Alokasi Buffer & Skalabilitas Ukuran Otomatis

Dynamic Array adalah array yang memesan satu blok memori fisik berurutan dengan **kapasitas cadangan (buffer)**. Saat elemen aktif (**Size**) bertambah hingga menyamai kapasitas cadangan (**Capacity**), array akan melipatgandakan ukurannya secara otomatis untuk mencegah kegagalan alokasi memori.

```
       Kapasitas Cadangan = 4
       ╭──────────────┬──────────────┬──────────────┬──────────────╮
       |    Data A    |    Data B    | ░░CADANGAN░░ | ░░CADANGAN░░ |
       ╰──────────────┴──────────────┴──────────────┴──────────────╯
         Aktif (Size) = 2  |  Kapasitas Fisik = 4
```

### 🏨 Analogi Dunia Nyata Rina
*   **Pemesanan Blok Kamar Hotel:** Panitia memesan 4 kamar hotel bersebelahan untuk rombongan. Jika tamu ke-5 datang, panitia membatalkan pesanan lama dan memesan blok baru berisi 8 kamar bersebelahan di lantai lain, lalu memindahkan semua tamu lama ke sana.

---

## 📊 Slide 6: Analisis Kompleksitas Performansi (Big-O)

Tabel perbandingan performa operasi pada struktur data linear milik Rina:

| Struktur Data | Pencarian (Search) | Penyisipan Awal (Insert Front) | Penyisipan Akhir (Insert Back) | Penghapusan (Delete) | Keunggulan Utama |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Stack** | $O(N)$ | $O(1)$ | N/A | $O(1)$ | Operasi LIFO instan |
| **Circular Queue** | $O(N)$ | N/A | $O(1)$ *(Rear)* | $O(1)$ *(Front)* | Bebas pergeseran memori RAM |
| **Doubly Linked List**| $O(N)$ | $O(1)$ | $O(1)$ *(Jika ada Tail)*| $O(1)$ *(Pointer diketahui)* | Navigasi dua arah fleksibel |
| **Dynamic Array** | $O(N)$ | $O(N)$ *(Harus geser)*| $O(1)$ *(Amortized)* | $O(N)$ *(Harus geser)* | Akses indeks acak instan $O(1)$ |

---

## 💻 Slide 7: Panduan Demo Live Aplikasi Rina (`main.py`)

Saat Anda melakukan demonstrasi program di hadapan dosen penguji, ikuti skenario interaktif berikut:

### 1. Eksekusi Program Rina
Buka Terminal di laptop dan masuk ke direktori program Rina:
```bash
cd /Users/gadingnst/Workspace/private/task-struktur-data/rina
python3 main.py
```

### 2. Pamerkan Circular Queue (Menu 2)
*   Tunjukkan visualisasi ring buffer yang memetakan RAM fisik secara nyata.
*   Masukkan 4 pelanggan (`Rina`, `Budi`, `Chandra`, `Dewi`). Slot memori akan terisi Idx 0 s.d 3.
*   Lakukan Dequeue sebanyak 2 kali. Tunjukkan bahwa `Rina` dan `Budi` terhapus, dan **penunjuk FRONT bergeser ke Idx 2 secara instan tanpa ada elemen memori yang bergeser ke kiri!**
*   Lakukan Enqueue data baru (`Eka`, `Fandi`). Tunjukkan secara visual bagaimana **REAR berputar secara ajaib kembali ke Idx 0 dan Idx 1** karena sirkular modulo! Dosen Anda akan sangat menyukai bagian ini.

### 3. Pamerkan Doubly Linked List (Menu 3)
*   Tunjukkan visualisasi rantai dua arah `NULL ◄──► [ Node ] ◄──► NULL`.
*   Pilih `Insert Front` dan `Insert Back` untuk menunjukkan kemudahan penambahan elemen di kedua ujung rantai dengan penunjuk ganda.

---

## 🙋‍♀️ Slide 8: Kunci Jawaban Ujian Q&A Dosen (Rina)

Dosen sering mengajukan pertanyaan kritis untuk menguji keaslian pengerjaan tugas Anda. Berikut adalah rangkuman pertanyaan terpopuler beserta kunci jawaban akademis terbaik:

#### 💬 **Pertanyaan 1:**
> *"Mengapa Anda memilih Circular Queue dibandingkan Queue biasa?"*
*   **Kunci Jawaban Rina:**
    "Pada Queue berbasis array biasa, ketika kita menghapus elemen terdepan (dequeue), seluruh elemen di belakangnya harus bergeser satu langkah ke kiri agar antrean tetap rapat. Pergeseran fisik ini memakan waktu $O(N)$. Atau jika tidak digeser, memori depan akan terbuang sia-sia (Queue Overflow palsu). Dengan **Circular Queue**, kita memanfaatkan aritmatika modulo `%` untuk memutar kembali indeks penunjuk. Hal ini membuat dequeue berjalan instan dalam waktu **$O(1)$** tanpa perlu menggeser memori fisik sama sekali, sehingga menghemat siklus CPU dan RAM."

#### 💬 **Pertanyaan 2:**
> *"Apa perbedaan besar manipulasi pointer pada Singly Linked List vs Doubly Linked List saat penghapusan Node?"*
*   **Kunci Jawaban Rina:**
    "Pada Singly Linked List, untuk menghapus Node di tengah, kita harus melacak Node pendahulu (*previous Node*) untuk menyambungkan pointernya melewati Node yang dihapus, yang mengharuskan pencarian linear satu arah. Sedangkan pada **Doubly Linked List**, setiap Node menyimpan penunjuk ke elemen sebelumnya (`prev`). Sehingga jika kita sudah memiliki referensi ke Node yang akan dihapus, kita bisa langsung menghubungkan Node sebelum dan Node sesudahnya secara instan tanpa perlu melakukan iterasi pencarian manual."

#### 💬 **Pertanyaan 3:**
> *"Mengapa pada Dynamic Array Anda menggunakan list pra-alokasi [None] * capacity secara manual?"*
*   **Kunci Jawaban Rina:**
    "Tujuannya adalah untuk mendemonstrasikan secara transparan manajemen memori tingkat rendah (low-level) di mana memori fisik komputer (Capacity) dicadangkan terlebih dahulu secara statis di memori. Dengan cara ini, proses penggandaan kapasitas memori (*resizing*) dan penyalinan data lama ke blok baru saat memori penuh terlihat jelas di layar, mendekati arsitektur aslinya di bahasa C++ atau Java."
