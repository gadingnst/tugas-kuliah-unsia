# Panduan Ujian & Presentasi: Kupas Tuntas Array List (Dynamic Array)
> **Topik Fokus:** Teori Dasar, Size vs Capacity, Mekanisme Resizing, Komparasi Linked List, & Dokumentasi Kode
> **Implementasi Kode:** `gading/array_list.py`
> **Pembuat:** Gading Nst

---

## 📌 Slide 1: Pendahuluan Array List (Dynamic Array)

### Apa itu Array List?
**Array List (Dynamic Array / Larik Dinamis)** adalah struktur data linear berbasis array biasa yang memiliki kemampuan untuk **menyesuaikan ukurannya secara otomatis (resizing)** ketika elemen data yang dimasukkan sudah melebihi kapasitas memori fisiknya.

Pada static array biasa (seperti di C++ atau Java), kita wajib mendeklarasikan ukuran memori di awal (misal: `int arr[5]`). Jika data ke-6 masuk, program akan *crash* karena kehabisan tempat. Array List memecahkan masalah ini dengan mengelola memori cadangan di belakang layar secara otomatis.

### 💺 Analogi Sederhana
Bayangkan Array List seperti **barisan kursi bioskop yang dipesan oleh rombongan**. Jika rombongan memesan 4 kursi bersebelahan, lalu tiba-tiba datang orang ke-5, seluruh rombongan terpaksa berdiri dan pindah ke barisan baru yang menyediakan 8 kursi kosong bersebelahan. Tempat duduk lama kemudian ditinggalkan.

---

## 📌 Slide 2: Anatomi Array List: Size vs Capacity

Dosen sangat sering menguji pemahaman mahasiswa tentang perbedaan dua parameter penting di belakang layar Array List:

```text
       Kapasitas Fisik (Capacity) = 4
       +───────────+───────────+───────────+───────────+
       |  Elemen A |  Elemen B |  [RESERVE]|  [RESERVE]|
       +───────────+───────────+───────────+───────────+
         Indeks 0    Indeks 1    Indeks 2    Indeks 3
         
       * Elemen Aktif (Size) = 2
```

1.  **Size (Ukuran Logis):**
    Menyatakan jumlah elemen aktual yang **aktif dan telah diisi data** oleh pengguna di dalam array.
2.  **Capacity (Kapasitas Fisik):**
    Menyatakan jumlah total **slot memori yang dipesan secara nyata** di dalam RAM. Capacity selalu $\ge$ Size. Selisih antara Capacity dan Size disebut sebagai *reserve memory* (memori cadangan).

---

## 📌 Slide 3: Mekanisme Kerja Resizing (Skalabilitas Geometris)

Bagaimana Array List bertambah besar saat memori fisiknya penuh?

```text
       Kapasitas Penuh (Size = 4, Capacity = 4)
       +─────+─────+─────+─────+
       |  A  |  B  |  C  |  D  |
       +─────+─────+─────+─────+
       
       Ketika dimasukkan data ke-5 ("E"), sistem akan otomatis:
       
       1. Membuat array baru di RAM dengan kapasitas ganda (8 slot).
       2. Menyalin (copy) seluruh elemen lama (A, B, C, D) ke array baru.
       3. Memasukkan elemen baru ("E") pada indeks ke-4.
       4. Menghapus array lama dari memori RAM.
       
       Kapasitas Baru (Capacity = 8)
       +─────+─────+─────+─────+─────+───────────+───────────+───────────+
       |  A  |  B  |  C  |  D  |  E  |  [RESERVE]|  [RESERVE]|  [RESERVE]|
       +─────+─────+─────+─────+─────+───────────+───────────+───────────+
```

> ⚠️ **Mengapa Kapasitas Dikali 2 (Bukan Ditambah 1)?**
> Jika kita hanya menambah kapasitas sebesar 1 setiap kali penuh, maka setiap kali memanggil `.append()`, komputer terpaksa melakukan penyalinan data ($O(N)$). Dengan melipatgandakan kapasitas secara geometris (faktor pengali 2), rata-rata biaya operasi penambahan elemen tetap sangat cepat, yaitu **$O(1)$ Amortized**.

---

## 📌 Slide 4: Kompleksitas Waktu: Static Array vs Array List vs Linked List

Berikut adalah tabel komparasi efisiensi waktu (Big-O) untuk membantu Anda menjelaskan posisi Array List dalam struktur data:

| Operasi | 📱 Static Array | 📦 Array List (Dynamic) | 🔗 Linked List |
| :--- | :---: | :---: | :---: |
| **Akses Indeks (Random Access)** | $O(1)$ *(Sangat Cepat)* | $O(1)$ *(Sangat Cepat)* | $O(N)$ *(Lambat)* |
| **Penyisipan di Akhir (Append)** | $O(1)$ (Selama muat) | $O(1)$ *(Amortized)* | $O(N)$ atau $O(1)$* |
| **Penyisipan di Tengah (Insert)**| $O(N)$ (Harus geser) | $O(N)$ *(Harus geser)* | $O(1)$ (Pointer diketahui) |
| **Penghapusan (Deletion)** | $O(N)$ (Harus geser) | $O(N)$ *(Harus geser)* | $O(1)$ atau $O(N)$ |

---

## 📌 Slide 5: Kelebihan & Kekurangan Array List

### ✅ Kelebihan Array List:
1.  **Akses Acak Instan ($O(1)$):** Kita dapat langsung mengambil atau mengubah nilai elemen di indeks mana saja secara instan karena alamat RAM dihitung dengan rumus: $\text{Alamat Dasar} + (\text{Indeks} \times \text{Ukuran Data})$.
2.  **Sangat Hemat Memori Pointer:** Tidak seperti Linked List yang boros menyimpan penunjuk alamat di setiap elemen, Array List murni hanya menyimpan data aktual secara berurutan.
3.  **Ramah Cache L1/L2 CPU:** Karena data kontigu (berurutan bersebelahan), CPU dapat membaca blok data ke dalam cache dengan sangat cepat (*spatial locality*).

### ❌ Kekurangan Array List:
1.  **Operasi Sisip/Hapus Lambat ($O(N)$):** Menyisipkan atau menghapus elemen di tengah/awal mengharuskan komputer menggeser (*shifting*) ribuan elemen lainnya ke kanan atau ke kiri.
2.  **Puncak Biaya Resizing:** Operasi `.append()` yang memicu resizing akan memakan waktu lambat ($O(N)$) karena proses alokasi dan penyalinan data baru.
3.  **Pemborosan Memori Cadangan:** Selisih kapasitas memori kosong (`[RESERVE]`) tetap memakan ruang RAM meskipun belum diisi data aktif oleh pengguna.

---

## 📌 Bagian 2: Panduan Membuat Array List Sederhana dari Nol (Python)

Berikut contoh paling sederhana cara memprogram Dynamic Array di Python menggunakan list pra-alokasi statis:

### 1. Inisialisasi Memori Awal
```python
class DynamicArraySederhana:
    def __init__(self):
        self.size = 0          # Indeks aktif
        self.capacity = 4      # Kapasitas fisik awal
        self.items = [None] * self.capacity  # Pra-alokasi memori kosong
```

### 2. Tambah Data & Resize Otomatis
```python
    def append(self, item):
        # Jika memori penuh, lakukan resize ganda
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        self.items[self.size] = item
        self.size += 1

    def _resize(self, new_capacity):
        print(f"Resize memori: {self.capacity} -> {new_capacity}")
        new_items = [None] * new_capacity
        
        # Salin data lama ke wadah memori baru
        for i in range(self.size):
            new_items[i] = self.items[i]
            
        self.items = new_items
        self.capacity = new_capacity
```

---

## 📌 Bagian 3: Detail Implementasi Kode (`gading/array_list.py`)

Di dalam berkas program utama **`gading/array_list.py`**, kita mengimplementasikan kelas `ArrayList` kustom dengan fitur lengkap:
*   **`append(item)`**: Menambahkan data di akhir, otomatis memicu penggandaan kapasitas jika penuh.
*   **`insert(index, item)`**: Menyisipkan data pada indeks spesifik dan menggeser seluruh elemen di kanannya ke arah kanan ($O(N)$).
*   **`delete_at(index)`**: Menghapus data pada indeks spesifik dan merapatkan kembali elemen di kanannya ke arah kiri ($O(N)$).
*   **`pop()`**: Mengambil data terakhir dan secara otomatis menyusutkan kapasitas fisik memori menjadi setengah jika elemen aktif turun di bawah 25% kapasitas (hemat RAM).
*   **`get_visualization()`**: Menampilkan representasi visual blok memori RAM kontigu bertuliskan elemen aktif dan cadangan memori kosong (`[RESERVE]`).

---

## 📌 Bagian 4: Panduan Skenario Rekaman Video Presentasi

Gunakan panduan naskah lisan berikut untuk menjelaskan topik Array List secara percaya diri saat merekam video presentasi:

1.  **Pembuka & Konsep Utama:**
    > *"Selanjutnya, saya akan menjelaskan konsep Array List atau Larik Dinamis. Sederhananya, ini adalah array yang bisa bertambah besar secara otomatis ketika penuh. Konsep kuncinya terletak pada pemisahan antara **Size** atau jumlah elemen aktif, dan **Capacity** atau total slot memori yang dipesan di RAM."*
2.  **Jelaskan Mekanisme Resizing:**
    *   Tunjukkan visualisasi Slide 3. *"Ketika kapasitas penuh, Array List melakukan resizing secara geometris sebesar dua kali lipat untuk memastikan rata-rata waktu operasi penambahan elemen tetap sangat cepat, yaitu $O(1)$ Amortized."*
3.  **Tunjukkan Demonstrasi Live:**
    *   Jalankan program utama `python3 main.py` lalu buka **Menu 4** (Array List).
    *   Tunjukkan visualisasi awal berisi 3 data dan 1 slot `[RESERVE]`.
    *   Masukkan data ke-4. Tunjukkan memori terisi penuh.
    *   Masukkan data ke-5. Tunjukkan kepada dosen bagaimana log sistem secara otomatis mencetak:
        `[ SYSTEM INFO ] Memori Penuh! Me-resize kapasitas: 4 ──► 8...`
        dan slot `[RESERVE]` di terminal langsung bertambah panjang menjadi 8 kolom! Ini adalah momen pembuktian terbaik di video Anda.
