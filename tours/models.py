from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _




class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"    


class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тура")
    city = models.ForeignKey(City, null=True, blank=True,
                             on_delete=models.CASCADE, verbose_name="Название области")
    address = models.ForeignKey(
        Address, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Город, адрес")
    distance = models.IntegerField(
        null=True, blank=True, verbose_name="Рассторяние от Бишкека")
    price = models.PositiveIntegerField(
        verbose_name=_('Цена тура'),
        validators=[
            MinValueValidator(0, _("Цена не может быть меньше 0")),
            MaxValueValidator(10000, _("Цена не может быть больше 10000"))
        ]
    )
    maxGroupSize = models.PositiveIntegerField(null=True, blank=True,
                                               verbose_name=_(
                                                   'Вместимость группы'),
                                               validators=[
                                                   MinValueValidator(
                                                       0, _("Вместимость не может быть меньше 0")),
                                                   MaxValueValidator(
                                                       15, _("Вместимость не может быть больше 15"))
                                               ]
                                               )
    desc = models.TextField(null=True, blank=True,
                            verbose_name="Описание тура")
    photo = models.ImageField("Постер", upload_to='media/', null=True)
    featured = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"
