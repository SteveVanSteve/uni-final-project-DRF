from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simulation.urls', namespace='simulation')),
    path('api/', include('simulation_api.urls', namespace='simulation_api')),
    path('__debug__/', include(debug_toolbar.urls)),
]
