# Panduan Ujian & Presentasi: Kupas Tuntas Stack (Tumpukan)
> **Topik Fokus:** Teori Dasar, LIFO Principle, Anatomi TOP Pointer, Kelebihan/Kekurangan, & Dokumentasi Kode
> **Implementasi Kode:** `gading/stack.py`
> **Pembuat:** Gading Nst

---

## 📌 Slide 1: Pendahuluan Stack (Tumpukan)

### Apa itu Stack?
**Stack (Tumpukan)** adalah struktur data linear dinamis yang beroperasi berdasarkan prinsip **LIFO (Last In, First Out)**, yang menyatakan bahwa elemen data yang terakhir kali dimasukkan akan menjadi elemen yang pertama kali dikeluarkan.

Penambahan dan pengambilan data dibatasi hanya pada satu ujung yang sama, yang dikenal sebagai **Puncak Tumpukan (TOP)**. Elemen terbawah disebut sebagai **BASE**.

### 🍽️ Analogi Sederhana
Bayangkan sebuah **tumpukan piring makan di restoran**. Piring terakhir yang dicuci bersih akan diletakkan di posisi paling atas tumpukan (TOP). Ketika pelanggan ingin mengambil piring, piring teratas itulah yang pertama kali diambil (LIFO). Piring paling bawah (BASE) adalah yang paling lama berada di tumpukan.

---

## 📌 Slide 2: Anatomi Stack & TOP Pointer

Struktur data Stack sangat bergantung pada satu variabel penunjuk posisi yang aktif memantau puncak tumpukan, yaitu **TOP Pointer**:

```text
     ┌───────────┐  ◄─── TOP (Gerbang Masuk & Keluar Data)
     │ Elemen C  │  (Elemen Terakhir Masuk / Pertama Keluar)
     ├───────────┤
     │ Elemen B  │
     ├───────────┤
     │ Elemen A  │  ◄─── BASE (Elemen Pertama Masuk / Terbawah)
     └───────────┘
```

1.  **TOP (Puncak):**
    Indeks memori yang menunjukkan posisi elemen teratas tumpukan saat ini. TOP pointer akan bergeser naik setiap kali ada data masuk, dan bergeser turun setiap kali ada data keluar.
2.  **BASE (Dasar):**
    Menandai elemen pertama yang dimasukkan ke dalam Stack (paling bawah). BASE tidak pernah bergeser.

---

## 📌 Slide 3: Operasi Utama pada Stack

Ada tiga operasi mutlak yang mengendalikan siklus hidup data di dalam Stack, semuanya berjalan sangat cepat dalam skala waktu konstan **$O(1)$**:

### 1. Push (Memasukkan Data) ──► $O(1)$
Operasi untuk menyisipkan elemen baru ke puncak tumpukan (TOP).
*   **Alur:** Data baru diletakkan di atas elemen berstatus TOP lama, lalu label TOP bergeser naik menunjuk ke data baru tersebut.

### 2. Pop (Mengeluarkan Data) ──► $O(1)$
Operasi untuk mengambil dan menghapus elemen dari puncak tumpukan (TOP).
*   **Alur:** Data pada posisi TOP diambil, lalu label TOP bergeser turun menunjuk ke elemen di bawahnya.

### 3. Peek (Mengintip Data Puncak) ──► $O(1)$
Operasi untuk membaca nilai elemen teratas (TOP) saat ini tanpa menghapusnya dari tumpukan.

---

## 📌 Slide 4: Kelebihan & Kekurangan Stack

### ✅ Kelebihan Stack:
1.  **Operasi Sangat Instan ($O(1)$):** Operasi Push, Pop, dan Peek berjalan dalam waktu konstan karena sistem tidak perlu mencari data atau menggeser memori fisik RAM.
2.  **Manajemen Memori yang Sangat Aman:** Mencegah modifikasi data acak karena titik akses terisolasi ketat hanya pada satu gerbang (TOP).
3.  **Cocok untuk Riwayat Berbalik (Backtracking):** Sangat ideal untuk riwayat pencarian web (fitur Back), pembatalan ketikan (Undo-Redo Editor), dan pemanggilan fungsi program (*Call Stack*).

### ❌ Kekurangan Stack:
1.  **Tidak Ada Akses Acak (No Random Access):** Kita tidak bisa langsung mengambil data di posisi BASE atau di tengah-tengah ($O(N)$). Kita terpaksa melakukan Pop berulang-ulang untuk membuang elemen di atasnya terlebih dahulu.
2.  **Bahaya Stack Overflow:** Jika kita melakukan operasi Push secara terus-menerus melampaui alokasi batas memori RAM yang disediakan, program akan *crash* karena kehabisan tempat (*Stack Overflow*).
3.  **Akses Ujung Terbatas:** Kita tidak bisa menambahkan data di dasar tumpukan (*insert base*).

---

## 📌 Bagian 2: Panduan Membuat Stack Sederhana dari Nol (Python)

Berikut adalah contoh pembuatan Stack paling sederhana di Python menggunakan list biasa bawaan:

### 1. Inisialisasi Wadah Stack
```python
class StackSederhana:
    def __init__(self):
        self.stack = []  # List kosong bawaan Python
```

### 2. Fungsi Push (Masuk TOP)
```python
    def push(self, item):
        self.stack.append(item)  # Menambahkan data di akhir list (bertindak sebagai TOP)
```

### 3. Fungsi Pop (Keluar TOP)
```python
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Stack Kosong!")
        # pop() tanpa argumen otomatis mengambil & menghapus elemen paling akhir (TOP)
        return self.stack.pop()
```

### 4. Fungsi Peek (Intip TOP)
```python
    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("Stack Kosong!")
        return self.stack[-1]  # Membaca indeks terakhir
```

---

## 📌 Bagian 3: Detail Implementasi Kode (`gading/stack.py`)

Di dalam berkas program utama **`gading/stack.py`**, kita mengimplementasikan kelas `Stack` dasar:
*   **`push(item)`**: Memasukkan elemen ke bagian atas tumpukan menggunakan fungsi bawaan `.append()`.
*   **`pop()`**: Menghapus dan mengambil elemen teratas menggunakan fungsi bawaan `.pop()`.
*   **`peek()`**: Melihat data teratas tanpa menghapusnya (`self.items[-1]`).
*   **`get_visualization()`**: Menghasilkan representasi ASCII vertikal yang rapi di terminal, lengkap dengan label penunjuk TOP dan BASE secara visual.

---

## 📌 Bagian 4: Panduan Skenario Rekaman Video Presentasi

Gunakan naskah panduan lisan berikut saat merekam bagian presentasi Stack untuk menunjukkan penguasaan materi yang lancar:

1.  **Pembuka Presentasi:**
    > *"Pertama, saya akan menjelaskan konsep Stack atau Tumpukan. Stack adalah struktur data linear dinamis yang beroperasi berdasarkan prinsip LIFO, Last In First Out. Artinya, data yang terakhir kali dimasukkan akan menjadi data yang pertama kali dikeluarkan, mirip dengan tumpukan piring makan di restoran."*
2.  **Jelaskan Anatomi TOP:**
    *   Tunjukkan visualisasi Slide 2. Jelaskan peran pointer **TOP** di puncak tumpukan sebagai satu-satunya pintu gerbang masuk dan keluarnya data secara instan dalam skala waktu $O(1)$.
3.  **Tunjukkan Demonstrasi Live:**
    *   Jalankan program utama `python3 main.py` lalu pilih **Menu 1** (Stack).
    *   Tunjukkan visualisasi awal tumpukan vertikal di layar terminal.
    *   Lakukan operasi `Push` untuk menambahkan data baru. Tunjukkan bahwa data baru selalu menempati posisi paling atas (**TOP**).
    *   Lakukan operasi `Pop` untuk mengeluarkan data. Tunjukkan kepada dosen secara visual bahwa data di posisi teratas (**TOP**) adalah yang terhapus dan keluar terlebih dahulu!
