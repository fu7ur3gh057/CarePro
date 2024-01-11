from rest_framework.permissions import BasePermissionMetaclass

from src.apps.students.models import Student


class IsStudent(metaclass=BasePermissionMetaclass):
    def has_permission(self, request, view):
        api_token = request.headers.get('api-token', None)
        if api_token:
            student = Student.objects.get(api_token=api_token)
            if student:
                request.student = student
                return True
            else:
                return False
        return False
