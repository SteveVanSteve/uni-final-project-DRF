from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'simulation'

urlpatterns = [
    path('', TemplateView.as_view(template_name="simulation/index.html")),
]
