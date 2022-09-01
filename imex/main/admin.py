from admin_auto_filters.filters import AutocompleteFilter
from admin_numeric_filter.admin import SliderNumericFilter, RangeNumericFilter, SingleNumericFilter, \
    NumericFilterModelAdmin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import People, City, Skill
from .resources import PeopleResource

admin.site.site_header = 'Django Import-Export'


class CityFilter(AutocompleteFilter):
    title = 'Город'
    field_name = 'city'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Город"""
    list_display = 'name', 'count_people',
    search_fields = 'name',
    list_per_page = 20


class SkillFilter(AutocompleteFilter):
    title = 'Умения'
    field_name = 'skill'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Умения"""
    list_display = 'name', 'count_people'
    search_fields = 'name',
    list_per_page = 20


@admin.register(People)
class PeopleAdmin(ImportExportModelAdmin, NumericFilterModelAdmin):
    """Информация о человеке"""
    resource_class = PeopleResource
    list_display = 'id', 'name', 'age', 'email', 'count_skill', 'is_active',
    list_editable = 'is_active', 'age'
    list_filter = (
        'is_active', CityFilter, SkillFilter,
        ('age', SliderNumericFilter),
    )
    list_per_page = 20
