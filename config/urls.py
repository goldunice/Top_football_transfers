from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from mainApp.views import (home, clubs, about, players, record_transfers, u20players, latest_transfers, davlat_clublari,
                           club_players, stats, transfer_archive, season)

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('', home),
                   path('stats/', stats),
                   path('clubs/', clubs),
                   path('about/', about),
                   path('players/', players),
                   path('season/<str:year>/', season),
                   path('transfer_archive/', transfer_archive),
                   path('stats/record_transfers/', record_transfers),
                   path('u20players/', u20players),
                   path('latest_transfers/', latest_transfers),
                   path('countries/<str:davlat>/', davlat_clublari),
                   path('club_players/<str:club>/', club_players),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
