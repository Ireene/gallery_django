from django.db import models
from django.contrib.auth.models import User
from time import time
from string import join
def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)
    
class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)

    
    def __unicode__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to=get_upload_file_name)
    albums = models.ForeignKey(Album)
    user = models.ForeignKey(User, null=True, blank=True)
   

    def __unicode__(self):
        return self.title
    
    def albums_(self):
        lst = [x[1] for x in self.albums.values_list()]
        return str(join(lst, ', '))    
 
class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(blank=False)
    pub_date = models.DateTimeField('date published')
    image = models.ForeignKey(Image)