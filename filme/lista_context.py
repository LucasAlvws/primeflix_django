from .models import Filme

def contextos(request):
    contexto = {}

    '''Filmes recentes'''
    filmes_recentes = Filme.objects.all().order_by('-data_criacao')
    contexto['filmes_recentes'] = filmes_recentes

    '''Filmes em alta'''
    filmes_emalta = Filme.objects.all().order_by('-vizualizacoes')
    contexto['filmes_alta'] = filmes_emalta


    return contexto