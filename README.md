# Sistem Manajemen Perpustakaan

Aplikasi desktop manajemen koleksi buku berbasis Python dengan arsitektur
MVC. Antarmuka memakai CustomTkinter dan data disimpan di MySQL.

## Fitur

- Login dengan password terenkripsi SHA-256
- Hak akses berbasis peran: **admin** (petugas) dan **anggota** (mahasiswa)
- Admin: tambah, ubah, dan hapus data buku
- Anggota: hanya melihat daftar buku
- Logout dan kembali ke halaman login

## Struktur Direktori (MVC)

```
Modul 5 RPL/
├── main.py                  # Titik masuk aplikasi
├── requirements.txt         # Daftar dependensi
├── config/
│   └── database.py          # Koneksi MySQL
├── models/                  # Model: akses data
│   ├── user_model.py
│   ├── buku_model.py
│   └── anggota_model.py
├── views/                   # View: tampilan antarmuka
│   ├── login_view.py
│   └── buku_view.py
├── controllers/             # Controller: logika aplikasi
│   ├── auth_controller.py
│   └── buku_controller.py
├── tests/                   # Pengujian otomatis (pytest)
└── .github/workflows/
    └── ci_pipeline.yml      # CI: flake8 + pytest
```

## Instalasi dan Konfigurasi Database

### 1. Prasyarat

- Python 3.10 atau lebih baru
- MySQL Server 8.x (aktif/berjalan)

### 2. Clone dan install dependensi

```bash
git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Buat database dan tabel

Jalankan di MySQL (HeidiSQL, phpMyAdmin, atau MySQL CLI):

```sql
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

CREATE TABLE users (
  id_user INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(50) NOT NULL UNIQUE,
  password VARCHAR(64) NOT NULL,
  role VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_user)
);

CREATE TABLE buku (
  id_buku INT NOT NULL AUTO_INCREMENT,
  judul VARCHAR(100) NOT NULL,
  penulis VARCHAR(100) NOT NULL,
  tahun_terbit YEAR DEFAULT NULL,
  PRIMARY KEY (id_buku)
);

-- Akun awal (password disimpan sebagai hash SHA-256)
INSERT INTO users (username, password, role) VALUES
('petugas', SHA2('GANTI_PASSWORD_ADMIN', 256), 'admin'),
('mahasiswa', SHA2('GANTI_PASSWORD_ANGGOTA', 256), 'anggota');
```

### 4. Konfigurasi koneksi

Sesuaikan host, user, password, dan nama database di
`config/database.py`:

```python
host = "127.0.0.1"
user = "root"
password = "..."
database = "perpustakaan"
```

## Cara Menjalankan Aplikasi

**Dari kode sumber:**

```bash
python main.py
```

**Dari file .exe (tanpa Python):**

1. Pastikan MySQL aktif dan database `perpustakaan` sudah dibuat.
2. Unduh `AplikasiPerpustakaan.exe` dari halaman
   [Releases](../../releases).
3. Jalankan file tersebut, lalu login.

**Build ulang .exe:**

```bash
pyinstaller --onefile --windowed --name AplikasiPerpustakaan --paths . --collect-submodules models --collect-submodules controllers --collect-submodules views --collect-submodules config --collect-all mysql --collect-all customtkinter main.py
```

## Pengujian

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
pytest
```

## Author

Triana (090)
