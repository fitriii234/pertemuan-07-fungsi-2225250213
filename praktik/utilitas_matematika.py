def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def faktorial(n):
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def input_float(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai < 0:
                print("Input tidak boleh negatif.")
                continue
            return nilai
        except ValueError:
            print("Masukkan angka yang valid.")


def input_bilangan_bulat(pesan):
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < 0:
                print("Bilangan harus nonnegatif.")
                continue
            return nilai
        except ValueError:
            print("Masukkan bilangan bulat yang valid.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            p = input_float("Masukkan panjang: ")
            l = input_float("Masukkan lebar: ")
            print("Luas persegi panjang =", luas_persegi_panjang(p, l))

        elif pilihan == "2":
            a = input_float("Masukkan alas: ")
            t = input_float("Masukkan tinggi: ")
            print("Luas segitiga =", luas_segitiga(a, t))

        elif pilihan == "3":
            n = input_bilangan_bulat("Masukkan n: ")
            print("Jumlah 1 sampai", n, "=", jumlah_n(n))

        elif pilihan == "4":
            n = input_bilangan_bulat("Masukkan n: ")
            print(n, "! =", faktorial(n))

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    main()
