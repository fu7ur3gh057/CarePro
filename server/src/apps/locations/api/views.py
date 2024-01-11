from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.locations.api.serializers import CitySerializer, SchoolSerializer
from src.apps.locations.models import City, School
from src.apps.locations.pagination import LocationPagination


class SearchCityListAPIView(APIView):
    serializer_class = CitySerializer

    def get(self, request: Request, query: str) -> Response:
        city_list = City.objects.filter(
            Q(title__icontains=query) | Q(area__icontains=query)
        )
        serializer_list = self.serializer_class(city_list, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class GetCityListAPIView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    pagination_class = LocationPagination

    def get_queryset(self) -> list[City]:
        return self.queryset


class GetCityByTitleAPIView(APIView):
    serializer_class = CitySerializer

    def get(self, request: Request, title: str) -> Response:
        pass


class GetSchoolListAPIView(ListAPIView):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    pagination_class = LocationPagination

    def get_queryset(self) -> list[School]:
        return self.queryset


class GetSchoolListByCityAPIView(APIView):
    serializer_class = SchoolSerializer

    def get(self, request: Request, city_id: int) -> Response:
        city = get_object_or_404(City, id=city_id)
        schools = city.schools.all()
        serializer_list = self.serializer_class(schools, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class GetSchoolListByTitleAndCityAPIView(APIView):
    serializer_class = SchoolSerializer

    def get(self, request: Request, city_id: int, title: str) -> Response:
        city = get_object_or_404(City, id=city_id)
        schools = city.schools.all().filter(title__icontains=title)
        serializer_list = self.serializer_class(schools, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class GetSchoolByTitleAndCityAPIView(APIView):
    serializer_class = SchoolSerializer

    def get(self, request: Request, city_id: int, title: str) -> Response:
        city = get_object_or_404(City, id=city_id)
        school = city.schools.all().filter(title=title).first()
        if not school:
            raise APIException("Школа не найдена")
        serializer = self.serializer_class(school)
        return Response(serializer.data, status=status.HTTP_200_OK)
