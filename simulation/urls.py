from django.urls import path
from simulation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('simulation/', views.ArrivalProbabilitiesList.as_view(),
         name='arrivalprobabilities-list'),
    path('simulation/<int:pk>/', views.ArrivalProbabilitiesDetail.as_view(),
         name='arrivalprobabilities-detail'),
    path('simulation/', views.BackgroundSetList.as_view(),
         name='backgroundset-list'),
    path('simulation/<int:pk>/', views.BackgroundSetDetail.as_view(),
         name='backgroundset-detail'),
    path('simulation/', views.BackgroundPowerList.as_view(),
         name='backgroundpower-list'),
    path('simulation/<int:pk>/', views.BackgroundPowerDetail.as_view(),
         name='backgroundpower-detail'),
    path('simulation/', views.ChargingCurveList.as_view(),
         name='chargingcurve-list'),
    path('simulation/<int:pk>/', views.ChargingCurveDetail.as_view(),
         name='chargingcurve-detail'),
    path('simulation/', views.SimulationConfigList.as_view(),
         name='simulationconfig-list'),
    path('simulation/<int:pk>/', views.SimulationConfigDetail.as_view(),
         name='simulationconfig-detail'),
    path('simulation/', views.SimulationResultList.as_view(),
         name='simulationresult-list'),
    path('simulation/<int:pk>/', views.SimulationResultDetail.as_view(),
         name='simulationresult-detail'),
])
