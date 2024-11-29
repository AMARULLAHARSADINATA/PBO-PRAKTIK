import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AplikasiKeluhan:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Keluhan Masyarakat")
        self.root.geometry("700x700")
        self.buat_widget()

    def buat_widget(self):
        # Label Judul
        label_judul = tk.Label(self.root, text="Aplikasi Keluhan Masyarakat", font=("Arial", 16, "bold"))
        label_judul.pack(pady=10)

        # Nama Pelapor
        label_nama = tk.Label(self.root, text="Nama Pelapor:")
        label_nama.pack()
        self.entri_nama = tk.Entry(self.root, width=40)
        self.entri_nama.pack(pady=5)

        # RT/RW Pelapor
        label_rt_rw = tk.Label(self.root, text="RT/RW Pelapor:")
        label_rt_rw.pack()
        opsi_rt_rw = [f"{i:02}/{j:02}" for i in range(1, 11) for j in range(1, 11)]
        self.menu_rt_rw = ttk.Combobox(self.root, values=opsi_rt_rw, state="readonly", width=15)
        self.menu_rt_rw.pack(pady=5)

        # Hari/Tanggal/Tahun
        label_tanggal = tk.Label(self.root, text="Hari/Tanggal/Tahun:")
        label_tanggal.pack()
        self.entri_tanggal = tk.Entry(self.root, width=40)
        self.entri_tanggal.pack(pady=5)

        # Keluhan
        label_keluhan = tk.Label(self.root, text="Keluhan:")
        label_keluhan.pack()
        self.entri_keluhan = tk.Entry(self.root, width=40)
        self.entri_keluhan.pack(pady=5)

        # Tabel Daftar Keluhan
        label_tabel_keluhan = tk.Label(self.root, text="Daftar Keluhan Masyarakat:")
        label_tabel_keluhan.pack(pady=10)

        self.tabel_keluhan = ttk.Treeview(
            self.root, 
            columns=("Nama", "RT/RW", "Tanggal", "Keluhan", "Status"), 
            show="headings"
        )
        self.tabel_keluhan.heading("Nama", text="Nama Pelapor")
        self.tabel_keluhan.heading("RT/RW", text="RT/RW Pelapor")
        self.tabel_keluhan.heading("Tanggal", text="Hari/Tanggal/Tahun")
        self.tabel_keluhan.heading("Keluhan", text="Keluhan")
        self.tabel_keluhan.heading("Status", text="Status")

        self.tabel_keluhan.pack(pady=10, fill="both", expand=True)

        # Tombol Tambah Keluhan
        tombol_tambah = tk.Button(self.root, text="Tambah Keluhan", command=self.tambah_keluhan)
        tombol_tambah.pack(pady=5)

        # Tombol Hapus Baris Terpilih
        tombol_hapus = tk.Button(self.root, text="Hapus Baris Terpilih", command=self.hapus_baris_terpilih)
        tombol_hapus.pack(pady=5)

        # Tombol Tandai Diterima
        tombol_terima = tk.Button(self.root, text="Tandai Diterima", command=self.tandai_diterima)
        tombol_terima.pack(pady=5)

    def tambah_keluhan(self):
        # Ambil data dari input pengguna
        nama = self.entri_nama.get()
        rt_rw = self.menu_rt_rw.get()
        tanggal = self.entri_tanggal.get()
        keluhan = self.entri_keluhan.get()

        # Validasi input
        if not nama or not rt_rw or not tanggal or not keluhan:
            messagebox.showerror("Error", "Semua kolom harus diisi!")
            return

        # Tambahkan data ke tabel dengan status awal "Belum Diterima"
        self.tabel_keluhan.insert("", "end", values=(nama, rt_rw, tanggal, keluhan, "Belum Diterima"))

        # Bersihkan input
        self.entri_nama.delete(0, tk.END)
        self.menu_rt_rw.set("")
        self.entri_tanggal.delete(0, tk.END)
        self.entri_keluhan.delete(0, tk.END)

    def hapus_baris_terpilih(self):
        # Ambil baris yang dipilih oleh pengguna
        item_terpilih = self.tabel_keluhan.selection()

        # Validasi apakah ada baris yang dipilih
        if not item_terpilih:
            messagebox.showerror("Error", "Pilih baris yang ingin dihapus!")
            return

        # Hapus baris yang dipilih
        for item in item_terpilih:
            self.tabel_keluhan.delete(item)

    def tandai_diterima(self):
        # Ambil baris yang dipilih oleh pengguna
        item_terpilih = self.tabel_keluhan.selection()

        # Validasi apakah ada baris yang dipilih
        if not item_terpilih:
            messagebox.showerror("Error", "Pilih baris yang ingin ditandai sebagai diterima!")
            return

        # Perbarui status menjadi "Diterima"
        for item in item_terpilih:
            nilai = self.tabel_keluhan.item(item, "values")
            nilai_diperbarui = (*nilai[:-1], "Diterima")
            self.tabel_keluhan.item(item, values=nilai_diperbarui)


if __name__ == '__main__':
    root = tk.Tk()
    app = AplikasiKeluhan(root)
    root.mainloop()
