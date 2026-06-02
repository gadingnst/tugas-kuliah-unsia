# -*- coding: utf-8 -*-
"""
Modul Struktur Data: Queue (Antrean)
Prinsip Kerja: FIFO (First In First Out) - Pertama Masuk, Pertama Keluar.
"""

class Queue:
    """
    Representasi Struktur Data Queue (Antrean) berbasis List Python.
    Sangat cocok untuk menggambarkan antrean kasir, proses cetak printer,
    atau mekanisme buffering / pengiriman data pada jaringan komputer.
    """
    def __init__(self):
        """Inisialisasi Queue kosong."""
        self.items = []

    def is_empty(self) -> bool:
        """Memeriksa apakah queue kosong."""
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        """Menambahkan elemen baru ke bagian belakang (rear) antrean."""
        self.items.append(item)

    def dequeue(self):
        """
        Menghapus dan mengembalikan elemen dari bagian depan (front) antrean.
        Mengangkat Exception jika queue kosong.
        """
        if self.is_empty():
            raise IndexError("Error: Dequeue dari Queue kosong tidak diperbolehkan!")
        return self.items.pop(0)

    def front(self):
        """
        Melihat elemen terdepan (front) antrean tanpa menghapusnya.
        Mengangkat Exception jika queue kosong.
        """
        if self.is_empty():
            raise IndexError("Error: Mengakses Front dari Queue kosong tidak diperbolehkan!")
        return self.items[0]

    def size(self) -> int:
        """Mengembalikan jumlah elemen dalam antrean."""
        return len(self.items)

    def clear(self) -> None:
        """Mengosongkan seluruh antrean."""
        self.items = []

    def get_visualization(self) -> str:
        """
        Menghasilkan representasi grafis ASCII Queue horizontal.
        Sangat efektif untuk memvisualisasikan elemen yang mengalir dari belakang ke depan.
        """
        if self.is_empty():
            return (
                "      [ KELUAR / EXIT ]                                  [ MASUK / ENTER ]\n"
                "            ▲                                                  ▲\n"
                "            │      +──────────────────────────────────────+    │\n"
                "      (FRONT Pointer)  |               KOSONG             |  (REAR Pointer)\n"
                "                   +──────────────────────────────────────+"
            )
        
        # Format masing-masing elemen dengan lebar yang seragam
        formatted_nodes = []
        for i, item in enumerate(self.items):
            val = str(item)
            if len(val) > 8:
                val = val[:5] + "..."
            padded_val = val.center(8)
            
            # Beri keterangan indeks dan data
            formatted_nodes.append(f"[ {padded_val} ]\n  indeks {i} ")
            
        # Pisahkan baris untuk merender baris elemen dan baris indeks
        lines = [n.split('\n') for n in formatted_nodes]
        element_row = " <=== ".join([l[0] for l in lines])
        index_row = "      ".join([l[1] for l in lines])
        
        vis_str = (
            f" [ KELUAR / FRONT ]                                                  [ MASUK / REAR ]\n"
            f"        ▲                                                                    ▲\n"
            f"        │      {element_row}\n"
            f"               {index_row}"
        )
        return vis_str


# Demo Penggunaan Queue secara Mandiri (jika file dijalankan langsung)
if __name__ == "__main__":
    print("=" * 70)
    print(" DEMO STRUKTUR DATA: QUEUE (ANTREAN)")
    print("=" * 70)
    
    # Inisialisasi Queue Baru
    antrean = Queue()
    print("1. Queue Baru Dibuat.")
    print(antrean.get_visualization())
    print()
    
    # Enqueue beberapa elemen
    print("2. Melakukan ENQUEUE (Masuk Antrean): 'Pelanggan 1', 'Pelanggan 2', 'Pelanggan 3'")
    antrean.enqueue("Pelanggan 1")
    antrean.enqueue("Pelanggan 2")
    antrean.enqueue("Pelanggan 3")
    print(antrean.get_visualization())
    print(f"Ukuran antrean: {antrean.size()}")
    print()
    
    # Front (Melihat elemen depan)
    print(f"3. Melakukan FRONT (Melihat elemen terdepan): '{antrean.front()}'")
    print()
    
    # Dequeue elemen depan
    print(f"4. Melakukan DEQUEUE (Keluar dari Antrean): '{antrean.dequeue()}'")
    print(antrean.get_visualization())
    print(f"Ukuran antrean sekarang: {antrean.size()}")
    print()
    
    # Enqueue elemen baru
    print("5. Melakukan ENQUEUE lagi: 'Pelanggan 4'")
    antrean.enqueue("Pelanggan 4")
    print(antrean.get_visualization())
    print()
    
    # Dequeue hingga habis
    print(f"6. Melakukan DEQUEUE: '{antrean.dequeue()}'")
    print(f"7. Melakukan DEQUEUE: '{antrean.dequeue()}'")
    print(f"8. Melakukan DEQUEUE: '{antrean.dequeue()}'")
    print(antrean.get_visualization())
    print(f"Apakah antrean kosong? {antrean.is_empty()}")
    print("=" * 70)
