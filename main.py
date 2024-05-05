#Sistem Antrean Berobat di Rumah Sakit
#Kami menggunakan Jenis Struktur Queue atau disebut Antrean, dengan prinsip FIFO (First In First Out)
#dengan contohnya seperti "Yang mendaftar berobat pertama akan dilayani terlebih dahulu"
#atau pasien yang mendaftar berobat pertama kali akan dilayani terlebih dahulu, dan pasien selanjutnya akan dilayani setelah pasien pertama keluar dari antrian berobatnya

class Antrian:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        if len(self.items) <5:
            self.items.append(item)
            print(f"Pasien {item} telah ditambahkan ke dalam antrean.")
        else:
            print("Antrian Sudah Penuh")
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def size(self):
        return len(self.items)


class RumahSakit:
    def __init__(self):
        self.antrian = Antrian()
    def tambah_pasien(self, nama):
        self.antrian.enqueue(nama)
        print(f" ")
    def panggil_pasien(self):
        if not self.antrian.is_empty():
            pasien = self.antrian.dequeue()
            print(f"Panggilan: Silakan masuk atas nama, {pasien}!")
            print(" ")
        else:
            print("Antrian kosong.")
            print(" ")
    def jumlah_pasien(self):
        return self.antrian.size()


# Membuat objek RumahSakit
rs = RumahSakit()

# Tampilan Menu dan input
while True:
    print("=========================================================")
    print("=         Sistem Antrian Berobat di Rumah Sakit         =")
    print("=========================================================")
    print("=    1. Tambah Pasien                                   =")
    print("=    2. Panggil Pasien                                  =")
    print("=    3. Cek Jumlah Pasien                               =")
    print("=    0. Keluar                                          =")
    print("=========================================================")
    print(" ")

    pilihan = input("Masukkan pilihan 1/2/3/0 :")
    print(" ")

    if pilihan == "1":
        nama_pasien = input("Masukkan nama pasien: ")
        rs.tambah_pasien(nama_pasien)
    elif pilihan == "2":
        rs.panggil_pasien()
    elif pilihan == "3":
        jumlah_pasien = rs.jumlah_pasien()
        print(f"Jumlah pasien yang masih menunggu: {jumlah_pasien}")
    elif pilihan == "0":
        print("Terima kasih. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
