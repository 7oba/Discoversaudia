from django.contrib import admin

# Register your models here.
from .models import Destination,Site,Event



admin.site.register(Destination)
admin.site.register(Site)
admin.site.register(Event)