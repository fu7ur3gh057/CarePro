from rest_framework import serializers

from src.apps.subjects.models import Subject, Grade


class SubjectSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    grade = serializers.SerializerMethodField()

    def get_grade(self, obj: Subject) -> int:
        return obj.grade.number

    class Meta:
        model = Subject
        fields = ["pk_id", "title", "grade"]


class GradeSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    number = serializers.IntegerField(read_only=True)

    class Meta:
        model = Grade
        fields = ["pk_id", "number"]
