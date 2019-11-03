from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mensagens
from .form import MensagemForm

def home(request):
    return render(request, 'helpyou/home.html')

def conversas(request):
    data = {}
    form = MensagemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_lista')
    data['form'] = form
    return render(request, 'helpyou/conversas.html', data)

def lista(request):
    data = {}
    data['mensagem'] = Mensagens.objects.all()
    return render(request, 'helpyou/lista.html', data)