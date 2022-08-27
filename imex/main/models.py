from django.db import models


class City(models.Model):
    """Город"""
    name = models.CharField(verbose_name='Название города', max_length=40, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'ГОРОДА'

    def __str__(self):
        return self.name

    def count_people(self):
        return self.peoples.count()

    count_people.short_description = 'Количество людей'


class Skill(models.Model):
    """Умения"""
    name = models.CharField(verbose_name='Умения', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Умения'
        verbose_name_plural = 'УМЕНИЯ'

    def __str__(self):
        return self.name

    def count_people(self):
        return self.peoples.count()

    count_people.short_description = 'Количество людей'


class People(models.Model):
    """Информация о человеке"""
    name = models.CharField(verbose_name='Имя', max_length=20, unique=True)
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='Электронная почта', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Город', related_name='peoples', on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill, verbose_name='Умения', related_name='peoples', blank=True)
    is_active = models.BooleanField(verbose_name='Активный', blank=False)

    class Meta:
        verbose_name = 'Информация о человеке'
        verbose_name_plural = 'ИНФОРМАЦИЯ О ЧЕЛОВЕКЕ'

    def __str__(self):
        return self.name

    def count_skill(self):
        return self.skill.count()

    count_skill.short_description = 'Количество умений'