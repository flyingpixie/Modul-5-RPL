from unittest.mock import MagicMock
from buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model dengan memberikan argumen mock koneksi
    mock_db = MagicMock()
    model = BukuModel(mock_db)

    # Memanipulasi (Mock) cursor database agar tidak mengotori data asli
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi (ubah ke tambah_buku jika fungsi di model Anda bernama demikian)
    hasil = model.tambah_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    mock_db.commit.assert_called_once()