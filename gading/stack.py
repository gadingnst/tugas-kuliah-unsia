# -*- coding: utf-8 -*-
"""
Modul Struktur Data: Stack (Tumpukan)
Prinsip Kerja: LIFO (Last In First Out) - Terakhir Masuk, Pertama Keluar.
"""

class Stack:
    """
    Representasi Struktur Data Stack (Tumpukan) berbasis Array/List Python.
    Sangat cocok untuk menggambarkan tumpukan piring, browser history (back button),
    atau fitur undo-redo pada editor.
    """
    def __init__(self):
        """Inisialisasi Stack kosong."""
        self.items = []

    def is_empty(self) -> bool:
        """Memeriksa apakah stack kosong. Mengembalikan True jika kosong, False jika ada isi."""
        return len(self.items) == 0

    def push(self, item) -> None:
        """Menambahkan elemen baru di posisi paling atas (top) stack."""
        self.items.append(item)

    def pop(self):
        """
        Menghapus dan mengembalikan elemen teratas (top) stack.
        Mengangkat Exception jika stack kosong.
        """
        if self.is_empty():
            raise IndexError("Error: Pop dari Stack kosong tidak diperbolehkan!")
        return self.items.pop()

    def peek(self):
        """
        Melihat elemen teratas (top) stack tanpa menghapusnya.
        Mengangkat Exception jika stack kosong.
        """
        if self.is_empty():
            raise IndexError("Error: Peek dari Stack kosong tidak diperbolehkan!")
        return self.items[-1]

    def size(self) -> int:
        """Mengembalikan jumlah elemen yang ada di dalam stack."""
        return len(self.items)

    def clear(self) -> None:
        """Mengosongkan seluruh isi stack."""
        self.items = []

    def get_visualization(self) -> str:
        """
        Menghasilkan representasi grafis ASCII Stack vertikal.
        Sangat berguna untuk demonstrasi visual saat presentasi.
        """
        if self.is_empty():
            return (
                "      +---------+\n"
                "      |  KOSONG |\n"
                "      +---------+\n"
                "     [BASE STACK]"
            )
        
        lines = []
        lines.append("     ┌───────────┐  <-- TOP (Elemen Teratas)")
        
        # Iterasi dari indeks terakhir (Top) ke indeks awal (Base)
        for i in range(len(self.items) - 1, -1, -1):
            val = str(self.items[i])
            # Batasi panjang string agar tampilan konsisten (maksimal 9 karakter)
            if len(val) > 9:
                val = val[:6] + "..."
            padded_val = val.center(9)
            
            if i == len(self.items) - 1:
                lines.append(f"     │ {padded_val} │  [{i}]")
            else:
                lines.append(f"     │ {padded_val} │  [{i}]")
                
            if i > 0:
                lines.append("     ├───────────┤")
        
        lines.append("     └───────────┘  <-- BASE (Elemen Terbawah)")
        return "\n".join(lines)


# Demo Penggunaan Stack secara Mandiri (jika file dijalankan langsung)
if __name__ == "__main__":
    print("=" * 50)
    print(" DEMO STRUKTUR DATA: STACK (TUMPUKAN)")
    print("=" * 50)
    
    # Inisialisasi Stack Baru
    tumpukan = Stack()
    print("1. Stack Baru Dibuat.")
    print(tumpukan.get_visualization())
    print()
    
    # Push beberapa elemen
    print("2. Melakukan PUSH: 'Buku A', 'Buku B', 'Buku C'")
    tumpukan.push("Buku A")
    tumpukan.push("Buku B")
    tumpukan.push("Buku C")
    print(tumpukan.get_visualization())
    print(f"Ukuran Stack sekarang: {tumpukan.size()}")
    print()
    
    # Peek (Melihat elemen teratas)
    print(f"3. Melakukan PEEK (Melihat elemen teratas): {tumpukan.peek()}")
    print()
    
    # Pop elemen teratas
    print(f"4. Melakukan POP (Mengambil elemen teratas): '{tumpukan.pop()}'")
    print(tumpukan.get_visualization())
    print(f"Ukuran Stack sekarang: {tumpukan.size()}")
    print()
    
    # Pop sisa elemen
    print(f"5. Melakukan POP lagi: '{tumpukan.pop()}'")
    print(f"6. Melakukan POP lagi: '{tumpukan.pop()}'")
    print(tumpukan.get_visualization())
    print(f"Apakah stack kosong? {tumpukan.is_empty()}")
    print("=" * 50)
