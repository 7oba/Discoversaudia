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
 ]