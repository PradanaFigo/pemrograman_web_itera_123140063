from abc import ABC, abstractmethod
from typing import List, Optional

# BAGIAN 1: DEFINISI CLASS

class LibraryItem(ABC):
    """Abstract Base Class untuk semua item di perpustakaan."""
    
    def __init__(self, item_id: str, title: str):
        self.__item_id = item_id  # Private
        self._title = title      # Protected
        self._is_available = True  # Protected

    @property
    def item_id(self) -> str:
        """Mendapatkan ID item (read-only)."""
        return self.__item_id

    @property
    def title(self) -> str:
        """Mendapatkan judul item (read-only)."""
        return self._title

    @property
    def is_available(self) -> bool:
        """Mendapatkan status ketersediaan (read-only)."""
        return self._is_available

    def check_out(self) -> bool:
        """Menandai item sebagai 'Dipinjam' jika tersedia."""
        if self._is_available:
            self._is_available = False
            print(f"-> Item '{self.title}' (ID: {self.item_id}) berhasil dipinjam.")
            return True
        else:
            print(f"-> Gagal: Item '{self.title}' sudah dipinjam.")
            return False

    def check_in(self) -> bool:
        """Menandai item sebagai 'Tersedia' jika sedang dipinjam."""
        if not self._is_available:
            self._is_available = True
            print(f"-> Item '{self.title}' (ID: {self.item_id}) berhasil dikembalikan.")
            return True
        else:
            print(f"-> Gagal: Item '{self.title}' sudah tersedia.")
            return False

    def get_status(self) -> str:
        """Mendapatkan status ketersediaan dalam bentuk string."""
        return "Tersedia" if self._is_available else "Dipinjam"

    @abstractmethod
    def display_details(self) -> None:
        """Abstract Method: Menampilkan detail lengkap dari item."""
        pass

class Book(LibraryItem):
    """Subclass untuk item 'Buku', mewarisi dari LibraryItem."""
    
    def __init__(self, item_id: str, title: str, author: str):
        super().__init__(item_id, title)
        self._author = author

    def display_details(self) -> None:
        """(Implementasi Polymorphism) Menampilkan detail spesifik untuk buku."""
        print("--- Detail Buku ---")
        print(f"  ID     : {self.item_id}")
        print(f"  Judul  : {self.title}")
        print(f"  Penulis: {self._author}")
        print(f"  Status : {self.get_status()}")

class Magazine(LibraryItem):
    """Subclass untuk item 'Majalah', mewarisi dari LibraryItem."""
    
    def __init__(self, item_id: str, title: str, issue_number: str):
        super().__init__(item_id, title)
        self._issue_number = issue_number

    def display_details(self) -> None:
        """(Implementasi Polymorphism) Menampilkan detail spesifik untuk majalah."""
        print("--- Detail Majalah ---")
        print(f"  ID     : {self.item_id}")
        print(f"  Judul  : {self.title}")
        print(f"  Edisi  : {self._issue_number}")
        print(f"  Status : {self.get_status()}")

class Library:
    """Class pengelola untuk koleksi LibraryItem."""
    
    def __init__(self, name: str):
        self._name = name
        self.__items: List[LibraryItem] = []  # Private list

    def add_item(self, item: LibraryItem) -> None:
        """Menambahkan objek (Buku atau Majalah) ke dalam koleksi."""
        self.__items.append(item)
        print(f"\n[Info] Item '{item.title}' berhasil ditambahkan ke {self._name}.")

    def display_available_items(self) -> None:
        """Menampilkan semua item yang statusnya 'Tersedia'."""
        print(f"\n📚 Daftar Item Tersedia di {self._name}:")
        print("=" * 40)
        available_count = 0
        for item in self.__items:
            if item.is_available:
                # === POLYMORPHISM ===
                item.display_details()
                print("-" * 20)
                available_count += 1
        
        if available_count == 0:
            print("Tidak ada item yang tersedia saat ini.")

    def search_item(self, search_query: str) -> Optional[LibraryItem]:
        """
        Mencari item berdasarkan ID atau Judul (case-insensitive).
        Mengembalikan objek item jika ditemukan.
        """
        search_query_lower = search_query.lower()
        
        for item in self.__items:
            if item.item_id.lower() == search_query_lower or \
               search_query_lower in item.title.lower():
                return item
        
        return None 

# BAGIAN 2: FUNGSI HELPER UNTUK MENU

def menu_tambah_item(library: Library):
    """Fungsi untuk memandu pengguna menambahkan item baru."""
    print("\n--- Tambah Item Baru ---")
    print("1. Buku")
    print("2. Majalah")
    
    tipe_item = input("Pilih tipe item (1/2): ")
    
    item_id = input("Masukkan ID Item (misal B001): ").strip()
    if not item_id:
        print("Error: ID Item tidak boleh kosong.")
        return
        
    title = input("Masukkan Judul: ").strip()
    if not title:
        print("Error: Judul tidak boleh kosong.")
        return

    if tipe_item == '1':
        author = input("Masukkan Nama Penulis: ").strip()
        new_item = Book(item_id, title, author)
        library.add_item(new_item)
        
    elif tipe_item == '2':
        issue = input("Masukkan Nomor Edisi: ").strip()
        new_item = Magazine(item_id, title, issue)
        library.add_item(new_item)
        
    else:
        print("Pilihan tidak valid. Kembali ke menu utama.")

def menu_cari_item(library: Library):
    """Fungsi untuk mencari dan menampilkan detail item."""
    print("\n--- Cari Item ---")
    query = input("Masukkan ID atau Judul yang ingin dicari: ").strip()
    
    item_ditemukan = library.search_item(query)
    
    if item_ditemukan:
        print("-> Item ditemukan:")
        item_ditemukan.display_details()
    else:
        print(f"-> Item dengan query '{query}' tidak ditemukan.")

def menu_pinjam_item(library: Library):
    """Fungsi untuk mencari dan meminjam item."""
    print("\n--- Pinjam Item ---")
    query = input("Masukkan ID atau Judul item yang akan dipinjam: ").strip()
    
    item_ditemukan = library.search_item(query)
    
    if item_ditemukan:
        item_ditemukan.check_out()
    else:
        print(f"-> Item dengan query '{query}' tidak ditemukan.")

def menu_kembalikan_item(library: Library):
    """Fungsi untuk mencari dan mengembalikan item."""
    print("\n--- Kembalikan Item ---")
    query = input("Masukkan ID atau Judul item yang akan dikembalikan: ").strip()
    
    item_ditemukan = library.search_item(query)
    
    if item_ditemukan:
        item_ditemukan.check_in()
    else:
        print(f"-> Item dengan query '{query}' tidak ditemukan.")

def tampilkan_menu(nama_perpustakaan: str):
    """Menampilkan opsi menu utama."""
    print(f"\n=====================================")
    print(f"  Sistem Manajemen Perpustakaan")
    print(f"  {nama_perpustakaan}")
    print("=====================================")
    print("1. Tambah Item Baru")
    print("2. Tampilkan Semua Item Tersedia")
    print("3. Cari Item")
    print("4. Pinjam Item")
    print("5. Kembalikan Item")
    print("0. Keluar")
    print("-------------------------------------")

# BAGIAN 3: PROGRAM UTAMA (MAIN LOOP)

def main():
    """Fungsi utama untuk menjalankan program interaktif."""
    my_library = Library("Perpustakaan Digital Interaktif")
    my_library.add_item(Book("B001", "Dasar Python", "Guido"))
    my_library.add_item(Magazine("M001", "NatGeo", "Oktober 2025"))
    
    while True:
        tampilkan_menu(my_library._name)
        pilihan = input("Masukkan pilihan Anda (0-5): ").strip()
        
        if pilihan == '1':
            menu_tambah_item(my_library)
            
        elif pilihan == '2':
            my_library.display_available_items()
            
        elif pilihan == '3':
            menu_cari_item(my_library)
            
        elif pilihan == '4':
            menu_pinjam_item(my_library)
            
        elif pilihan == '5':
            menu_kembalikan_item(my_library)
            
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan sistem. Sampai jumpa!")
            break  
            
        else:
            print("\nPilihan tidak valid. Silakan masukkan angka antara 0 dan 5.")
        input("\n... Tekan Enter untuk melanjutkan ...")

if __name__ == "__main__":
    main()