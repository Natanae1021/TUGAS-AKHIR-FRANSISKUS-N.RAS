from abc import ABC, abstractmethod

class Manusia(ABC):
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
    @abstractmethod
    def sapa(self):
        pass

    @abstractmethod
    def tugas(self):
        pass

class Dokter(Manusia):
    def __init__(self, nama, usia, spesialisasi):
        super().__init__(nama, usia)
        self.spesialisasi = spesialisasi
    
    def sapa(self):
        return f"Halo, saya Dokter {self.nama}, spesialis {self.spesialisasi}"

    def tugas(self):
        return "Merawat dan menyembuhkan pasien"

class Tentara(Manusia):
    def __init__(self, nama, usia, pangkat):
        super().__init__(nama, usia)
        self.pangkat = pangkat
    
    def sapa(self):
        return f"Halo, saya Tentara {self.nama}, pangkat {self.pangkat}"

    def tugas(self):
        return "Melindungi negara dan menjaga keamanan"

# Contoh penggunaan
dokter = Dokter("ancis ras", 35, "Bedah")
tentara = Tentara("Ahmad", 30, "Letnan")
print(dokter.sapa())
print(dokter.tugas())
print(tentara.sapa())
print(tentara.tugas())
