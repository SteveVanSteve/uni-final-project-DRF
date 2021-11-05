from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from simulation import views

urlpatterns = [
    path('simulation/', views.ArrivalProbabilities_list),
    path('simulation/<int:pk>', views.ArrivalProbabilities_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
