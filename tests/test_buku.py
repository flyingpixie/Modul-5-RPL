from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # 1. Buat mock untuk koneksi database
    mock_db = MagicMock()
    
    # 2. Inisialisasi BukuModel dan set atribut self.db ke mock_db sesuai buku_model.py
    model = BukuModel()
    model.db = mock_db  
    
    # 3. Buat mock untuk cursor
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor

    # 4. Eksekusi fungsi tambah buku
    hasil = model.tambah_buku("Buku Testing", "Penulis QA", 2026)

    # 5. Verifikasi hasil dan pemanggilan fungsi database
    assert hasil is True
    mock_cursor.execute.assert_called_once()
    mock_db.commit.assert_called_once()