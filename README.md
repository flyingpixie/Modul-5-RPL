# 📚 Sistem Manajemen Perpustakaan (Library Management System)

Aplikasi desktop berbasis Python yang menggunakan arsitektur **Model-View-Controller (MVC)**, antarmuka grafis **CustomTkinter**, basis data **MySQL**, serta dilengkapi dengan otomasi pengujian dan CI/CD menggunakan **GitHub Actions**.

---

## 🚀 Fitur Utama

1. **Autentikasi & RBAC (Role-Based Access Control)**:
   - **Admin**: Mengelola data buku, data anggota, dan kontrol sistem penuh.
   - **Anggota**: Melakukan pencarian dan peminjaman buku.
   - Menggunakan enkripsi kata sandi **SHA-256** untuk keamanan akun.
2. **Manajemen Buku & Anggota**: Tambah, ubah, hapus, dan tampilkan data secara _real-time_ terhubung ke database MySQL.
3. **Automated CI/CD Pipeline**: Pengujian otomatis menggunakan `pytest` dan pengecekan kualitas kode (`flake8`) di GitHub Actions.

---

## 🛠️ Prasyarat (Requirements)

- Python versi 3.11 atau yang lebih baru.
- Laragon / MySQL Server aktif di komputer lokal.
- Pustaka Python terdaftar di `requirements.txt`.

---

## ⚙️ Cara Instalasi & Menjalankan Proyek

1. **Clone Repositori**:
   ```bash
   git clone [https://github.com/flyingpixie/Modul-5-RPL.git](https://github.com/flyingpixie/Modul-5-RPL.git)
   cd Modul-5-RPL
   ```
