from django.urls import path
from simulation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('simulation/', views.ArrivalProbabilitiesList.as_view()),
    path('simulation/<int:pk>/', views.ArrivalProbabilitiesDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
