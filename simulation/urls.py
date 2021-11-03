from django.urls import path
from .views import ArrivalProbabilitiesList, ArrivalProbabilitiesDetail

app_name = 'simulation'

urlpatterns = [
    path('<int:pk>/', ArrivalProbabilitiesDetail.as_view(), name='detailcreate'),
    path('', ArrivalProbabilitiesList.as_view(), name='listcreate'),
]
