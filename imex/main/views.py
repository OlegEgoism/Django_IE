from django.shortcuts import render
from .models import People, City


def info(request):
    people = People.objects.all()
    city = City.objects.get(name='Орша')
    context = {'people': people, 'city': city}
    return render(request, template_name='info.html', context=context)
