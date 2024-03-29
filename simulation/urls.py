from django.urls import path
from simulation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('simulationresult/', views.SimulationResultViewSet.as_view())
])
