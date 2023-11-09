from django.db import models
from core import settings



class Profile(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg',  upload_to='profiles/')
    bio = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

