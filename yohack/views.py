from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserCharacteristics
from .forms import UserUpdateForm, UserCharacteristicsUpdateForm
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

def about(request):
    context = {
        'developers' : User.objects.all()
    }
    return render(request, 'yohack/about.html', context)

@login_required
def search(request):
    matcher = utils.Matcher(request.user.user_characteristics)

    partners = matcher.get_partners()
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
    u_form = UserUpdateForm()
    p_form = UserCharacteristicsUpdateForm()

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'yohack/profile.html', context)