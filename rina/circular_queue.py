# -*- coding: utf-8 -*-
"""
Modul Struktur Data (Rina): Antrean Melingkar (Circular Queue)
Metodologi: First In First Out (FIFO) - Ring Buffer Berkapasitas Tetap.
"""

class CircularQueue:
    """
    Circular Queue (Antrean Melingkar) dengan kapasitas statis.
    Sangat efisien karena operasi dequeue bernilai O(1) tanpa perlu menggeser elemen
    fisik di memori RAM, memanfaatkan konsep indeks berputar (modulo arithmetic).
    """
    def __init__(self, capacity: int = 5):
        """Inisialisasi antrean sirkular dengan kapasitas tetap (default 5)."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0  # Menyimpan jumlah elemen aktif saat ini

    def is_empty(self) -> bool:
        """Memeriksa apakah antrean dalam keadaan kosong."""
        return self.count == 0

    def is_full(self) -> bool:
        """Memeriksa apakah seluruh slot antrean sudah penuh."""
        return self.count == self.capacity

    def enqueue(self, item) -> None:
        """
        Menambahkan elemen baru ke posisi belakang (rear) antrean.
        Memanfaatkan aritmatika modulo untuk memutar indeks ke depan jika ada slot kosong.
        """
        if self.is_full():
            raise IndexError("Gagal: Antrean sirkular sudah penuh (Queue Overflow)!")
        
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Putar indeks rear secara sirkular
            self.rear = (self.rear + 1) % self.capacity
            
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        """
        Menghapus dan mengembalikan elemen terdepan (front) antrean.
        Sangat efisien karena hanya merotasi penunjuk FRONT tanpa menggeser array.
        """
        if self.is_empty():
            raise IndexError("Gagal: Antrean sirkular kosong (Queue Underflow)!")
            
        removed_item = self.queue[self.front]
        self.queue[self.front] = None  # Kosongkan slot fisik di memori
        
        if self.count == 1:
            # Jika elemen terakhir diambil, reset penunjuk
            self.front = -1
            self.rear = -1
        else:
            # Putar indeks front secara sirkular
            self.front = (self.front + 1) % self.capacity
            
        self.count -= 1
        return removed_item

    def get_front(self):
        """Melihat elemen terdepan (front) antrean."""
        if self.is_empty():
            raise IndexError("Gagal: Antrean sirkular kosong!")
        return self.queue[self.front]

    def get_rear(self):
        """Melihat elemen terakhir (rear) antrean."""
        if self.is_empty():
            raise IndexError("Gagal: Antrean sirkular kosong!")
        return self.queue[self.rear]

    def size(self) -> int:
        """Mendapatkan jumlah elemen aktif saat ini."""
        return self.count

    def clear(self) -> None:
        """Mengosongkan seluruh antrean sirkular."""
        self.queue = [None] * self.capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def get_visualization(self) -> str:
        """
        Menghasilkan visualisasi linear ring-buffer yang memetakan slot memori statis secara nyata.
        Menampilkan posisi penunjuk FRONT (F) dan REAR (R) secara visual.
        """
        slots = []
        for i in range(self.capacity):
            val = self.queue[i]
            if val is None:
                slots.append("   -   ")
            else:
                val_str = str(val)
                if len(val_str) > 5:
                    val_str = val_str[:3] + ".."
                slots.append(f" {val_str.center(5)} ")
        
        # Tampilkan pointer di bawah kotak memori
        pointers = []
        for i in range(self.capacity):
            label = ""
            if i == self.front and i == self.rear:
                label = " [F & R] "
            elif i == self.front:
                label = " [FRONT] "
            elif i == self.rear:
                label = "  [REAR] "
            else:
                label = "         "
            pointers.append(label)

        # Gambar box
        border = "+" + "+".join(["─────────" for _ in range(self.capacity)]) + "+"
        content = "|" + "|".join(slots) + "|"
        pointers_str = " " + " ".join(pointers)
        
        indices = " " + " ".join([f"  Idx {i}  " for i in range(self.capacity)])
        
        info = f" -> INFO: Aktif = {self.count}/{self.capacity} | Front Indeks = {self.front} | Rear Indeks = {self.rear}"
        return f"{border}\n{content}\n{border}\n{indices}\n{pointers_str}\n{info}"


# Pengujian Mandiri
if __name__ == "__main__":
    print("=" * 70)
    print(" PROGRAM DEMO CIRCULAR QUEUE (ANTREAN SIRKULAR RINA)")
    print("=" * 70)
    
    cq = CircularQueue(capacity=5)
    print("• Membuat Circular Queue baru (Kapasitas = 5)...")
    print(cq.get_visualization())
    print()
    
    print("• Enqueue 4 Pelanggan: 'Rina', 'Budi', 'Chandra', 'Dewi'")
    cq.enqueue("Rina")
    cq.enqueue("Budi")
    cq.enqueue("Chandra")
    cq.enqueue("Dewi")
    print(cq.get_visualization())
    print()
    
    print(f"• Dequeue 2 Pelanggan pertama: '{cq.dequeue()}' dan '{cq.dequeue()}'")
    print(cq.get_visualization())
    print()
    
    print("• Enqueue 2 Pelanggan baru: 'Eka', 'Fandi' (Akan memutar balik indeks rear ke Idx 0 & 1!)")
    cq.enqueue("Eka")
    cq.enqueue("Fandi")
    print(cq.get_visualization())
    print()
    
    print(f"• Mencoba enqueue saat penuh (harus gagal)...")
    try:
        cq.enqueue("Gani")
    except IndexError as e:
        print(f"  Respon Sistem: {e}")
    print("=" * 70)
