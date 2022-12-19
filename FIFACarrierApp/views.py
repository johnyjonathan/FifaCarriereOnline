from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from FIFACarrierApp import models

# Logowanie
def helloView(request):
    if request.method == "GET":
        return render(request, 'hello_page.html')
    else:
        if request.POST.get('sign_in'):
            user = authenticate(request, username=request.POST['user_name'], password=request.POST['login_password'])
            if user is None:
                return render(request, 'hello_page.html', {'error': 'Username or password did not match!'})
            else:
                login(request, user)
                return redirect('mainView')

# Main view - widok wywoływany jest po poprawnym zalogowaniu
def mainView(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, 'app\main.html')
        else:
            pass
    else:
        return redirect('helloView')

# Widok odpowiadający za wyświetlenie danych zawodnika / odczytuje dane z bazy danych 
def PlayerDetailView(request, pk):
    if request.user.is_authenticated:
        resp = None
        if request.method == "GET":
            try:
                # Pobiranie z modelu danych zawodnika
                player_query = models.PLayersData.objects.get(pk=pk)
                player_info = player_query.__dict__ # Zamiana na słownik
                resp = player_info
                positions = list(player_query.player_position.split(',')) # Pozycje zapisane jako lista
            except:
                error = "FATAL ERROR - player info not found"
                return render(request, 'app/player_detail.html', {'error': error})
            # Zwraca widok z danymi zawodnika oraz pozycjami
            return render(request, 'app/player_detail.html', {'player_info': resp, 'positions': positions})
        else:
            pass
    else:
        return redirect('helloView')