from django.urls import path, include
from people import views
from people.views.dashboard import dashboard
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register('people', views.PersonViewSet)
router.register('checkins', views.CheckinViewSet)
router.register('patient_companion_checkin', views.PatientCompanionCheckinViewSet)
router.register('home_services', views.HomeServicesViewSet)
router.register('professional_services', views.ProfessionalServicesViewSet)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include(router.urls)), # Coloquei 'api/' para organizar melhor
     # ESTAS SÃO AS LINHAS QUE FALTAVAM PARA O SWAGGER:
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]