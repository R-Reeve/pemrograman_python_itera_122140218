from abc import ABC, abstractmethod

# Abstract class: dasar untuk semua item di perpustakaan (tidak bisa dipakai langsung)
class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self._item_id = item_id          # Protected: hanya bisa diakses oleh class ini dan turunannya
        self._title = title              # Protected: menyimpan judul item

    @abstractmethod
    def display_info(self):
        # Method abstrak: harus diisi oleh class turunannya
        pass

    @property
    def title(self):  # Property: akses aman ke judul
        return self._title

    @property
    def item_id(self):  # Property: akses aman ke ID
        return self._item_id


# Class Book mewarisi dari LibraryItem
class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)   # Panggil constructor parent
        self.__author = author             # Private: hanya bisa diakses di dalam class ini

    def display_info(self):
        # Implementasi method abstrak: tampilkan info buku
        print(f"[BOOK] ID: {self._item_id}, Title: {self._title}, Author: {self.__author}")


# Class Magazine juga mewarisi dari LibraryItem
class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue):
        super().__init__(item_id, title)   # Panggil constructor parent
        self.__issue = issue               # Private: hanya bisa diakses di dalam class ini

    def display_info(self):
        # Implementasi method abstrak: tampilkan info majalah
        print(f"[MAGAZINE] ID: {self._item_id}, Title: {self._title}, Issue: {self.__issue}")


# Class untuk mengelola semua item perpustakaan
class Library:
    def __init__(self):
        self.__collection = []  # Private: daftar untuk menyimpan item (buku/majalah)

    def add_item(self, item):
        # Tambahkan item ke koleksi
        self.__collection.append(item)
        print("Item berhasil ditambahkan!")

    def show_all_items(self):
        # Tampilkan semua item yang ada
        if not self.__collection:
            print("Belum ada item dalam perpustakaan.")
        else:
            print("\nDaftar Item Perpustakaan:")
            for item in self.__collection:
                item.display_info()  # Polymorphism: tergantung class-nya, akan tampil beda

    def search_item(self, keyword):
        # Cari item berdasarkan ID atau Judul
        found = False
        for item in self.__collection:
            if item.title == keyword or item.item_id == keyword:
                print("\nItem ditemukan:")
                item.display_info()
                found = True
                break
        if not found:
            print("Item tidak ditemukan.")


# ===== PROGRAM UTAMA =====
def main():
    library = Library()  # Buat objek perpustakaan

    while True:
        # Tampilkan menu utama
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Majalah")
        print("3. Tampilkan Semua Item")
        print("4. Cari Item (berdasarkan Judul atau ID)")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            # Input data buku dari pengguna
            item_id = input("Masukkan ID Buku: ")
            title = input("Masukkan Judul Buku: ")
            author = input("Masukkan Nama Penulis: ")
            book = Book(item_id, title, author)
            library.add_item(book)

        elif pilihan == '2':
            # Input data majalah dari pengguna
            item_id = input("Masukkan ID Majalah: ")
            title = input("Masukkan Judul Majalah: ")
            issue = input("Masukkan Edisi: ")
            magazine = Magazine(item_id, title, issue)
            library.add_item(magazine)

        elif pilihan == '3':
            # Tampilkan semua item
            library.show_all_items()

        elif pilihan == '4':
            # Cari item berdasarkan judul atau ID
            keyword = input("Masukkan Judul atau ID: ")
            library.search_item(keyword)

        elif pilihan == '5':
            # Keluar dari program
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            # Input salah
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    main()