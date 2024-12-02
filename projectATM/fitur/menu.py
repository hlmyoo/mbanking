import os
from fitur.transfer import transfer
from fitur.tarik_tunai import tarik_tunai
from fitur.cek_data import cek_data
from fitur.lihat_riwayat import lihat_riwayat

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_utama(user):
    try:
        saldo = int(float(user.get("saldo", 0)))  # Validasi saldo
    except ValueError:
        print("Saldo tidak valid. Menggunakan nilai default 0.")
        saldo = 0

    while True:
        print("\n--- Selamat datang, {}! ---".format(user["nama"]))
        pilihan_user = input("1. Transfer\n2. Tarik Tunai\n3. Cek Data\n4. Lihat Riwayat\n5. Keluar\nPilih menu [1/2/3/4/5]: ")

        if pilihan_user == "1":  # Transfer
            saldo = transfer(saldo, user["rekening"], user["bank"], user["nama"])

        elif pilihan_user == "2":  # Tarik Tunai
            saldo = tarik_tunai(saldo, user["rekening"])

        elif pilihan_user == "3":  # Cek Data
            cek_data(user, saldo)

        elif pilihan_user == "4":  # Lihat Riwayat
            kembali_ke_menu = lihat_riwayat(user["nama"], user["rekening"], saldo)

        elif pilihan_user == "5":  # Keluar
            print("Terima kasih telah menggunakan ATM Ambatukam!")
            clear_screen()
            break  # Keluar dari aplikasi

        else:
            print("Pilihan tidak valid.\n")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()
