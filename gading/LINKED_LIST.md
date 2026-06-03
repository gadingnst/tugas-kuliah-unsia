# Panduan Ujian & Presentasi: Kupas Tuntas Linked List
> **Topik Fokus:** Teori Dasar, Anatomi Node, Komparasi Array, Kelebihan/Kekurangan, & Dokumentasi Kode
> **Implementasi Kode:** `gading/linked_list.py`
> **Pembuat:** Gading Nst

---

## 📌 Slide 1: Pendahuluan Linked List

### Apa itu Linked List?
**Linked List (Senarai Berantai)** adalah struktur data linear dinamis yang terdiri dari sekumpulan elemen yang disebut **Node (Simpul)**. 

Berbeda dengan Array biasa yang menuntut penyimpanan data berdampingan secara fisik di dalam RAM (kontigu), Node pada Linked List dialokasikan secara dinamis di alamat memori mana saja secara tersebar. Hubungan antar elemen dibangun menggunakan variabel penunjuk alamat (**Pointer**).

### 🚂 Analogi Sederhana
Bayangkan Linked List seperti **gerbong kereta api**. Setiap gerbong memuat barang bawaan (Data) dan memiliki rantai pengait besi (Pointer) yang menghubungkannya ke gerbong berikutnya. Jika kita kehilangan gerbong lokomotif paling depan (**Head**), kita akan kehilangan jejak seluruh gerbong di belakangnya.

---

## 📌 Slide 2: Anatomi Node (Simpul) Linked List

Simpul atau **Node** adalah unit pembentuk terkecil dari Linked List. Secara garis besar, sebuah Node wajib terbagi menjadi **dua bagian (atribut)**:

```text
               +───────────────────────────+
               |   DATA   |  POINTER (NEXT)| ──► Menunjuk ke Node tetangga
               +───────────────────────────+
```

1.  **Bagian Data (Data Field):** 
    Menyimpan nilai atau informasi aktual dari elemen tersebut (misalnya angka, teks, atau objek data lainnya).
2.  **Bagian Pointer (Pointer Field / Next):**
    Menyimpan alamat memori fisik dari Node berikutnya di RAM. Atribut pointer pada Node terakhir akan selalu bernilai `None` atau `NULL`, menandakan rantai telah berakhir.

---

## 📌 Slide 3: Jenis-Jenis Linked List (Garis Besar)

Berdasarkan arah penunjuk pointernya, Linked List terbagi menjadi 3 jenis utama yang wajib Anda pahami secara konsep garis besar:

### 1. Singly Linked List (Satu Arah)
Varian paling dasar di mana setiap Node hanya memiliki satu pointer (`next`) yang menunjuk ke depan. Navigasi hanya bisa berjalan maju searah.
```text
   Head ──► [ Data | Next ] ──► [ Data | Next ] ──► NULL
```

### 2. Doubly Linked List (Dua Arah)
Setiap Node memiliki dua pointer: `next` (menunjuk ke depan) dan `prev` (menunjuk ke belakang). Memungkinkan navigasi bolak-balik.
```text
   NULL ◄──► [ Prev | Data | Next ] ◄──► [ Prev | Data | Next ] ◄──► NULL
```

### 3. Circular Linked List (Melingkar)
Pointer Node terakhir tidak menunjuk ke `NULL`, melainkan berputar kembali menunjuk ke Node pertama (`Head`), membentuk lingkaran tanpa ujung.
```text
   Head ──► [ Data | Next ] ──► [ Data | Next ] ──► (Kembali ke Head)
              ▲                                        │
              └────────────────────────────────────────┘
```

---

## 📌 Slide 4: Kompleksitas Waktu: Array vs Linked List

Berikut adalah tabel perbandingan performa (Big-O Time Complexity) antara Array dan Linked List untuk memukau dosen saat ujian presentasi:

| Operasi Struktur Data | 📱 Array / Array List | 🔗 Linked List (Dasar) | Penjelasan Teknis |
| :--- | :---: | :---: | :--- |
| **Akses Elemen (Access)** | $O(1)$ | $O(N)$ | Array memiliki alamat memori berurutan sehingga bisa diakses langsung lewat indeks. Linked List harus ditelusuri dari depan satu per satu. |
| **Pencarian Data (Search)** | $O(N)$ | $O(N)$ | Kedua struktur data sama-sama harus memeriksa data satu per satu dari awal sampai ketemu. |
| **Penyisipan di Awal (Insert Front)** | $O(N)$ | $O(1)$ | Array harus menggeser semua data di kanannya. Linked List hanya perlu mengganti pointer Head secara instan. |
| **Penyisipan di Akhir (Insert End)** | $O(1)$ *Amortized* | $O(N)$ atau $O(1)$* | Linked List bernilai $O(N)$ karena harus mencari ujung akhir terlebih dahulu, kecuali jika kita menyimpan pointer `Tail` ($O(1)$). |
| **Penghapusan (Deletion)** | $O(N)$ | $O(1)$ atau $O(N)$ | Array harus merapatkan memori kembali. Linked List hanya memotong pointer simpul yang dibypass. |

---

## 📌 Slide 5: Kelebihan & Kekurangan Linked List

Struktur data Linked List dirancang bukan untuk menggantikan Array, melainkan sebagai alternatif solusi dengan kelebihan dan kekurangan tersendiri:

### ✅ Kelebihan Linked List:
1.  **Ukuran Dinamis:** Kapasitas memori tidak perlu ditentukan di awal. Node baru bisa dialokasikan kapan saja selama memori RAM laptop masih cukup.
2.  **Penyisipan & Penghapusan Cepat:** Operasi menambah atau menghapus elemen di awal rantai berjalan sangat instan ($O(1)$) tanpa pergeseran memori RAM.
3.  **Bebas Pemborosan Memori Terfragmentasi:** Alokasi memori dinamis tersebar acak, sehingga memanfaatkan celah memori kosong kecil di RAM dengan maksimal.

### ❌ Kekurangan Linked List:
1.  **Konsumsi Memori Lebih Besar:** Setiap Node memakan memori ekstra untuk menyimpan alamat pointer tetangganya (di samping menyimpan data aktual).
2.  **Tidak Ada Akses Acak (No Random Access):** Kita tidak bisa langsung memanggil `data[5]`. Kita terpaksa melakukan pencarian sekuensial dari Head secara berurutan.
3.  **Sulit untuk Traversing Mundur:** Pada Linked List dasar satu arah, kita tidak bisa kembali ke elemen sebelumnya jika sudah terlewat.

---

## 📌 Bagian 2: Panduan Membuat Linked List Sederhana dari Nol (Python)

Berikut adalah contoh pembuatan Linked List paling sederhana dari dasar di Python untuk mendemonstrasikan pemahaman Anda di depan dosen:

### 1. Definisikan Kelas Node (Wadah Simpul)
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer ke Node berikutnya (default kosong)
```

### 2. Hubungkan Simpul Secara Manual
```python
# Buat dua node terpisah
node1 = Node("Apple")
node2 = Node("Banana")

# Sambungkan pointer next node1 ke node2
node1.next = node2  # Hasil: "Apple" ──► "Banana" ──► None
```

### 3. Buat Kelas Pengendali Utama (`LinkedList`)
```python
class LinkedList:
    def __init__(self):
        self.head = None  # Awal mula rantai selalu kosong

    def insert_at_end(self, data):
        new_node = Node(data)  # Buat node baru
        if self.head is None:
            self.head = new_node  # Jika kosong, node ini jadi Head
            return
        
        # Telusuri sampai Node paling ujung belakang
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node  # Sambungkan di ujung rantai
```

---

## 📌 Bagian 3: Detail Implementasi Kode (`gading/linked_list.py`)

Di dalam berkas program utama **`gading/linked_list.py`**, kita mengimplementasikan kelas `LinkedList` dasar satu arah secara lengkap:

*   **`insert_at_beginning(data)`**: Menyisipkan Node di depan secara instan ($O(1)$).
*   **`insert_at_end(data)`**: Menelusuri seluruh rantai sampai ujung belakang untuk menambahkan Node baru ($O(N)$).
*   **`delete_value(value)`**: Mencari Node target, lalu memutus hubungan pointernya dengan menghubungkan Node sebelum target langsung ke Node setelah target ($O(N)$).
*   **`get_visualization()`**: Menghasilkan representasi string ASCII horizontal cantik yang menampilkan seluruh simpul di konsol.

---

## 📌 Bagian 4: Panduan Skenario Rekaman Video Presentasi

Gunakan naskah panduan lisan berikut saat Anda merekam video untuk menunjukkan penguasaan materi yang matang:

1.  **Pembuka Presentasi:**
    > *"Selamat pagi/siang Bapak/Ibu Dosen. Saya Gading Nst. Hari ini saya akan mempresentasikan struktur data Linked List secara garis besar. Linked List adalah rantai simpul dinamis di memori komputer yang saling terhubung melalui pointer, mirip dengan gerbong kereta api."*
2.  **Jelaskan Anatomi & Komparasi:**
    *   Tunjukkan visualisasi Slide 2 bahwa Node terdiri dari **Data** dan **Pointer (Next)**.
    *   Sebutkan keunggulan Linked List dibandingkan Array: *"Pada Array, kita harus menggeser memori fisik saat menyisipkan data. Namun pada Linked List, kita cukup mengganti alamat pointernya saja dalam waktu instan $O(1)$."*
3.  **Tunjukkan Demonstrasi Live:**
    *   Jalankan program interaktif Anda: `python3 main.py` lalu pilih **Menu 3** (Linked List).
    *   Tunjukkan bagaimana simpul-simpul berantai tergambar di terminal dengan tanda panah pointer `──►` yang bergeser dinamis secara real-time saat Anda menambah atau menghapus elemen!
