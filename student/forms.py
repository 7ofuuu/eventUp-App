from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import StudentRecord

BATCH_START = [('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')]
BATCH_END = [('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'),
             ('2026', '2026'), ('2027', '2027')]
BRANCHES = [('RPL', 'RPL'), ('TKJ', 'TKJ'), ('MM', 'MM'), ('TITL', 'TITL'), ('TOI', 'TOI'), ('TEAV', 'TEAV'), ('GURU', 'GURU'),
            ('Other', 'Other')]


class StudentForm(forms.ModelForm):
    nis = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nomor Induk Siswa'}), required=True, max_length=15)
    nama_sekolah = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Asal Sekolah', 'value': 'SMK Negeri 4 Bandung', 'readonly':'readonly'}),
        required=True, max_length=200)
    jurusan = forms.CharField(
        label='JURUSAN', widget=forms.Select(choices=BRANCHES, attrs={'class': 'form-control'}), required=True)
    tahun_masuk = forms.CharField(
        label='TAHUN MASUK', widget=forms.Select(choices=BATCH_START, attrs={'class': 'form-control'}), required=True)
    tahun_lulus = forms.CharField(
        label='TAHUN LULUS', widget=forms.Select(choices=BATCH_END, attrs={'class': 'form-control'}), required=True)
    telepon = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon', 'pattern': "^(\+62|62)?[\s-]?0?8[1-9]{1}\d{1}[\s-]?\d{4}[\s-]?\d{2,5}$"}), required=True,
        max_length=20)

    class Meta:
        model = StudentRecord
        fields = ['nis', 'nama_sekolah', 'jurusan', 'tahun_masuk', 'tahun_lulus', 'telepon']

    def clean_roll_no(self):
        nis = None
        try:
            nis = self.cleaned_data['nis']
            StudentRecord.objects.get(nis=nis.upper())
            raise forms.ValidationError("NIS sudah terpakai. Hubungi admin untuk memperbaiki kendala")
        except ObjectDoesNotExist:
            return nis.upper()
