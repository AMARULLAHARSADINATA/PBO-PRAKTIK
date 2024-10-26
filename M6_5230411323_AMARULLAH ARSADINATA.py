class Order:
    def __init__(self, ID, nama, rincian, alamat):
        self.__ID = ID
        self.nama = nama
        self.rincian = rincian
        self.alamat = alamat

    def tampilkan(self):
        return f"ID Pesanan: {self.__ID}, Nama: {self.nama}, Rincian: {self.rincian}, Alamat: {self.alamat}"


class Delivery:
    def __init__(self, id, nama, informasi, tanggal, alamat):
        self.__id = id
        self.nama = nama
        self.informasi = informasi
        self.tanggal = tanggal
        self.alamat = alamat

    def tampilkan(self):
        return (f"ID Pengiriman: {self.__id}, Nama: {self.nama}, Informasi: {self.informasi}, "
                f"Tanggal: {self.tanggal}, Alamat: {self.alamat}")


def buat_pesanan_dan_pengiriman(pesanan, pengiriman):
    while True:
        print("\n--- Sub Menu Pesanan dan Pengiriman ---")
        sub_menu = {
            '1': 'Buat Pesanan',
            '2': 'Buat Pengiriman',
            '3': 'Kembali ke Menu Utama'
        }

        for key, value in sub_menu.items():
            print(f"{key}. {value}")
        
        pilihan_sub_menu = input("Masukkan pilihan Anda: ")
        
        if pilihan_sub_menu == '1':
            ID = input("Masukkan ID Pesanan: ")
            nama_pesanan = input("Masukkan Nama Barang: ")
            rincian = input("Masukkan Rincian Barang: ")
            alamat_pesanan = input("Masukkan Alamat Pemesanan: ")

            if not ID or not nama_pesanan or not rincian or not alamat_pesanan:
                print("Semua input harus diisi. Silakan coba lagi.")
                continue
            
            order = Order(int(ID), nama_pesanan, rincian, alamat_pesanan)
            pesanan.append(order)
            print("Pesanan berhasil dibuat.")

        elif pilihan_sub_menu == '2':
            if not pesanan:
                print("Belum ada pesanan yang dibuat. Silakan buat pesanan terlebih dahulu.")
                continue
            
            id_pengiriman = input("Masukkan ID Pengiriman: ")
            nama_pengiriman = input("Masukkan Nama Penerima: ")
            informasi = input("Masukkan Informasi Pengiriman: ")
            tanggal = input("Masukkan Tanggal Pengiriman: ")
            alamat_pengiriman = pesanan[-1].alamat
            
            if not id_pengiriman or not nama_pengiriman or not informasi or not tanggal:
                print("Semua input harus diisi. Silakan coba lagi.")
                continue
            
            delivery = Delivery(int(id_pengiriman), nama_pengiriman, informasi, tanggal, alamat_pengiriman)
            pengiriman.append(delivery)
            print("Pengiriman berhasil dibuat.")

        elif pilihan_sub_menu == '3':
            break

        else:
            print("Pilihan tidak valid, coba lagi.")
        

def tampilkan_gabungan(pesanan, pengiriman):
    if pesanan or pengiriman:
        print("\nGabungan Pesanan dan Pengiriman:")
        urutan = 1
        
        for order in pesanan:
            print(f"{urutan}. {order.tampilkan()}")
            urutan += 1

        for delivery in pengiriman:
            print(f"{urutan}. {delivery.tampilkan()}")
            urutan += 1
    else:
        print("Belum ada pesanan atau pengiriman.")


def main():
    pesanan = []
    pengiriman = []
    
    menu_utama = {
        '1': 'Buat Pesanan dan Pengiriman',
        '2': 'Tampilkan Pesanan dan Pengiriman Gabungan',
        '3': 'Keluar'
    }

    while True:
        print("\nMenu Utama:")
        for key, value in menu_utama.items():
            print(f"{key}. {value}")
        
        pilihan_menu = input("Masukkan pilihan Anda: ")
        
        if pilihan_menu == '1':
            buat_pesanan_dan_pengiriman(pesanan, pengiriman)
        
        elif pilihan_menu == '2':
            tampilkan_gabungan(pesanan, pengiriman)
        
        elif pilihan_menu == '3':
            print("Keluar...")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
