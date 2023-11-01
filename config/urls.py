from django.contrib import admin
from django.urls import path
from mainApp.views import (home, clubs, about, players, record_transfers)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('clubs/', clubs),
    path('about/', about),
    path('players/', players),
    path('stats/record_transfers/', record_transfers)
]
