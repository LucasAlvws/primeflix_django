from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, CreateView, ListView, DetailView
# Create your views here.


class Homepage(TemplateView):
    template_name = "filme/homepage.html"
    

'''def homepage(request):
    return render(request, 'filme/homepage.html')'''

'''def homefilmes(request):
    context = {}
    lista_filmes = Filme.objects.all()
    context['lista_filmes'] =  lista_filmes
    return render(request, 'filme/homefilmes.html', context)'''
class Homefilmes(ListView):
    template_name = "filme/homefilmes.html"
    model = Filme


class Detalhefilme(DetailView):
    template_name = "filme/detalhefilme.html"
    model = Filme