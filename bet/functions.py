import bs4, requests
from .models import User


# def givePoint():
#     winner = User.objects.filter(bet=compareBets(User.objects.all(), covidCases()))[0]
#     winner.points = winner.points + 1
#     print(winner.points)
#     winner.save()
#     print("Sprawdzanie")
#     return