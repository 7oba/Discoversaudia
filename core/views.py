from django.shortcuts import render,redirect
from .models import Destination,Comment,Site,Event
import datetime
from django.db.models import Q
# Create your views here.
def home_index(request):
    return render(request,'home/homepage.html')


def destination_list_view(request):
    destination_list=Destination.objects.all()
    site_list=Site.objects.all()
    context={'Destinations_list_Var':destination_list,'Sites_list_Var':site_list}
    return render(request,'destinations/destination_list.html',context)


def destination_detail_view(request,slug):
    destination_detail=Destination.objects.get(slug=slug)
    site_list=Site.objects.filter(destination=destination_detail)
    event_list=Event.objects.filter(Q(published_at__gte=datetime.date(2024, 1, 1))&Q(price__gte=50),destination=destination_detail)
    if request.method == 'POST':
        body = request.POST.get('body')
        username=request.POST.get('username')
        if len(body) >= 10 and len(body) <= 2000:
            comment = Comment.objects.create(
                body=body,
                username=username,
                destination=destination_detail,
            )
            comment.save()
            return redirect('core:destination_detail_view', slug=slug)
        else:
            print('Invalid form data')


    context={'Destination_detail_Var':destination_detail,'Sites_list_Var':site_list,'Events_list_Var':event_list}
    return render(request,'destinations/destination_detail.html',context)



def site_detail_view(request,slug):
    site_detail=Site.objects.get(slug=slug)
    context={'Site_detail_Var':site_detail}
    return render(request,'destinations/site_detail.html',context)




def event_detail_view(request,slug):
    event_detail=Event.objects.get(slug=slug)
    context={'Event_detail_Var':event_detail}
    return render(request,'destinations/event_detail.html',context)



