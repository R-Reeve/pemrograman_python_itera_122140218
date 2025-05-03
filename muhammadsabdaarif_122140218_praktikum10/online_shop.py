# Mengimpor modul ABC dan abstractmethod untuk membuat kelas abstrak
from abc import ABC, abstractmethod

# Kelas LibraryItem adalah kelas abstrak yang menjadi dasar bagi semua item perpustakaan
class LibraryItem(ABC):
    # Konstruktor untuk inisialisasi ID dan judul item
    def __init__(self, item_id, title):
        self._item_id = item_id          # ID item (protected)
        self._title = title              # Judul item (protected)

    # Method abstrak yang harus diimplementasikan oleh subclass
    @abstractmethod
    def display_info(self):
        pass

    # Property untuk mendapatkan judul item
    @property
    def title(self):
        return self._title

    # Property untuk mendapatkan ID item
    @property
    def item_id(self):
        return self._item_id


# Kelas Book merupakan subclass dari LibraryItem dan mengimplementasikan display_info
class Book(LibraryItem):
    # Konstruktor untuk inisialisasi ID, judul, dan penulis buku
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)  # Memanggil konstruktor kelas induk
        self.__author = author            # Penulis buku (private)

    # Implementasi method display_info untuk menampilkan informasi buku
    def display_info(self):
        print(f"   [BOOK]     ID    : {self._item_id}")
        print(f"                Title : {self._title}")
        print(f"                Author: {self.__author}")
        print("-" * 40)


# Kelas Magazine merupakan subclass dari LibraryItem dan mengimplementasikan display_info
class Magazine(LibraryItem):
    # Konstruktor untuk inisialisasi ID, judul, dan edisi majalah
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)  # Memanggil konstruktor kelas induk
        self.__issue = issue              # Edisi majalah (private)

    # Implementasi method display_info untuk menampilkan informasi majalah
    def display_info(self):
        print(f"   [MAGAZINE] ID    : {self._item_id}")
        print(f"                Title : {self._title}")
        print(f"                Issue : {self.__issue}")
        print("-" * 40)


# Kelas Library untuk mengelola koleksi item dalam perpustakaan
class Library:
    # Konstruktor untuk inisialisasi koleksi item yang akan disimpan
    def __init__(self):
        self.__collection = []  # List untuk menyimpan item (buku/majalah)

    # Method untuk menambahkan item ke koleksi perpustakaan
    def add_item(self, item):
        self.__collection.append(item)  # Menambahkan item ke koleksi
        print("\n Item berhasil ditambahkan ke perpustakaan!")

    # Method untuk menampilkan semua item yang ada di perpustakaan
    def show_all_items(self):
        if not self.__collection:  # Jika koleksi kosong
            print("\n Belum ada item dalam perpustakaan.")
        else:
            print("\n Daftar Item Perpustakaan:")
            print("=" * 40)
            for item in self.__collection:
                item.display_info()  # Memanggil display_info pada setiap item

    # Method untuk mencari item berdasarkan judul atau ID
    def search_item(self, keyword):
        found = False
        for item in self.__collection:
            if item.title == keyword or item.item_id == keyword:  # Jika ditemukan
                print("\n Item ditemukan:")
                print("=" * 40)
                item.display_info()
                found = True
                break
        if not found:  # Jika item tidak ditemukan
            print("\n Item tidak ditemukan.")


# Fungsi utama untuk menjalankan program perpustakaan
def main():
    library = Library()  # Membuat objek Library untuk mengelola koleksi

    # Looping menu untuk memilih aksi dalam program
    while True:
        print("\n" + "=" * 40)
        print(" SISTEM MANAJEMEN PERPUSTAKAAN")
        print("=" * 40)
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Semua Item")
        print("4. Cari Item (berdasarkan Judul atau ID)")
        print("5. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu (1-5): ")

        # Menangani pilihan untuk menambah buku
        if pilihan == '1':
            print("\n Tambah Buku:")
            item_id = input("  Masukkan ID Buku     : ")
            title = input("  Masukkan Judul Buku  : ")
            author = input("  Masukkan Nama Penulis: ")
            book = Book(item_id, title, author)  # Membuat objek Book
            library.add_item(book)

        # Menangani pilihan untuk menambah majalah
        elif pilihan == '2':
            print("\n Tambah Majalah:")
            item_id = input("  Masukkan ID Majalah  : ")
            title = input("  Masukkan Judul       : ")
            issue = input("  Masukkan Edisi       : ")
            magazine = Magazine(item_id, title, issue)  # Membuat objek Magazine
            library.add_item(magazine)

        # Menangani pilihan untuk menampilkan semua item
        elif pilihan == '3':
            library.show_all_items()

        # Menangani pilihan untuk mencari item berdasarkan ID atau judul
        elif pilihan == '4':
            print("\n Cari Item:")
            keyword = input("  Masukkan Judul atau ID: ")
            library.search_item(keyword)

        # Menangani pilihan untuk keluar dari program
        elif pilihan == '5':
            print("\n Terima kasih telah menggunakan sistem.")
            break

        # Menangani input yang tidak valid
        else:
            print("\n Pilihan tidak valid. Silakan coba lagi.")

# Memulai program jika file ini dijalankan
if __name__ == "__main__":
    main()