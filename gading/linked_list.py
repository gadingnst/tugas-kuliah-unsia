# -*- coding: utf-8 -*-
"""
Modul Struktur Data: Linked List (Senarai Berantai)
Karakteristik: Elemen-elemen disimpan dalam objek 'Node' yang terhubung
oleh pointer (penunjuk) alamat memori berikutnya. Tidak berurutan secara fisik di memori.
"""

class Node:
    """
    Representasi sebuah Node (simpul) dalam Linked List.
    Tiap Node menyimpan data dan pointer ke Node berikutnya.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Menunjuk ke None secara default


class LinkedList:
    """
    Representasi dari Linked List Sederhana.
    Menyediakan operasi dasar: penyisipan awal/akhir, penghapusan, pencarian, dan visualisasi.
    """
    def __init__(self):
        """Inisialisasi Linked List kosong dengan Head menunjuk ke None."""
        self.head = None

    def is_empty(self) -> bool:
        """Memeriksa apakah Linked List kosong."""
        return self.head is None

    def insert_at_beginning(self, data) -> None:
        """Menyisipkan Node baru di awal Linked List (Head baru)."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data) -> None:
        """Menyisipkan Node baru di akhir Linked List."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value) -> bool:
        """
        Menghapus Node pertama yang bernilai cocok dengan 'value'.
        Mengembalikan True jika berhasil dihapus, False jika tidak ditemukan.
        """
        if self.is_empty():
            return False

        # Kasus khusus jika Node yang akan dihapus berada di Head
        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.data == value:
                # Bypass Node yang akan dihapus
                current.next = current.next.next
                return True
            current = current.next
        
        return False  # Elemen tidak ditemukan

    def search(self, value) -> bool:
        """Mencari apakah ada Node dengan nilai tertentu. Mengembalikan True/False."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """Menghitung jumlah total Node dalam Linked List."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self) -> None:
        """Mengosongkan Linked List."""
        self.head = None

    def get_visualization(self) -> str:
        """
        Menghasilkan representasi ASCII visual rantai pointer yang sangat intuitif.
        Menunjukkan dengan jelas bagaimana pointer dari satu Node menunjuk ke Node berikutnya.
        """
        if self.is_empty():
            return "Head ──► NULL (Kosong)"

        parts = []
        current = self.head
        parts.append("Head")
        
        while current:
            val = str(current.data)
            # Batasi panjang string
            if len(val) > 8:
                val = val[:5] + "..."
            padded_val = val.center(8)
            
            # Format visual satu Node: [ Data | Next ]
            node_str = f"[ {padded_val} | • ]"
            parts.append(node_str)
            current = current.next
            
        parts.append("NULL")
        
        # Gabungkan dengan panah pointer
        return " ──► ".join(parts)


# Demo Penggunaan Linked List secara Mandiri
if __name__ == "__main__":
    print("=" * 80)
    print(" DEMO STRUKTUR DATA: LINKED LIST (SENARAI BERANTAI)")
    print("=" * 80)
    
    # Inisialisasi
    ll = LinkedList()
    print("1. Linked List Baru Dibuat.")
    print(ll.get_visualization())
    print()
    
    # Menyisipkan di akhir
    print("2. Menyisipkan di AKHIR (Insert End): 'Node A', 'Node B'")
    ll.insert_at_end("Node A")
    ll.insert_at_end("Node B")
    print(ll.get_visualization())
    print()
    
    # Menyisipkan di awal
    print("3. Menyisipkan di AWAL (Insert Beginning): 'Node C'")
    ll.insert_at_beginning("Node C")
    print(ll.get_visualization())
    print()
    
    # Menyisipkan di akhir lagi
    print("4. Menyisipkan di AKHIR lagi (Insert End): 'Node D'")
    ll.insert_at_end("Node D")
    print(ll.get_visualization())
    print(f"Total ukuran Linked List: {ll.size()} Node")
    print()
    
    # Pencarian
    search_val = "Node B"
    print(f"5. Melakukan pencarian nilai '{search_val}': Found? {ll.search(search_val)}")
    print()
    
    # Penghapusan elemen
    del_val = "Node B"
    print(f"7. Menghapus Node bernilai '{del_val}': Success? {ll.delete_value(del_val)}")
    print(ll.get_visualization())
    print("=" * 80)
