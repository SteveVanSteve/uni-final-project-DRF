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
router.register(r'simulationresult', views.SimulationResultViewSet)


# Wire up our API using automatic URL routing.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# The viewsets and urls will need to be changed for SimulationConfig and
# SimulationResult in order for the simulation to run
