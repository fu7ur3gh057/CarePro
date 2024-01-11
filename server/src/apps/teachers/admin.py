from django.contrib import admin

from src.apps.teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["tg_id", "full_name", "phone_number", "created_at"]
    list_display_links = ["tg_id", "full_name", "phone_number"]


admin.site.register(Teacher, TeacherAdmin)
