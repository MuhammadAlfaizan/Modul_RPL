# Muhammad Alfaizan_F5212520036
from config.database import Database


class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name}
                (nama, alamat)
                VALUES (%s, %s)
            """

            val = (nama, alamat)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True

        return False

    def hapus_anggota(self, id_anggota):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                query = """
                    DELETE FROM anggota
                    WHERE id_anggota = %s
                """
                cursor.execute(query, (id_anggota,))
                self.conn.commit()

                return cursor.rowcount > 0

            except Exception as e:
                self.conn.rollback()
                print("Error menghapus anggota:", e)
                return False

            finally:
                cursor.close()

        return False

    def update_anggota(self, id_anggota, nama, alamat):
        if not self.conn:
            return False

        cursor = self.conn.cursor()

        try:
            query = """
                UPDATE anggota
                SET nama = %s,
                    alamat = %s
                WHERE id_anggota = %s
            """

            cursor.execute(
                query,
                (nama, alamat, id_anggota)
            )

            self.conn.commit()

            cursor.execute(
                "SELECT id_anggota FROM anggota WHERE id_anggota = %s",
                (id_anggota,)
            )

            ditemukan = cursor.fetchone()
            return ditemukan is not None

        except Exception as e:
            self.conn.rollback()
            print("ERROR UPDATE ANGGOTA:", e)
            return False

        finally:
            cursor.close()