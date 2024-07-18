from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse
from . import models 

class ListaProdutos(ListView):
        model = models.Produto
        template_name = 'produto/lista.html'
        context_object_name = 'produtos'
        paginate_by = 10


class DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class AdicionarAoCarrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Add carrinho')
class RemoverDoCarrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('remover carrinho')

class Carrinho(View):
      def get(self, *args, **kwargs):
        return HttpResponse('carrinho')
class Finalizar(View):
      def get(self, *args, **kwargs):
        return HttpResponse('finalizar')

