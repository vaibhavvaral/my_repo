from django import forms 

class BookForm(forms.Form):
    tital=forms.CharField()
    author=forms.CharField()
    pages=forms.IntegerField()
    prise=forms.FloatField()
