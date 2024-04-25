from unicodedata import name
from core import views
from django.urls import path

app_name='core'

urlpatterns = [
    path('',views.home_index,name="home_page_view"),
    path('destinations/',views.destination_list_view,name="destination_list_view"),
    path('destinations/<str:slug>',views.destination_detail_view,name="destination_detail_view"),
    path('destinations/sites/<str:slug>',views.site_detail_view,name="site_detail_view"),
    path('destinations/events/<str:slug>',views.event_detail_view,name="event_detail_view"),
        ########Destination path##########
    path('management/destinatons-list',views.destlist_view,name="destlist_view"),
    path('management/show-destinaton/<str:slug>',views.showdest_view,name="showdest_view"),
    path('management/update-destinaton/<str:slug>',views.updatedest_view,name="updatedest_view"),
    path('management/create-destinaton',views.createdest_view,name="createdest_view"),
    path('management/delete-destinaton/<str:slug>',views.deletedest_view,name="deletedest_view"),
 ]