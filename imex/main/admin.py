from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionMixin
from .models import People, City, Skill
from .resources import PeopleResource
admin.site.site_header = 'Django Import-Export'  # Надпись в админке сайта

@admin.register(People)
class PeopleAdmin(ImportExportModelAdmin):
    """Информация о человеке"""
    resource_class = PeopleResource
    list_display = 'name', 'age', 'email', 'city',
    list_filter = 'city', 'skill',
    list_per_page = 10


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Город"""
    list_display = 'name', 'count_people'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Умения"""
    list_display = 'name', 'count_people'
