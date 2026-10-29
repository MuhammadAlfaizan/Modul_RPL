# Muhammad Alfaizan_F5212520036
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_anggota)
        self.view.btn_hapus.configure(command=self.hapus_anggota)

        # Binding pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_anggota
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Hapus data lama dari tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Ambil data dari Model
        data_anggota = self.model.get_all_anggota()

        # Tampilkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"],
                    anggota["no_hp"],
                ),
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")
        self.view.entry_no_hp.delete(0, "end")

    def ambil_id_anggota(self):
        selected = self.view.tabel.selection()

        if not selected:
            return None

        item = self.view.tabel.item(selected[0])
        return item["values"][0]

    def pilih_anggota(self, event=None):
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = self.view.tabel.item(selected[0])
        data = item["values"]

        self.bersihkan_form()

        self.view.entry_nama.insert(0, data[1])
        self.view.entry_alamat.insert(0, data[2])
        self.view.entry_no_hp.insert(0, data[3])

    def simpan_data(self):
        # Ambil data dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()
        no_hp = self.view.entry_no_hp.get().strip()

        # Validasi form
        if not nama or not alamat or not no_hp:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!",
            )
            return

        # Simpan melalui Model
        berhasil = self.model.create_anggota(
            nama, alamat, no_hp
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!",
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data anggota.",
            )

    def update_anggota(self):
        # Ambil ID anggota yang dipilih
        id_anggota = self.ambil_id_anggota()

        if id_anggota is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota yang ingin diperbarui!",
            )
            return

        # Ambil data terbaru dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()
        no_hp = self.view.entry_no_hp.get().strip()

        if not nama or not alamat or not no_hp:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!",
            )
            return

        # Perbarui melalui Model
        berhasil = self.model.update_anggota(
            id_anggota, nama, alamat, no_hp
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!",
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data anggota.",
            )

    def hapus_anggota(self):
        # Ambil ID anggota yang dipilih
        id_anggota = self.ambil_id_anggota()

        if id_anggota is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!",
            )
            return

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus anggota ini?",
        )

        if not konfirmasi:
            return

        # Hapus melalui Model
        berhasil = self.model.hapus_anggota(id_anggota)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!",
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menghapus data anggota!",
            )

    def run(self):
        self.view.mainloop()