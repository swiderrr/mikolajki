from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from random import choice


def home_page(request):
    if request.method == "POST":
        currentUser = request.user
        # Pobierz wszystkich użytkowników, którzy nie są jeszcze wylosowani
        nie_wylosowani = User.objects.filter(czy_wylosowany=False, is_superuser=False).exclude(username=currentUser.username)
        
        # Jeśli nie ma użytkowników, którzy spełniają kryteria, zwróć odpowiedni komunikat
        if not nie_wylosowani.exists():
            messages.warning(request, 'Brak użytkowników do wylosowania')
            return redirect("home_page")
        if currentUser.wylosowany != None:
            messages.warning(request, 'Już losowałeś cwaniaku!!!')
            return redirect("home_page")
        
        # Wylosuj użytkownika
        wylosowany_uzytkownik = choice(nie_wylosowani)
        
        # Ustaw atrybuty
        currentUser.wylosowany = wylosowany_uzytkownik.username
        wylosowany_uzytkownik.czy_wylosowany = True
        
        # Zapisz zmiany
        wylosowany_uzytkownik.save()
        currentUser.save()
        messages.warning(request, 'Twoja Mikołajka to ' + currentUser.wylosowany)
        return redirect('home_page')
    return render(request, 'bet/homepage.html',)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        userAuth = authenticate(request, username=username, password=password)
        if userAuth is not None:
            login(request, userAuth)
            return redirect('home_page')
        else:
            messages.success(request, ("Wystąpił błąd podczas logowania, spróbuj ponownie."))
            return redirect('login_user')
    else:
        return render(request, 'bet/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany")
    return redirect('home_page')
