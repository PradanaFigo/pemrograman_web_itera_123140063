mahasiswa_list = [
    {"nama": "Andi", "nim": "12345", "nilai_uts": 78, "nilai_uas": 85, "nilai_tugas": 80},
    {"nama": "Budi", "nim": "12346", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 60},
    {"nama": "Citra", "nim": "12347", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 88},
    {"nama": "Dewi", "nim": "12348", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
    {"nama": "Eka", "nim": "12349", "nilai_uts": 45, "nilai_uas": 40, "nilai_tugas": 50},
]

def hitung_nilai_akhir(m):
    return round(m["nilai_uts"] * 0.3 + m["nilai_uas"] * 0.4 + m["nilai_tugas"] * 0.3, 2)

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

def tampilkan_data(mahasiswa):
    print("=" * 70)
    print(f"{'NIM':<10} {'Nama':<15} {'UTS':<8} {'UAS':<8} {'Tugas':<8} {'Akhir':<8} {'Grade':<5}")
    print("-" * 70)
    for m in mahasiswa:
        nilai_akhir = hitung_nilai_akhir(m)
        grade = tentukan_grade(nilai_akhir)
        print(f"{m['nim']:<10} {m['nama']:<15} {m['nilai_uts']:<8} {m['nilai_uas']:<8} {m['nilai_tugas']:<8} {nilai_akhir:<8} {grade:<5}")
    print("=" * 70)

def cari_nilai_tertinggi(mahasiswa):
    return max(mahasiswa, key=lambda m: hitung_nilai_akhir(m))

def cari_nilai_terendah(mahasiswa):
    return min(mahasiswa, key=lambda m: hitung_nilai_akhir(m))

def tambah_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM: ")
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    tugas = float(input("Masukkan nilai Tugas: "))
    mahasiswa_list.append({
        "nama": nama,
        "nim": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas
    })
    print("Data mahasiswa berhasil ditambahkan!\n")

def filter_berdasarkan_grade(grade):
    hasil = []
    for m in mahasiswa_list:
        nilai_akhir = hitung_nilai_akhir(m)
        if tentukan_grade(nilai_akhir) == grade.upper():
            hasil.append(m)
    return hasil

def rata_rata_kelas():
    total = sum(hitung_nilai_akhir(m) for m in mahasiswa_list)
    return round(total / len(mahasiswa_list), 2)

while True:
    print("\n=== PROGRAM PENGELOLAAN DATA NILAI MAHASISWA ===")
    print("1. Tampilkan Semua Data")
    print("2. Tambah Data Mahasiswa")
    print("3. Cari Mahasiswa Nilai Tertinggi")
    print("4. Cari Mahasiswa Nilai Terendah")
    print("5. Filter Berdasarkan Grade")
    print("6. Hitung Rata-rata Nilai Kelas")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampilkan_data(mahasiswa_list)
    elif pilihan == "2":
        tambah_mahasiswa()
    elif pilihan == "3":
        tertinggi = cari_nilai_tertinggi(mahasiswa_list)
        print("\nMahasiswa dengan nilai tertinggi:")
        print(f"{tertinggi['nama']} ({tertinggi['nim']}) - Nilai Akhir: {hitung_nilai_akhir(tertinggi)}")
    elif pilihan == "4":
        terendah = cari_nilai_terendah(mahasiswa_list)
        print("\nMahasiswa dengan nilai terendah:")
        print(f"{terendah['nama']} ({terendah['nim']}) - Nilai Akhir: {hitung_nilai_akhir(terendah)}")
    elif pilihan == "5":
        g = input("Masukkan grade (A/B/C/D/E): ")
        hasil = filter_berdasarkan_grade(g)
        if hasil:
            print(f"\nDaftar Mahasiswa dengan grade {g.upper()}:")
            tampilkan_data(hasil)
        else:
            print("Tidak ada mahasiswa dengan grade tersebut.")
    elif pilihan == "6":
        print(f"Rata-rata nilai akhir kelas: {rata_rata_kelas()}")
    elif pilihan == "0":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
