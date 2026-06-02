# -*- coding: utf-8 -*-
"""
Dashboard Interaktif Utama: Simulasi Visualisasi Struktur Data Majemuk Linear.
Mengintegrasikan Stack, Queue, Linked List, dan Array List dalam satu aplikasi CLI premium.
"""
import os
import sys
import time

# Import modul struktur data kustom
from stack import Stack
from queue_custom import Queue
from linked_list import LinkedList
from array_list import ArrayList

# Kode warna ANSI untuk visualisasi premium di terminal Mac/Linux
CLEAR = "\033[H\033[J"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_enter():
    """Menahan layar dan menunggu pengguna menekan Enter."""
    input(f"\n{YELLOW}Tekan [ENTER] untuk melanjutkan...{RESET}")

def print_header(title):
    """Mencetak header menu yang estetis."""
    clear_screen()
    print(f"{BLUE}{BOLD}{'=' * 70}{RESET}")
    print(f"{CYAN}{BOLD}  {title.center(66)}{RESET}")
    print(f"{BLUE}{BOLD}{'=' * 70}{RESET}\n")

def menu_stack():
    stack = Stack()
    # Isi data awal agar tidak kosong saat dibuka
    stack.push("Piring 1")
    stack.push("Piring 2")
    stack.push("Piring 3")
    
    message = f"{GREEN}Stack berhasil diinisialisasi dengan data awal!{RESET}"
    
    while True:
        print_header("DEMO STRUKTUR DATA: STACK (TUMPUKAN)")
        
        # Tampilkan Visualisasi Stack
        print(f"{BOLD}Visualisasi Stack saat ini:{RESET}")
        print(stack.get_visualization())
        print()
        
        if message:
            print(f"Status: {message}\n")
            message = ""
            
        print(f"{BOLD}PILIHAN OPERASI:{RESET}")
        print(f"[{CYAN}1{RESET}] Push (Tambahkan Elemen Teratas)")
        print(f"[{CYAN}2{RESET}] Pop  (Keluarkan Elemen Teratas)")
        print(f"[{CYAN}3{RESET}] Peek (Lihat Elemen Teratas)")
        print(f"[{CYAN}4{RESET}] Clear (Kosongkan Tumpukan)")
        print(f"[{RED}5{RESET}] Kembali ke Menu Utama")
        
        pilihan = input(f"\n{BOLD}Pilih operasi (1-5): {RESET}").strip()
        
        if pilihan == '1':
            item = input(f"{YELLOW}Masukkan nilai data baru: {RESET}").strip()
            if item:
                stack.push(item)
                message = f"{GREEN}Berhasil push '{item}' ke dalam Stack!{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '2':
            try:
                removed = stack.pop()
                message = f"{GREEN}Berhasil pop '{removed}' dari Stack!{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '3':
            try:
                top_val = stack.peek()
                message = f"{YELLOW}Elemen teratas (TOP) saat ini adalah: '{top_val}'{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '4':
            stack.clear()
            message = f"{YELLOW}Stack berhasil dikosongkan!{RESET}"
        elif pilihan == '5':
            break
        else:
            message = f"{RED}Pilihan tidak valid! Silakan masukkan angka 1-5.{RESET}"

def menu_queue():
    queue = Queue()
    # Isi data awal
    queue.enqueue("Kasir A")
    queue.enqueue("Kasir B")
    queue.enqueue("Kasir C")
    
    message = f"{GREEN}Queue berhasil diinisialisasi dengan data awal!{RESET}"
    
    while True:
        print_header("DEMO STRUKTUR DATA: QUEUE (ANTREAN)")
        
        # Tampilkan Visualisasi Queue
        print(f"{BOLD}Visualisasi Queue saat ini:{RESET}")
        print(queue.get_visualization())
        print()
        
        if message:
            print(f"Status: {message}\n")
            message = ""
            
        print(f"{BOLD}PILIHAN OPERASI:{RESET}")
        print(f"[{CYAN}1{RESET}] Enqueue (Masuk Antrean di Belakang)")
        print(f"[{CYAN}2{RESET}] Dequeue (Keluar Antrean di Depan)")
        print(f"[{CYAN}3{RESET}] Front   (Lihat Elemen Terdepan)")
        print(f"[{CYAN}4{RESET}] Clear   (Kosongkan Antrean)")
        print(f"[{RED}5{RESET}] Kembali ke Menu Utama")
        
        pilihan = input(f"\n{BOLD}Pilih operasi (1-5): {RESET}").strip()
        
        if pilihan == '1':
            item = input(f"{YELLOW}Masukkan nama/nilai data baru: {RESET}").strip()
            if item:
                queue.enqueue(item)
                message = f"{GREEN}Berhasil enqueue '{item}' ke antrean!{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '2':
            try:
                removed = queue.dequeue()
                message = f"{GREEN}Berhasil dequeue '{removed}' dari antrean!{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '3':
            try:
                front_val = queue.front()
                message = f"{YELLOW}Elemen terdepan (FRONT) saat ini: '{front_val}'{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '4':
            queue.clear()
            message = f"{YELLOW}Queue berhasil dikosongkan!{RESET}"
        elif pilihan == '5':
            break
        else:
            message = f"{RED}Pilihan tidak valid! Silakan masukkan angka 1-5.{RESET}"

def menu_linked_list():
    ll = LinkedList()
    # Isi data awal
    ll.insert_at_end("Node 1")
    ll.insert_at_end("Node 2")
    ll.insert_at_end("Node 3")
    
    message = f"{GREEN}Linked List berhasil diinisialisasi!{RESET}"
    
    while True:
        print_header("DEMO STRUKTUR DATA: LINKED LIST (SENARAI BERANTAI)")
        
        # Tampilkan Visualisasi Linked List
        print(f"{BOLD}Visualisasi Rantai Node (Pointer Chain) saat ini:{RESET}")
        print(f"{CYAN}{ll.get_visualization()}{RESET}")
        print()
        
        if message:
            print(f"Status: {message}\n")
            message = ""
            
        print(f"{BOLD}PILIHAN OPERASI:{RESET}")
        print(f"[{CYAN}1{RESET}] Insert Beginning (Sisipkan di Awal / Head)")
        print(f"[{CYAN}2{RESET}] Insert End       (Sisipkan di Akhir)")
        print(f"[{CYAN}3{RESET}] Delete Value      (Hapus Node Berdasarkan Nilai)")
        print(f"[{CYAN}4{RESET}] Search            (Cari Keberadaan Nilai)")
        print(f"[{CYAN}5{RESET}] Clear             (Kosongkan Rantai)")
        print(f"[{RED}6{RESET}] Kembali ke Menu Utama")
        
        pilihan = input(f"\n{BOLD}Pilih operasi (1-6): {RESET}").strip()
        
        if pilihan == '1':
            item = input(f"{YELLOW}Masukkan nilai data untuk disisipkan di AWAL: {RESET}").strip()
            if item:
                ll.insert_at_beginning(item)
                message = f"{GREEN}Berhasil menyisipkan '{item}' di awal Linked List!{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '2':
            item = input(f"{YELLOW}Masukkan nilai data untuk disisipkan di AKHIR: {RESET}").strip()
            if item:
                ll.insert_at_end(item)
                message = f"{GREEN}Berhasil menyisipkan '{item}' di akhir Linked List!{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '3':
            item = input(f"{YELLOW}Masukkan nilai data yang ingin dihapus: {RESET}").strip()
            if item:
                success = ll.delete_value(item)
                if success:
                    message = f"{GREEN}Berhasil menghapus Node bernilai '{item}'!{RESET}"
                else:
                    message = f"{RED}Node bernilai '{item}' tidak ditemukan!{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '4':
            item = input(f"{YELLOW}Masukkan nilai data yang dicari: {RESET}").strip()
            if item:
                found = ll.search(item)
                if found:
                    message = f"{GREEN}Ditemukan! Node bernilai '{item}' ada dalam rantai.{RESET}"
                else:
                    message = f"{RED}Tidak Ditemukan! Node bernilai '{item}' tidak ada dalam rantai.{RESET}"
            else:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
        elif pilihan == '5':
            ll.clear()
            message = f"{YELLOW}Linked List berhasil dikosongkan!{RESET}"
        elif pilihan == '6':
            break
        else:
            message = f"{RED}Pilihan tidak valid! Silakan masukkan angka 1-6.{RESET}"

def menu_array_list():
    # Buat array list dengan kapasitas 4
    arr = ArrayList(initial_capacity=4)
    # Isi data awal
    arr.append("Data 1")
    arr.append("Data 2")
    arr.append("Data 3")
    
    message = f"{GREEN}Dynamic Array List berhasil diinisialisasi (Cap = 4)!{RESET}"
    
    while True:
        print_header("DEMO STRUKTUR DATA: DYNAMIC ARRAY LIST (LARIK DINAMIS)")
        
        # Tampilkan Visualisasi Array List
        print(f"{BOLD}Visualisasi Blok Memori Kontigu saat ini:{RESET}")
        print(arr.get_visualization())
        print()
        
        if message:
            print(f"Status: {message}\n")
            message = ""
            
        print(f"{BOLD}PILIHAN OPERASI:{RESET}")
        print(f"[{CYAN}1{RESET}] Append (Tambahkan ke Akhir)")
        print(f"[{CYAN}2{RESET}] Insert (Sisipkan pada Indeks Tertentu)")
        print(f"[{CYAN}3{RESET}] Delete Index (Hapus pada Indeks Tertentu)")
        print(f"[{CYAN}4{RESET}] Pop (Hapus & Ambil Elemen Terakhir)")
        print(f"[{CYAN}5{RESET}] Clear (Reset Array)")
        print(f"[{RED}6{RESET}] Kembali ke Menu Utama")
        
        pilihan = input(f"\n{BOLD}Pilih operasi (1-6): {RESET}").strip()
        
        if pilihan == '1':
            item = input(f"{YELLOW}Masukkan nilai data baru: {RESET}").strip()
            if item:
                # Capture output print dari resize (jika terjadi resize)
                arr.append(item)
                message = f"{GREEN}Berhasil menambahkan '{item}' ke Array List!{RESET}"
            else:
                message = f"{RED}Input tidak boleh kosong!{RESET}"
        elif pilihan == '2':
            item = input(f"{YELLOW}Masukkan nilai data baru: {RESET}").strip()
            if not item:
                message = f"{RED}Input data tidak boleh kosong!{RESET}"
                continue
            idx_str = input(f"{YELLOW}Masukkan indeks penyisipan (0 - {arr.size()}): {RESET}").strip()
            try:
                idx = int(idx_str)
                arr.insert(idx, item)
                message = f"{GREEN}Berhasil menyisipkan '{item}' pada indeks {idx}!{RESET}"
            except ValueError:
                message = f"{RED}Indeks harus berupa angka bulat!{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '3':
            if arr.is_empty():
                message = f"{RED}Array List kosong! Tidak ada elemen yang bisa dihapus.{RESET}"
                continue
            idx_str = input(f"{YELLOW}Masukkan indeks yang ingin dihapus (0 - {arr.size() - 1}): {RESET}").strip()
            try:
                idx = int(idx_str)
                removed = arr.delete_at(idx)
                message = f"{GREEN}Berhasil menghapus elemen '{removed}' pada indeks {idx}!{RESET}"
            except ValueError:
                message = f"{RED}Indeks harus berupa angka bulat!{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '4':
            try:
                removed = arr.pop()
                message = f"{GREEN}Berhasil pop '{removed}' dari akhir Array List!{RESET}"
            except IndexError as e:
                message = f"{RED}{str(e)}{RESET}"
        elif pilihan == '5':
            arr.clear()
            message = f"{YELLOW}Array List direset kembali ke kapasitas awal (4)!{RESET}"
        elif pilihan == '6':
            break
        else:
            message = f"{RED}Pilihan tidak valid! Silakan masukkan angka 1-6.{RESET}"

def main():
    while True:
        clear_screen()
        print(f"{BLUE}{BOLD}{'=' * 70}{RESET}")
        print(f"{CYAN}{BOLD}      Aplikasi Simulasi Visualisasi Struktur Data Majemuk Linear    {RESET}")
        print(f"{BLUE}{BOLD}{'=' * 70}{RESET}")
        print(f"  Topik: Stack | Queue | Linked List | Array List  ")
        print(f"  Pembuat: Gading Nst                                             ")
        print(f"{BLUE}{'=' * 70}{RESET}\n")
        
        print(f"{BOLD}PILIH TOPIK STRUKTUR DATA:{RESET}")
        print(f"[{CYAN}1{RESET}] {BOLD}Stack (Tumpukan - Prinsip LIFO){RESET}")
        print(f"      - Karakteristik: Operasi Push & Pop hanya pada satu ujung (TOP)")
        print(f"      - Contoh: Back History Browser, Undo-Redo Editor")
        print()
        print(f"[{CYAN}2{RESET}] {BOLD}Queue (Antrean - Prinsip FIFO){RESET}")
        print(f"      - Karakteristik: Masuk dari REAR (belakang), keluar dari FRONT (depan)")
        print(f"      - Contoh: Antrean print dokumen, buffer jaringan")
        print()
        print(f"[{CYAN}3{RESET}] {BOLD}Linked List (Senarai Berantai){RESET}")
        print(f"      - Karakteristik: Rantai dinamis dengan node [Data | Next Pointer]")
        print(f"      - Contoh: Manajemen playlist musik, alokasi memori berantai")
        print()
        print(f"[{CYAN}4{RESET}] {BOLD}Array List (Dynamic Array){RESET}")
        print(f"      - Karakteristik: Lokasi memori fisik berurutan dengan resizing otomatis")
        print(f"      - Contoh: Array/List dinamis bawaan bahasa pemrograman")
        print()
        print(f"[{RED}5{RESET}] {BOLD}Keluar dari Aplikasi{RESET}")
        print(f"{BLUE}{'=' * 70}{RESET}")
        
        pilihan = input(f"\n{BOLD}Masukkan Pilihan Topik (1-5): {RESET}").strip()
        
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
            print(f"\n{GREEN}{BOLD}Terima kasih telah menggunakan aplikasi simulasi ini!{RESET}")
            print(f"{YELLOW}Semoga sukses dengan presentasi Anda tentang Struktur Data Majemuk Linear!{RESET}\n")
            sys.exit(0)
        else:
            print(f"\n{RED}Pilihan tidak valid! Silakan masukkan angka 1-5.{RESET}")
            wait_enter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Aplikasi dihentikan oleh pengguna. Sampai jumpa!{RESET}\n")
        sys.exit(0)
