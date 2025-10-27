# 📝 Aplikasi Manajemen Tugas Mahasiswa

##  Deskripsi Singkat  
Aplikasi ini dibuat untuk membantu mahasiswa mengelola aktivitas akademik mereka seperti tugas kuliah. Pengguna dapat menambahkan, mengedit, menandai selesai, dan menghapus tugas secara interaktif. Semua data tersimpan **lokal di browser** menggunakan `localStorage`, sehingga data tidak hilang meskipun halaman direfresh.

---

##  Screenshot Aplikasi

### 1. Tampilan Awal & Tambah Tugas
<img width="1233" height="243" alt="image" src="https://github.com/user-attachments/assets/2f6a40bb-c54e-4f87-8263-9a389dfccc4b" />


### 2. Tugas Tersimpan & Filter
<img width="991" height="472" alt="image" src="https://github.com/user-attachments/assets/64349aa2-5de4-4464-be2a-3aa8b72d1503" />


### 3. Edit & Hapus Tugas
<img width="907" height="309" alt="image" src="https://github.com/user-attachments/assets/7fa42b2a-940a-4355-940c-912e4d495797" />


---

##  Cara Menjalankan Aplikasi

1. Pastikan sudah menginstal [Visual Studio Code](https://code.visualstudio.com/) dan extension **Live Server**.  
2. Clone atau download repository project ini.  
3. Buka folder project di VS Code.  
4. Klik kanan pada `index.html` → pilih **“Open with Live Server”**.  
5. Aplikasi akan berjalan otomatis di browser .

---

##  Daftar Fitur yang Telah Diimplementasikan

- ✅ Menambahkan tugas baru (nama tugas, mata kuliah, deadline)  
- ✅ Menandai tugas sebagai selesai/belum selesai  
- ✅ Mengedit tugas yang sudah ada  
- ✅ Menghapus tugas yang tidak diperlukan  
- ✅ Filter dan pencarian tugas berdasarkan mata kuliah  
- ✅ Menampilkan jumlah tugas belum selesai  
- ✅ Validasi input form

---

##  Penjelasan Teknis

###  Penyimpanan Data Menggunakan `localStorage`
Aplikasi ini menggunakan `localStorage` untuk menyimpan data tugas.  
Contoh implementasi:
```javascript
// Simpan data
localStorage.setItem('tasks', JSON.stringify(tasks));

// Ambil data
const savedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
