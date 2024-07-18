from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models 

class ListaProdutos(ListView):
        model = models.Produto
        template_name = 'produto/lista.html'
        context_object_name = 'produtos'
        paginate_by = 10


class DetalheProduto(View):
      def get(self, *args, **kwargs):
        return HttpResponse('Detalhe Produto')
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

