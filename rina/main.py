# -*- coding: utf-8 -*-
"""
Aplikasi Utama Rina: Dashboard Visualisasi Struktur Data Majemuk Linear.
Menggunakan skema warna Magenta-Kuning premium dan terintegrasi penuh.
"""
import os
import sys

# Import modul struktur data Rina
from stack import ArrayStack
from circular_queue import CircularQueue
from doubly_linked_list import DoublyLinkedList
from dynamic_array import DynamicArray

# Kode warna ANSI untuk Rina: Magenta & Kuning/Hijau
MAGENTA = "\033[95m"
BOLD_MAGENTA = "\033[1;95m"
YELLOW = "\033[93m"
BOLD_YELLOW = "\033[1;93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_enter():
    """Menahan layar dan menunggu penekanan Enter."""
    input(f"\n{YELLOW}Tekan [ENTER] untuk melanjutkan...{RESET}")

def print_header(title):
    """Mencetak header menu yang artistik bertema Magenta."""
    clear_screen()
    print(f"{MAGENTA}{BOLD}{'=' * 75}{RESET}")
    print(f"{BOLD_MAGENTA}  {title.center(71)}{RESET}")
    print(f"{MAGENTA}{BOLD}{'=' * 75}{RESET}\n")

def menu_stack():
    stack = ArrayStack()
    stack.push("CD Musik A")
    stack.push("CD Musik B")
    stack.push("CD Musik C")
    
    msg = f"{GREEN}Stack Rina berhasil diinisialisasi dengan data awal!{RESET}"
    
    while True:
        print_header("SIMULASI STACK (TUMPUKAN CD RINA)")
        
        print(f"{BOLD}Visualisasi Tumpukan CD (Rounded Box):{RESET}")
        print(stack.get_visualization())
        print()
        
        if msg:
            print(f"Status: {msg}\n")
            msg = ""
            
        print(f"{BOLD}AKSI OPERASI STACK:{RESET}")
        print(f"[{YELLOW}1{RESET}] Push (Tambahkan data baru di atas)")
        print(f"[{YELLOW}2{RESET}] Pop  (Keluarkan data teratas)")
        print(f"[{YELLOW}3{RESET}] Peek (Intip data teratas)")
        print(f"[{YELLOW}4{RESET}] Clear (Kosongkan Tumpukan)")
        print(f"[{RED}5{RESET}] Kembali ke Menu Utama Rina")
        
        opsi = input(f"\nPilih aksi (1-5): {RESET}").strip()
        
        if opsi == '1':
            item = input(f"{CYAN}Masukkan nama CD baru: {RESET}").strip()
            if item:
                stack.push(item)
                msg = f"{GREEN}CD '{item}' berhasil di-Push ke dalam Stack!{RESET}"
            else:
                msg = f"{RED}Input nama tidak boleh kosong!{RESET}"
        elif opsi == '2':
            try:
                removed = stack.pop()
                msg = f"{GREEN}CD '{removed}' berhasil di-Pop keluar!{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '3':
            try:
                top = stack.peek()
                msg = f"{CYAN}Melihat elemen teratas: '{top}'{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '4':
            stack.clear()
            msg = f"{BOLD_YELLOW}Tumpukan CD berhasil dikosongkan!{RESET}"
        elif opsi == '5':
            break
        else:
            msg = f"{RED}Input salah! Harap masukkan angka 1-5.{RESET}"

def menu_queue():
    # Buat Circular Queue berkapasitas 5
    cq = CircularQueue(capacity=5)
    cq.enqueue("Rina 1")
    cq.enqueue("Rina 2")
    cq.enqueue("Rina 3")
    
    msg = f"{GREEN}Circular Queue Rina siap dengan kapasitas tetap = 5!{RESET}"
    
    while True:
        print_header("SIMULASI CIRCULAR QUEUE (RING BUFFER FIFO)")
        
        print(f"{BOLD}Visualisasi Struktur Sirkular di Memori RAM:{RESET}")
        print(cq.get_visualization())
        print()
        
        if msg:
            print(f"Status: {msg}\n")
            msg = ""
            
        print(f"{BOLD}AKSI OPERASI CIRCULAR QUEUE:{RESET}")
        print(f"[{YELLOW}1{RESET}] Enqueue (Masuk antrean secara sirkular)")
        print(f"[{YELLOW}2{RESET}] Dequeue (Keluar antrean tanpa pergeseran memori)")
        print(f"[{YELLOW}3{RESET}] Get Front / Rear (Intip ujung antrean)")
        print(f"[{YELLOW}4{RESET}] Clear (Kosongkan antrean)")
        print(f"[{RED}5{RESET}] Kembali ke Menu Utama Rina")
        
        opsi = input(f"\nPilih aksi (1-5): {RESET}").strip()
        
        if opsi == '1':
            if cq.is_full():
                msg = f"{RED}Gagal: Antrean sirkular sudah penuh! Silakan dequeue terlebih dahulu.{RESET}"
                continue
            item = input(f"{CYAN}Masukkan data pengantre baru: {RESET}").strip()
            if item:
                cq.enqueue(item)
                msg = f"{GREEN}Pelanggan '{item}' masuk ke antrean!{RESET}"
            else:
                msg = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif opsi == '2':
            try:
                removed = cq.dequeue()
                msg = f"{GREEN}Pelanggan '{removed}' keluar dari antrean (Dequeue)!{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '3':
            if cq.is_empty():
                msg = f"{RED}Queue masih kosong!{RESET}"
            else:
                msg = f"{CYAN}Front: '{cq.get_front()}' | Rear: '{cq.get_rear()}'{RESET}"
        elif opsi == '4':
            cq.clear()
            msg = f"{BOLD_YELLOW}Circular Queue dibersihkan kembali kosong!{RESET}"
        elif opsi == '5':
            break
        else:
            msg = f"{RED}Input salah! Harap masukkan angka 1-5.{RESET}"

def menu_linked_list():
    dll = DoublyLinkedList()
    dll.insert_back("Node A")
    dll.insert_back("Node B")
    dll.insert_back("Node C")
    
    msg = f"{GREEN}Doubly Linked List Rina berhasil dibuat!{RESET}"
    
    while True:
        print_header("SIMULASI DOUBLY LINKED LIST (SENARAI GANDA)")
        
        print(f"{BOLD}Visualisasi Rantai Node Dua Arah (Double Pointers):{RESET}")
        print(f"{CYAN}{dll.get_visualization()}{RESET}")
        print()
        
        if msg:
            print(f"Status: {msg}\n")
            msg = ""
            
        print(f"{BOLD}AKSI OPERASI DOUBLY LINKED LIST:{RESET}")
        print(f"[{YELLOW}1{RESET}] Insert Front  (Sisipkan di Awal / Head)")
        print(f"[{YELLOW}2{RESET}] Insert Back   (Sisipkan di Akhir / Tail)")
        print(f"[{YELLOW}3{RESET}] Delete Node   (Hapus Node berdasarkan nilai)")
        print(f"[{YELLOW}4{RESET}] Search Value  (Cari elemen secara linear)")
        print(f"[{YELLOW}5{RESET}] Clear Rantai  (Reset seluruh Node)")
        print(f"[{RED}6{RESET}] Kembali ke Menu Utama Rina")
        
        opsi = input(f"\nPilih aksi (1-6): {RESET}").strip()
        
        if opsi == '1':
            item = input(f"{CYAN}Masukkan nilai data baru untuk bagian depan: {RESET}").strip()
            if item:
                dll.insert_front(item)
                msg = f"{GREEN}Berhasil menyisipkan '{item}' di Head!{RESET}"
            else:
                msg = f"{RED}Input tidak boleh kosong!{RESET}"
        elif opsi == '2':
            item = input(f"{CYAN}Masukkan nilai data baru untuk bagian belakang: {RESET}").strip()
            if item:
                dll.insert_back(item)
                msg = f"{GREEN}Berhasil menyisipkan '{item}' di Tail!{RESET}"
            else:
                msg = f"{RED}Input tidak boleh kosong!{RESET}"
        elif opsi == '3':
            item = input(f"{CYAN}Masukkan nilai Node yang ingin dihapus: {RESET}").strip()
            if item:
                success = dll.delete_node(item)
                if success:
                    msg = f"{GREEN}Node bernilai '{item}' berhasil dihapus dari rantai!{RESET}"
                else:
                    msg = f"{RED}Gagal: Node bernilai '{item}' tidak ditemukan!{RESET}"
            else:
                msg = f"{RED}Input tidak boleh kosong!{RESET}"
        elif opsi == '4':
            item = input(f"{CYAN}Masukkan nilai yang ingin dicari: {RESET}").strip()
            if item:
                found = dll.search(item)
                if found:
                    msg = f"{GREEN}Ditemukan! Elemen '{item}' ada di dalam Doubly Linked List.{RESET}"
                else:
                    msg = f"{RED}Tidak Ditemukan! Elemen '{item}' tidak terdaftar.{RESET}"
            else:
                msg = f"{RED}Input tidak boleh kosong!{RESET}"
        elif opsi == '5':
            dll.clear()
            msg = f"{BOLD_YELLOW}Seluruh Node Doubly Linked List telah dihapus!{RESET}"
        elif opsi == '6':
            break
        else:
            msg = f"{RED}Input salah! Harap masukkan angka 1-6.{RESET}"

def menu_array_list():
    da = DynamicArray(initial_capacity=4)
    da.add("Data Rina A")
    da.add("Data Rina B")
    da.add("Data Rina C")
    
    msg = f"{GREEN}Dynamic Array Rina siap dengan kapasitas awal 4!{RESET}"
    
    while True:
        print_header("SIMULASI DYNAMIC ARRAY (LARIK DINAMIS RINA)")
        
        print(f"{BOLD}Visualisasi Blok Memori Dinamis (Size vs Capacity):{RESET}")
        print(da.get_visualization())
        print()
        
        if msg:
            print(f"Status: {msg}\n")
            msg = ""
            
        print(f"{BOLD}AKSI OPERASI DYNAMIC ARRAY:{RESET}")
        print(f"[{YELLOW}1{RESET}] Add (Tambahkan data ke posisi paling belakang)")
        print(f"[{YELLOW}2{RESET}] Insert At (Sisipkan data pada indeks tertentu)")
        print(f"[{YELLOW}3{RESET}] Remove At (Hapus data pada indeks tertentu)")
        print(f"[{YELLOW}4{RESET}] Pop (Ambil data paling belakang)")
        print(f"[{YELLOW}5{RESET}] Clear (Reset kapasitas menjadi 4)")
        print(f"[{RED}6{RESET}] Kembali ke Menu Utama Rina")
        
        opsi = input(f"\nPilih aksi (1-6): {RESET}").strip()
        
        if opsi == '1':
            item = input(f"{CYAN}Masukkan nilai data baru: {RESET}").strip()
            if item:
                da.add(item)
                msg = f"{GREEN}Elemen '{item}' sukses ditambahkan ke Array!{RESET}"
            else:
                msg = f"{RED}Input tidak boleh kosong!{RESET}"
        elif opsi == '2':
            item = input(f"{CYAN}Masukkan nilai data baru: {RESET}").strip()
            if not item:
                msg = f"{RED}Input data tidak boleh kosong!{RESET}"
                continue
            idx_str = input(f"{CYAN}Masukkan target indeks (0 - {da.size()}): {RESET}").strip()
            try:
                idx = int(idx_str)
                da.insert_at(idx, item)
                msg = f"{GREEN}Berhasil menyisipkan '{item}' di indeks [{idx}]!{RESET}"
            except ValueError:
                msg = f"{RED}Indeks harus berupa angka bulat!{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '3':
            if da.is_empty():
                msg = f"{RED}Dynamic Array kosong!{RESET}"
                continue
            idx_str = input(f"{CYAN}Masukkan indeks yang ingin dihapus (0 - {da.size() - 1}): {RESET}").strip()
            try:
                idx = int(idx_str)
                removed = da.remove_at(idx)
                msg = f"{GREEN}Berhasil menghapus data '{removed}' dari indeks [{idx}]!{RESET}"
            except ValueError:
                msg = f"{RED}Indeks harus berupa angka bulat!{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '4':
            try:
                removed = da.pop()
                msg = f"{GREEN}Berhasil mengambil data '{removed}' dari ujung belakang!{RESET}"
            except IndexError as e:
                msg = f"{RED}{str(e)}{RESET}"
        elif opsi == '5':
            da.clear()
            msg = f"{BOLD_YELLOW}Array berhasil dikosongkan ke kapasitas dasar (4)!{RESET}"
        elif opsi == '6':
            break
        else:
            msg = f"{RED}Input salah! Harap masukkan angka 1-6.{RESET}"

def main():
    while True:
        clear_screen()
        print(f"{MAGENTA}{BOLD}{'=' * 75}{RESET}")
        print(f"{BOLD_MAGENTA}      PROGRAM INTERAKTIF SIMULASI VISUAL STRUKTUR DATA LINEAR - RINA      {RESET}")
        print(f"{MAGENTA}{BOLD}{'=' * 75}{RESET}")
        print(f"  Materi: Stack | Circular Queue | Doubly Linked List | Dynamic Array  ")
        print(f"  Disusun Oleh: Rina                                                   ")
        print(f"{MAGENTA}{'=' * 75}{RESET}\n")
        
        print(f"{BOLD_YELLOW}DAFTAR TOPIK STRUKTUR DATA RINA:{RESET}")
        print(f"[{YELLOW}1{RESET}] {BOLD}Stack (Tumpukan LIFO - Kotak Melengkung){RESET}")
        print(f"      - Representasi visual tumpukan CD musik.")
        print()
        print(f"[{YELLOW}2{RESET}] {BOLD}Circular Queue (Antrean Sirkular FIFO - Ring Buffer){RESET}")
        print(f"      - Demonstrasi rotasi indeks sirkular modulo di RAM fisik.")
        print()
        print(f"[{YELLOW}3{RESET}] {BOLD}Doubly Linked List (Senarai Ganda Dua Arah){RESET}")
        print(f"      - Demonstrasi rantai node ganda dengan prev & next pointer.")
        print()
        print(f"[{YELLOW}4{RESET}] {BOLD}Dynamic Array (Larik Dinamis Pra-alokasi){RESET}")
        print(f"      - Demonstrasi real-time resizing & shifting memori cadangan.")
        print()
        print(f"[{RED}5{RESET}] {BOLD}Keluar dari Program Rina{RESET}")
        print(f"{MAGENTA}{'=' * 75}{RESET}")
        
        pilihan = input(f"\nPilih Menu (1-5): {RESET}").strip()
        
        if pilihan == '1':
            menu_stack()
        elif pilihan == '2':
            menu_queue()
        elif pilihan == '3':
            menu_linked_list()
        elif pilihan == '4':
            menu_array_list()
        elif pilihan == '5':
            clear_screen()
            print(f"\n{GREEN}{BOLD}Terima kasih telah menggunakan program simulasi Rina!{RESET}")
            print(f"{BOLD_YELLOW}Sukses besar untuk ujian presentasi tugas struktur data Anda!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}Menu tidak valid! SIlakan pilih angka 1-5.{RESET}")
            wait_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{BOLD_YELLOW}Aplikasi dihentikan paksa. Sampai jumpa!{RESET}\n")
        sys.exit(0)
