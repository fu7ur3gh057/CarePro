from django.contrib import admin

from src.apps.locations.models import City, School


class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "area", "region"]
    list_display_links = ["id"]
    list_filter = ["area", "region"]


class SchoolAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "city"]
    list_display_links = ["id", "city"]


admin.site.register(City, CityAdmin)
admin.site.register(School, SchoolAdmin)
