import os
import django

# Configura o Django para rodar fora do servidor
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'danielle.settings')
django.setup()

from people.models.person import Person
from people.models.checkin import Checkin

def run_seed():
    print("Limpando banco antigo...")
    # APAGUE NESTA ORDEM (Primeiro Checkin, depois Person)
    Checkin.objects.all().delete() 
    Person.objects.all().delete() 

    print("Criando novas pessoas e check-ins...")
    nomes = ["Alice Silva", "Bruno Souza", "Carla Oliveira", "Daniel Santos", "Erica Lima"]
    
    for nome in nomes:
        p = Person.objects.create(name=nome)
        print(f"✅ Criada: {p.name}")
        # Criar check-in para os 3 primeiros
        if nomes.index(nome) < 3:
            Checkin.objects.create(person=p)

    print("\n🚀 Seed finalizada! Agora ligue o server e veja o Dashboard.")
if __name__ == "__main__":
    run_seed()