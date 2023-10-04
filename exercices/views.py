from django.shortcuts import render, get_object_or_404


from .models import Exercice

def index(request):
    latest_exercice_list = Exercice.objects.order_by("id")[:5]
    context = { "latest_exercice_list": latest_exercice_list }
    return render(request, "exercices/index.html", context)

def detail(request, exercice_id):
    exercice = get_object_or_404(Exercice, pk=exercice_id)
    return render(request, "exercices/detail.html", {"exercice": exercice})

def newSession(request):
    exercice_list = Exercice.objects.order_by("id")
    context = { "exercice_list": exercice_list } 
    return render(request, "sessions/add.html", context)
