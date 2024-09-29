def cek_prima(n):
   if n <= 1:
        return False
   for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
   return True

def bil_prima(awal, akhir):
    print(f"Bilangan Prima dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if cek_prima(num):
            print(num, end=" ")
    print()

def bil_ganjil(awal, akhir):
    print(f"Angka Ganjil dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print()

def bil_genap(awal, akhir):
    print(f"Bilangan Genap dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()

def menu():
    while True:
        print("===========MENU============")
        print("1.Menampilkan bilangan prima")
        print("2.Menampilkan bilangan genap")
        print("3.bilangan ganjil")
        print("4.keluar")

        pilih = input("Pilih menu (1/2/3/4) :")

        awal = int(input("Masukkan bilangan pertama: "))
        akhir = int(input("Masukkan bilangan terahir: "))

        if pilih == "1":
            bil_prima(awal, akhir)
        elif pilih == "2":
            bil_genap(awal, akhir)
        elif pilih == "3":
            bil_ganjil(awal, akhir)
        elif pilih == "4":
            print("Keluar dari program")
            break
        else:
            print("Masukan angka yang benar broo")

menu()