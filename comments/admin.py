from django.contrib import admin
<<<<<<< HEAD
from .models import Review

admin.site.register(Review)
=======
from .models import *


@admin.register(Review)  

class CommentAdmin(admin.ModelAdmin):  
    list_display = ('name', 'tours', 'created', 'active')  
    list_filter = ('active', 'created', 'updated')  
    search_fields = ('name', 'body')
>>>>>>> c21bb4f
