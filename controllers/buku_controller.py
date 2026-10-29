import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView
#Muhammad Alfaizan_F5212520036

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding tombol simpan
        self.view.btn_simpan.configure(command=self.simpan_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit'])
            )

#Muhammad Alfaizan_F5212520036
    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data."
            )

    def run(self):
        self.view.mainloop()

    def ambil_id_buku(self):
        selected = self.view.tabel.selection()
        if not selected:
            return None
        item = self.view.tabel.item(selected[0])
        id_buku = item["values"][0]
        return id_buku
    
    def pilih_buku(self, event=None):
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = self.view.tabel.item(selected[0])
        data = item["values"]

        self.bersihkan_form()

        self.view.entry_judul.insert(0, data[1])
        self.view.entry_penulis.insert(0, data[2])
        self.view.entry_tahun.insert(0, data[3])

    def update_buku(self):
        id_buku = self.ambil_id_buku()

        if id_buku is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )

            berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        print("ID Buku:", id_buku)
        print("Judul Baru:", judul)
        print("Status Update:", berhasil)

        if berhasil:
            self.muat_data_tabel()
            print("Tabel berhasil dimuat ulang")
            
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data buku."
            )

    def pilih_buku(self, event=None):
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = self.view.tabel.item(selected[0])
        data = item["values"]

        self.bersihkan_form()

        self.view.entry_judul.insert(0, data[1])
        self.view.entry_penulis.insert(0, data[2])
        self.view.entry_tahun.insert(0, data[3])



    def hapus_buku(self):
        print("Tombol Hapus diklik")

        selected = self.view.tabel.selection()

        if not selected:
             messagebox.showwarning(
            "Peringatan",
            "Pilih buku yang ingin dihapus!"
            )
             return
    
        item = self.view.tabel.item(selected[0])
        id_buku = item["values"][0]

        konfirmasi = messagebox.askyesno(
        "Konfirmasi",
        "Yakin ingin menghapus buku ini?"
        )

        if konfirmasi:
         berhasil = self.model.hapus_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menghapus data buku!"
            )

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()