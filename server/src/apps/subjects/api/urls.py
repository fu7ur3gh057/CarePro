from django.urls import path
from src.apps.subjects.api.views import (
    GetSubjectListAPIView,
    GetSubjectByTitleAPIView,
    GetSubjectByTitleAndGradeAPIView,
    GetGradeListAPIView,
)

urlpatterns = [
    path("", GetSubjectListAPIView.as_view(), name="subjects"),
    path("grades/", GetGradeListAPIView.as_view(), name="grades"),
    path("<title>/", GetSubjectByTitleAPIView.as_view(), name="get-by-title"),
    path(
        "<title>/<grade>/",
        GetSubjectByTitleAndGradeAPIView.as_view(),
        name="get-by-title-and-grade",
    ),
]
