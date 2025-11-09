# Sistem Manajemen Perpustakaan Sederhana (OOP Python)

Proyek ini adalah implementasi sistem manajemen perpustakaan sederhana berbasis konsol (CLI) yang ditulis dalam Python. Program ini dibuat untuk memenuhi tugas praktikum Pemrograman Berorientasi Objek (OOP).

Fokus utama program ini adalah untuk menerapkan 4 pilar utama OOP: **Inheritance**, **Encapsulation**, **Polymorphism**, dan **Abstraction** dalam sebuah aplikasi yang fungsional.

## 📚 Penjelasan Singkat dan Fitur

Program ini berfungsi sebagai sistem manajemen untuk perpustakaan digital, memungkinkan pengguna untuk berinteraksi melalui menu sederhana di terminal.

**Fitur-fitur utama:**

* **Tambah Item Baru**: Pengguna dapat menambahkan item baru ke perpustakaan, dengan memilih tipe item (Buku atau Majalah) dan memasukkan detailnya (ID, Judul, Penulis/Edisi).
* **Tampilkan Item Tersedia**: Menampilkan daftar lengkap semua item dalam koleksi yang saat ini berstatus "Tersedia".
* **Cari Item**: Mencari item spesifik dalam koleksi berdasarkan **ID** atau **Judul**. Pencarian bersifat *case-insensitive* dan dapat menemukan berdasarkan sebagian judul.
* **Pinjam Item**: Mengubah status item yang tersedia menjadi "Dipinjam".
* **Kembalikan Item**: Mengubah status item yang dipinjam kembali menjadi "Tersedia".

### Penerapan Konsep OOP

* **Abstract Class & Inheritance**:
    * `LibraryItem` adalah *abstract class* yang menjadi cetak biru (induk) untuk semua item.
    * `Book` dan `Magazine` adalah *subclass* yang mewarisi (inheritance) dari `LibraryItem`.
* **Encapsulation**:
    * Atribut penting seperti `__item_id` (di `LibraryItem`) dan `__items` (di `Library`) dibuat *private* (`__`).
    * Atribut internal seperti `_title` dan `_author` dibuat *protected* (`_`).
    * Akses aman ke atribut disediakan menggunakan `@property` decorator.
* **Polymorphism**:
    * Method `display_available_items()` di class `Library` memanggil `item.display_details()` pada setiap item.
    * Python secara otomatis menjalankan `display_details()` versi `Book` atau `display_details()` versi `Magazine` tergantung pada objek `item` saat itu, tanpa memerlukan `if-else` tambahan.

## 🚀 Screenshot Hasil Running Program

*(Harap ganti blok teks di bawah ini dengan screenshot atau salinan teks dari terminal Anda saat menjalankan program).*

**Contoh Sesi Penggunaan:**