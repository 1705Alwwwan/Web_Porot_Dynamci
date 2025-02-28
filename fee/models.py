from django.db import models
from django.contrib.auth.models import User

class DataFakultas(models.Model):
    kdoe_fakulatas = models.CharField(max_length=3)
    nama_fakultas = models.CharField(max_length=50) 

    def __str__(self):
        return self.nama_fakultas

class DataBank (models.Model):
    kode_bank = models.CharField(max_length=4)
    nama_bank = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_bank 
    
class Rekening (models.Model):
    bank = models.ForeignKey(DataBank, on_delete=models.CASCADE, null=True)
    nomor_rekening = models.CharField(max_length=50)
    pemilik_rekening = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bank} - {self.nomor_rekening}"
    


class DataProgramStudi(models.Model):
    kdoe_program = models.CharField(max_length=3)
    nama_program = models.CharField(max_length=50) 

    def __str__(self):
        return self.nama_program
class DataJurusan (models.Model):
    kode_jurusan = models.CharField(max_length=4)
    nama_jurusan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_jurusan
    
class DataTahunAkademik (models.Model):
    tahun_akademik = models.CharField(max_length=4)
    semester = models.CharField(max_length=2)

    def __str__(self):
        return self.semester

class MetodePembayaran (models.Model):
    class Metode_Pembayaran (models. IntegerChoices):
        LANGSUNG = 1, 'Langsung'
        TRANSFER = 2, 'Transfer'


    nama_metode_pembayaran = models.BigIntegerField(choices=Metode_Pembayaran.choices)
    jumlah_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_pembayaran = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"{self.Metode_Pembayaran} {self.tanggal_pembayaran}"


class DetailPembayaran (models.Model):
    pembayaran = models.OneToOneField(MetodePembayaran, on_delete=models.CASCADE)
    Rekening = models.ForeignKey(Rekening, on_delete=models.CASCADE)
    catatan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.pembayaran.Metode_Pembayaran}"
    

class Sppmahasiswa (models.Model):
    class JenisKelamin(models.IntegerChoices):
        LAKI_LAKI = 1, 'Laki-laki'
        PEREMPUAN = 2, 'Perempuan'
        LAINNYA = 3, 'lainnya'

    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=8) 
    jenis_kelamin = models.IntegerField(choices=JenisKelamin.choices)  
    alamat = models.CharField(max_length=200) 
    fakultas = models.ForeignKey(DataFakultas, max_length=100, on_delete=models.CASCADE, null=True)
    program = models.ForeignKey(DataProgramStudi,max_length=10,on_delete=models.CASCADE, null=True)
    jurusan =  models.ForeignKey(DataJurusan, max_length=100, on_delete=models.CASCADE, null=True)
    nomor_hp = models.CharField(max_length=15)
    date_posted = models.DateTimeField(auto_now_add=True) 
    

    user = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE, null=True) 

    def __str__(self):
        return self.nama 
    



