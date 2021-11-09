from django.shortcuts import render
from core.models import Evento

# Create your views here.


# def index(request):
#     return redirect('/agenda/') # from django.shortcuts import redirect

def lista_eventos(request):
    #  usuario = request.user
    #  evento = Evento.objects.filter(usuario=usuario)
    #  evento = Evento.objects.get(id=1) # busca um registro específico
    evento = Evento.objects.all()  # CUIDADO com o tamanho do banco de dados ao ser utilizado "ALL"
    dados = {'eventos': evento}  # cria um dicionário
    return render(request, 'agenda.html', dados)
