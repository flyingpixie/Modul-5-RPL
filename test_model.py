import mysql.connector
from buku_model import BukuModel
from models.anggota_model import AnggotaModel

# Koneksi ke database MySQL Laragon (menggunakan nama baru: perpustakaan)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)

# --- PENGUJIAN BUKU ---
buku_model = BukuModel(db)

print("=== Menambahkan Buku ===")
buku_model.tambah_buku("Belajar Python", "Guido van Rossum", 2024)
buku_model.tambah_buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)
buku_model.tambah_buku("Filosofi Teras", "Henry Manampiring", 2018)
buku_model.tambah_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)

print("\n=== Daftar Buku ===")
for b in buku_model.get_semua_buku():
    print(f"[{b['id_buku']}] {b['judul']} - {b['penulis']} ({b['tahun_terbit']})")

print("\n=== Update Buku ===")
buku_model.update_buku(4, "Pemrograman Python MVC", "Guido van Rossum", 2023)

print("\n=== Data Setelah Update ===")
for b in buku_model.get_semua_buku():
    print(f"[{b['id_buku']}] {b['judul']} - {b['penulis']} ({b['tahun_terbit']})")

print("\n=== Delete Buku ===")
buku_model.delete_buku(4)  # Menghapus buku ID 4

print("\n=== Data Setelah Delete ===")
for b in buku_model.get_semua_buku():
    print(f"[{b['id_buku']}] {b['judul']} - {b['penulis']} ({b['tahun_terbit']})")


# --- PENGUJIAN ANGGOTA ---
anggota_model = AnggotaModel(db)

print("\n=== Menambahkan Anggota ===")
data_anggota = [
    (1, "Triana", "jl.Lengaru"),
    (2, "Melani", "Per.Huntap"),
    (3, "Aqilah", "jl.Karajahlemba"),
    (4, "Alfaira", "jl.Soeprapto"),
    (5, "Fila", "Tinggede")
]

for id_agt, nama, alamat in data_anggota:
    try:
        anggota_model.tambah_anggota(id_agt, nama, alamat)
    except Exception:
        pass  # Mengantisipasi jika data ID anggota sudah ada sebelumnya di database

print("\n=== Daftar Anggota ===")
for a in anggota_model.get_semua_anggota():
    print(f"[{a['id_anggota']}] {a['nama']} - {a['alamat']}")

db.close()