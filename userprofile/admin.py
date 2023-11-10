from django.contrib import admin
from .models import Profile, Gallery



class GalleryInline(admin.TabularInline):
    fk_name = 'profile'
    model = Gallery


@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]