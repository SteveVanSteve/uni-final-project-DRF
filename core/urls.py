from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from simulation import views

router = routers.DefaultRouter()
router.register(r'arrivalprobabilities', views.ArrivalProbabilitiesViewSet)
router.register(r'backgroundsets', views.BackgroundSetViewSet)
router.register(r'backgroundpower', views.BackgroundPowerViewSet)
router.register(r'chargingcurve', views.ChargingCurveViewSet)
router.register(r'simulationconfig', views.SimulationConfigViewSet)


# Wire up our API using automatic URL routing.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('simulation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
