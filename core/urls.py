
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)


def home(request):
    return HttpResponse("Small App API is running!")


urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path("api/", include("app.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path(
        "api/redoc/",
        SpectacularRedocView.as_view(
            url_name="schema",
            template_name="drf_spectacular/redoc.html",
        ),
        name="redoc",
    ),
]
