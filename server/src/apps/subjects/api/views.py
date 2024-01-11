from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.subjects.api.serializers import SubjectSerializer, GradeSerializer
from src.apps.subjects.models import Subject, Grade


class GetSubjectListAPIView(APIView):
    serializer_class = SubjectSerializer

    def get(self, request: Request) -> Response:
        subjects = Subject.objects.all()
        serializer_list = self.serializer_class(subjects, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class GetSubjectByTitleAPIView(APIView):
    serializer_class = SubjectSerializer

    def get(self, request: Request, title: str) -> Response:
        subject = get_list_or_404(Subject, title=title)
        serializer = self.serializer_class(subject, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetSubjectByTitleAndGradeAPIView(APIView):
    serializer_class = SubjectSerializer

    def get(self, request: Request, title: str, grade: int) -> Response:
        subject = Subject.objects.filter(
            Q(title=title) & Q(grade__number=grade)
        ).first()
        if not subject:
            raise APIException("Предмет с таким названием и классом не найден")
        serializer = self.serializer_class(subject)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetGradeListAPIView(APIView):
    serializer_class = GradeSerializer

    def get(self, request: Request) -> Response:
        grades = Grade.objects.all()
        serializer_list = self.serializer_class(grades, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)
