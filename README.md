# Projek Visualisasi Struktur Data Majemuk Linear (Python)

Projek ini berisi implementasi mandiri dari struktur data linear majemuk (**Stack, Queue, Linked List, dan Array List**) dalam bahasa pemrograman Python. 

Repositori ini menampung **dua tugas individu yang berbeda secara struktural dan konseptual** (Milik **Gading** dan **Rina**) guna memenuhi persyaratan tugas akademik individu tanpa adanya kesamaan/plagiarisme kode.

---

## 📂 Struktur Direktori

```text
task-struktur-data/
├── README.md                 <-- Panduan Utama Repositori (Berkas Ini)
├── SOAL.md                   <-- Persyaratan Soal Tugas
│
├── gading/                   <-- DIREKTORI TUGAS GADING
│   ├── stack.py              (LIFO Stack dengan Visualisasi Siku Vertikal)
│   ├── queue_custom.py       (FIFO Queue standar dengan Aliran Horizontal)
│   ├── linked_list.py        (Singly Linked List - Satu Arah)
│   ├── array_list.py         (Dynamic Array dengan C-types Memory Allocation)
│   ├── main.py               (Aplikasi Dashboard Utama Gading - Tema Biru & Cyan)
│   └── PRESENTASI.md         (Dokumentasi Panduan Presentasi Gading)
│
└── rina/                     <-- DIREKTORI TUGAS RINA
    ├── stack.py              (LIFO Stack dengan Visualisasi Rounded Unicode)
    ├── circular_queue.py     (Circular Queue - FIFO Ring Buffer Modulo)
    ├── doubly_linked_list.py (Doubly Linked List - Dua Arah)
    ├── dynamic_array.py      (Dynamic Array berbasis Pra-alokasi List Dinamis)
    ├── main.py               (Aplikasi Dashboard Utama Rina - Tema Magenta & Kuning)
    └── PRESENTASI_RINA.md    (Dokumentasi Panduan Presentasi Rina)
```

---

## 📊 Perbandingan Teknis & Keunikan Kode

Meskipun membahas topik yang sama, kedua pengerjaan diprogram menggunakan metodologi dan struktur algoritma yang berbeda total:

| Komponen | 👨‍💻 Versi Gading | 👩‍💻 Versi Rina |
| :--- | :--- | :--- |
| **Stack** | List dinamis biasa dengan visualisasi vertikal siku (`┌───┐`). | ArrayStack dengan visualisasi kotak melengkung Unicode (`╭───╮`). |
| **Queue** | **Standard Queue** (FIFO horizontal) dengan pergeseran indeks. | **Circular Queue** (Antrean melingkar ring buffer dengan indeks modulo `%`). |
| **Linked List** | **Singly Linked List** (Satu arah `Head ──► Node ──► NULL`). | **Doubly Linked List** (Dua arah `NULL ◄──► Node ◄──► NULL`). |
| **Array List** | Larik Dinamis menggunakan **`ctypes`** untuk pemesanan RAM fisik mentah. | Larik Dinamis menggunakan teknik **pra-alokasi list** `[None] * capacity`. |
| **Tema CLI** | **Blue & Cyan** (Modern Tech-style) | **Magenta & Yellow** (Premium Elegant-style) |

---

## 🚀 Cara Menjalankan Program

### 1. Menjalankan Dashboard Interaktif Utama (Sangat Direkomendasikan)
Dashboard utama menyediakan menu visual interaktif yang mempermudah demonstrasi secara langsung saat presentasi atau perekaman video.

*   **Menjalankan Dashboard Gading:**
    ```bash
    cd gading
    python3 main.py
    ```
*   **Menjalankan Dashboard Rina:**
    ```bash
    cd rina
    python3 main.py
    ```

### 2. Menjalankan Modul Secara Mandiri (Uji Coba Topik Satu per Satu)
Setiap berkas struktur data dilengkapi dengan fungsi `if __name__ == "__main__":` yang berisi skenario uji coba terisolasi di konsol.

**Folder Gading (`/gading`):**
```bash
python3 gading/stack.py
python3 gading/queue_custom.py
python3 gading/linked_list.py
python3 gading/array_list.py
```

**Folder Rina (`/rina`):**
```bash
python3 rina/stack.py
python3 rina/circular_queue.py
python3 rina/doubly_linked_list.py
python3 rina/dynamic_array.py
```

---

## 📝 Catatan Tambahan Presentasi & Video
Untuk panduan materi presentasi lengkap, diagram visual tambahan, analogi dunia nyata, naskah demo, serta prediksi pertanyaan dari dosen penguji beserta kunci jawabannya, silakan buka berkas dokumentasi markdown berikut:
*   Panduan Presentasi Gading: [gading/PRESENTASI.md](file:///Users/gadingnst/Workspace/private/task-struktur-data/gading/PRESENTASI.md)
*   Panduan Presentasi Rina: [rina/PRESENTASI_RINA.md](file:///Users/gadingnst/Workspace/private/task-struktur-data/rina/PRESENTASI_RINA.md)
