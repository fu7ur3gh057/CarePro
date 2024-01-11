from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.subjects.models import Subject
from src.apps.teachers.api.permissions import IsTeacher
from src.apps.teachers.api.serializers import TeacherSerializer, TeacherCreateSerializer
from src.apps.teachers.models import Teacher


# TEACHER VIEWS
class GetTeacherAPIView(APIView):
    serializer_class = TeacherSerializer

    def get(self, request: Request, tg_id: int) -> Response:
        teacher = get_object_or_404(Teacher, tg_id=tg_id)
        serializer = self.serializer_class(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTeacherAPIView(APIView):
    serializer_class = TeacherCreateSerializer

    def post(self, request: Request) -> Response:
        try:
            data = request.data
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            teacher = get_object_or_404(Teacher, tg_id=data["tg_id"])
            response_data = TeacherSerializer(teacher).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)


class UpdateTeachersAPIView(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsTeacher]

    def patch(self, request: Request, subject_id: int) -> Response:
        teacher = request.teacher
        subject = get_object_or_404(Subject, pk_id=subject_id)
        teacher.subjects.add(subject)
        teacher.save(update_fields=["subjects"])
        serializer = self.serializer_class(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

# CHECK VIEWS
