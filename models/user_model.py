import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Enkripsi password mentah menjadi SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def _pastikan_koneksi(self):
        """Memastikan koneksi aktif; mencoba menyambung ulang bila perlu."""
        try:
            if self.conn is not None and self.conn.is_connected():
                return True
        except Exception:
            pass
        self.conn = self.db.get_connection()
        return self.conn is not None

    def autentikasi(self, username, password):
        if not self._pastikan_koneksi():
            raise ConnectionError("Tidak dapat terhubung ke database.")

        cursor = self.conn.cursor(dictionary=True)
        try:
            password_hash = self.hash_password(password)
            query = (
                f"SELECT id_user, username, role FROM {self.table_name} "
                "WHERE username = %s AND password = %s"
            )
            cursor.execute(query, (username, password_hash))
            return cursor.fetchone()
        finally:
            cursor.close()

    def register_user(self, username, password, role='anggota'):
        """Menambahkan akun baru dengan password terenkripsi SHA-256."""
        if not self._pastikan_koneksi():
            print("Error registrasi: tidak dapat terhubung ke database.")
            return False

        cursor = self.conn.cursor()
        try:
            password_hash = self.hash_password(password)
            query = (
                f"INSERT INTO {self.table_name} (username, password, role) "
                "VALUES (%s, %s, %s)"
            )
            cursor.execute(query, (username, password_hash, role))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error registrasi: {e}")
            return False
        finally:
            cursor.close()