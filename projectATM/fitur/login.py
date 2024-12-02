import csv
import os

def clear_screen():
    # Bersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Path ke file database
database_file = os.path.join("database", "data_user.csv")

# Fungsi untuk login pengguna
def login():
    clear_screen()
    print("\n--- Form Login ---")
    email = input("Masukkan email: ")
    password = input("Masukkan password: ")

    with open(database_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["email"] == email and row["password"] == password:
                print("Login berhasil!\n")
                print(f"Selamat datang di {row['bank']}! Nomor rekening Anda adalah {row['rekening']}")
                return row  # Mengembalikan data pengguna
    print("Login gagal! Email atau password salah.\n")
    return None
