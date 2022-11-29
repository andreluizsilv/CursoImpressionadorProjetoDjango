from django.shortcuts import render, redirect, reverse
from .models import Filme
#from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list


class Detalhefilmes(DetailView):
    template_name = "detalhesfilmes.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detalhefilmes, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context

#def homepage(request):
#    return render(request, "homepage.html")


#def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#    return render(request, "homefilmes.html", context)
