# 📝 Aplikasi Manajemen Tugas Mahasiswa

## 📌 Deskripsi Singkat  
Aplikasi ini dibuat untuk membantu mahasiswa mengelola aktivitas akademik mereka seperti tugas kuliah. Pengguna dapat menambahkan, mengedit, menandai selesai, dan menghapus tugas secara interaktif. Semua data tersimpan **lokal di browser** menggunakan `localStorage`, sehingga data tidak hilang meskipun halaman direfresh.

---

## 📸 Screenshot Aplikasi

### 1. Tampilan Awal & Tambah Tugas
![Screenshot 1](./screenshot/tambah_tugas.png)

### 2. Tugas Tersimpan & Filter
![Screenshot 2](./screenshot/filter_tugas.png)

### 3. Edit & Hapus Tugas
![Screenshot 3](./screenshot/edit_hapus.png)

> 📌 *Ganti gambar di atas dengan hasil screenshot asli dari aplikasi kamu, simpan di folder `screenshot`.*

---

## 🧭 Cara Menjalankan Aplikasi

1. Pastikan sudah menginstal [Visual Studio Code](https://code.visualstudio.com/) dan extension **Live Server**.  
2. Clone atau download repository project ini.  
3. Buka folder project di VS Code.  
4. Klik kanan pada `index.html` → pilih **“Open with Live Server”**.  
5. Aplikasi akan berjalan otomatis di browser (misalnya `http://localhost:5500`).

---

## ✨ Daftar Fitur yang Telah Diimplementasikan

- ✅ Menambahkan tugas baru (nama tugas, mata kuliah, deadline)  
- ✅ Menandai tugas sebagai selesai/belum selesai  
- ✅ Mengedit tugas yang sudah ada  
- ✅ Menghapus tugas yang tidak diperlukan  
- ✅ Filter dan pencarian tugas berdasarkan mata kuliah  
- ✅ Menampilkan jumlah tugas belum selesai  
- ✅ Validasi input form

---

## 🧠 Penjelasan Teknis

### 📂 Penyimpanan Data Menggunakan `localStorage`
Aplikasi ini menggunakan `localStorage` untuk menyimpan data tugas.  
Contoh implementasi:
```javascript
// Simpan data
localStorage.setItem('tasks', JSON.stringify(tasks));

// Ambil data
const savedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
