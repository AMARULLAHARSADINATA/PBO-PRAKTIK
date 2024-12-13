import mysql.connector

# Koneksi ke database
mydb = mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="penjualan"
)

cur = mydb.cursor()

# CREATE TABLE pegawai (
#     NIK INT PRIMARY KEY,
#     Nama VARCHAR(100),
#     Alamat VARCHAR(255)
# );

# CREATE TABLE produk (
#     Kode_Produk INT PRIMARY KEY,
#     Nama_Produk VARCHAR(100),
#     Jenis_Produk VARCHAR(50)
# );

# CREATE TABLE transaksi (
#     No_Transaksi INT PRIMARY KEY,
#     NIK INT,
#     Detail_Transaksi TEXT,
#     FOREIGN KEY (NIK) REFERENCES pegawai(NIK)
# );

# CREATE TABLE struk (
#     No_Transaksi INT,
#     Nama_Pegawai VARCHAR(100),
#     Kode_Produk INT,
#     Jumlah_Produk INT,
#     Total_Harga DECIMAL(10, 2),
#     FOREIGN KEY (No_Transaksi) REFERENCES transaksi(No_Transaksi),
#     FOREIGN KEY (Kode_Produk) REFERENCES produk(Kode_Produk)
# );

def validate_non_empty(prompt):
    value = input(prompt)
    while not value.strip():
        print("Input tidak boleh kosong.")
        value = input(prompt)
    return value

def validate_integer(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Harap masukkan angka yang valid.")
        return validate_integer(prompt)

while True:
    print("\n=== Menu Utama ===")
    print("1. Tampilkan Semua Data")
    print("2. Input Data Pegawai")
    print("3. Input Data Transaksi")
    print("4. Input Data Produk")
    print("5. Input Data Struk")
    print("6. Hapus Data")
    print("0. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        print("\n=== Tampilkan Semua Data ===")
        print("1. Data Pegawai")
        print("2. Data Produk")
        print("3. Data Transaksi")
        print("4. Data Struk")
        sub_menu = input("Pilih sub-menu: ")

        if sub_menu == "1":
            print("\n=== Data Pegawai ===")
            cur.execute("SELECT * FROM pegawai")
            result = cur.fetchall()
            if result:
                for row in result:
                    print(f"NIK: {row[0]}, Nama: {row[1]}, Alamat: {row[2]}")
            else:
                print("Tidak ada data pegawai.")

        elif sub_menu == "2":
            print("\n=== Data Produk ===")
            cur.execute("SELECT * FROM produk")
            result = cur.fetchall()
            if result:
                for row in result:
                    print(f"Kode Produk: {row[0]}, Nama Produk: {row[1]}, Jenis Produk: {row[2]}, Harga: {row[3]}")
            else:
                print("Tidak ada data produk.")

        elif sub_menu == "3":
            print("\n=== Data Transaksi ===")
            cur.execute("SELECT * FROM transaksi")
            result = cur.fetchall()
            if result:
                for row in result:
                    print(f"No Transaksi: {row[0]}, Detail Transaksi: {row[1]}")
            else:
                print("Tidak ada data transaksi.")

        elif sub_menu == "4":
            print("\n=== Data Struk ===")
            cur.execute(
                """
                SELECT s.No_Transaksi, s.Nama_Pegawai, p.Nama_Produk, s.Jumlah_Produk, p.Harga_Produk, s.Total_Harga
                FROM struk s
                INNER JOIN produk p ON s.Kode_Produk = p.Kode_Produk
                """
            )
            result = cur.fetchall()
            if result:
                for row in result:
                    print(f"No Transaksi: {row[0]}, Nama Pegawai: {row[1]}, Nama Produk: {row[2]}, Jumlah: {row[3]}, Harga Satuan: {row[4]}, Total Harga: {row[5]}")
            else:
                print("Tidak ada data struk.")

        else:
            print("Sub-menu tidak valid!")

    elif menu == "2":
        print("\n=== Input Data Pegawai ===")
        nik_pegawai = validate_non_empty("Masukkan NIK Pegawai: ")
        nama_pegawai = validate_non_empty("Masukkan Nama Pegawai: ")
        alamat_pegawai = validate_non_empty("Masukkan Alamat Pegawai: ")

        cur.execute(
            "INSERT INTO pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)",
            [nik_pegawai, nama_pegawai, alamat_pegawai]
        )
        mydb.commit()
        print("Data Pegawai berhasil ditambahkan!")

    elif menu == "3":
        print("\n=== Input Data Transaksi ===")
        no_transaksi = validate_non_empty("Masukkan No Transaksi: ")
        detail_transaksi = validate_non_empty("Masukkan Detail Transaksi: ")

        cur.execute(
            "INSERT INTO transaksi (No_Transaksi, Detail_Transaksi) VALUES (%s, %s)",
            [no_transaksi, detail_transaksi]
        )
        mydb.commit()
        print("Data Transaksi berhasil ditambahkan!")

    elif menu == "4":
        print("\n=== Input Data Produk ===")
        kode_produk = validate_non_empty("Masukkan Kode Produk: ")
        nama_produk = validate_non_empty("Masukkan Nama Produk: ")
        jenis_produk = validate_non_empty("Masukkan Jenis Produk: ")
        harga_produk = validate_integer("Masukkan Harga Produk: ")

        cur.execute(
            "INSERT INTO produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga_Produk) VALUES (%s, %s, %s, %s)",
            [kode_produk, nama_produk, jenis_produk, harga_produk]
        )
        mydb.commit()
        print("Data Produk berhasil ditambahkan!")

    elif menu == "5":
        print("\n=== Input Data Struk ===")
        no_transaksi = validate_non_empty("Masukkan No Transaksi: ")
        cur.execute("SELECT * FROM transaksi WHERE No_Transaksi = %s", [no_transaksi])
        if not cur.fetchone():
            print("No Transaksi tidak ditemukan!")
            continue

        nama_pegawai = validate_non_empty("Masukkan Nama Pegawai: ")
        cur.execute("SELECT * FROM pegawai WHERE Nama = %s", [nama_pegawai])
        if not cur.fetchone():
            print("Nama Pegawai tidak ditemukan!")
            continue

        nama_produk = validate_non_empty("Masukkan Nama Produk: ")
        cur.execute("SELECT Kode_Produk, Harga_Produk FROM produk WHERE Nama_Produk = %s", [nama_produk])
        produk_data = cur.fetchone()
        if not produk_data:
            print("Nama Produk tidak ditemukan!")
            continue

        kode_produk = produk_data[0]
        harga_produk = produk_data[1]
        jumlah_produk = validate_integer("Masukkan Jumlah Produk: ")
        total_harga = jumlah_produk * harga_produk

        cur.execute(
            "INSERT INTO struk (No_Transaksi, Nama_Pegawai, Kode_Produk, Jumlah_Produk, Total_Harga) VALUES (%s, %s, %s, %s, %s)",
            [no_transaksi, nama_pegawai, kode_produk, jumlah_produk, total_harga]
        )
        mydb.commit()
        print(f"Data Struk berhasil ditambahkan! Total Harga: {total_harga}")

    elif menu == "6":
        print("\n=== Hapus Data ===")
        print("1. Hapus Data Pegawai")
        print("2. Hapus Data Transaksi")
        print("3. Hapus Data Produk")
        print("4. Hapus Data Struk")
        sub_menu = input("Pilih sub-menu: ")

        if sub_menu == "1":
            nik_pegawai = validate_non_empty("Masukkan NIK Pegawai yang akan dihapus: ")
            cur.execute("DELETE FROM pegawai WHERE NIK = %s", [nik_pegawai])
            mydb.commit()
            print("Data Pegawai berhasil dihapus!")

        elif sub_menu == "2":
            no_transaksi = validate_non_empty("Masukkan No Transaksi yang akan dihapus: ")
            cur.execute("DELETE FROM transaksi WHERE No_Transaksi = %s", [no_transaksi])
            mydb.commit()
            print("Data Transaksi berhasil dihapus!")

        elif sub_menu == "3":
            kode_produk = validate_non_empty("Masukkan Kode Produk yang akan dihapus: ")
            cur.execute("DELETE FROM produk WHERE Kode_Produk = %s", [kode_produk])
            mydb.commit()
            print("Data Produk berhasil dihapus!")

        elif sub_menu == "4":
            no_transaksi = validate_non_empty("Masukkan No Transaksi untuk Struk yang akan dihapus: ")
            cur.execute("DELETE FROM struk WHERE No_Transaksi = %s", [no_transaksi])
            mydb.commit()
            print("Data Struk berhasil dihapus!")

        else:
            print("Sub-menu tidak valid!")

    elif menu == "0":
        print("Keluar dari program.")
        break

    else:
        print("Menu tidak valid! Silakan pilih kembali.")

# Tutup koneksi
cur.close()
mydb.close()
