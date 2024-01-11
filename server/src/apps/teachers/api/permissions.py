from rest_framework.permissions import BasePermissionMetaclass

from src.apps.teachers.models import Teacher


class IsTeacher(metaclass=BasePermissionMetaclass):
    def has_permission(self, request, view):
        api_token = request.headers.get('api-token', None)
        if api_token:
            teacher = Teacher.objects.get(api_token=api_token)
            if teacher:
                request.teacher = teacher
                return True
            else:
                return False
        return False
