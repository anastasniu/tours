from django.contrib import admin
from django.urls import path, include, re_path
from core.swagger import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('accounts.urls')),
<<<<<<< HEAD
   
    path('tours/', include('tours.urls')),
    path('comments/', include('comments.urls')),
=======
    path('tours/', include('tours.urls')),
    path('comments/', include('tours.urls')),

>>>>>>> c21bb4f


    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
