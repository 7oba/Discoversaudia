from django.shortcuts import render
from .models import Destination

# Create your views here.
def home_index(request):
    return render(request,'home/homepage.html')


def destination_list_view(request):
    destination_list=Destination.objects.all()
    context={'Destinations_list_Var':destination_list}
    return render(request,'destinations/destination_list.html',context)


def destination_detail_view(request,slug):
    destination_detail=Destination.objects.get(slug=slug)
    context={'Destination_detail_Var':destination_detail}
    return render(request,'destinations/destination_detail.html',context)