from datetime import date


class Murid:
    nama_sekolah = 'Pesantren Depok'  # class attributes
    def __init__(self, input_nama, input_usia, address='No Address'):  # constructor
        self.nama = input_nama  # instance attributes
        self.usia = input_usia  # instance attributes
        self.address = address  # instance attributs
    
    def bio(self):  # instance method
        print('nama murid {}, usia {}, {}'.format(self.nama, self.usia, self.address))

    @classmethod
    def by_tahun_lahir(cls, nama, address, year):
        usia = date.today().year - year
        return cls(nama, usia, address)

    @staticmethod
    def cukup_umur(usia):
        if usia > 10:
            print('cukup')
        else:
            print('belum cukup')


class SekolahDasar(Murid):
    nama_sekolah = 'Pesantren Depok - SD'  # class attributes
    def __init__(self, hobby, nama, usia):
        Murid.__init__(self, nama, usia)  # construstor
        self.hobby = hobby

    def bio(self):
        print('nama murid Sekolah Dasar (SD) {}, alamat: {}, usia: {}'.format(self.nama, self.address, self.usia))
    
    def new_method(self):
        print('new')


class SekolahMenegah(Murid):
    pass


class SekolahAtas(Murid):
    pass


class SekolahDasarUnggulan(SekolahDasar):
    pass


class SekolahDasarBiasa(SekolahDasar):
    pass



# ==================
    
print(Murid.nama_sekolah)

# create object
murid_1 = Murid(input_nama='agus', input_usia=20, address='JKT')
murid_2 = Murid('bambang', 20, 'JKT')
murid_3 = Murid.by_tahun_lahir("Anung", 'JKT', 1997)

# create object SD
murid_sd_1 = SekolahDasar('Renang', 'Ani', 20)

# create object SD unggulan
murid_sd_unggulan_1 = SekolahDasarUnggulan(nama='Ana', usia=20, hobby='')

# get data from Murid
print(murid_1.nama)
print(murid_2.nama)
print(murid_3.nama, murid_3.usia)
murid_1.bio()
murid_1.cukup_umur(15)
print('\n')

# get data from SekolahDasar
print(murid_sd_1.nama)
murid_sd_1.bio()
print(murid_sd_1.hobby)
print(murid_sd_1.nama_sekolah)
print('\n')

# get data from SekolahDasarUnggulan
print(murid_sd_unggulan_1.nama)