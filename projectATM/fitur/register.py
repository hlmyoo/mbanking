import csv
import os
import random

def clear_screen():
    # Bersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Path ke file database
database_file = os.path.join("database", "data_user.csv")

# Fungsi untuk membuat nomor rekening unik
def generate_rekening():
    return str(random.randint(1000000000, 9999999999))

# Fungsi untuk registrasi pengguna baru
def register():
    clear_screen()
    print("\n--- Form Registrasi ---")
    nama = input("Masukkan nama: ")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")
    pin = input("Masukkan PIN (4 digit): ")
    no_telfon = input("Masukkan nomor telepon: ")

    # Pilih bank
    print("\nPilih bank:")
    print("1. BCA\n2. BRI\n3. BTN")
    bank_pilihan = input("Masukkan pilihan bank [1/2/3]: ")
    while bank_pilihan not in ["1", "2", "3"]:
        print("Pilihan tidak valid. Silakan pilih lagi.")
        bank_pilihan = input("Masukkan pilihan bank [1/2/3]: ")

    bank_dict = {"1": "BCA", "2": "BRI", "3": "BTN"}
    bank = bank_dict[bank_pilihan]

    # Generate nomor rekening
    rekening = generate_rekening()

    # Simpan data ke file CSV
    with open(database_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, email, password, pin, no_telfon, bank, rekening, 0])  # Saldo awal 0

    print(f"Registrasi berhasil! Bank: {bank}, No. Rekening: {rekening}")
    print("Silakan login.\n")
