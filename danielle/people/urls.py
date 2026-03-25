from django.urls import path, include
from people import views
from people.views.dashboard import dashboard  # Importando a sua função do dashboard
from rest_framework.routers import DefaultRouter

# Configuração das rotas da API (ViewSet)
router = DefaultRouter()
router.register('people', views.PersonViewSet)
router.register('checkins', views.CheckinViewSet)
router.register('patient_companion_checkin', views.PatientCompanionCheckinViewSet)
router.register('home_services', views.HomeServicesViewSet)
router.register('professional_services', views.ProfessionalServicesViewSet)

# O segredo está aqui: as rotas que o Django realmente "enxerga"
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Criando o caminho para o dashboard!
    path('', include(router.urls)),                   # Incluindo as rotas da API
]