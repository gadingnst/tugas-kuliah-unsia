# Panduan Kupas Tuntas: Struktur Data Linked List (Senarai Berantai)
> **Implementasi Kode:** `gading/linked_list.py`
> **Pembuat:** Gading Nst

---

## 📌 Bagian 1: Pengenalan Dasar Linked List

### Apa itu Linked List secara Dasar?
**Linked List (Senarai Berantai)** adalah struktur data linear dinamis yang digunakan untuk menyimpan kumpulan data. 

Bayangkan Linked List seperti **gerbong kereta api**. Setiap gerbong berisi barang (Data) dan rantai besi pengait (Pointer) yang menyambungkannya ke gerbong berikutnya.

```text
    Head (Lokomotif)
     │
     ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Data | Pointer───►  │ Data | Pointer───►  │ Data | None  │ (Akhir Rantai)
└──────────────┘      └──────────────┘      └──────────────┘
    Gerbong 1             Gerbong 2             Gerbong 3
```

### Mengapa Kita Butuh Linked List? (Dibanding Array/List biasa)
Pada Array biasa, data disimpan bersebelahan secara fisik di dalam RAM. 
*   **Masalah Array:** Jika kita ingin menyisipkan data di tengah-tengah, komputer harus menggeser posisi seluruh data di kanannya satu per satu ke kanan. Proses ini memakan waktu lambat ($O(N)$).
*   **Solusi Linked List:** Karena setiap simpul menyimpan alamat memori tetangganya, kita **tidak perlu menggeser data fisik**. Kita cukup memutus rantai pointer dan menyambungkannya ke simpul baru ($O(1)$).

---

## 📌 Bagian 2: Panduan Membuat Linked List Sederhana dari Nol (Python)

Membuat Linked List dari dasar di Python sangat mudah jika Anda memahami dua kelas ini:

### Langkah 1: Membuat Kelas Simpul (Node)
Wadah terkecil untuk menyimpan satu elemen data dan penunjuk arah berikutnya.
```python
class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan barang/nilai di dalam simpul
        self.next = None    # Pointer penunjuk berikutnya (default masih kosong)
```

### Langkah 2: Menyambungkan Simpul Secara Manual
Mari kita buat simpul-simpul terpisah lalu sambungkan rantainya secara manual agar Anda paham alurnya:
```python
# 1. Buat 3 simpul terpisah di memori RAM
simpul1 = Node("Apel")
simpul2 = Node("Pisang")
simpul3 = Node("Ceri")

# 2. Sambungkan pointer `next` dari satu simpul ke simpul selanjutnya
simpul1.next = simpul2  # Simpul 1 menunjuk ke Simpul 2
simpul2.next = simpul3  # Simpul 2 menunjuk ke Simpul 3

# Hasil rantai di memori: "Apel" ──► "Pisang" ──► "Ceri" ──► None
```

### Langkah 3: Membuat Kelas Pengendali Otomatis
Untuk mengotomatisasi penyambungan data baru, kita buat kelas pengendali utama yang memegang gerbong terdepan (**Head**):
```python
class LinkedListSederhana:
    def __init__(self):
        self.head = None  # Mulanya rantai kosong tidak ada isinya

    # Fungsi untuk menyambungkan gerbong baru di ujung paling belakang
    def tambah_di_akhir(self, data_baru):
        node_baru = Node(data_baru)
        
        # Jika rantai masih kosong, langsung jadikan simpul baru sebagai Head
        if self.head is None:
            self.head = node_baru
            return
            
        # Jika sudah ada isi, berjalan melompati rantai hingga menemukan gerbong terakhir
        current = self.head
        while current.next is not None:
            current = current.next
            
        # Sambungkan gerbong terakhir ke simpul baru
        current.next = node_baru
```

---

## 📌 Bagian 3: Detail Implementasi Kode (`gading/linked_list.py`)

Setelah memahami konsep dasar Linked List di atas, kelas **`LinkedList`** yang kita gunakan di berkas **`gading/linked_list.py`** adalah perwujudan langsung dari struktur data Linked List dasar ini.

### Karakteristik Utama Kode:
1.  **Struktur Satu Arah:** Setiap simpul Node menyimpan pointer `next` untuk menunjuk ke depan.
2.  **Operasi Utama:**
    *   `insert_at_beginning()`: Menyisipkan Node baru langsung di Head.
    *   `insert_at_end()`: Menelusuri rantai ke belakang lalu menggantungkan Node baru.
    *   `delete_value()`: Mencari simpul dengan nilai tertentu, lalu melakukan *bypass* pointer (memutuskan hubungan simpul tersebut agar dilewati rantai).

---

## 📌 Bagian 4: Panduan Skenario Rekaman Video Presentasi

Saat merekam video presentasi untuk bagian Linked List, ikuti alur penjelasan lisan berikut agar terdengar natural dan menguasai materi:

1.  **Pendahuluan Dasar (Kunci Sukses):**
    > *"Halo Bapak/Ibu Dosen, kali ini saya akan menjelaskan konsep dasar Linked List. Sederhananya, Linked List adalah rantai simpul dinamis di memori komputer yang saling terhubung menggunakan pointer penunjuk arah, layaknya gerbong kereta api. Struktur ini memecahkan masalah kelemahan Array biasa yang boros waktu saat harus menggeser memori fisik."*
2.  **Jelaskan Logika Dasar Pembuatan:**
    *   Tunjukkan bagaimana kelas `Node` menyimpan data dan pointer `self.next`.
    *   Jelaskan bahwa dengan memegang pointer terdepan (`self.head`), kita bisa menelusuri seluruh isi rantai dari awal hingga akhir.
3.  **Jalankan Kode & Tunjukkan Aksi Dashboard:**
    *   Jalankan program utama `python3 main.py` lalu buka **Menu 3** (Linked List).
    *   Lakukan simulasi penambahan data, dan jelaskan bagaimana alamat memori pointer `──►` diperbarui secara real-time di layar konsol saat elemen baru ditambahkan.
