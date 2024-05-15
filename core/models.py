from django.db import models
from django.utils.text import slugify
from accounts.models import Profile
# Create your models here.


def destination_image_upload(instance,filename):
    txt='imgdestination_'
    imagename,extension=filename.split('.')
    return "destinations/%s%s.%s"%(txt,instance.id,extension)
def sites_image_upload(instance,filename):
    txt='imgsites_'
    imagename,extension=filename.split('.')
    return "sites/%s%s.%s"%(txt,instance.id,extension)

def locations_image_upload(instance,filename):
    txt='imglocations_'
    imagename,extension=filename.split('.')
    return "locations/%s%s.%s"%(txt,instance.id,extension)

def events_image_upload(instance,filename):
    txt='imgevents_'
    imagename,extension=filename.split('.')
    return "events/%s%s.%s"%(txt,instance.id,extension)

class Destination(models.Model):
    name=models.CharField(max_length=100)
    summary=models.TextField(max_length=1000)
    published_at=models.DateTimeField( auto_now=True)
    image=models.ImageField(upload_to=destination_image_upload)
    slug=models.SlugField(blank=True,null=True)
  
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Destination,self).save(*args, **kwargs)

    def __str__(self) :
        return self.name
    





class Comment(models.Model):
    destination = models.ForeignKey(Destination, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=25)
    body = models.TextField(max_length=100,blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,related_name='comment_owner',on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_added']


class Site(models.Model):
    name=models.CharField(max_length=100)
    summary=models.TextField(max_length=1000)
    image=models.ImageField(upload_to=sites_image_upload)
    location=models.ImageField(upload_to=locations_image_upload)
    destination=models.ForeignKey(Destination, related_name='sites', on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,null=True)
    map_link=models.URLField(max_length=250)



    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Site,self).save(*args, **kwargs)

    def __str__(self) :
        return self.name




class Event(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to=events_image_upload)
    price=models.IntegerField(default=0)
    published_at=models.DateTimeField()
    destination=models.ForeignKey(Destination, related_name='events', on_delete=models.CASCADE)
    ticket_link=models.URLField(max_length=250)
    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Event,self).save(*args, **kwargs)

    def __str__(self) :
        return self.name