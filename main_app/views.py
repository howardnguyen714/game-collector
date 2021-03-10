from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello GAMER!! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', { 'games': games })


class Game:
  def __init__(self, title, genre, description, playtime):
    self.title = title
    self.genre = genre
    self.description = description
    self.playtime = playtime

games = [
  Game('Lolo', 'tabby', 'foul little demon', 3),
  Game('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Game('Raven', 'black tripod', '3 legged cat', 4)
]