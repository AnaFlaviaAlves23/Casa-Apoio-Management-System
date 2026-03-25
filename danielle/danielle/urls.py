from people.views.dashboard import dashboard
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

from people.views import UserCreate, CustomObtainAuthToken, UserRetrieve
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('people.urls')),
    path('dashboard/', dashboard),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('users/<int:pk>/', UserRetrieve.as_view(), name='user_retrieve'),
    path("login/", CustomObtainAuthToken.as_view(), name="login"),
    path('api-token-auth/', obtain_auth_token, name='api_token_path')
]
