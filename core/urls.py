from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from simulation.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('simulation.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
