from django.shortcuts import render
from .forms import AddInfoForm
from .models import People, City, Skill


def info(request):
    people = People.objects.all()
    context = {'people': people}
    return render(request, template_name='info.html', context=context)


def add_info(request):
    add_form = AddInfoForm()
    if request.method == 'POST':
        people = People.objects.all()
        # city = City.objects.all()
        add_form = AddInfoForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            context = {
                # 'city': city,
                'people': people,
                'add_form': add_form,
            }
            return render(request, template_name='info.html', context=context)
    context = {
        'add_form': add_form
        }
    return render(request, template_name='add_info.html', context=context)
