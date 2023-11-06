from django.shortcuts import render
from .models import *
from datetime import date


def home(request):
    return render(request, 'index.html')


def stats(request):
    return render(request, 'stats.html')


def clubs(request):
    content = {
        "clubs": Club.objects.all()
    }
    return render(request, 'clubs.html', content)


def about(request):
    return render(request, 'about.html')


def players(request):
    content = {
        "players": Player.objects.all()
    }
    return render(request, 'players.html', content)


def record_transfers(request):
    content = {
        "transfers": Transfer.objects.filter(narx__gt=5000000)[:100]
    }
    return render(request, 'stats/transfer-records.html', content)


def u20players(request):
    h_sana = str(date.today().year)  # "2023"
    yil = int(h_sana) - 20  # int("2023") - 20 = 2003
    content = {
        "players": Player.objects.filter(t_sana__year__gte=yil).order_by("-narx", "-t_sana"),
        "h_yil": int(date.today().year)
    }
    return render(request, 'U-20 players.html', content)


def latest_transfers(request):
    h_mavsum = HMavsum.objects.all()[0]
    content = {
        "latest_transfers": Transfer.objects.filter(mavsum=str(h_mavsum))
    }
    return render(request, 'latest-transfers.html', content)


def davlat_clublari(request, davlat):
    content = {
        "davlat_clublari": Club.objects.filter(davlat=davlat.capitalize()),
        "tanlangan_davlat": davlat.capitalize()
    }
    return render(request, 'england.html', content)


def club_players(request, club):
    content = {
        "club_players": Player.objects.filter(club__nom=club),
        "club": club
    }
    return render(request, 'country-clubs.html', content)


def transfer_archive(request):
    content = {
        "seasons": Transfer.objects.exclude(
            mavsum=HMavsum.objects.first()
        ).values("mavsum").distinct().order_by("mavsum")
    }
    return render(request, 'transfer-archive.html', content)


def season(request, year):
    content = {
        "season_year": year,
        "season_transfer": Transfer.objects.filter(mavsum=year)
    }
    return render(request, '2017-18season.html', content)
