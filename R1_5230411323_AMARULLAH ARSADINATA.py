# NAMA : AMARULLAH ARSADINATA
# NPM  : 5230411323

import time  

class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat


class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi


class Produk:
    def __init__(self, kode_produk, nama_produk, harga, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.jenis_produk = jenis_produk

    def get_info(self):
        return f"Kode Produk: {self.kode_produk}, Nama Produk: {self.nama_produk}, Jenis Produk: {self.jenis_produk}, Harga: {self.harga}"


class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, harga, "Snack")


    def get_info(self):
        return f"Snack - {super().get_info()}"


class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, harga, "Makanan")

   
    def get_info(self):
        return f"Makanan - {super().get_info()}"


class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, harga, "Minuman")

   
    def get_info(self):
        return f"Minuman - {super().get_info()}"


class Struk:
    def __init__(self, no_transaksi, nama_pegawai):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.items = []
        self.total_harga = 0

    def tambah_item(self, produk, jumlah):
        self.items.append((produk, jumlah))
        self.total_harga += produk.harga * jumlah

    def cetak_struk(self):
        print("\n========== STRUK PEMBELIAN ==========")
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Pegawai: {self.nama_pegawai}")
        print("Items:")
        for produk, jumlah in self.items:
            print(f"- {produk.get_info()} x {jumlah}")
        print(f"Total Harga: {self.total_harga}")
        print("=====================================")
        print("Terimakaasih sudah berbelanja di toko kami...")
        print("=====================================")


def tambah_produk():
    while True:
        jenis_produk = input("Masukkan jenis produk (Snack/Makanan/Minuman): ").strip().lower()
        if jenis_produk not in ["snack", "makanan", "minuman"]:
            print("Jenis produk tidak valid! Silakan masukkan 'Snack', 'Makanan', atau 'Minuman'.")
            continue
        break

    kode_produk = input("Masukkan kode produk: ").strip()
    nama_produk = input("Masukkan nama produk: ").strip()

    while True:
        try:
            harga = int(input("Masukkan harga produk: "))
            if harga <= 0:
                print("Harga harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Harga tidak valid! Harap masukkan angka.")

    while True:
        try:
            jumlah = int(input("Masukkan jumlah produk: "))
            if jumlah <= 0:
                print("Jumlah harus lebih besar dari 0.")
                continue
            break
        except ValueError:
            print("Jumlah tidak valid! Harap masukkan angka.")

    if jenis_produk == "snack":
        produk = Snack(kode_produk, nama_produk, harga)
    elif jenis_produk == "makanan":
        produk = Makanan(kode_produk, nama_produk, harga)
    elif jenis_produk == "minuman":
        produk = Minuman(kode_produk, nama_produk, harga)
    
    return produk, jumlah


def input_data_pegawai():
    nik = input("Masukkan NIK Pegawai: ").strip()
    nama = input("Masukkan Nama Pegawai: ").strip()
    alamat = input("Masukkan Alamat Pegawai: ").strip()
    return Pegawai(nik, nama, alamat)


def main():
    print("=== Selamat Datang di Sistem Pembelian ===")
    time.sleep(1)
    
   
    print("\n--- Input Data Pegawai ---")
    pegawai = input_data_pegawai()
    
  
    no_transaksi = input("\nMasukkan No Transaksi: ").strip()
    detail_transaksi = input("Masukkan Detail Transaksi: ").strip()
    transaksi = Transaksi(no_transaksi, detail_transaksi)

   
    struk = Struk(transaksi.no_transaksi, pegawai.nama)

   
    while True:
        print("\n--- Pilih Produk ---")
        produk, jumlah = tambah_produk()
        if produk:
            struk.tambah_item(produk, jumlah)
        
        lanjut = input("Tambah produk lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            break

    
    struk.cetak_struk()


main()
