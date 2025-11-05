# 📘 Dashboard Tugas & Jadwal Mahasiswa

Aplikasi dashboard interaktif untuk mengelola daftar tugas dan jadwal kuliah mahasiswa. Pengguna dapat menambah, mengedit, menghapus, serta menandai tugas selesai. Semua data tersimpan otomatis menggunakan `localStorage`, sehingga tetap aman meskipun halaman direfresh.

---

## ✅ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| ➕ Tambah Tugas | Input tugas baru dan tampil langsung di daftar |
| ✏ Edit Tugas | Mengubah nama tugas yang sudah dibuat |
| ✅ Tandai Selesai | Checklist untuk menandai tugas selesai |
| 🗑 Hapus Tugas | Hapus tugas dengan konfirmasi |
| 📚 Kelola Jadwal | Tambah, edit, dan hapus jadwal kuliah |
| 📊 Progress Bar | Menampilkan persentase tugas selesai |
| 📆 Real-Time Clock | Tanggal & jam berjalan otomatis |
| 🌙 Dark Mode | Mode gelap/terang disimpan di localStorage |
| 💾 Local Storage | Data tugas & jadwal disimpan lokal |

---

## 🛠️ Persyaratan ES6+ yang Terpenuhi

| Fitur ES6+ | Contoh Implementasi | Status |
|-----------|---------------------|--------|
| `let` & `const` | `let currentFilter = 'all'; const tasks = [...]` | ✅ |
| Arrow Function (≥3) | `const el = id => ...`, `const updateTasksUI = () => {...}` | ✅ |
| Template Literals | Pada fungsi `renderTasks()` dan `renderSchedules()` | ✅ |
| Fungsi Async/Await | Digunakan di fitur waktu/opsional quote | ✅ |
| Classes | `class Task`, `class Schedule`, `class Storage` | ✅ |

---

## 💾 Penyimpanan Data (localStorage)

Key yang digunakan:
- `tasks` → Menyimpan daftar tugas
- `schedules` → Menyimpan daftar jadwal
- `darkMode` → Menyimpan status tema

---


## 📸 Screenshot Aplikasi

<img width="1677" height="709" alt="image" src="https://github.com/user-attachments/assets/383ddcbe-ac7a-4037-9176-f2a70c87d1b8" />


---

## 🚀 Cara Menggunakan

1. Buka `index.html` menggunakan web browser.
2. Isi tugas atau jadwal lalu klik **Tambah**.
3. Klik ikon ✏ untuk edit atau 🗑 untuk hapus.
4. Gunakan filter: Semua | Aktif | Selesai.
5. Aktifkan dark mode dari footer.


