from django.contrib import admin
from .models import *


# admin.site.register(Club)
# admin.site.register(Player)
# admin.site.register(Transfer)
# admin.site.register(HMavsum)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "logo", "davlat", "prezident", "murabbiy", "yili", "record_trans", "record_sotuv"]
    list_display_links = ["id", "nom"]
    search_fields = ["nom"]
    list_filter = ["davlat"]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "davlat", "narx", "t_sana", "club", "pozitsiya"]
    list_display_links = ["id", "ism"]
    search_fields = ["ism__startswith"]
    list_filter = ["club"]
    autocomplete_fields = ["club"]


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ["id", "player", "eski_club", "yangi_club", "narx", "tax_narx", "mavsum"]
    list_display_links = ["id", "player"]
    search_fields = ["narx", "player__ism"]
    list_filter = ["mavsum"]
    autocomplete_fields = ["eski_club", "yangi_club", "player"]
