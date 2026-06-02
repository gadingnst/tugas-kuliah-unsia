# -*- coding: utf-8 -*-
"""
Modul Struktur Data (Rina): Larik Dinamis (Dynamic Array)
Karakteristik: Menggunakan pra-alokasi kapasitas list Python statis [None] * capacity,
menunjukkan pemisahan tegas antara Size (Elemen Aktif) dan Capacity (Fasilitas Memori Cadangan).
"""

class DynamicArray:
    """
    Implementasi Dynamic Array tanpa menggunakan modul ctypes (berbeda dengan versi Gading).
    Menggunakan teknik pra-alokasi list Python statis untuk mendemonstrasikan bagaimana
    resizing (penggandaan kapasitas) dan shifting (pergeseran indeks memori) bekerja secara manual.
    """
    def __init__(self, initial_capacity: int = 4):
        """Inisialisasi Dynamic Array dengan kapasitas awal."""
        self._size = 0  # Elemen aktif (Logical Size)
        self._capacity = initial_capacity  # Kapasitas fisik (Physical Capacity)
        # Pra-alokasi memori kosong dengan None
        self._A = [None] * self._capacity

    def size(self) -> int:
        """Mengembalikan jumlah elemen aktif saat ini."""
        return self._size

    def get_capacity(self) -> int:
        """Mengembalikan kapasitas memori fisik yang dipesan."""
        return self._capacity

    def is_empty(self) -> bool:
        """Memeriksa apakah array kosong."""
        return self._size == 0

    def get(self, index: int):
        """Mengambil elemen pada indeks tertentu dengan pengecekan batas jangkauan."""
        if not 0 <= index < self._size:
            raise IndexError("Gagal: Indeks di luar jangkauan (Index Out of Bounds)!")
        return self._A[index]

    def add(self, item) -> None:
        """Menambahkan elemen baru di akhir array. Menggandakan kapasitas jika memori penuh."""
        if self._size == self._capacity:
            # Pemicu Resize geometris 2x lipat
            self._resize(2 * self._capacity)
            
        self._A[self._size] = item
        self._size += 1

    def insert_at(self, index: int, item) -> None:
        """ Menyisipkan elemen pada indeks tertentu dan menggeser sisa elemen ke kanan. """
        if not 0 <= index <= self._size:
            raise IndexError("Gagal: Indeks penyisipan tidak valid!")

        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Menggeser elemen dari indeks terakhir ke kanan secara terbalik
        for i in range(self._size, index, -1):
            self._A[i] = self._A[i - 1]

        self._A[index] = item
        self._size += 1

    def remove_at(self, index: int):
        """ Menghapus elemen pada indeks tertentu dan menggeser sisa elemen ke kiri. """
        if not 0 <= index < self._size:
            raise IndexError("Gagal: Indeks penghapusan di luar jangkauan!")

        removed_item = self._A[index]

        # Geser seluruh elemen di sebelah kanan ke kiri
        for i in range(index, self._size - 1):
            self._A[i] = self._A[i + 1]

        self._A[self._size - 1] = None  # Bantu Garbage Collection
        self._size -= 1

        # Perkecil kapasitas jika elemen aktif < 25% kapasitas untuk hemat memori
        if 0 < self._size <= self._capacity // 4 and self._capacity > 4:
            self._resize(self._capacity // 2)

        return removed_item

    def pop(self):
        """Menghapus dan mengembalikan elemen terakhir."""
        if self.is_empty():
            raise IndexError("Gagal: Pop dari Dynamic Array kosong tidak diperbolehkan!")
        return self.remove_at(self._size - 1)

    def clear(self) -> None:
        """Mereset Array kembali ke kapasitas awal 4."""
        self._size = 0
        self._capacity = 4
        self._A = [None] * self._capacity

    def _resize(self, new_capacity: int) -> None:
        """
        Melakukan realokasi memori fisik baru dengan menyalin elemen lama ke array baru
        yang berukuran berbeda (Dynamic Scaling).
        """
        print(f"\n[ SYSTEM INFO ] Kapasitas Penuh! Realokasi memori: {self._capacity} ──► {new_capacity}...")
        new_list = [None] * new_capacity  # Alokasi list baru
        
        # Salin data lama ke list baru
        for i in range(self._size):
            new_list[i] = self._A[i]
            
        self._A = new_list  # Ganti referensi
        self._capacity = new_capacity  # Perbarui variabel kapasitas

    def get_visualization(self) -> str:
        """
        Visualisasi grafis Array dengan pembagian logis antara Slot Aktif dan Slot Cadangan (Kosong).
        """
        blocks = []
        for i in range(self._capacity):
            val = self._A[i]
            if val is None:
                blocks.append(" ░░CADANGAN░░ ")
            else:
                val_str = str(val)
                if len(val_str) > 8:
                    val_str = val_str[:5] + "..."
                blocks.append(f" {val_str.center(12)} ")

        border = "╭" + "┬".join(["──────────────" for _ in range(self._capacity)]) + "╮"
        content = "│" + "│".join(blocks) + "│"
        footer = "╰" + "┴".join(["──────────────" for _ in range(self._capacity)]) + "╯"
        
        indices = []
        for i in range(self._capacity):
            if i < self._size:
                indices.append(f"  [Idx {i}].size  ")
            else:
                indices.append(f"  [Idx {i}].cap   ")
        indices_str = " " + " ".join(indices)
        
        info = f" -> INFO: Elemen Aktif (Size) = {self._size} | Total Kapasitas = {self._capacity}"
        return f"{border}\n{content}\n{footer}\n{indices_str}\n{info}"


# Pengujian Mandiri
if __name__ == "__main__":
    print("=" * 80)
    print(" PROGRAM DEMO DYNAMIC ARRAY (LARIK DINAMIS RINA)")
    print("=" * 80)
    
    da = DynamicArray(initial_capacity=4)
    print("• Dynamic Array baru dengan Kapasitas = 4.")
    print(da.get_visualization())
    print()
    
    print("• Menambahkan elemen: 'Rina', 'Budi', 'Chandra'")
    da.add("Rina")
    da.add("Budi")
    da.add("Chandra")
    print(da.get_visualization())
    print()
    
    print("• Menambahkan elemen ke-4: 'Dewi'")
    da.add("Dewi")
    print(da.get_visualization())
    print()
    
    print("• Menambahkan elemen ke-5: 'Eka' (Akan memicu resizing otomatis!)")
    da.add("Eka")
    print(da.get_visualization())
    print()
    
    print("• Menyisipkan 'Mega' pada indeks 1...")
    da.insert_at(1, "Mega")
    print(da.get_visualization())
    print()
    
    print(f"• Menghapus elemen pada indeks 3: '{da.remove_at(3)}'")
    print(da.get_visualization())
    print("=" * 80)
