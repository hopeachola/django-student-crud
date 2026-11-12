from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  #  Changed 'name' to 'urls'
    path('', include('myapp.urls')),
]
