from django import forms
from .models import Destination,Event,Site



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








class EventForm(forms.ModelForm):
    name=forms.CharField(label='Event Name', min_length=3,required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    description = forms.CharField(label='Event description', min_length=10,required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    image=forms.ImageField(label='ُEvent Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    published_at=forms.DateTimeField(label="choose DateTime Published_at",required=False,widget=DateTimeIn(attrs={'class': 'form-control mb-3'}))
    destination=forms.ModelChoiceField(label='Select Destination',queryset=Destination.objects.all(), required=False,widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    ticket_link=forms.URLField(label='Event TICKET LINK',required=False, max_length=250, widget=forms.URLInput(attrs={'class': 'form-control mb-3'}))
    price=forms.IntegerField(label='ُEvent Price',required=False,widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Event
        fields=('name','description','image','published_at','destination','ticket_link','price')
  





class SiteForm(forms.ModelForm):
    name=forms.CharField(label='Site Name', min_length=3,required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    summary = forms.CharField(label='Site summary', min_length=10,required=False, max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))
    image=forms.ImageField(label='ُSite Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    location=forms.ImageField(label='ُSite Location',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}))
    destination=forms.ModelChoiceField(label='Select Destination',queryset=Destination.objects.all(), required=False,widget=forms.Select(attrs={'class': 'form-control mb-3'}))
    map_link=forms.URLField(label='Map LINK',required=False, max_length=250, widget=forms.URLInput(attrs={'class': 'form-control mb-3'}))
    class Meta:
        model = Site
        fields=('name','summary','image','location','destination','map_link')
  