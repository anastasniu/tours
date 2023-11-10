from django.db import models
from core import settings



class Profile(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg',  upload_to='profiles/')
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f'Профайл пользователя {self.name}' 
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='images')

