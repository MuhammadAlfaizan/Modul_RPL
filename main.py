# print("=== Kalkulator Terminal Modul 3 ===")
# angka1 = float(input("Masukkan angka pertama: "))
# angka2 = float(input("Masukkan angka kedua: "))
# hasil = angka1 + angka2

# print(f"Status: Setup Berhasil!")
# print(f"Hasil Penjumlahan: {hasil}")
# print('Muhammad Alfaizan (036)')
# #Muhammad Alfaizan Rifatullah (036)

#Muhammad Alfaizan_F5212520036
from controllers.buku_controller import BukuController

if __name__ == "__main__":
    app = BukuController()
    app.run()