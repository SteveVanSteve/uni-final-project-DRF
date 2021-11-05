from django.urls import path
from simulation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('simulation/', views.ArrivalProbabilitiesList.as_view()),
    path('simulation/<int:pk>/', views.ArrivalProbabilitiesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
