import mysql.connector
from models.buku_model import BukuModel

# Koneksi ke database MySQL Laragon
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)

# --- PENGUJIAN BUKU ---
buku_model = BukuModel()

print("=== Menambahkan Buku ===")
buku_model.create_buku("Belajar Python", "Penulis A", 2024)
buku_model.create_buku("Bumi Manusia", "Pramoedya", 2005)
buku_model.create_buku("Filosofi Teras", "Henry Manampiring", 2019)
buku_model.create_buku("Pemrograman Web", "Penulis B", 2023)

print("\n=== Daftar Buku ===")
# Sesuaikan nama fungsi dengan yang ada di BukuModel Anda (misal: get_all_buku)
data_buku = buku_model.get_all_buku()
for b in data_buku:
    print(f"[{b['id_buku']}] {b['judul']} - {b['penulis']} ({b['tahun_terbit']})")

print("\n=== Selesai ===")