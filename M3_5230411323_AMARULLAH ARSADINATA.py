class DaftarMenu():

    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama} - Rp{self.harga:.2f}"
    
class Menu:
    def __init__(self):
        self.item_menu = []

    def tambah_item(self, item):
        self.item_menu.append(item)

    def tampilkan_menu(self):
        print("\n ==========Sub Menu==========")
        for index, item in enumerate(self.item_menu, start=1):
            print(f"{index}.{item}")

def main():
    menu_makan = Menu()
    menu_minuman = Menu()

    menu_makan.tambah_item(DaftarMenu("Nasi Goreng", 12000))
    menu_makan.tambah_item(DaftarMenu("Mie Goreng", 12000))
    menu_makan.tambah_item(DaftarMenu("Kwetiaw", 12000))
    menu_makan.tambah_item(DaftarMenu("Pangsit", 12000))
    menu_makan.tambah_item(DaftarMenu("Nasi Godog", 12000))

    menu_minuman.tambah_item(DaftarMenu("Teh Manis", 2000))
    menu_minuman.tambah_item(DaftarMenu("Es Jeruk", 4000))
    menu_minuman.tambah_item(DaftarMenu("Kelapa Muda", 10000))
    menu_minuman.tambah_item(DaftarMenu("Es Teler", 9000))
    menu_minuman.tambah_item(DaftarMenu("Air Mineral", 2000))

    while True:
        print("\n ==========Menu Utama==========")
        print("1.Tampilkan Makanan")
        print("2.Tampilkan Minuman")
        print("3.Tambah Menu")
        print("4.Keluar")

        try:
            pilihan = int(input("Pilih opsi (1-4): "))
            if pilihan == 1:
                menu_makan.tampilkan_menu() 
            elif pilihan == 2:
                menu_minuman.tampilkan_menu()  
            elif pilihan == 3:
                while True:
                    jenis_menu = input("Tambahkan menu (makanan/minuman): ").strip().lower()
                    if jenis_menu in ["makanan", "minuman"]:
                        while True:
                            nama = input("Masukkan nama item: ").strip()
                            if len(nama) == 0:
                                print("Nama item tidak boleh kosong. Silakan coba lagi.")
                            else:
                                break
                        while True:
                            try:
                                harga = float(input("Masukkan harga item: "))
                                break
                            except ValueError:
                                print("Harga item harus berupa angka. Silakan coba lagi.")
                        if jenis_menu == "makanan":
                            menu_makan.tambah_item(DaftarMenu(nama, harga))
                            print(f"Item '{nama}' ditambahkan ke menu makanan.")
                        elif jenis_menu == "minuman":
                            menu_minuman.tambah_item(DaftarMenu(nama, harga))
                            print(f"Item '{nama}' ditambahkan ke menu minuman.")
                        break
                    else:
                        print("Jenis menu tidak valid. Silakan coba lagi.")
            elif pilihan == 4:
                print("Terima kasih telah belanja di sini broooooooo !")
                break
            else:
                print("Pilih angka sesuai pilihan menu yaa.....")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")


if __name__ == "__main__":
    main()