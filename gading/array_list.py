# -*- coding: utf-8 -*-
"""
Modul Struktur Data: Array List (Dynamic Array / Larik Dinamis)
Karakteristik: Struktur data linear dengan elemen yang disimpan di lokasi memori berurutan (kontigu).
Kapasitas memori dicadangkan sebelumnya dan akan bertambah secara otomatis (resizing) saat penuh.
"""
import ctypes

class ArrayList:
    """
    Implementasi kustom Array List (Dynamic Array) untuk tujuan edukasi.
    Di Python, list bawaan sudah dinamis. Namun, kelas ini menggunakan modul 'ctypes'
    untuk membuat static array mentah (fixed-size) agar dapat mendemonstrasikan bagaimana
    resizing (penggandaan kapasitas) dan manajemen memori kontigu bekerja di balik layar 
    (seperti std::vector di C++ atau ArrayList di Java).
    """
    def __init__(self, initial_capacity: int = 4):
        """Inisialisasi Array List dengan kapasitas awal default 4."""
        self.n = 0  # Ukuran elemen aktif (size)
        self.capacity = initial_capacity  # Kapasitas memori fisik yang dialokasikan
        self.A = self._make_array(self.capacity)  # Array internal statis

    def __len__(self) -> int:
        """Mengembalikan jumlah elemen aktif dalam Array List."""
        return self.n

    def size(self) -> int:
        """Mengembalikan jumlah elemen aktif (alias len)."""
        return self.n

    def get_capacity(self) -> int:
        """Mengembalikan kapasitas memori fisik saat ini."""
        return self.capacity

    def is_empty(self) -> bool:
        """Memeriksa apakah Array List kosong."""
        return self.n == 0

    def __getitem__(self, index: int):
        """Mengambil elemen pada indeks tertentu (mendukung notasi array[index])."""
        if not 0 <= index < self.n:
            raise IndexError("Error: Indeks di luar jangkauan (Index Out of Bounds)!")
        return self.A[index]

    def get(self, index: int):
        """Mengambil elemen pada indeks tertentu."""
        return self.__getitem__(index)

    def append(self, item) -> None:
        """Menambahkan elemen baru di akhir Array List. Otomatis me-resize jika penuh."""
        if self.n == self.capacity:
            # Jika kapasitas penuh, lipat gandakan kapasitas memori (Faktor Penggali = 2)
            self._resize(2 * self.capacity)
            
        self.A[self.n] = item
        self.n += 1

    def insert(self, index: int, item) -> None:
        """
        Menyisipkan elemen pada indeks tertentu dan menggeser elemen di kanannya.
        Mengangkat Exception jika indeks tidak valid.
        """
        if not 0 <= index <= self.n:
            raise IndexError("Error: Indeks penyisipan tidak valid!")

        # Resize jika kapasitas penuh sebelum menyisipkan
        if self.n == self.capacity:
            self._resize(2 * self.capacity)

        # Geser seluruh elemen di sebelah kanan indeks ke arah kanan
        for i in range(self.n, index, -1):
            self.A[i] = self.A[i - 1]

        # Sisipkan elemen baru
        self.A[index] = item
        self.n += 1

    def pop(self):
        """Menghapus dan mengembalikan elemen terakhir dari Array List."""
        if self.is_empty():
            raise IndexError("Error: Pop dari Array List kosong tidak diperbolehkan!")
        
        item = self.A[self.n - 1]
        self.A[self.n - 1] = None  # Bantu Garbage Collector
        self.n -= 1
        
        # Opsional: Perkecil kapasitas jika elemen aktif terlalu sedikit (misal < 25%)
        if 0 < self.n <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)
            
        return item

    def delete_at(self, index: int):
        """Menghapus elemen pada indeks tertentu dan menggeser elemen sisanya ke kiri."""
        if not 0 <= index < self.n:
            raise IndexError("Error: Indeks penghapusan di luar jangkauan!")

        removed_item = self.A[index]

        # Geser semua elemen setelah indeks ke arah kiri
        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = None
        self.n -= 1

        # Perkecil kapasitas jika elemen sangat sedikit
        if 0 < self.n <= self.capacity // 4 and self.capacity > 4:
            self._resize(self.capacity // 2)

        return removed_item

    def _resize(self, new_capacity: int) -> None:
        """
        Melakukan alokasi array statis baru dengan kapasitas baru,
        menyalin elemen lama, dan mengganti referensi array lama.
        """
        print(f"\n[ SYSTEM INFO ] Memori Penuh! Me-resize kapasitas: {self.capacity} ──► {new_capacity}...")
        B = self._make_array(new_capacity)  # Buat array statis baru
        
        # Salin elemen dari array A ke array baru B
        for i in range(self.n):
            B[i] = self.A[i]
            
        self.A = B  # Ganti referensi array A ke B
        self.capacity = new_capacity  # Perbarui nilai kapasitas

    def _make_array(self, capacity: int):
        """Mengembalikan array statis baru menggunakan representasi ctypes."""
        return (capacity * ctypes.py_object)()

    def clear(self) -> None:
        """Mengosongkan Array List dan mereset kapasitas ke 4."""
        self.n = 0
        self.capacity = 4
        self.A = self._make_array(self.capacity)

    def get_visualization(self) -> str:
        """
        Menghasilkan visualisasi Array List di memori fisik.
        Menunjukkan dengan jelas elemen aktif (Active) dan cadangan memori kosong (Reserve/Buffer).
        """
        elements = []
        for i in range(self.capacity):
            if i < self.n:
                val = str(self.A[i])
                if len(val) > 7:
                    val = val[:4] + "..."
                elements.append(f" {val.center(7)} ")
            else:
                # Menunjukkan reserve memory (belum diisi elemen aktif)
                elements.append(" [RESERVE] ")

        # Tampilan block kontigu di memori
        border = "+" + "+".join(["─────────" for _ in range(self.capacity)]) + "+"
        content = "|" + "|".join(elements) + "|"
        
        indices = []
        for i in range(self.capacity):
            if i < self.n:
                indices.append(f"  [{i}].size  ")
            else:
                indices.append(f"  [{i}].cap   ")
        indices_str = " " + " ".join(indices)

        info = f" -> INFO: Size (Elemen Aktif) = {self.n} | Capacity (Fisik) = {self.capacity}"
        return f"{border}\n{content}\n{border}\n{indices_str}\n{info}"


# Demo Penggunaan Array List secara Mandiri (jika file dijalankan langsung)
if __name__ == "__main__":
    print("=" * 80)
    print(" DEMO STRUKTUR DATA: DYNAMIC ARRAY LIST (LARIK DINAMIS KUSTOM)")
    print("=" * 80)
    
    # Inisialisasi kapasitas awal 4
    arr = ArrayList(initial_capacity=4)
    print("1. Array List Baru Dibuat (Kapasitas Awal = 4).")
    print(arr.get_visualization())
    print()
    
    # Menambahkan elemen
    print("2. Menambahkan 3 elemen: 'A', 'B', 'C'")
    arr.append("A")
    arr.append("B")
    arr.append("C")
    print(arr.get_visualization())
    print()
    
    # Menambahkan elemen keempat (tepat batas kapasitas)
    print("3. Menambahkan elemen ke-4: 'D'")
    arr.append("D")
    print(arr.get_visualization())
    print()
    
    # Menambahkan elemen kelima (akan memicu RESIZING kapasitas 4 -> 8)
    print("4. Menambahkan elemen ke-5: 'E' (Akan memicu Resizing!)")
    arr.append("E")
    print(arr.get_visualization())
    print()
    
    # Menyisipkan elemen di tengah
    insert_idx = 2
    print(f"5. Menyisipkan 'X' pada indeks {insert_idx} (Element lain tergeser ke kanan):")
    arr.insert(insert_idx, "X")
    print(arr.get_visualization())
    print()
    
    # Menghapus elemen pada indeks tertentu
    del_idx = 3
    print(f"6. Menghapus elemen pada indeks {del_idx}: '{arr.delete_at(del_idx)}'")
    print(arr.get_visualization())
    print()
    
    # Melakukan POP
    print(f"7. Melakukan POP (Mengambil elemen terakhir): '{arr.pop()}'")
    print(arr.get_visualization())
    print("=" * 80)
