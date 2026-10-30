# Sistem Manajemen Perpustakaan

## 1. Deskripsi Aplikasi

Sistem Manajemen Perpustakaan merupakan aplikasi desktop berbasis Python yang digunakan untuk membantu pengelolaan data buku dan pengguna perpustakaan. Aplikasi ini menggunakan CustomTkinter sebagai antarmuka grafis dan MySQL sebagai sistem manajemen basis data.

Aplikasi dikembangkan dengan menerapkan pola arsitektur Model-View-Controller (MVC) untuk memisahkan logika pengolahan data, tampilan antarmuka, dan pengendalian alur aplikasi.

### Fitur Utama

- Login dan autentikasi pengguna.
- Registrasi akun pengguna.
- Pengelolaan data buku.
- Menambahkan data buku.
- Mengubah data buku.
- Menghapus data buku.
- Menampilkan daftar buku dari database.
- Penyimpanan password dalam bentuk hash SHA-256.
- Pengujian otomatis menggunakan pytest.
- Pemeriksaan kualitas kode menggunakan flake8 melalui GitHub Actions CI Pipeline.

## 2. Struktur Direktori MVC

Struktur direktori proyek disusun sebagai berikut:

```text
Modul 3/
├── config/
│   └── database.py
├── models/
│   ├── __init__.py
│   ├── user_model.py
│   └── buku_model.py
├── views/
│   ├── __init__.py
│   ├── login_view.py
│   └── buku_view.py
├── controllers/
│   ├── __init__.py
│   ├── login_controller.py
│   └── buku_controller.py
├── tests/
│   └── test_buku.py
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml
├── requirements.txt
└── README.md
```

*Catatan: Struktur di atas merupakan contoh. Sesuaikan nama file dan folder dengan struktur proyek yang sebenarnya.*

### Penjelasan MVC

**1. Model (`models/`)**

Model bertanggung jawab mengelola data dan berinteraksi dengan database MySQL.

Contoh:
- `user_model.py`: mengelola data pengguna, autentikasi, registrasi, dan hashing password.
- `buku_model.py`: mengelola operasi data buku, seperti menambah, menampilkan, memperbarui, dan menghapus data.

**2. View (`views/`)**

View bertanggung jawab menampilkan antarmuka grafis kepada pengguna menggunakan CustomTkinter.

Contoh:
- `login_view.py`: menampilkan halaman login dan registrasi.
- `buku_view.py`: menampilkan formulir input dan tabel daftar buku.

**3. Controller (`controllers/`)**

Controller menghubungkan View dengan Model. Controller menerima interaksi pengguna, memanggil metode Model, dan memperbarui tampilan berdasarkan hasil operasi.

Contoh:
- `login_controller.py`: menangani proses login dan registrasi.
- `buku_controller.py`: menangani interaksi formulir buku dengan operasi database.

**4. Config (`config/`)**

Folder ini berisi konfigurasi aplikasi, termasuk koneksi ke database MySQL melalui `database.py`.

**5. Tests (`tests/`)**

Folder ini menyimpan pengujian otomatis untuk memeriksa fungsi aplikasi menggunakan pytest.

**6. GitHub Actions (`.github/workflows/`)**

Folder ini berisi konfigurasi CI Pipeline untuk menjalankan pemeriksaan kode dengan flake8 dan pengujian otomatis menggunakan pytest.

## 3. Persyaratan Sistem

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki:

- Python 3.10 atau versi yang sesuai dengan proyek.
- MySQL Server atau MariaDB.
- pip untuk menginstal pustaka Python.
- Git untuk mengambil atau memperbarui kode proyek.
- Visual Studio Code atau editor kode lainnya (opsional).

## 4. Panduan Instalasi

### 4.1. Mengunduh Proyek

Jika proyek sudah tersedia di komputer, buka terminal pada root direktori proyek.

Jika ingin mengunduh dari GitHub, jalankan:

```bash
git clone <URL_REPOSITORI_GITHUB>
cd <NAMA_FOLDER_PROYEK>
```

Ganti placeholder dengan URL repositori dan nama folder proyek yang sebenarnya.

### 4.2. Membuat Virtual Environment

Buat lingkungan virtual Python agar pustaka proyek terpisah dari instalasi Python utama.

Windows:

```bash
python -m venv env
```

Aktifkan virtual environment melalui Command Prompt:

```bat
env\Scripts\activate.bat
```

Jika menggunakan PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

### 4.3. Menginstal Dependensi

Pastikan virtual environment sudah aktif, kemudian jalankan:

```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum berisi semua dependensi yang diperlukan, instal pustaka yang digunakan proyek, misalnya:

```bash
pip install customtkinter mysql-connector-python pytest flake8
```

Pastikan nama paket sesuai dengan import yang digunakan dalam kode proyek.

## 5. Konfigurasi Database MySQL

### 5.1. Menjalankan MySQL

Jalankan MySQL Server melalui layanan yang digunakan, misalnya Laragon atau XAMPP.

Pastikan layanan MySQL aktif sebelum menjalankan aplikasi.

### 5.2. Membuat Database

Buka phpMyAdmin atau MySQL client, kemudian jalankan SQL berikut:

```sql
CREATE DATABASE db_perpustakaan;
```

Pilih database yang telah dibuat:

```sql
USE db_perpustakaan;
```

Buat tabel pengguna sesuai dengan kolom yang digunakan oleh `UserModel`:

```sql
CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password CHAR(64) NOT NULL,
    role VARCHAR(20) NOT NULL
);
```

Tipe `CHAR(64)` digunakan untuk menyimpan hasil hash SHA-256 dalam format heksadesimal.

Buat tabel buku sesuai dengan kebutuhan `BukuModel`. Contoh struktur dasar:

```sql
CREATE TABLE buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(150) NOT NULL,
    tahun INT NOT NULL
);
```

*Catatan: Sesuaikan nama tabel dan kolom dengan query yang digunakan dalam Model proyek. Jika tabel buku atau pengguna sudah tersedia, tidak perlu membuatnya kembali.*

### 5.3. Mengatur Koneksi Database

Buka file `config/database.py` dan pastikan konfigurasi koneksi menggunakan alamat server, nama database, username, dan password MySQL yang benar.

Contoh menggunakan `mysql-connector-python`:

```python
import mysql.connector

class Database:
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="db_perpustakaan"
            )
            return connection
        except mysql.connector.Error as error:
            print(f"Koneksi database gagal: {error}")
            return None
```

Contoh tersebut mengasumsikan MySQL berjalan pada komputer lokal dengan pengguna `root` tanpa password. Sesuaikan nilainya dengan konfigurasi MySQL di perangkat masing-masing.

Untuk penggunaan nyata, hindari menyimpan kredensial sensitif langsung di dalam kode sumber.

## 6. Cara Menjalankan Aplikasi

### 6.1. Mengaktifkan Virtual Environment

Jika belum aktif, jalankan:

```powershell
.\env\Scripts\Activate.ps1
```

### 6.2. Menjalankan Aplikasi

Jalankan file utama aplikasi dari root direktori proyek.

Contoh jika file utama bernama `main.py`:

```bash
python main.py
```

Jika belum ada `main.py`, jalankan file utama yang menginisialisasi aplikasi dan membuka halaman login.

Pastikan koneksi MySQL sudah aktif sebelum menjalankan aplikasi.

### 6.3. Menggunakan Aplikasi

1. Jalankan aplikasi.
2. Masukkan username dan password pada halaman login.
3. Jika belum memiliki akun, gunakan fitur registrasi jika tersedia.
4. Setelah autentikasi berhasil, aplikasi membuka halaman pengelolaan buku.
5. Gunakan formulir untuk menambahkan data buku.
6. Pilih data pada tabel untuk melakukan perubahan atau penghapusan sesuai implementasi aplikasi.
7. Gunakan tombol Logout untuk kembali ke halaman login jika fitur tersebut telah diintegrasikan.

## 7. Pengujian Otomatis

Pengujian dilakukan menggunakan pytest.

Jalankan seluruh pengujian dengan perintah:

```bash
pytest
```

Untuk menjalankan pengujian pada file tertentu:

```bash
pytest tests/test_buku.py
```

Pastikan seluruh pengujian menunjukkan status passed sebelum perubahan dikirim ke repositori.

## 8. Pemeriksaan Kualitas Kode

Proyek menggunakan flake8 untuk memeriksa kategori kesalahan kode tertentu pada folder `models/` dan `controllers/`.

Jalankan perintah berikut:

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Pemeriksaan yang sama dijalankan melalui GitHub Actions CI Pipeline sebelum langkah pengujian pytest.

## 9. Kontribusi dan Pengembangan

Pengembangan aplikasi dapat dilakukan dengan memperbaiki fitur yang tersedia, menambahkan fungsi baru, dan meningkatkan kualitas kode. Setiap perubahan sebaiknya diuji terlebih dahulu sebelum dikirim ke repositori GitHub.

## 10. Teknologi yang Digunakan

- Python: bahasa pemrograman utama.
- CustomTkinter: pustaka antarmuka grafis.
- MySQL: sistem manajemen basis data.
- mysql-connector-python: penghubung Python dengan MySQL.
- pytest: pengujian otomatis.
- flake8: pemeriksaan kualitas kode.
- Git dan GitHub: pengelolaan versi dan repositori.
- GitHub Actions: otomatisasi CI Pipeline.
