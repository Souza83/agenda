from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# def index(request):
#     return redirect('/agenda/') # from django.shortcuts import redirect


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    #  evento = Evento.objects.get(id=1) # busca um registro específico
    # evento = Evento.objects.all()  # CUIDADO com o tamanho do banco de dados ao ser utilizado "ALL"
    dados = {'eventos': evento}  # cria um dicionário
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        derscricao = request.POST.get('derscricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              derscricao=derscricao,
                              usuario=usuario)
    return redirect('/')
