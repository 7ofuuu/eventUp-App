from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from .utils import get_unique_slug


# Create your models here.
class EventRecord(models.Model):
    slug = models.SlugField(unique=True)
    tipe_event = models.CharField(max_length=50)
    tema_event = models.CharField(max_length=75)

    penyelenggara = models.CharField(max_length=64)
    nama_event = models.CharField(max_length=110)
    event_pic = models.FileField(default='')
    event_banner = models.FileField(default='')
    biaya = models.FloatField()
    tanggal_awal_pendaftaran = models.DateField()
    tanggal_akhir_pendaftaran = models.DateField()
    tanggal_event = models.DateField()
    nomor_durasi = models.CharField(max_length=10)
    jenis_durasi = models.CharField(max_length=10)
    jurusan_eligible = models.CharField(max_length=100)
    angkatan_eligible = models.CharField(max_length=100)

    tautan_lanjutan_1 =  models.URLField(max_length=100)
    tautan_detail_1 = models.CharField(max_length=50)
    tautan_lanjutan_2 = models.URLField(max_length=100)
    tautan_detail_2 = models.CharField(max_length=50)
    tautan_lanjutan_3 = models.URLField(max_length=100)
    tautan_detail_3 = models.CharField(max_length=50)

    persyaratan_1 = models.CharField(max_length=50, default='')
    persyaratan_2 = models.CharField(max_length=50, default='')
    persyaratan_3 = models.CharField(max_length=50, default='')
    persyaratan_4 = models.CharField(max_length=50, default='')
    persyaratan_5 = models.CharField(max_length=50, default='')
    persyaratan_6 = models.CharField(max_length=50, default='')

    benefit_event_1 = models.CharField(max_length=100, default='')
    benefit_event_2 = models.CharField(max_length=100, default='')
    benefit_event_3 = models.CharField(max_length=100, default='')
    benefit_event_4 = models.CharField(max_length=100, default='')
    benefit_event_5 = models.CharField(max_length=100, default='')
    benefit_event_6 = models.CharField(max_length=100, default='')
    deskripsi = RichTextUploadingField()

    alumni = models.IntegerField(default=0)
    venue = models.CharField(max_length=50)
    narahubung = models.CharField(max_length=110)
    narahubung_pic = models.FileField(default='')
    narahubung_desc = RichTextUploadingField()

    registered_student = models.IntegerField(default=0)
    membutuhkan_pendaftaran = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, self.tema_event, self.tanggal_event)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug


class DataList(models.Model):
    place = models.CharField(max_length=50)
    number = models.IntegerField()

    def __str__(self):
        return self.place
