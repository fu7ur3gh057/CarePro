from rest_framework import serializers

from src.apps.locations.models import City, School


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["id", "title", "area", "region"]


class SchoolSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, obj):
        return obj.city.id

    class Meta:
        model = School
        fields = ["id", "city", "title"]
