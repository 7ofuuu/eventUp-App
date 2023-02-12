from datetime import date

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import EventRecord

EVENTS = [('event-resmi-sekolah', 'Event Resmi Sekolah'), ('Event-non-sekolah', 'Event Non-Sekolah'), ('acara-sponsor', 'Acara Sponsor')]
BRANCHES = [('RPL', 'RPL'), ('TKJ', 'TKJ'), ('MM', 'MM'), ('TITL', 'TITL'), ('TOI', 'TOI'), ('TEAV', 'TEAV'), ('GURU', 'GURU'), 
            ('Alumni', 'Alumni') , ('Other', 'Other')]
YEAR = [('Kelas 10', 'Kelas 10'), ('Kelas 11', 'Kelas 11'), ('Kelas 12', 'Kelas 12'), ('Kelas 13', 'Kelas 13')]
CHOICE = [(1, 'YES'), (0, 'NO')]
TOPIC = [('Workshop', 'Workshop'),
                        ('Kompetisi', 'Kompetisi'),
                        ('Pelatihan', 'Pelatihan'),
                        ('PORAK', 'Pekan Olahraga dan Kesenian Siswa'),
                        ('Kegiatan-Olahraga', 'Kegiatan Olahraga'),
                        ('Hang-Out', 'Hang-Out / Main Bareng'),
                        ('Travelling', 'Travelling'),
                        ('Kegiatan-Alam', 'Kegiatan Alam'),
                        ('Festival-Musik', 'Festival Musik'),
                        ('Festival-Anime', 'Festival Jepang'),
                        ('Kegiatan-Rohis', 'Kegiatan Keagamaan Islam')]
DURATION_STRING = [('Jam', 'Jam'), ('Hari', 'Hari'), ('Minggu', 'Minggu'), ('Bulan', 'Bulan')]
EXTERNAL_LINKS = [('google-form','Google Form'), ('grup-whatsapp','Grup WhatsApp'), ('google-drive','Google Drive'), 
                    ('grup-telegram','Grup Telegram')]


class EventForm(forms.ModelForm):
    tipe_event = forms.CharField(widget=forms.Select(
        choices=EVENTS, attrs={'class': 'form-control'}), required=True)
    tema_event = forms.CharField(widget=forms.Select(
        choices=TOPIC, attrs={'class': 'form-control'}), required=True)

    penyelenggara = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Penyelenggara'}), required=True, max_length=100)
    nama_event = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nama Event'}), required=True, max_length=100)
    event_pic = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input', 'style': "opacity:1"}), required=True)
    event_banner = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input', 'style': "opacity:1"}), required=True)
    biaya = forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Biaya registrasi'}), min_value=0, max_value=200000, required=True)
    tanggal_awal_pendaftaran = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    tanggal_akhir_pendaftaran = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    tanggal_event = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'form-control'}))
    nomor_durasi = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Durasi Event'}), required=True, max_length=5)
    jenis_durasi = forms.CharField(widget=forms.Select(
        choices=DURATION_STRING, attrs={'class': 'form-control'}), required=True)
    jurusan_eligible = forms.CharField(widget=forms.CheckboxSelectMultiple(
        choices=BRANCHES, attrs={'class': 'form-check-inline'}), required=True)
    angkatan_eligible = forms.CharField(widget=forms.CheckboxSelectMultiple(
        choices=YEAR, attrs={'class': 'form-check-inline'}), required=True)

    tautan_lanjutan_1 = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder':'Tautan Eksternal'}), required=True, max_length=100)
    tautan_detail_1 = forms.CharField(widget=forms.Select(
        choices=EXTERNAL_LINKS, attrs={'class': 'form-control'}), required=True)

    tautan_lanjutan_2 = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder':'Tautan Eksternal (Opsional)'}), required=False, max_length=100)
    tautan_detail_2 = forms.CharField(widget=forms.Select(
        choices=EXTERNAL_LINKS, attrs={'class': 'form-control'}), required=False)
        
    tautan_lanjutan_3 = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control', 'placeholder':'Tautan Eksternal (Opsional)'}), required=False, max_length=100)
    tautan_detail_3 = forms.CharField(widget=forms.Select(
        choices=EXTERNAL_LINKS, attrs={'class': 'form-control'}), required=False)

    persyaratan_1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta'}), required=True, max_length=50)
    persyaratan_2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta (Opsional)'}), required=False, max_length=50)
    persyaratan_3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta (Opsional)'}), required=False, max_length=50)
    persyaratan_4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta (Opsional)'}), required=False, max_length=50)
    persyaratan_5 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta (Opsional)'}), required=False, max_length=50)
    persyaratan_6 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pesyaratan Peserta (Opsional)'}), required=False, max_length=50)
        
    benefit_event_1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event'}), required=True, max_length=100)
    benefit_event_2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event (Opsional)'}), required=False, max_length=100)
    benefit_event_3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event (Opsional)'}), required=False, max_length=100)
    benefit_event_4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event (Opsional)'}), required=False, max_length=100)
    benefit_event_5 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event (Opsional)'}), required=False, max_length=100)
    benefit_event_6 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Benefit Event (Opsional)'}), required=False, max_length=100)
    deskripsi = forms.CharField(widget=CKEditorUploadingWidget())

    alumni = forms.IntegerField(widget=forms.RadioSelect(
        choices=CHOICE, attrs={'class': 'form-check-inline'}), required=True)
    membutuhkan_pendaftaran = forms.IntegerField(widget=forms.RadioSelect(
        choices=CHOICE, attrs={'class': 'form-check-inline'}), required=True)
    venue = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Venue Event'}), required=True, max_length=50)
    narahubung = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Narahubung'}), required=True, max_length=100)
    narahubung_desc = forms.CharField(widget=CKEditorUploadingWidget())
    narahubung_pic = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'class': 'custom-file-input', 'style': "opacity:1"}), required=True)

    class Meta:
        model = EventRecord
        fields = ['nama_event', 'deskripsi', 'nomor_durasi', 'narahubung', 'narahubung_desc', 'venue',
                  'biaya', 'tanggal_awal_pendaftaran', 'tanggal_akhir_pendaftaran', 'tanggal_event', 'tipe_event', 'tema_event', 'jenis_durasi',
                  'jurusan_eligible', 'alumni', 'persyaratan_1', 'persyaratan_2', 'persyaratan_3', 'persyaratan_4', 'persyaratan_5', 'persyaratan_6',
                  'benefit_event_1', 'benefit_event_2', 'benefit_event_3', 'benefit_event_4',
                  'benefit_event_5', 'benefit_event_6', 'narahubung_pic', 'event_pic', 'event_banner' , 'angkatan_eligible', 'penyelenggara',
                  'tautan_lanjutan_1', 'tautan_detail_1', 'tautan_lanjutan_2', 'tautan_detail_2', 'tautan_lanjutan_3', 'tautan_detail_3', 'membutuhkan_pendaftaran']

    def clean_registration_start(self):
        try:
            tanggal_awal_pendaftaran = self.cleaned_data['tanggal_awal_pendaftaran']
            if True or tanggal_awal_pendaftaran.strftime('%Y-%m-%d') >= date.today().strftime('%Y-%m-%d'):
                return tanggal_awal_pendaftaran
            raise forms.ValidationError("Tanggal awal pendaftaran tidak valid")
        except Exception:
            raise forms.ValidationError("Tanggal awal pendaftaran tidak valid")

    def clean_registration_end(self):
        try:
            tanggal_awal_pendaftaran = self.cleaned_data['tanggal_awal_pendaftaran']
            tanggal_akhir_pendaftaran = self.cleaned_data['tanggal_akhir_pendaftaran']
            if tanggal_awal_pendaftaran <= tanggal_akhir_pendaftaran:
                return tanggal_akhir_pendaftaran
            raise forms.ValidationError("Tanggal akhir pendaftaran tidak valid")
        except Exception:
            raise forms.ValidationError("Tanggal akhir pendaftaran tidak valid")

    def clean_event_date(self):
        try:
            tanggal_awal_pendaftaran = self.cleaned_data['tanggal_awal_pendaftaran']
            tanggal_event = self.cleaned_data['tanggal_event']
            if tanggal_awal_pendaftaran <= tanggal_event:
                return tanggal_event
            raise forms.ValidationError("Tanggal event tidak valid")
        except Exception:
            raise forms.ValidationError("Tanggal event tidak valid")
