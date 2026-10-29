from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku():
    # Inisialisasi Model
    model = BukuModel()

    # Mock koneksi database
    model.conn = MagicMock()

    # Data buku simulasi
    data_buku = [
        {
            "id_buku": 1,
            "judul": "Pemrograman Python",
            "penulis": "Alfaizan",
            "tahun_terbit": 2025
        },
        {
            "id_buku": 2,
            "judul": "Basis Data",
            "penulis": "Budi",
            "tahun_terbit": 2024
        }
    ]

    # Mock cursor dan hasil query
    cursor_mock = MagicMock()
    model.conn.cursor.return_value = cursor_mock
    cursor_mock.fetchall.return_value = data_buku

    # Jalankan fungsi yang diuji
    hasil = model.get_all_buku()

    # Validasi hasil
    assert hasil == data_buku
    assert len(hasil) == 2

    # Pastikan query dijalankan
    cursor_mock.execute.assert_called_once_with(
        "SELECT * FROM buku"
    )

    # Pastikan cursor ditutup
    cursor_mock.close.assert_called_once()
