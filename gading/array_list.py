# -*- coding: utf-8 -*-
"""
Modul Struktur Data: Array List (Dynamic Array / Larik Dinamis)
Karakteristik: Menggunakan lokasi memori berurutan (kontigu) dengan kapasitas statis
yang akan bertambah ganda secara otomatis saat terisi penuh.
"""

class ArrayList:
    """
    Implementasi Dynamic Array (Array List) sederhana untuk tujuan pembelajaran.
    Menggunakan pra-alokasi list Python biasa `[None] * capacity` untuk menyimulasikan
    pemesanan memori fisik dan mekanisme penggandaan kapasitas (resizing) otomatis.
    """
    def __init__(self, initial_capacity: int = 4):
        """Inisialisasi Array List dengan kapasitas awal default 4."""
        self._size = 0  # Elemen aktif yang terisi (Logical Size)
        self._capacity = initial_capacity  # Kapasitas memori fisik yang dialokasikan (Physical Capacity)
        self._items = [None] * self._capacity  # Larik internal statis awal

    def __len__(self) -> int:
        """Mengembalikan jumlah elemen aktif."""
        return self._size

    def size(self) -> int:
        """Mengembalikan jumlah elemen aktif."""
        return self._size

    def get_capacity(self) -> int:
        """Mengembalikan kapasitas memori saat ini."""
        return self._capacity

    def is_empty(self) -> bool:
        """Memeriksa apakah Array List kosong."""
        return self._size == 0

    def __getitem__(self, index: int):
        """Mengambil elemen pada indeks tertentu (notasi array[index])."""
        if not 0 <= index < self._size:
            raise IndexError("Error: Indeks di luar jangkauan (Index Out of Bounds)!")
        return self._items[index]

    def get(self, index: int):
        """Mengambil elemen pada indeks tertentu."""
        return self.__getitem__(index)

    def append(self, item) -> None:
        """Menambahkan elemen baru di akhir Array List. Otomatis me-resize jika penuh."""
        if self._size == self._capacity:
            # Jika kapasitas penuh, lipat gandakan kapasitas memori (Faktor Penggali = 2)
            self._resize(2 * self._capacity)
            
        self._items[self._size] = item
        self._size += 1

    def insert(self, index: int, item) -> None:
        """Menyisipkan elemen pada indeks tertentu dan menggeser elemen di kanannya."""
        if not 0 <= index <= self._size:
            raise IndexError("Error: Indeks penyisipan tidak valid!")

        # Resize jika kapasitas penuh sebelum menyisipkan
        if self._size == self._capacity:
            self._resize(2 * self._capacity)

        # Geser seluruh elemen di sebelah kanan indeks ke arah kanan
        for i in range(self._size, index, -1):
            self._items[i] = self._items[i - 1]

        # Sisipkan elemen baru
        self._items[index] = item
        self._size += 1

    def pop(self):
        """Menghapus dan mengembalikan elemen terakhir dari Array List."""
        if self.is_empty():
            raise IndexError("Error: Pop dari Array List kosong tidak diperbolehkan!")
        
        item = self._items[self._size - 1]
        self._items[self._size - 1] = None  # Bantu Garbage Collector
        self._size -= 1
        
        # Perkecil kapasitas jika elemen aktif terlalu sedikit (< 25% kapasitas)
        if 0 < self._size <= self._capacity // 4 and self._capacity > 4:
            self._resize(self._capacity // 2)
            
        return item

    def delete_at(self, index: int):
        """Menghapus elemen pada indeks tertentu dan menggeser elemen sisa ke kiri."""
        if not 0 <= index < self._size:
            raise IndexError("Error: Indeks penghapusan di luar jangkauan!")

        removed_item = self._items[index]

        # Geser semua elemen setelah indeks ke arah kiri
        for i in range(index, self._size - 1):
            self._items[i] = self._items[i + 1]

        self._items[self._size - 1] = None
        self._size -= 1

        # Perkecil kapasitas jika elemen sangat sedikit
        if 0 < self._size <= self._capacity // 4 and self._capacity > 4:
            self._resize(self._capacity // 2)

        return removed_item

    def _resize(self, new_capacity: int) -> None:
        """Mengalokasikan array baru dengan kapasitas baru dan menyalin elemen lama."""
        print(f"\n[ SYSTEM INFO ] Memori Penuh! Me-resize kapasitas: {self._capacity} ──► {new_capacity}...")
        new_items = [None] * new_capacity  # Buat array kosong baru
        
        # Salin elemen lama ke array baru
        for i in range(self._size):
            new_items[i] = self._items[i]
            
        self._items = new_items  # Ganti referensi array internal
        self._capacity = new_capacity  # Perbarui kapasitas

    def clear(self) -> None:
        """Mengosongkan Array List dan mereset kapasitas ke 4."""
        self._size = 0
        self._capacity = 4
        self._items = [None] * self._capacity

    def get_visualization(self) -> str:
        """Menampilkan visualisasi elemen aktif (Active) dan cadangan memori kosong (Reserve)."""
        elements = []
        for i in range(self._capacity):
            if i < self._size:
                val = str(self._items[i])
                if len(val) > 7:
                    val = val[:4] + "..."
                elements.append(f" {val.center(7)} ")
            else:
                elements.append(" [RESERVE] ")

        border = "+" + "+".join(["─────────" for _ in range(self._capacity)]) + "+"
        content = "|" + "|".join(elements) + "|"
        
        indices = []
        for i in range(self._capacity):
            if i < self._size:
                indices.append(f"  [{i}].size  ")
            else:
                indices.append(f"  [{i}].cap   ")
        indices_str = " " + " ".join(indices)

        info = f" -> INFO: Size = {self._size} | Capacity = {self._capacity}"
        return f"{border}\n{content}\n{border}\n{indices_str}\n{info}"


# Demo Mandiri
if __name__ == "__main__":
    print("=" * 80)
    print(" DEMO STRUKTUR DATA: DYNAMIC ARRAY LIST (GADING)")
    print("=" * 80)
    
    arr = ArrayList(initial_capacity=4)
    print("1. Array List Baru (Kapasitas = 4).")
    print(arr.get_visualization())
    print()
    
    print("2. Menambahkan 3 elemen: 'A', 'B', 'C'")
    arr.append("A")
    arr.append("B")
    arr.append("C")
    print(arr.get_visualization())
    print()
    
    print("3. Menambahkan elemen ke-4: 'D'")
    arr.append("D")
    print(arr.get_visualization())
    print()
    
    print("4. Menambahkan elemen ke-5: 'E' (Akan memicu Resizing!)")
    arr.append("E")
    print(arr.get_visualization())
    print()
    
    print("5. Melakukan POP (Mengambil elemen terakhir): '" + arr.pop() + "'")
    print(arr.get_visualization())
    print("=" * 80)
