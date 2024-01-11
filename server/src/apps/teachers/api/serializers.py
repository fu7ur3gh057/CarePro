from django_enum_choices.forms import EnumChoiceField
from rest_framework import serializers

from src.apps.subjects.api.serializers import SubjectSerializer
from src.apps.teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    def get_subjects(self, obj: Teacher) -> list[SubjectSerializer]:
        return [SubjectSerializer(subject).data for subject in obj.subjects.all()]

    class Meta:
        model = Teacher
        fields = [
            "tg_id",
            "full_name",
            "subjects",
            "phone_number",
            "api_token",
            "created_at",
            "updated_at"
        ]


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["tg_id", "full_name", "phone_number"]
