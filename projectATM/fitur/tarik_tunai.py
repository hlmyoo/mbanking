import os
import random
import csv
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_codeless_code():
    """
    Fungsi untuk menghasilkan kode penarikan unik (6 digit).
    """
    return str(random.randint(100000, 999999))

def update_saldo(rekening_user, saldo_baru, file_path="database/data_user.csv"):
    """
    Mengupdate saldo pengguna di file data_user.csv.
    """
    updated_data = []
    updated = False
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["rekening"] == rekening_user:
                row["saldo"] = str(saldo_baru)  # Update saldo pengguna
                updated = True
            updated_data.append(row)
    
    if updated:
        with open(file_path, mode='w', newline='') as file:
            fieldnames = ["nama", "email", "password", "pin", "no_telfon", "bank", "rekening", "saldo"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(updated_data)
    else:
        print("Rekening pengguna tidak ditemukan.")

def simpan_riwayat_tarik_tunai(rekening_user, penarikan, codeless_code, file_path="database/riwayat_tarik_tunai.csv"):
    """
    Menyimpan riwayat penarikan tunai ke file CSV.
    """
    tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([rekening_user, penarikan, codeless_code, tanggal])

def tarik_tunai(saldo, rekening_user):
    while True:
        clear_screen()
        print("--- Tarik Tunai Cardless ---")
        print(f"Saldo Anda saat ini: Rp {saldo:,.2f}".replace(",", "."))
        print("----------------------------")     
        print("1. Lanjutkan Tarik Tunai")
        print("2. Kembali ke Menu Utama")
        print("----------------------------")
        
        pilihan = input("Pilih [1/2]: ").strip()

        if pilihan == "1":
            clear_screen()
            print("=== FORMULIR TARIK TUNAI ===")
            print(f"Saldo Anda saat ini: Rp {saldo:,.2f}".replace(",", "."))

            try:
                penarikan = float(input("Masukkan jumlah uang yang ingin ditarik: Rp ").replace(",", "."))

                if penarikan <= 0:
                    clear_screen()
                    print("Jumlah penarikan harus lebih dari Rp 0.\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

                if penarikan > saldo:
                    clear_screen()
                    print("Saldo Anda tidak mencukupi untuk penarikan ini.\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

                # Proses pengurangan saldo dan pembuatan kode tarik tunai
                saldo -= penarikan
                codeless_code = generate_codeless_code()

                # Update saldo di file database
                update_saldo(rekening_user, saldo)  # Pastikan saldo terupdate di file CSV

                # Simpan riwayat penarikan ke dalam database riwayat_tarik_tunai
                simpan_riwayat_tarik_tunai(rekening_user, penarikan, codeless_code)

                clear_screen()
                print(f"Penarikan sebesar Rp {penarikan:,.2f}".replace(",", ".") + " berhasil diproses.")
                print(f"Sisa saldo Anda: Rp {saldo:,.2f}".replace(",", "."))
                print(f"Kode Tarik Tunai Anda: {codeless_code}")
                print("Gunakan kode ini untuk menarik uang di ATM terdekat dalam waktu 2 jam.\n")

                input("Tekan Enter untuk kembali ke menu utama...")
                clear_screen()  # Bersihkan tampilan sebelum kembali
                return saldo  # Kembali ke menu utama dengan saldo yang diperbarui

            except ValueError:
                clear_screen()
                print("Input tidak valid. Masukkan angka dengan format yang benar.\n")
                input("Tekan Enter untuk melanjutkan...")

        elif pilihan == "2":
            clear_screen()
            return saldo  # Kembali ke menu utama
        
        else:
            clear_screen()
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
