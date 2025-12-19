# Aplikasi Manajemen Matakuliah Berbasis Pyramid

Proyek ini merupakan REST API sederhana untuk mengelola data Matakuliah menggunakan framework **Pyramid**. Sistem mendukung operasi **CRUD** (Create, Read, Update, Delete) dan menggunakan **PostgreSQL** sebagai database utama.

---

## 🚀 Panduan Instalasi

Berikut langkah lengkap untuk menyiapkan dan menjalankan aplikasi di lingkungan lokal.

### 1. Membuat Virtual Environment

Pastikan Python 3.10+ telah terpasang.

```bash
python -m venv venv
```

Aktifkan venv:

```bash
# Windows CMD
venv\Scripts\activate

# Git Bash
source venv/Scripts/activate

# Linux/MacOS
source venv/bin/activate
```

Perbarui pip:

```bash
python -m pip install --upgrade pip
```

### 2. Menginstall Dependensi

```bash
pip install -e ".[testing]"
```

### 3. Konfigurasi Database PostgreSQL

#### a. Membuat Database Baru

```bash
createdb -U postgres pyramid_matakuliah
```

Atau melalui psql:

```bash
psql -U postgres
CREATE DATABASE pyramid_matakuliah;
\q
```

#### b. Mengatur Connection String

Edit `development.ini`:

```ini
sqlalchemy.url = postgresql://user_matakuliah:pass_matakuliah@localhost:5432/pyramid_matakuliah
```

Sesuaikan `alembic.ini` juga:

```ini
sqlalchemy.url = postgresql://user_matakuliah:pass_matakuliah@localhost:5432/pyramid_matakuliah
```

> Gunakan username/password PostgreSQL Anda sendiri.

---

## 🏃 Menjalankan Aplikasi

### 1. Migrasi Database

```bash
alembic upgrade head
```

Atau:

```bash
initialize_pyramid_matakuliah_db development.ini
```

### 2. Menjalankan Server

```bash
pserve development.ini
```

Server berjalan di:

```
http://localhost:6543
```

---

## 📡 Dokumentasi API

Berikut daftar endpoint yang tersedia.

### 1. GET Semua Matakuliah

```bash
curl -X GET http://localhost:6543/api/matakuliah
```

### 2. GET Matakuliah Berdasarkan ID

```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```

### 3. POST Tambah Matakuliah

```bash
curl -X POST http://localhost:6543/api/matakuliah \
-H "Content-Type: application/json" \
-d '{"kode_mk":"IF104","nama_mk":"Pemrograman Web","sks":3,"semester":4}'
```

### 4. PUT Update Matakuliah

```bash
curl -X PUT http://localhost:6543/api/matakuliah/4 \
-H "Content-Type: application/json" \
-d '{"nama_mk":"Pemrograman Aplikasi Web","sks":5}'
```

### 5. DELETE Matakuliah

```bash
curl -X DELETE http://localhost:6543/api/matakuliah/2
```

---

## 🧪 Pengujian API

Pengujian bisa dilakukan menggunakan **cURL** atau **Postman**. Semua contoh perintah sudah disertakan untuk memudahkan proses testing.

---

## 🗄️ Struktur Tabel Matakuliah

| Kolom    | Tipe    | Constraint       | Keterangan           |
| -------- | ------- | ---------------- | -------------------- |
| id       | Integer | Primary Key      | Auto increment       |
| kode_mk  | Text    | Unique, Not Null | Kode mata kuliah     |
| nama_mk  | Text    | Not Null         | Nama mata kuliah     |
| sks      | Integer | Not Null         | Jumlah SKS           |
| semester | Integer | Not Null         | Semester pengambilan |

---

## 🔧 Masalah Umum & Solusinya

### Kendala Koneksi Database

Pastikan:

* PostgreSQL aktif
* Username/password benar
* Port 5432 tidak digunakan proses lain

### Error Migrasi Alembic

```bash
alembic downgrade base
alembic upgrade head
```

### Port 6543 Bentrok

Ubah `development.ini`:

```ini
listen = localhost:6544
```

---

## 👨‍💻 Pengembang

* **Nama:** Pradana Figo Ariasya
* **NIM:** 123140063
* **Kelas:** Pertemuan 6



