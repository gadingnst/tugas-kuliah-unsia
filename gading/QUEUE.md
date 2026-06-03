# Panduan Ujian & Presentasi: Kupas Tuntas Queue (Antrean)
> **Topik Fokus:** Teori Dasar, FIFO Principle, Anatomi Front & Rear, Kelebihan/Kekurangan, & Dokumentasi Kode
> **Implementasi Kode:** `gading/queue_custom.py`
> **Pembuat:** Gading Nst

---

## 📌 Slide 1: Pendahuluan Queue (Antrean)

### Apa itu Queue?
**Queue (Antrean)** adalah struktur data linear dinamis yang beroperasi berdasarkan prinsip **FIFO (First In, First Out)**, yang berarti elemen data yang pertama kali masuk ke dalam antrean akan menjadi elemen yang pertama kali keluar.

Ini adalah kebalikan dari Stack (Tumpukan) yang menganut prinsip LIFO. Pada Queue, penambahan elemen dilakukan di satu ujung (belakang), dan penghapusan dilakukan di ujung lainnya (depan).

### 👥 Analogi Sederhana
Bayangkan sebuah **antrean pembelian tiket di kasir bioskop**. Orang pertama yang berdiri mengantre di depan loket akan dilayani pertama kali dan keluar dari antrean pertama kali. Orang yang baru datang harus berdiri di posisi paling belakang untuk menunggu giliran mereka.

---

## 📌 Slide 2: Anatomi Queue: Front & Rear

Struktur data Queue dikendalikan oleh **dua penunjuk posisi (pointer)** penting yang menandai gerbang keluar dan masuknya data:

```text
   [ KELUAR / EXIT ]                                                [ MASUK / ENTER ]
         ▲                                                                ▲
         │      +─────────+─────────+─────────+  <─── Aliran Data         │
         └───── | FRONT:A |    B    | REAR:C  | ──────────────────────────┘
                +─────────+─────────+─────────+
                  Index 0   Index 1   Index 2
```

1.  **FRONT (Depan):**
    Penunjuk indeks memori yang menandai elemen terdepan dari antrean (kepala antrean). Semua operasi pengambilan/penghapusan data dilakukan di posisi FRONT.
2.  **REAR (Belakang / Tail):**
    Penunjuk indeks memori yang menandai elemen paling akhir dari antrean (ekor antrean). Semua operasi penambahan data baru dilakukan di posisi REAR.

---

## 📌 Slide 3: Operasi Utama pada Queue

Ada dua operasi mutlak yang mengendalikan siklus hidup data di dalam Queue:

### 1. Enqueue (Memasukkan Data) ──► Berjalan di REAR ($O(1)$)
Operasi untuk memasukkan elemen baru ke bagian belakang antrean. 
*   **Alur:** Data baru masuk tepat di belakang elemen berstatus REAR, lalu label REAR berpindah menunjuk ke data baru tersebut.

### 2. Dequeue (Mengeluarkan Data) ──► Berjalan di FRONT ($O(N)$ atau $O(1)$*)
Operasi untuk menghapus dan mengambil elemen dari bagian depan antrean.
*   **Alur:** Data pada posisi FRONT diambil, lalu label FRONT berpindah ke elemen kedua.
*   *Catatan Performa:* Pada Array biasa, setelah elemen FRONT diambil, komputer harus menggeser (*shifting*) seluruh sisa elemen di belakangnya ke arah kiri agar posisi FRONT tetap berada di indeks 0. Pergeseran fisik ini memakan waktu $O(N)$.

---

## 📌 Slide 4: Kelebihan & Kekurangan Queue

### ✅ Kelebihan Queue:
1.  **Menjamin Keadilan Aliran Data (FIFO):** Data diproses secara berurutan sesuai urutan kedatangan. Sangat penting untuk sistem penjadwalan CPU, printer spooler, atau transmisi paket data jaringan.
2.  **Mencegah Tabrakan Data (Buffering):** Berguna sebagai penampung sementara (buffer) saat kecepatan pengirim data lebih cepat daripada kecepatan penerima data (misalnya saat buffering streaming video).
3.  **Implementasi Sederhana:** Aturan akses data terstruktur rapi (masuk belakang, keluar depan), meminimalisir kesalahan manipulasi memori.

### ❌ Kekurangan Queue:
1.  **Tidak Ada Akses Acak (No Random Access):** Kita tidak bisa melompati antrean untuk membaca elemen di tengah secara acak ($O(N)$). Kita harus mengeluarkan semua elemen di depannya satu per satu.
2.  **Biaya Pergeseran Memori ($O(N)$ Dequeue):** Pada implementasi antrean berbasis list standar, proses mengeluarkan elemen depan memaksa sistem menggeser seluruh elemen tersisa ke kiri, memakan waktu lambat untuk antrean skala besar.
3.  **Keterbatasan Akses Ujung:** Operasi penambahan di depan (*insert front*) atau pengambilan di belakang (*pop rear*) tidak diizinkan dalam konsep dasar Queue murni.

---

## 📌 Bagian 2: Panduan Membuat Queue Sederhana dari Nol (Python)

Berikut adalah contoh pembuatan Queue paling dasar di Python menggunakan list biasa:

### 1. Inisialisasi Wadah Queue
```python
class Queue:
    def __init__(self):
        self.items = []  # List internal untuk menyimpan elemen antrean
```

### 2. Fungsi Enqueue (Masuk Belakang)
```python
    def enqueue(self, item):
        self.items.append(item)  # Tambahkan item ke bagian belakang antrean
```

### 3. Fungsi Dequeue (Keluar Depan)
```python
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Error: Dequeue dari Queue kosong tidak diperbolehkan!")
        return self.items.pop(0)  # Hapus dan kembalikan elemen paling depan
```

### 4. Front (Intip Depan)
```python
    def front(self):
        if self.is_empty():
            raise IndexError("Error: Queue kosong!")
        return self.items[0]  # Kembalikan elemen depan tanpa menghapusnya
```

---

## 📌 Bagian 3: Detail Implementasi Kode (`gading/queue_custom.py`)

Di dalam berkas program utama **`gading/queue_custom.py`**, kita mengimplementasikan kelas `Queue` dasar:
*   **`enqueue(item)`**: Memasukkan elemen ke bagian belakang antrean menggunakan fungsi `.append()`.
*   **`dequeue()`**: Menghapus dan mengambil elemen terdepan menggunakan fungsi `.pop(0)`.
*   **`front()`**: Melihat data terdepan antrean tanpa menghapusnya (`self.items[0]`).
*   **`get_visualization()`**: Menghasilkan representasi ASCII horizontal dinamis yang menampilkan arah panah masuk-keluar antrean secara intuitif di layar terminal.

---

## 📌 Bagian 4: Panduan Skenario Rekaman Video Presentasi

Gunakan panduan naskah lisan berikut saat merekam bagian presentasi Queue untuk menunjukkan penguasaan materi yang lancar:

1.  **Pembuka Presentasi:**
    > *"Berikutnya, saya akan menjelaskan konsep Queue atau Antrean. Berbeda dengan Stack yang bersifat LIFO, Queue beroperasi berdasarkan prinsip FIFO, First In First Out. Artinya, data yang masuk pertama kali akan dilayani dan keluar pertama kali, layaknya antrean di loket kasir bioskop."*
2.  **Jelaskan Anatomi Pointer:**
    *   Tunjukkan visualisasi Slide 2. Jelaskan peran pointer **FRONT** di depan sebagai pintu keluar data, dan pointer **REAR** di belakang sebagai pintu masuk data baru.
3.  **Tunjukkan Demonstrasi Live:**
    *   Jalankan program utama `python3 main.py` lalu pilih **Menu 2** (Queue).
    *   Tunjukkan visualisasi awal antrean horizontal di layar terminal.
    *   Lakukan operasi `Enqueue` untuk menambahkan data baru. Tunjukkan bahwa data baru selalu menempel di sisi paling kanan (**REAR**).
    *   Lakukan operasi `Dequeue` untuk mengeluarkan data. Tunjukkan kepada dosen secara visual bahwa data di posisi paling kiri (**FRONT**) adalah yang terhapus dan keluar terlebih dahulu!
