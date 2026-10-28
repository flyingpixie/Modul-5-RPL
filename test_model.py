import mysql.connector
from buku_model import BukuModel
from models.anggota_model import AnggotaModel

# Koneksi ke database MySQL Laragon
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)

# --- PENGUJIAN BUKU ---
buku_model = BukuModel(db)

print("=== Menambahkan Buku ===")
buku_model.tambah_buku("Belajar Python", "Penulis A", 2024)
buku_model.tambah_buku("Bumi Manusia", "Pramoedya", 2005)
buku_model.tambah_buku("Filosofi Teras", "Henry Manampiring", 2019)
buku_model.tambah_buku("Pemrograman Web", "Penulis B", 2023)

print("\n=== Daftar Buku ===")
# Ubah get_all_buku menjadi get_semua_buku
data_buku = buku_model.get_semua_buku()
for b in data_buku:
    print(f"[{b['id_buku']}] {b['judul']} - {b['penulis']} ({b['tahun_terbit']})")

print("\n=== Selesai ===")