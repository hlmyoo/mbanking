import os
from fitur.register import register
from fitur.login import login
from fitur.menu import menu_utama

def clear_screen():
    # Bersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# Program utama
def main():
    while True:  # Selama program berjalan, terus tampilkan tampilan awal
        clear_screen()
        print("--- SELAMAT DATANG DI ATM AMBATUKAM ---")
        pilihan = input("1. Login\n2. Register\nPilih menu [1/2]: ")

        if pilihan == "1":  # Login
            user = login()
            if user:
                clear_screen()  # Bersihkan layar setelah login
                menu_utama(user)

        elif pilihan == "2":  # Register
            register()

        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__":
    main()
