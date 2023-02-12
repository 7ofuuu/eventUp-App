from django import forms

from .models import TransactionRecord


class TransactionForm(forms.ModelForm):
    jumlah_pembayaran = forms.FloatField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Jumlah Pembayaran'}), required=True, max_value=200000, min_value=-200000)
    detail_bayar = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Detail Bayar'}), required=False, max_length=50)

    class Meta:
        model = TransactionRecord
        fields = ['jumlah_pembayaran', 'detail_bayar']

    def clean_amount(self):
        jumlah_pembayaran = self.cleaned_data['jumlah_pembayaran']
        if -200000 <= jumlah_pembayaran <= 200000:
            return jumlah_pembayaran
        raise forms.ValidationError("Jumlah Pembayaran Tidak Valid")
