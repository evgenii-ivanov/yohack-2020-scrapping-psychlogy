from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserCharacteristics
from . import utils
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
    partners = utils.get_partners(UserCharacteristics.objects.all().first())
    context = {
        'partners' : partners,
        'title' : 'Search'
    }
    return render(request, 'yohack/search.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}'.format(username))
            return redirect('login')
    return render(request, 'yohack/register.html', {'form' : form})

@login_required
def profile(request):
    return render(request, 'yohack/profile.html')