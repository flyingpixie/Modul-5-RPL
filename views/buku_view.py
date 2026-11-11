import customtkinter as ctk
from tkinter import ttk

# Mengatur tema tampilan aplikasi menjadi warna putih (Light Mode)
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("850x550")
        self.resizable(False, False)

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ---------- FRAME KIRI: FORMULIR INPUT BUKU & TOMBOL AKSI ----------
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kiri, text="Form Data Buku", font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Komponen Input
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Judul Buku"
        )
        self.entry_judul.pack(pady=8, padx=15, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Nama Penulis"
        )
        self.entry_penulis.pack(pady=8, padx=15, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Tahun Terbit (Misal: 2024)"
        )
        self.entry_tahun.pack(pady=8, padx=15, fill="x")

        # Tombol Aksi (Simpan, Update, Delete)
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri, text="Simpan Data",
            fg_color="green", hover_color="darkgreen"
        )
        self.btn_simpan.pack(pady=10, padx=15, fill="x")

        self.btn_update = ctk.CTkButton(
            self.frame_kiri, text="Perbarui Data (Update)",
            fg_color="blue", hover_color="darkblue"
        )
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(
            self.frame_kiri, text="Hapus Data (Delete)",
            fg_color="red", hover_color="darkred"
        )
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri, text="Logout",
            fg_color="gray", hover_color="darkgray"
        )
        self.btn_logout.pack(pady=15, padx=15, fill="x")

        # ---------- FRAME KANAN: TABEL DAFTAR BUKU ----------
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kanan, text="Daftar Koleksi Buku Triana.090",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Gaya tabel
        style = ttk.Style()
        style.configure("Treeview", rowheight=26, font=("Arial", 10))
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

        # Wadah tabel + scrollbar
        wadah_tabel = ctk.CTkFrame(self.frame_kanan, fg_color="transparent")
        wadah_tabel.pack(fill="both", expand=True, padx=15, pady=10)

        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(
            wadah_tabel, columns=kolom, show="headings",
            height=18, selectmode="browse"
        )

        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")

        self.tabel.column("id", width=40, anchor="center", stretch=False)
        self.tabel.column("judul", width=160)
        self.tabel.column("penulis", width=130)
        self.tabel.column("tahun", width=60, anchor="center", stretch=False)

        scrollbar = ttk.Scrollbar(
            wadah_tabel, orient="vertical", command=self.tabel.yview
        )
        self.tabel.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tabel.pack(side="left", fill="both", expand=True)


if __name__ == "__main__":
    app = BukuView()
    app.mainloop()