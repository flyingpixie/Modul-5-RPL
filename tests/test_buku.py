from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model dengan memberikan argumen mock koneksi
    mock_db = MagicMock()
    model = BukuModel()
    model.conn = mock_db  # Menyesuaikan dengan inisialisasi koneksi di BukuModel Anda

    # Memanipulasi (Mock) cursor database agar tidak mengotori data asli
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    # Gunakan nama fungsi yang benar sesuai buku_model.py Anda (misal: tambah_buku)
    hasil = model.tambah_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True (atau sesuaikan dengan return model Anda)
    assert hasil is not None
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    mock_db.commit.assert_called_once()