
# 📖 Aplikasi Manajer Buku Pribadi

Aplikasi React untuk melacak koleksi buku pribadi Anda. Aplikasi ini memungkinkan Anda untuk menambah, mengedit, menghapus, dan memfilter buku berdasarkan status baca (Sudah Dimiliki, Sedang Dibaca, atau Ingin Dibeli).

Aplikasi ini dibuat sebagai latihan untuk mendemonstrasikan fitur-fitur modern React, termasuk Context API, Custom Hooks, dan React Router.

---

## 📸 Tampilan Antarmuka (Screenshot)

### Halaman Utama (Homepage)
Halaman ini menampilkan filter, pencarian, dan daftar semua buku Anda.


<img width="1905" height="916" alt="image" src="https://github.com/user-attachments/assets/ed6d77b3-a491-41b9-aa25-7c35346af8c3" />


### Modal Tambah/Edit Buku
Formulir ini muncul saat Anda menambah atau mengedit buku, lengkap dengan validasi error.

<img width="1270" height="725" alt="image" src="https://github.com/user-attachments/assets/71e5a584-cbc4-4942-9e93-688f77a31efe" />

### Halaman Statistik
Halaman ini menampilkan rincian jumlah total buku berdasarkan statusnya.

<img width="1911" height="708" alt="image" src="https://github.com/user-attachments/assets/bd589a11-1500-4ae9-93fd-d0c80077a77b" />

---

## 🚀 Fitur React yang Digunakan

Aplikasi ini dibangun menggunakan fungsionalitas React modern:

### Components & Props
Aplikasi dipecah menjadi komponen-komponen reusable seperti:
- `BookItem`
- `BookList`
- `BookFilter`
- `Modal`
- `StatsCard`

### Hooks (Hooks Fungsional)
- **`useState`**: Mengelola state lokal di komponen (seperti data form di `BookForm` atau status modal)
- **`useEffect`**: Digunakan di dalam custom hook `useLocalStorage` untuk membaca data dari localStorage saat aplikasi pertama kali dimuat

### Context API (`BookContext.jsx`)
- Digunakan untuk state management global
- `BookProvider` membungkus seluruh aplikasi, menyediakan:
  - Data buku (termasuk `filteredBooks`)
  - Fungsi (`addBook`, `updateBook`, `deleteBook`)
  - State filter (`searchTerm`)
- Menghilangkan kebutuhan prop drilling

### 2 Custom Hooks (`hooks/`)
1. **`useLocalStorage.jsx`**: Hook kustom yang secara otomatis menyimpan state ke localStorage setiap kali state berubah, dan mengambilnya kembali saat halaman dimuat ulang
2. **`useBookStats.jsx`**: Hook kustom yang menerima daftar semua buku dan menggunakan `useMemo` untuk menghitung statistik (total, dimiliki, dibaca, dibeli) secara efisien

### React Router (`react-router-dom`)
- Navigasi multi-halaman antara Halaman Utama (`/`) dan Halaman Statistik (`/stats`)
- Menggunakan `createBrowserRouter`, `<RouterProvider>`, `<Outlet>`, dan `<Link>` untuk navigasi yang bersih dan modern

### Error Handling Form
- Komponen `BookForm` memiliki fungsi `validateForm` yang memeriksa apakah input "Judul" dan "Penulis" kosong sebelum mengizinkan submit

---

## 🔧 Instalasi dan Menjalankan

Ikuti langkah-langkah ini untuk menjalankan proyek ini di komputer lokal Anda.

### 1. Prasyarat
Pastikan Anda memiliki **Node.js** (versi 16 atau lebih baru) terinstal di sistem Anda.

### 2. Instalasi

Clone repositori ini (atau unduh dan ekstrak file ZIP):
```bash
git clone 
cd manajer-buku
```

Instal semua dependensi yang diperlukan:
```bash
npm install
```

Instal React Router (jika belum ada di `package.json`):
```bash
npm install react-router-dom
```

### 3. Menjalankan Aplikasi

Setelah instalasi selesai, jalankan server pengembangan:
```bash
npm run dev
```

Aplikasi akan otomatis terbuka di `http://localhost:5173` (atau port serupa) di browser Anda.

---

## 💬 Komentar Dalam Kode

Kode ini telah diberi komentar di bagian-bagian penting untuk menjelaskan logika yang kompleks:

- **`src/context/BookContext.jsx`**: Penjelasan tentang `useMemo` untuk pemfilteran
- **`src/hooks/useLocalStorage.jsx`**: Penjelasan tentang cara kerja penyimpanan ke localStorage
- **`src/main.jsx`**: Penjelasan tentang cara setup React Router
- **`src/components/BookForm.jsx`**: Penjelasan tentang logika validasi form
- **`src/App.test.jsx`**: Komentar di setiap `describe` dan `it` menjelaskan tujuan dari setiap tes

---

## 🧪 Laporan Testing

Aplikasi ini dikonfigurasi dengan **Vitest** dan **React Testing Library (RTL)**.

### 1. Instalasi Alat Tes (Hanya perlu sekali)

Jika Anda belum melakukannya, jalankan ini untuk menginstal alat pengujian:
```bash
npm install --save-dev vitest jsdom @testing-library/react @testing-library/user-event @testing-library/jest-dom
```

### 2. Menjalankan Tes

Untuk menjalankan 5 unit tes yang telah disiapkan:
```bash
npm test
```

### Hasil Tes (Screenshot)

Tes ini mencakup:
- ✅ Rendering komponen
- ✅ Interaksi pengguna (mengetik dan klik)
- ✅ Validasi error
- ✅ Logika context

![Gambar WhatsApp 2025-11-05 pukul 11 24 14_ec89d42b](https://github.com/user-attachments/assets/181f474e-36aa-4e2f-9a48-237a55b61f82)


---
