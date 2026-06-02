# -*- coding: utf-8 -*-
"""
Modul Struktur Data (Rina): Tumpukan (Stack)
Metodologi: Last In First Out (LIFO)
"""

class ArrayStack:
    """
    Implementasi Tumpukan (Stack) berbasis Larik Dinamis bawaan Python.
    Dirancang secara khusus dengan visualisasi kotak melengkung Unicode
    untuk materi presentasi mandiri Rina.
    """
    def __init__(self):
        """Membangun objek Stack baru."""
        self._data = []

    def is_empty(self) -> bool:
        """Memeriksa apakah tumpukan tidak berisi elemen."""
        return len(self._data) == 0

    def push(self, element) -> None:
        """Memasukkan elemen baru ke bagian paling atas tumpukan."""
        self._data.append(element)

    def pop(self):
        """
        Mengeluarkan dan mengembalikan elemen dari puncak tumpukan.
        Memunculkan IndexError jika tumpukan dalam keadaan kosong.
        """
        if self.is_empty():
            raise IndexError("Gagal: Tidak dapat melakukan POP pada Stack yang kosong!")
        return self._data.pop()

    def peek(self):
        """
        Mengintip elemen teratas tumpukan tanpa menghapusnya.
        Memunculkan IndexError jika tumpukan dalam keadaan kosong.
        """
        if self.is_empty():
            raise IndexError("Gagal: Tidak dapat melakukan PEEK pada Stack yang kosong!")
        return self._data[-1]

    def size(self) -> int:
        """Mendapatkan jumlah elemen aktif di dalam tumpukan."""
        return len(self._data)

    def clear(self) -> None:
        """Mereset tumpukan menjadi kosong."""
        self._data = []

    def get_visualization(self) -> str:
        """
        Menghasilkan representasi ASCII bertema kotak melengkung Unicode (Rounded Box).
        Memiliki style visual yang berbeda dengan tugas milik Gading.
        """
        if self.is_empty():
            return (
                "      ╭─────────╮\n"
                "      │  EMPTY  │\n"
                "      ╰─────────╯\n"
                "     [Batas Bawah]"
            )
        
        output_lines = []
        output_lines.append("     ╭───────────╮  ◄── [ TOP OF STACK ]")
        
        # Iterasi terbalik dari elemen teratas ke terbawah
        for index in range(len(self._data) - 1, -1, -1):
            val_str = str(self._data[index])
            # Potong jika terlalu panjang
            if len(val_str) > 9:
                val_str = val_str[:6] + "..."
            padded_val = val_str.center(9)
            
            output_lines.append(f"     │ {padded_val} │  Indeks-{index}")
            
            if index > 0:
                output_lines.append("     ├───────────┤")
                
        output_lines.append("     ╰───────────╯  ◄── [ BASE OF STACK ]")
        return "\n".join(output_lines)


# Pengujian Mandiri
if __name__ == "__main__":
    print("=" * 60)
    print(" PROGRAM DEMO STACK (TUMPUKAN RINA)")
    print("=" * 60)
    
    tumpukan_rina = ArrayStack()
    print("• Membuat Tumpukan baru...")
    print(tumpukan_rina.get_visualization())
    print()
    
    print("• Memasukkan data: 'Buku Rina A', 'Buku Rina B', 'Buku Rina C'")
    tumpukan_rina.push("Buku Rina A")
    tumpukan_rina.push("Buku Rina B")
    tumpukan_rina.push("Buku Rina C")
    print(tumpukan_rina.get_visualization())
    print()
    
    print(f"• Mengintip puncak tumpukan: '{tumpukan_rina.peek()}'")
    print()
    
    print(f"• Mengambil elemen teratas (POP): '{tumpukan_rina.pop()}'")
    print(tumpukan_rina.get_visualization())
    print()
    
    print("• Mengosongkan tumpukan...")
    tumpukan_rina.clear()
    print(tumpukan_rina.get_visualization())
    print("=" * 60)
