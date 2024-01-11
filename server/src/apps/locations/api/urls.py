from django.urls import path

from src.apps.locations.api.views import (
    GetCityListAPIView,
    GetSchoolListAPIView,
    GetCityByTitleAPIView,
    GetSchoolListByCityAPIView,
    GetSchoolByTitleAndCityAPIView,
    SearchCityListAPIView,
)

urlpatterns = [
    path("cities/", GetCityListAPIView.as_view(), name="cities"),
    path("schools/", GetSchoolListAPIView.as_view(), name="schools"),
    path("cities/<title>/", GetCityByTitleAPIView.as_view(), name="city-by-title"),
    path(
        "schools/<city_id>/",
        GetSchoolListByCityAPIView.as_view(),
        name="schools-by-city",
    ),
    path(
        "schools/<city_id>/<title>/",
        GetSchoolListByCityAPIView.as_view(),
        name="schools-by-city-and-title",
    ),
    path(
        "schools/detail/<city_id>/<title>/",
        GetSchoolByTitleAndCityAPIView.as_view(),
        name="school-by-city-and-title",
    ),
    path("search/<query>/", SearchCityListAPIView.as_view(), name="search-city"),
]
