from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import UserCharacteristics
#from services.user_service import all


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

class PartnerListView(ListView):
    model = UserCharacteristics
    template_name = 'yohack/search.html'
    context_object_name = 'partners'

def about(request):
    context = {
        'developers' : User.objects.all()
    }
    return render(request, 'yohack/about.html', context)

def search(request):
    return render(request, 'yohack/search.html')