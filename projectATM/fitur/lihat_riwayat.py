import csv
import os

def clear_screen():
    # Bersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def format_saldo(saldo):
    """
    Fungsi untuk memformat saldo menjadi format pemisah ribuan dengan titik.
    Contoh: 10000 -> 10.000
    """
    if saldo is None:
        return "Saldo tidak tersedia"
    
    try:
        saldo = float(saldo)  # Pastikan saldo berupa angka (int/float)
        return f"{saldo:,.2f}".replace(",", ".")
    except ValueError:
        return "Saldo tidak valid"

def lihat_riwayat(user_nama, rekening, saldo):
    while True:
        clear_screen()  # Bersihkan layar sebelum menampilkan menu riwayat
        # Pilihan menu untuk melihat riwayat
        print("--- Pilih Riwayat ---")
        print("1. Riwayat Transfer")
        print("2. Riwayat Tarik Tunai")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih [1/2/3]: ").strip()

        if pilihan == "1":
            clear_screen()
            lihat_riwayat_transfer(user_nama, saldo)  # Panggil fungsi untuk riwayat transfer
        elif pilihan == "2":
            clear_screen()
            lihat_riwayat_tarik_tunai(user_nama, rekening, saldo)  # Panggil fungsi untuk riwayat tarik tunai
        elif pilihan == "3":
            clear_screen()
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")
            clear_screen()


def lihat_riwayat_transfer(user_nama, saldo):
    clear_screen()  # Bersihkan layar sebelum menampilkan riwayat transfer
    mutasi_file = "database/mutasi_transfer.csv"
    found = False

    try:
        with open(mutasi_file, mode="r") as file:
            reader = csv.DictReader(file)
            print("\n--- Riwayat Transfer ---")
            formatted_saldo = format_saldo(saldo)  # Format saldo sesuai dengan yang diinginkan
            print(f"Saldo Anda: {formatted_saldo}\n")  # Menampilkan saldo sebelum riwayat

            for row in reader:
                if row["nama_pengirim"] == user_nama:
                    print(f"Rekening Pengirim: {row['rekening_pengirim']}")
                    print(f"Rekening Tujuan: {row['rekening_tujuan']}")
                    print(f"Bank Pengirim: {row['bank_pengirim']}")
                    print(f"Bank Tujuan: {row['bank_tujuan']}")
                    print(f"Jumlah Transfer: {format_saldo(row['jumlah_transfer'])}")
                    print(f"Pajak: {format_saldo(row['pajak'])}")
                    print(f"Total Transfer: {format_saldo(row['total_transfer'])}")
                    print(f"Tanggal Transfer: {row['tanggal']}")
                    print("-" * 40)
                    found = True

            if not found:
                print("Tidak ada riwayat transfer ditemukan.\n")

    except FileNotFoundError:
        print(f"File {mutasi_file} tidak ditemukan.\n")

    input("Tekan Enter untuk kembali...")
    clear_screen()  # Bersihkan layar setelah selesai
    return


def lihat_riwayat_tarik_tunai(user_nama, rekening, saldo):
    clear_screen()  # Bersihkan layar sebelum menampilkan riwayat tarik tunai
    tarik_tunai_file = "database/riwayat_tarik_tunai.csv"
    found = False

    try:
        with open(tarik_tunai_file, mode="r") as file:
            reader = csv.DictReader(file)

            print("\n--- Riwayat Tarik Tunai ---")
            formatted_saldo = format_saldo(saldo)
            print(f"Saldo Anda: {formatted_saldo}\n")

            for row in reader:
                if row["rekening_user"] == str(rekening):
                    print(f"Jumlah Penarikan: {format_saldo(row['jumlah_penarikan'])}")
                    print(f"Kode Penarikan: {row['kode_tarik_tunai']}")
                    print(f"Tanggal Penarikan: {row['tanggal']}")
                    print("-" * 40)
                    found = True

            if not found:
                print("Data belum ada.\n")

    except FileNotFoundError:
        print(f"File {tarik_tunai_file} tidak ditemukan.\n")

    input("Tekan Enter untuk kembali...")
    clear_screen()  # Bersihkan layar setelah selesai
    return


