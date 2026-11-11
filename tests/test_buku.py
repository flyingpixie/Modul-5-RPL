from unittest.mock import MagicMock, patch
from models.buku_model import BukuModel

@patch('models.buku_model.mysql.connector.connect')
def test_create_buku_berhasil(mock_connect):
    # Membuat mock untuk koneksi dan cursor database
    mock_db = MagicMock()
    mock_cursor = MagicMock()
    
    mock_connect.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor

    # Inisialisasi model (koneksi otomatis akan ditangkap oleh patch)
    model = BukuModel()

    # Eksekusi fungsi tambah buku
    hasil = model.tambah_buku("Buku Testing", "Penulis QA", 2026)

    # Verifikasi hasil dan pemanggilan fungsi database
    assert hasil is True
    mock_cursor.execute.assert_called_once()
    mock_db.commit.assert_called_once()