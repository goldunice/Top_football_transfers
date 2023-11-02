from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'index.html')


def clubs(request):
    return render(request, 'clubs.html')


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
