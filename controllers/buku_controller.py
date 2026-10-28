import tkinter.messagebox as messagebox
from buku_model import BukuModel
from config.database import Database
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Menginisialisasi Model dan View
        db_connection = Database().get_connection()
        if db_connection is None:
            raise ConnectionError("Tidak dapat terhubung ke database perpustakaan.")
        
        self.model = BukuModel(db_connection)
        self.view = BukuView()

        # Menyimpan ID buku yang sedang dipilih
        self.selected_id = None

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Binding event klik pada tabel untuk memilih data
        self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_tabel)

        # Memuat data ke tabel saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari database (Model)
        data_buku = self.model.get_semua_buku()

        # Memasukkan data ke dalam tabel GUI
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def isi_form_dari_tabel(self, event):
        # Mengambil baris yang dipilih di tabel
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item)
            values = item_data['values']
            
            if values:
                self.selected_id = values[0]
                # Mengisi form di sebelah kiri dengan data dari tabel
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, values[1])
                
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, values[2])
                
                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, values[3])

    def clear_form(self):
        self.selected_id = None
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.tambah_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def update_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku yang ingin diperbarui dari tabel terlebih dahulu!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_buku(self.selected_id, judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku yang ingin dihapus dari tabel terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            berhasil = self.model.hapus_buku(self.selected_id)

            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.clear_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def run(self):
        self.view.mainloop()