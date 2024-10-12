class Debitur:
    def __init__(self, nama, ktp, limit_pinjaman):
        self.nama = nama 
        self.__ktp = ktp  
        self._limit_pinjaman = limit_pinjaman  

    def get_ktp(self):
        return self.__ktp

    def get_limit_pinjaman(self):
        return self._limit_pinjaman
    
class KelolaDebitur:
    def __init__(self):
        self.data_debitur = {}

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        if ktp in self.data_debitur:
            print("Validasi Gagal: Debitur dengan KTP ini sudah ada.")
        else:
            debitur = Debitur(nama, ktp, limit_pinjaman)
            self.data_debitur[ktp] = debitur
            print(f"Debitur {nama} berhasil ditambahkan.")

    def tampilkan_debitur(self):
        for debitur in self.data_debitur.values():
            print(f"Nama: {debitur.nama}, KTP: [Private], Limit Pinjaman: {debitur.get_limit_pinjaman()}")

    def cari_debitur(self, nama):
        for debitur in self.data_debitur.values():
            if debitur.nama == nama:
                print(f"Nama: {debitur.nama}, KTP: {debitur.get_ktp()}, Limit Pinjaman: {debitur.get_limit_pinjaman()}")
                return debitur
        print("Debitur tidak ditemukan.")
        return None

class Pinjaman:
    def __init__(self, debitur, jumlah_pinjaman, bunga, bulan):
        self.debitur = debitur
        self.jumlah_pinjaman = jumlah_pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran_pokok = jumlah_pinjaman * (1 + (bunga / 100)) 
        self.angsuran_bulanan = self.angsuran_pokok / bulan  
        self.total_angsuran = self.angsuran_pokok + self.angsuran_bulanan  

    def tampilkan_pinjaman(self):
        print(f"======================================================|")
        print(f"Nama: {self.debitur.nama}, Pinjaman: {self.jumlah_pinjaman}, Bunga: {self.bunga}%, Bulan: {self.bulan}")
        print(f"======================================================|")
        print(f"Angsuran Pokok: {self.angsuran_pokok:.2f}")
        print(f"======================================================|")
        print(f"Angsuran Bulanan: {self.angsuran_bulanan:.2f}")
        print(f"======================================================|")
        print(f"======================================================|")
        print(f"Total Angsuran: {self.total_angsuran:.2f}")
        print(f"======================================================|")

class KelolaPinjaman:
    def __init__(self, kelola_debitur):
        self.kelola_debitur = kelola_debitur
        self.data_pinjaman = []

    def tambah_pinjaman(self, nama, jumlah_pinjaman, bunga, bulan):
        debitur = self.kelola_debitur.cari_debitur(nama)
        if debitur is None:
            print("Validasi Gagal: Debitur tidak ditemukan.")
        elif jumlah_pinjaman > debitur.get_limit_pinjaman():
            print("Validasi Gagal: Jumlah pinjaman melebihi limit.")
        else:
            pinjaman = Pinjaman(debitur, jumlah_pinjaman, bunga, bulan)
            self.data_pinjaman.append(pinjaman)
            print(f"Pinjaman untuk {nama} berhasil ditambahkan.")

    def tampilkan_pinjaman(self):
        for pinjaman in self.data_pinjaman:
            pinjaman.tampilkan_pinjaman()

def menu():
    kelola_debitur = KelolaDebitur()
    kelola_pinjaman = KelolaPinjaman(kelola_debitur)

    while True:
        print("\n===== Menu  UTAMA =====")
        print("1. Tambah Debitur           |")
        print("2. Cari Debitur             |")
        print("3. Tambah Pinjaman          |")
        print("4. Tampilkan Semua Pinjaman |")
        print("5. Keluar                   |")
        print(f"============================")
        pilihan = input("Pilih input yang dibutuhkan ==>> ")

        if pilihan == '1':
            nama = input("Masukkan nama debitur: ")
            ktp = input("Masukkan nomor KTP debitur: ")
            limit_pinjaman = int(input("Masukkan limit pinjaman: "))
            kelola_debitur.tambah_debitur(nama, ktp, limit_pinjaman)

        elif pilihan == '2':
            nama = input("Masukkan nama debitur yang ingin dicari: ")
            kelola_debitur.cari_debitur(nama)

        elif pilihan == '3':
            nama = input("Masukkan nama debitur untuk pinjaman: ")
            jumlah_pinjaman = int(input("Masukkan jumlah pinjaman: "))
            bunga = float(input("Masukkan bunga (%): "))
            bulan = int(input("Masukkan jangka waktu (bulan): "))
            kelola_pinjaman.tambah_pinjaman(nama, jumlah_pinjaman, bunga, bulan)

        elif pilihan == '4':
            kelola_pinjaman.tampilkan_pinjaman()

        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()