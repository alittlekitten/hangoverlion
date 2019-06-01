from django.shortcuts import render

# Create your views here.

def random(request):
    return render(request, 'random.html')

def randomgame(request):
    return render(request, 'randomgame.html')

def randompanalty(request):
    return render(request, 'randompanalty.html')