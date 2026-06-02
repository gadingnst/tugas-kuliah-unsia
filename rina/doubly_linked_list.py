# -*- coding: utf-8 -*-
"""
Modul Struktur Data (Rina): Senarai Berantai Ganda (Doubly Linked List)
Karakteristik: Elemen (Node) menyimpan dua pointer (next & prev),
memungkinkan traversal maju dan mundur dengan tingkat fleksibilitas tinggi.
"""

class DoubleNode:
    """
    Representasi Simpul Ganda (Node) dalam Doubly Linked List.
    Menyimpan data, penunjuk ke Node berikutnya (next), dan penunjuk ke Node sebelumnya (prev).
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Implementasi Doubly Linked List dengan penunjuk Head dan Tail.
    Menyediakan operasi dua arah yang lengkap dan efisien.
    """
    def __init__(self):
        """Inisialisasi Linked List kosong."""
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Memeriksa apakah Linked List kosong."""
        return self.head is None

    def insert_front(self, data) -> None:
        """Menyisipkan Node baru di posisi paling depan (Head)."""
        new_node = DoubleNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_back(self, data) -> None:
        """Menyisipkan Node baru di posisi paling belakang (Tail)."""
        new_node = DoubleNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, value) -> bool:
        """
        Menghapus Node pertama yang bernilai 'value'.
        Memutus dan memperbarui kedua pointer tetangganya (prev & next).
        """
        if self.is_empty():
            return False

        current = self.head
        while current:
            if current.data == value:
                # Kasus 1: Elemen tunggal dalam list
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                # Kasus 2: Menghapus Head
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                # Kasus 3: Menghapus Tail
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                # Kasus 4: Menghapus Node di tengah
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True
            current = current.next
            
        return False  # Tidak ditemukan

    def search(self, value) -> bool:
        """Mencari elemen dalam list dari arah depan."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """Menghitung total Node dalam list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self) -> None:
        """Mengosongkan Linked List."""
        self.head = None
        self.tail = None

    def get_visualization(self) -> str:
        """
        Menghasilkan diagram visual penunjuk rantai dua arah.
        Menggunakan simbol panah bolak-balik ◄──► untuk merepresentasikan prev dan next pointer.
        """
        if self.is_empty():
            return "NULL ◄──► Head (Kosong) ◄──► NULL"

        parts = []
        parts.append("NULL")
        
        current = self.head
        while current:
            val_str = str(current.data)
            if len(val_str) > 7:
                val_str = val_str[:4] + "..."
            padded_val = val_str.center(7)
            
            # Format Node Ganda: [ Prev | Data | Next ]
            parts.append(f"[ • | {padded_val} | • ]")
            current = current.next
            
        parts.append("NULL")
        
        # Gabungkan dengan panah dua arah yang cantik
        return " ◄──► ".join(parts)


# Pengujian Mandiri
if __name__ == "__main__":
    print("=" * 80)
    print(" PROGRAM DEMO DOUBLY LINKED LIST (SENARAI GANDA RINA)")
    print("=" * 80)
    
    dll = DoublyLinkedList()
    print("• Membuat Doubly Linked List baru...")
    print(dll.get_visualization())
    print()
    
    print("• Menyisipkan di depan: 'Rina A'")
    dll.insert_front("Rina A")
    print(dll.get_visualization())
    print()
    
    print("• Menyisipkan di belakang: 'Rina B', 'Rina C'")
    dll.insert_back("Rina B")
    dll.insert_back("Rina C")
    print(dll.get_visualization())
    print()
    
    print("• Menyisipkan di depan lagi: 'Rina Premium'")
    dll.insert_front("Rina Premium")
    print(dll.get_visualization())
    print(f"Ukuran linked list: {dll.size()} Node")
    print()
    
    print("• Menghapus Node tengah 'Rina B'...")
    dll.delete_node("Rina B")
    print(dll.get_visualization())
    print()
    
    print("• Menghapus Head 'Rina Premium'...")
    dll.delete_node("Rina Premium")
    print(dll.get_visualization())
    print("=" * 80)
