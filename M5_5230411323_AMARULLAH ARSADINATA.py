class Musik:
    def __init__(self, judul, penyanyi, genre, playlist):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre
        self.playlist = playlist

    def tampilkan(self):
        print("-----------------------------------------------------------------------------------------------------")
        print("")
        print(f" |Judul: {self.judul} | Penyanyi: {self.penyanyi} | Genre: {self.genre} | Playlist: {self.playlist}|")
        print("")
        print("______________________________________________________________________________________________________")

        

class PengelolaMusik:
    def __init__(self):
        self.daftar_musik = []

    def tambah_musik(self, musik):
        self.daftar_musik.append(musik)
        print(f"Ditambahkan: {musik.judul} oleh {musik.penyanyi} ke playlist {musik.playlist}")

    def hapus_musik(self, judul):
        for musik in self.daftar_musik:
            if musik.judul == judul:
                self.daftar_musik.remove(musik)
                print(f"Dihapus: {musik.judul}")
                return
        print(f"Musik dengan judul '{judul}' tidak ditemukan.")

    def tampilkan_semua_musik(self):
        musik_urut = sorted(self.daftar_musik, key=lambda x: x.judul)
        print("Koleksi Musik (Diurutkan A-Z):")
        for musik in musik_urut:
            musik.tampilkan()

    def cari_berdasarkan_penyanyi(self, penyanyi):
        print(f"Hasil pencarian untuk penyanyi '{penyanyi}':")
        ditemukan = False
        for musik in self.daftar_musik:
            if musik.penyanyi == penyanyi:
                musik.tampilkan()
                ditemukan = True
        if not ditemukan:
            print(f"Tidak ada musik ditemukan untuk penyanyi '{penyanyi}'.")


def tampilkan_menu():
    print("\n=== Menu Pengelola Musik ===")
    print("1. Tambah Musik")
    print("2. Hapus Musik")
    print("3. Tampilkan Semua Musik")
    print("4. Cari Musik Berdasarkan Penyanyi")
    print("5. Keluar")

def tampilkan_sub_menu_playlist():
    print("\n=== Pilihan Playlist ===")
    print("1. Playlist Rock")
    print("2. Playlist Pop")
    print("3. Playlist Jazz")
    print("4. Buat Playlist Baru")

def tampilkan_sub_menu_judul():
    print("\n=== Pilihan Judul ===")
    print("1. Guru Oemar Bakri")
    print("2. Ujung Aspal Pondok Gede")
    print("3. Serdadu")
    print("4. Masukkan Judul Baru")

def tampilkan_sub_menu_penyanyi():
    print("\n=== Pilihan Penyanyi ===")
    print("1. Iwan Flas")
    print("2. Bernadya ")
    print("3. Deny Caknan ")
    print("4. Masukkan Penyanyi Baru")

def tampilkan_sub_menu_genre():
    print("\n=== Pilihan Genre ===")
    print("1. Pop")
    print("2. Rock")
    print("3. Jazz")
    print("4. Masukkan Genre Baru")

def main():
    pengelola = PengelolaMusik()
    
    while True:
        tampilkan_menu()
        pilihan = input("Masukan pilihan anda (1-5): ")

        if pilihan == "1":
            tampilkan_sub_menu_judul()
            pilihan_judul = input("Pilih judul (1-4): ")
            if pilihan_judul == "1":
                judul = "Guru Oemar Bakri"
            elif pilihan_judul == "2":
                judul = "Ujung Aspal Pondok Gede"
            elif pilihan_judul == "3":
                judul = "Serdadu"
            elif pilihan_judul == "4":
                judul = input("Masukkan judul baru: ")
            else:
                print("Pilihan tidak valid.")
                continue

           
            tampilkan_sub_menu_penyanyi()
            pilihan_penyanyi = input("Pilih penyanyi yang anda suka (1-4): ")
            if pilihan_penyanyi == "1":
                penyanyi = "Iwan Flas"
            elif pilihan_penyanyi == "2":
                penyanyi = "Bernadya"
            elif pilihan_penyanyi == "3":
                penyanyi = "Deny Caknan"
            elif pilihan_penyanyi == "4":
                penyanyi = input("Masukkan penyanyi baru: ")
            else:
                print("Pilihan tidak valid.")
                continue

           
            tampilkan_sub_menu_genre()
            pilihan_genre = input("Pilih genre kesukaan anda (1-4): ")
            if pilihan_genre == "1":
                genre = "Pop"
            elif pilihan_genre == "2":
                genre = "Rock"
            elif pilihan_genre == "3":
                genre = "Jazz"
            elif pilihan_genre == "4":
                genre = input("Masukkan genre baru: ")
            else:
                print("Pilihan tidak valid.")
                continue

            
            tampilkan_sub_menu_playlist()
            pilihan_playlist = input("Pilih playlist anda (1-4): ")
            if pilihan_playlist == "1":
                playlist = "Playlist Rock"
            elif pilihan_playlist == "2":
                playlist = "Playlist Pop"
            elif pilihan_playlist == "3":
                playlist = "Playlist Jazz"
            elif pilihan_playlist == "4":
                playlist = input("Masukkan nama playlist baru: ")
            else:
                print("Pilihan tidak valid. Menggunakan playlist 'Umum'.")
                playlist = "Umum"

           
            musik = Musik(judul, penyanyi, genre, playlist)
            pengelola.tambah_musik(musik)
        
        elif pilihan == "2":
            judul = input("Masukkan judul musik yang akan dihapus: ")
            pengelola.hapus_musik(judul)
        
        elif pilihan == "3":
            pengelola.tampilkan_semua_musik()
        
        elif pilihan == "4":
            penyanyi = input("Masukkan nama penyanyi yang akan dicari: ")
            pengelola.cari_berdasarkan_penyanyi(penyanyi)
        
        elif pilihan == "5":
            print("Terima kasih temankuuh .....")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
