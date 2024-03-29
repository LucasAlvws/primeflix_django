from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.http import Http404
# Create your views here.

def teste(request):
    return render(request, 'filme/teste.html')

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


    def get(self, request, *args, **kwargs):
        filme_ = self.get_object()
        filme_.vizualizacoes += 1
        filme_.save()
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(Detalhefilme, self).get_context_data(**kwargs)
        filmes_rel = Filme.objects.filter(categoria=self.get_object().categoria)
        filmes_rel = filmes_rel.exclude(titulo=self.get_object().titulo)
        filmes_rel = filmes_rel.order_by('titulo')[:6]
        context['filmes_rel'] = filmes_rel
        horse = Filme.objects.get(pk = self.kwargs['pk'])
        if not horse:
            raise Http404
        return context