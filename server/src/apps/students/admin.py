from django.contrib import admin

from src.apps.students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ["tg_id", "full_name", "grade", "city", "phone_number", "created_at"]
    list_display_links = ["tg_id", "city", "phone_number"]


admin.site.register(Student, StudentAdmin)
