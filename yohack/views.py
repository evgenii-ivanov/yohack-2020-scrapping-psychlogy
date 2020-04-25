from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'yohack/home.html')

developers = [
    {
        'name' : 'Evgeniy Ivanov',
        'age' : 19
    },
    {
        'name' : 'Pavel Klimovskoy',
        'age' : 20
    }
]

def about(request):
    context = {
        'developers' : developers
    }
    return render(request, 'yohack/about.html', context)