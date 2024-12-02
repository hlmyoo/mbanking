import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_saldo(saldo):
    try:
        saldo = int(saldo)  # Ubah saldo menjadi integer jika memungkinkan
        return f"{saldo:,}".replace(",", ".")
    except ValueError:
        return "Saldo tidak valid"

def cek_data(user, saldo):
    clear_screen()  # Bersihkan layar saat memasuki fitur cek data
    print("\n--- Informasi Akun ---")
    print(f"Nama: {user['nama']}")
    print(f"Email: {user['email']}")
    print(f"Password: {user['password']}")
    print(f"Pin: {user['pin']}")
    print(f"Nomor Telepon: {user['no_telfon']}")
    print(f"Bank: {user['bank']}")
    print(f"No. Rekening: {user['rekening']}")
    formatted_saldo = format_saldo(saldo)
    print(f"Saldo: {formatted_saldo}")
    print("Untuk mengisi saldo, silakan datang ke kantor bank terdekat.\n")
    
    input("Tekan Enter untuk kembali ke Menu Utama...")  # User harus menekan Enter untuk kembali
    clear_screen()  # Bersihkan layar sebelum kembali ke menu utama
    return False  # Menandakan untuk tetap berada di menu utama (kembali ke daftar fitur)
