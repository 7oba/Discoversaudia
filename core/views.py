from django.shortcuts import render,redirect
from .models import Destination,Comment

# Create your views here.
def home_index(request):
    return render(request,'home/homepage.html')


def destination_list_view(request):
    destination_list=Destination.objects.all()
    context={'Destinations_list_Var':destination_list}
    return render(request,'destinations/destination_list.html',context)

def destination_detail_view(request,slug):
    destination_detail=Destination.objects.get(slug=slug)
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


    context={'Destination_detail_Var':destination_detail}
    return render(request,'destinations/destination_detail.html',context)
