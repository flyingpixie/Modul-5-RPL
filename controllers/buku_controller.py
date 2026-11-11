import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = (user_role or "anggota").strip().lower()
        self.id_terpilih = None
        self.model = BukuModel()
        self.view = BukuView()
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Tombol logout tersedia untuk semua peran
        if hasattr(self.view, 'btn_logout'):
            self.view.btn_logout.configure(command=self.logout_app)

        if self.user_role == "admin":
            # Admin: semua fitur aktif
            self.view.btn_simpan.configure(command=self.simpan_data)
            if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(command=self.update_data)
            if hasattr(self.view, 'btn_delete'):
                self.view.btn_delete.configure(command=self.hapus_data)
            # Klik baris tabel -> isi form otomatis
            self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)
        else:
            # Anggota: hanya melihat data (RBAC)
            self.view.btn_simpan.configure(
                state="disabled", text="Akses Terkunci (Khusus Admin)"
            )
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(state="disabled")
            if hasattr(self.view, 'btn_delete'):
                self.view.btn_delete.configure(state="disabled")

        self.muat_data_tabel()

    # ---------- Helper ----------
    def _ambil_input(self):
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()
        return judul, penulis, tahun

    def _validasi(self, judul, penulis, tahun):
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return False
        if not tahun.isdigit() or len(tahun) != 4:
            messagebox.showwarning(
                "Peringatan", "Tahun terbit harus 4 digit angka, misal 2024."
            )
            return False
        if not (1901 <= int(tahun) <= 2155):
            messagebox.showwarning(
                "Peringatan", "Tahun terbit harus antara 1901 sampai 2155."
            )
            return False
        if len(judul) > 100 or len(penulis) > 100:
            messagebox.showwarning(
                "Peringatan", "Judul dan penulis maksimal 100 karakter."
            )
            return False
        return True

    def _kosongkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.id_terpilih = None
        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def _cek_admin(self, aksi):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak", f"Anda tidak memiliki izin untuk {aksi} data!"
            )
            return False
        return True

    # ---------- Tabel ----------
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert(
                "", "end",
                values=(
                    buku['id_buku'], buku['judul'],
                    buku['penulis'], buku['tahun_terbit']
                )
            )

    def pilih_baris(self, event=None):
        terpilih = self.view.tabel.selection()
        if not terpilih:
            return
        nilai = self.view.tabel.item(terpilih[0], "values")
        self.id_terpilih = nilai[0]

        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')
        self.view.entry_judul.insert(0, nilai[1])
        self.view.entry_penulis.insert(0, nilai[2])
        self.view.entry_tahun.insert(0, nilai[3])

    # ---------- CRUD ----------
    def simpan_data(self):
        if not self._cek_admin("menambah"):
            return

        judul, penulis, tahun = self._ambil_input()
        if not self._validasi(judul, penulis, tahun):
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def update_data(self):
        if not self._cek_admin("memperbarui"):
            return

        if not self.id_terpilih:
            messagebox.showwarning(
                "Peringatan", "Pilih dulu buku di tabel yang ingin diperbarui!"
            )
            return

        judul, penulis, tahun = self._ambil_input()
        if not self._validasi(judul, penulis, tahun):
            return

        if not hasattr(self.model, "update_buku"):
            messagebox.showerror("Error", "Method update_buku belum ada di BukuModel.")
            return

        if self.model.update_buku(self.id_terpilih, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if not self._cek_admin("menghapus"):
            return

        if not self.id_terpilih:
            messagebox.showwarning(
                "Peringatan", "Pilih dulu buku di tabel yang ingin dihapus!"
            )
            return

        if not hasattr(self.model, "delete_buku"):
            messagebox.showerror("Error", "Method delete_buku belum ada di BukuModel.")
            return

        if not messagebox.askyesno("Konfirmasi Hapus", "Yakin ingin menghapus buku ini?"):
            return

        if self.model.delete_buku(self.id_terpilih):
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
            self._kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menghapus data.")

    # ---------- Logout & run ----------
    def logout_app(self):
        """Menutup jendela perpustakaan dan kembali ke halaman Login."""
        from controllers.auth_controller import AuthController
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar dari sistem?"):
            self.view.destroy()
            auth_app = AuthController()
            auth_app.run()

    def run(self):
        self.view.mainloop()