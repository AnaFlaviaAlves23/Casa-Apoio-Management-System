from django.shortcuts import render
from people.models import Person, Checkin, Checkout

def dashboard(request):
    # Contagens totais
    total_pessoas = Person.objects.count()
    total_checkins = Checkin.objects.count()
    total_checkouts = Checkout.objects.count()
    
    # Lógica de "Pessoas no Local" (Melhoria 1)
    no_local = total_checkins - total_checkouts

    context = {
        'pessoas': total_pessoas,
        'checkins': total_checkins,
        'checkouts': total_checkouts,
        'no_local': no_local,
    }

    return render(request, 'dashboard.html', context)