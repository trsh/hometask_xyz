from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("docs/", include("docs.urls")),
    path('admin/', admin.site.urls),
]
