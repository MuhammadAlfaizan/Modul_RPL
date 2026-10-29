#Muhammad Alfaizan_F5212520036
from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            val = (judul, penulis, tahun_terbit)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False
        
    def hapus_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                query = "DELETE FROM buku WHERE id_buku = %s"
                cursor.execute(query, (id_buku,))
                self.conn.commit()

                return cursor.rowcount > 0

            except Exception as e:
                self.conn.rollback()
                print("Error menghapus buku:", e)
                return False

            finally:
                cursor.close()

        return False

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if not self.conn:
            return False

        cursor = self.conn.cursor()

        try:
            query = """
                UPDATE buku
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            cursor.execute(
                query,
                (judul, penulis, tahun_terbit, id_buku)
            )

            jumlah = cursor.rowcount
            self.conn.commit()

            print("Jumlah baris diperbarui:", jumlah)

            # Pastikan buku dengan ID tersebut masih ada
            cursor.execute(
                "SELECT id_buku FROM buku WHERE id_buku = %s",
                (id_buku,)
            )

            ditemukan = cursor.fetchone()

            return ditemukan is not None

        except Exception as e:
            self.conn.rollback()
            print("ERROR UPDATE:", e)
            return False

        finally:
            cursor.close()

   