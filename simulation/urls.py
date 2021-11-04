from django.urls import path
from simulation import views

app_name = 'simulation'


urlpatterns = [
    path('simulation/', views.ArrivalProbabilities_list),
    path('simulation/<int:pk>/', views.ArrivalProbabilities_detail),
]
