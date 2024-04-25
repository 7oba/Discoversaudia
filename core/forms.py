from django import forms
from .models import Destination



class DateTimeIn(forms.DateTimeInput):
    input_type='datetime-local'

class DestinationForm(forms.ModelForm):
    name=forms.CharField(label='Destination Name', min_length=3,required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    image=forms.ImageField(label='Destination Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    # published_at=forms.DateTimeField(label="choose DateTime Published_at",required=False,widget=DateTimeIn(attrs={'class': 'form-control mb-3'}))
    summary = forms.CharField(label='Destination summary', min_length=10,required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Destination
        fields = ('name','summary','image')



