from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class StudentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nis = models.CharField(max_length=16, default="0000000000")
    nama_sekolah = models.CharField(max_length=50, default='SMK Negeri 4 Bandung')
    jurusan = models.CharField(max_length=5, default='Other')
    tahun_masuk = models.CharField(max_length=10, default="2022")
    tahun_lulus = models.CharField(max_length=10, default="2025")
    telepon = models.CharField(max_length=20, default="089800000000")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
