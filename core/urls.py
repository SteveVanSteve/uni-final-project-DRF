from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simulation.urls', namespace='simulation')),
    path('api/', include('simulation_api.urls', namespace='simulation_api')),
]
