from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2>Hello, world. <br> Django Import-Export работает, я рад!!!</h2>")
