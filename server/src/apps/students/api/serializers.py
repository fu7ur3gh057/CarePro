from rest_framework import serializers

from src.apps.students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField()

    def get_grade(self, obj: Student) -> int:
        return obj.grade.number

    class Meta:
        model = Student
        fields = "__all__"


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["tg_id", "full_name", "phone_number", "city", "school", "grade"]
