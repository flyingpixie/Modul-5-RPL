class BukuModel:
    def __init__(self, db_connection):
        self.db = db_connection

    def get_semua_buku(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buku")
        result = cursor.fetchall()
        cursor.close()
        return result

    def tambah_buku(self, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        cursor.execute(query, (judul, penulis, tahun_terbit))
        self.db.commit()
        cursor.close()
        return True

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        query = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
        cursor.execute(query, (judul, penulis, tahun_terbit, id_buku))
        self.db.commit()
        cursor.close()
        return True

    def hapus_buku(self, id_buku):
        cursor = self.db.cursor()
        query = "DELETE FROM buku WHERE id_buku = %s"
        cursor.execute(query, (id_buku,))
        self.db.commit()
        cursor.close()
        return True