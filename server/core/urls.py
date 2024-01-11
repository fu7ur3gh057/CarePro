from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from core.settings import API_URL

schema_view = get_schema_view(
    openapi.Info(
        title="CarePro API",
        default_version="v1",
        description="Distribution Message API",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="carepro@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    # url="https://carepro.su/",
    public=True,
)

urlpatterns = [
    # Healthcheck
    path(
        f"{API_URL}/health/",
        lambda request: HttpResponse("OK", content_type="text/plain"),
    ),
    path(f"{API_URL}/students/", include("src.apps.students.api.urls")),
    path(f"{API_URL}/subjects/", include("src.apps.subjects.api.urls")),
    path(f"{API_URL}/locations/", include("src.apps.locations.api.urls")),
    # Admin Panel
    path("admin/", admin.site.urls),
    # Swagger
    path(
        "swagger<str:format>",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
