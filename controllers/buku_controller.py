import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")
        
        # Event binding tombol aksi utama
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # Hubungkan tombol logout ke fungsi logout_app jika ada di view
        if hasattr(self.view, 'btn_logout'):
            self.view.btn_logout.configure(command=self.logout_app)

        # Pembatasan hak akses berbasis peran (RBAC)
        if self.user_role == "anggota":
            # Kunci form input dan tombol simpan khusus admin
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")
            
            # Kunci tombol Perbarui (Update) dan Hapus (Delete)
            if hasattr(self.view, 'btn_update'):
                self.view.btn_update.configure(state="disabled")
            if hasattr(self.view, 'btn_delete'):
                self.view.btn_delete.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def logout_app(self):
        """Fungsi untuk menutup jendela perpustakaan dan kembali ke halaman Login"""
        from controllers.auth_controller import AuthController
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar dari sistem?"):
            self.view.destroy()
            auth_app = AuthController()
            auth_app.run()

    def run(self):
        self.view.mainloop()