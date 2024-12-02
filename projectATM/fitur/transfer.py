import os
import csv
from datetime import datetime

# Mendapatkan tanggal dan waktu saat ini
tanggal = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# File mutasi_transfer.csv untuk mencatat riwayat transfer
mutasi_file = "database/mutasi_transfer.csv"

# Pastikan file mutasi_transfer.csv ada, jika tidak buat dengan header
if not os.path.exists(mutasi_file):
    with open(mutasi_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["nama_pengirim", "rekening_pengirim", "rekening_tujuan", "bank_pengirim", "bank_tujuan", "jumlah_transfer", "pajak", "total_transfer", "tanggal"])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fitur Transfer
def transfer(saldo, user_rekening, user_bank, user_nama):
    database_path = "database/data_user.csv"

    while True:
        clear_screen()
        print("=== MENU TRANSFER ===")
        print(f"Saldo Anda saat ini: Rp {saldo:,.2f}".replace(",", "."))
        print("----------------------------")
        print("1. Lanjutkan Transfer")
        print("2. Kembali ke Menu Utama")
        print("----------------------------")
        
        pilihan = input("Pilih [1/2]: ").strip()
        
        if pilihan == "1":
            clear_screen()
            print("=== FORMULIR TRANSFER ===")
            try:
                rekening_tujuan = input("Masukkan nomor rekening tujuan: ").strip()
                jumlah_transfer = float(input("Masukkan jumlah transfer: Rp ").replace(",", "."))

                if jumlah_transfer <= 0:
                    clear_screen()
                    print("Jumlah transfer harus lebih dari Rp 0!\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                if jumlah_transfer > saldo:
                    clear_screen()
                    print("Saldo Anda tidak mencukupi untuk melakukan transfer ini.\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

                # Baca database untuk menemukan penerima
                penerima = None
                with open(database_path, mode="r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["rekening"] == rekening_tujuan:
                            penerima = row
                            break

                if not penerima:
                    clear_screen()
                    print("Nomor rekening tujuan tidak ditemukan.\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

                # Hitung pajak transfer jika bank berbeda
                pajak = 0
                if user_bank != penerima["bank"]:
                    if user_bank == "BCA" and penerima["bank"] == "BRI":
                        pajak = jumlah_transfer * 0.02  # Pajak 2%
                    elif user_bank == "BCA" and penerima["bank"] == "BTN":
                        pajak = jumlah_transfer * 0.03  # Pajak 3%
                    elif user_bank == "BRI" and penerima["bank"] == "BCA":
                        pajak = jumlah_transfer * 0.02  # Pajak 2%
                    elif user_bank == "BRI" and penerima["bank"] == "BTN":
                        pajak = jumlah_transfer * 0.03  # Pajak 3%
                    elif user_bank == "BTN" and penerima["bank"] == "BCA":
                        pajak = jumlah_transfer * 0.03  # Pajak 3%
                    elif user_bank == "BTN" and penerima["bank"] == "BRI":
                        pajak = jumlah_transfer * 0.03  # Pajak 3%

                total_transfer = jumlah_transfer + pajak
                if total_transfer > saldo:
                    clear_screen()
                    print(f"Saldo tidak cukup untuk transfer sebesar Rp {jumlah_transfer:,.2f} + pajak Rp {pajak:,.2f}.\n")
                    input("Tekan Enter untuk melanjutkan...")
                    continue

                # Konfirmasi transfer
                clear_screen()
                print("=== KONFIRMASI TRANSFER ===")
                print(f"Transfer sebesar Rp {jumlah_transfer:,.2f}")
                print(f"Rekening Tujuan: {rekening_tujuan} ({penerima['nama']})")
                print(f"Bank Tujuan: {penerima['bank']}")
                print(f"Pajak: Rp {pajak:,.2f}")
                print(f"Total Transfer: Rp {total_transfer:,.2f}")
                konfirmasi = input("Lanjutkan transfer? (y/n): ").strip().lower()
                if konfirmasi != "y":
                    continue

                # Update saldo pengirim dan penerima
                saldo -= total_transfer
                updated_data = []
                with open(database_path, mode="r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["rekening"] == user_rekening:  # Pengirim
                            row["saldo"] = str(float(row["saldo"]) - total_transfer)  # Kurangi saldo pengirim
                        elif row["rekening"] == rekening_tujuan:  # Penerima
                            row["saldo"] = str(float(row["saldo"]) + jumlah_transfer)  # Tambah saldo penerima
                        updated_data.append(row)

                # Tulis kembali data ke file
                with open(database_path, mode="w", newline="") as file:
                    fieldnames = ["nama", "email", "password", "pin", "no_telfon", "bank", "rekening", "saldo"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_data)

                # Tambahkan riwayat transfer ke mutasi_transfer.csv
                with open(mutasi_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([
                        user_nama,            # Nama Pengirim
                        user_rekening,        # Rekening Pengirim
                        rekening_tujuan,      # Rekening Tujuan
                        user_bank,            # Bank Pengirim
                        penerima["bank"],     # Bank Tujuan
                        jumlah_transfer,      # Jumlah Transfer
                        pajak,                # Pajak
                        total_transfer,       # Total Transfer
                        tanggal               # Tanggal dan Waktu Transfer
                    ])

                clear_screen()
                print("=== TRANSFER BERHASIL ===")
                print(f"Pajak: Rp {pajak:,.2f}. Sisa saldo Anda: Rp {saldo:,.2f}".replace(",", "."))
                input("Tekan Enter untuk melanjutkan...")
                continue  # Kembali ke menu transfer

            except ValueError:
                clear_screen()
                print("Input tidak valid. Masukkan angka dengan format yang benar.\n")
                input("Tekan Enter untuk melanjutkan...")
                continue
        
        elif pilihan == "2":
            clear_screen()
            return saldo  # Kembali ke menu utama
        
        else:
            clear_screen()
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan.")
