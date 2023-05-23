
from django.contrib import admin
from django.urls import path, include

from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/', include('mail.urls')),
    path('translation', include('translation.urls')),
]
