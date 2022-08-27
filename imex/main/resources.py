from django.db.models import QuerySet
from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from .models import Skill, City, People


class ForeignKeyWidgetWithCreation(ForeignKeyWidget):
    def __init__(self, model, field="pk", create=False, **kwargs):
        self.model = model
        self.field = field
        self.create = create
        super(ForeignKeyWidgetWithCreation, self).__init__(model, field=field, **kwargs)

    def clean(self, value, **kwargs):
        print(value)
        if not value:
            return None
        if self.create:
            self.model.objects.get_or_create(**{self.field: value})
        val = super(ForeignKeyWidgetWithCreation, self).clean(value, **kwargs)
        return self.model.objects.get(**{self.field: val}) if val else None


class ManyToManyWidgetWithCreation(ManyToManyWidget):
    def __init__(self, model, field="pk", create=False, **kwargs):
        self.model = model
        self.field = field
        self.create = create
        super(ManyToManyWidgetWithCreation, self).__init__(model, field=field, **kwargs)

    def clean(self, value, **kwargs):
        if not value:
            return self.model.objects.none()
        cleaned_value: QuerySet = super(ManyToManyWidgetWithCreation, self).clean(value, **kwargs)
        object_list = value.split(self.separator)
        if len(cleaned_value.all()) == len(object_list):
            return cleaned_value
        if self.create:
            for object_value in object_list:
                _instance, _new = self.model.objects.get_or_create(**{self.field: object_value})
        model_objects = self.model.objects.filter(**{f"{self.field}__in": object_list})
        return model_objects


class PeopleResource(resources.ModelResource):
    name = Field(column_name='Имя', attribute='name')
    age = Field(column_name='Возраст', attribute='age')
    email = Field(column_name='Почта', attribute='email')
    city = fields.Field(column_name='Город', attribute='city',
                        widget=ForeignKeyWidgetWithCreation(City, field='name', create=True))
    skill = fields.Field(column_name='Умения', attribute='skill',
                         widget=ManyToManyWidgetWithCreation(Skill, field='name', separator=', ', create=True))
    is_active = Field(column_name='Автивно', attribute='is_active', default=False)

    class Meta:
        model = People
        fields = 'name', 'age', 'email', 'city', 'skill', 'is_active'
        export_order = 'name', 'age', 'email', 'city', 'skill', 'is_active'  # порядок экспорта полей
        import_id_fields = 'name',  # поля для определения идентификатора
        exclude = 'id',  # исключить поле
        # force_init_instance = False  # Если установлено значение True, этот параметр предотвратит проверку базы данных на наличие существующих экземпляров при импорте. Включение этого параметра повышает производительность, если ваш набор данных импорта гарантированно содержать новые экземпляры.
