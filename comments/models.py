from django.db import models
from tours.models import Tour
from datetime import datetime  
from core import settings
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Rating(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rated_object_id = models.ForeignKey(Tour, on_delete=models.CASCADE)  
    rating = models.PositiveIntegerField()

    class Meta:  
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

    def str(self) -> str:
        return f'Rated by {self.user_id} on {self.rated_object_id}'


class Review(models.Model):  
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews',default=None)  
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_review',default=None)  
    body = models.TextField("Сообщение", max_length=5000, default=None)  
    created = models.DateTimeField(default=datetime.now)  
    updated = models.DateTimeField(default=datetime.now)  
    active = models.BooleanField(default=True)  
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, blank=True, null=True )


    class Meta:  
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ('created',)  
          
    def __str__(self):  
        return f'Comment by {self.name} on {self.tours}'
    

