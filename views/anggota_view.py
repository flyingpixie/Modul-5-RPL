import customtkinter as ctk
from tkinter import ttk

# Mengatur tema tampilan aplikasi menjadi warna putih (Light Mode)views/anggota_view.py
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("850x520")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota Triana.090", font=("Arial", 16, "bold")).pack(pady=20)

        # Komponen Input Form Anggota
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota", height=35)
        self.entry_nama.pack(pady=10, padx=20, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat", height=35)
        self.entry_alamat.pack(pady=10, padx=20, fill="x")

        # Tombol Aksi (Simpan, Update, Delete)
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green", hover_color="darkgreen", height=38)
        self.btn_simpan.pack(pady=10, padx=20, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue", hover_color="darkblue", height=38)
        self.btn_update.pack(pady=10, padx=20, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red", hover_color="darkred", height=38)
        self.btn_delete.pack(pady=10, padx=20, fill="x")

        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan 084", font=("Arial", 16, "bold")).pack(pady=20)

        # Komponen Tabel (Treeview)
        kolom_anggota = ("id", "nama", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom_anggota, show="headings", height=15)

        # Konfigurasi Header Tabel
        self.tabel.heading("id", text="ID")
        self.tabel.heading("nama", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        # Konfigurasi Lebar & Posisi Kolom Tabel
        self.tabel.column("id", width=50, anchor="center")
        self.tabel.column("nama", width=160, anchor="w")
        self.tabel.column("alamat", width=200, anchor="w")

        self.tabel.pack(fill="both", expand=True, padx=20, pady=10)

        # Contoh data statis sesuai gambar contoh
        data_contoh = [
            (1, "Bino", "Jl. Merdeka No. 10"),
            (2, "Melani", "Jl. Mawar No. 4"),
            (3, "Kiara", "Jl. Diponegoro No. 25"),
            (4, "Mario Win", "Jl. Untad 1")
        ]
        for row in data_contoh:
            self.tabel.insert("", "end", values=row)

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()