# -*- coding: utf-8 -*-
"""
Dashboard Interaktif Utama: Simulasi Visualisasi Struktur Data Linked List.
"""
import os
import sys

# Import modul struktur data kustom
from linked_list import LinkedList

# Kode warna ANSI untuk visualisasi premium di terminal Mac/Linux
BOLD = "\033[1m"
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
        print(f"[{RED}6{RESET}] Keluar dari Aplikasi")

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
            clear_screen()
            print(f"\n{GREEN}{BOLD}Terima kasih telah menggunakan aplikasi simulasi ini!{RESET}\n")
            sys.exit(0)
        else:
            message = f"{RED}Pilihan tidak valid! Silakan masukkan angka 1-6.{RESET}"

if __name__ == "__main__":
    try:
        menu_linked_list()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Aplikasi dihentikan oleh pengguna. Sampai jumpa!{RESET}\n")
        sys.exit(0)
