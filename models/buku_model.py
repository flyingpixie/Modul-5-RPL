from config.database import Database


class BukuModel:
    def __init__(self, db_connection=None):
        self._db_instance = None
        if db_connection is None:
            self._db_instance = Database()
            self.db = self._db_instance.get_connection()
        else:
            self.db = db_connection
        self.table_name = "buku"

    def _pastikan_koneksi(self):
        """Memastikan koneksi aktif; mencoba menyambung ulang bila perlu."""
        try:
            if self.db is not None and self.db.is_connected():
                return True
        except Exception:
            pass
        if self._db_instance is not None:
            self.db = self._db_instance.get_connection()
        return self.db is not None

    def get_all_buku(self):
        if not self._pastikan_koneksi():
            return []
        cursor = self.db.cursor(dictionary=True)
        try:
            cursor.execute(
                f"SELECT * FROM {self.table_name} ORDER BY id_buku"
            )
            return cursor.fetchall()
        finally:
            cursor.close()

    def get_semua_buku(self):
        # Alias agar kompatibel dengan pemanggilan test_model.py
        return self.get_all_buku()

    def create_buku(self, judul, penulis, tahun_terbit):
        if not self._pastikan_koneksi():
            return False
        cursor = self.db.cursor()
        try:
            query = (
                f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) "
                "VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (judul, penulis, int(tahun_terbit)))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error tambah buku: {e}")
            self.db.rollback()
            return False
        finally:
            cursor.close()

    def tambah_buku(self, judul, penulis, tahun_terbit):
        # Alias nama lama
        return self.create_buku(judul, penulis, tahun_terbit)

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if not self._pastikan_koneksi():
            return False
        cursor = self.db.cursor()
        try:
            query = (
                f"UPDATE {self.table_name} "
                "SET judul = %s, penulis = %s, tahun_terbit = %s "
                "WHERE id_buku = %s"
            )
            cursor.execute(query, (judul, penulis, int(tahun_terbit), id_buku))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error update buku: {e}")
            self.db.rollback()
            return False
        finally:
            cursor.close()

    def delete_buku(self, id_buku):
        if not self._pastikan_koneksi():
            return False
        cursor = self.db.cursor()
        try:
            query = f"DELETE FROM {self.table_name} WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error hapus buku: {e}")
            self.db.rollback()
            return False
        finally:
            cursor.close()

    def hapus_buku(self, id_buku):
        # Alias nama lama
        return self.delete_buku(id_buku)