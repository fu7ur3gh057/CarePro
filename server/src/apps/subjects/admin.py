from django.contrib import admin

from src.apps.subjects.models import Subject, Grade


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["pk_id", "title", "grade", "created_at"]
    list_display_links = ["pk_id", "created_at"]


class GradeAdmin(admin.ModelAdmin):
    list_display = ["pk_id", "number"]
    list_display_links = ["pk_id", "number"]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
