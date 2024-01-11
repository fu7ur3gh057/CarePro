from django.urls import path
from src.apps.students.api.views import GetStudentAPIView, CreateStudentAPIView

urlpatterns = [
    path("create/", CreateStudentAPIView.as_view(), name="register"),
    path("<tg_id>/", GetStudentAPIView.as_view(), name="get-student"),
]
