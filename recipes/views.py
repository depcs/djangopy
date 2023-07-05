from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    #return render(request, 'recipes/home.html')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Eron Cavalcante',
    })


def contato(request):
    return HttpResponse('Contato')
