from django.db import models
from django.contrib.auth.models import User
from gallery.models import Album

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


