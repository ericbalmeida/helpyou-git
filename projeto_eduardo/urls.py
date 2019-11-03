from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from helpyou.views import conversas, home, lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('conversas/', conversas, name='url_conversas'),
    path('lista/', lista, name='url_lista'),
]

