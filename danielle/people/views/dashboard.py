from django.shortcuts import render
from people.models.person import Person
from people.models.checkin import Checkin

def dashboard(request):
    total_pessoas = Person.objects.count()
    total_checkins = Checkin.objects.count()
    total_checkouts = 0 # Podemos implementar checkout depois
    
    # Melhoria 2: Pegar os últimos 5 check-ins (Atividade Recente)
    atividades = Checkin.objects.select_related('person').order_by('-id')[:5]

    context = {
        'pessoas': total_pessoas,
        'checkins': total_checkins,
        'checkouts': total_checkouts,
        'no_local': total_checkins - total_checkouts,
        'atividades': atividades, # Enviando para o HTML
    }
    return render(request, 'dashboard.html', context)