from django.urls import path
from simulation import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('simulation/', views.ArrivalProbabilitiesList.as_view(),
         name='arrivalprobabilities-list'),
    path('simulation/<int:pk>/', views.ArrivalProbabilitiesDetail.as_view(),
         name='arrivalprobabilities-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])
