from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.students.api.serializers import StudentSerializer, StudentCreateSerializer
from src.apps.students.models import Student
from src.apps.subjects.models import Grade


class GetStudentAPIView(APIView):
    serializer_class = StudentSerializer

    def get(self, request: Request, tg_id: int) -> Response:
        student = get_object_or_404(Student, tg_id=tg_id)
        serializer = self.serializer_class(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateStudentAPIView(APIView):
    serializer_class = StudentCreateSerializer

    @swagger_auto_schema(request_body=StudentCreateSerializer)
    def post(self, request: Request) -> Response:
        try:
            data = request.data
            grade = get_object_or_404(Grade, number=data["grade"])
            data["grade"] = grade.pk_id
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)


class GetStudentSubjectsAPIView(APIView):
    pass
