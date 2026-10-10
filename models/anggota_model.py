class AnggotaModel:
    def __init__(self, db_connection):
        self.db = db_connection

    def tambah_anggota(self, id_anggota, nama, alamat):
        cursor = self.db.cursor()
        query = "INSERT INTO anggota (id_anggota, nama, alamat) VALUES (%s, %s, %s)"
        cursor.execute(query, (id_anggota, nama, alamat))
        self.db.commit()
        cursor.close()
        print("Data anggota berhasil ditambahkan!")

    def get_semua_anggota(self):
        cursor = self.db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        result = cursor.fetchall()
        cursor.close()
        return result