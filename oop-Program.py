class Manusia:
    # inisialisasi kelas Manusia
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # metode untuk mengatakan halo
    def sapa(self):
        print(f'Halo, nama saya {self.nama} dan saya berumur {self.umur} tahun')

# membuat objek dari kelas Manusia
saya = Manusia('John', 30)

# memanggil metode sapa()
saya.sapa()

