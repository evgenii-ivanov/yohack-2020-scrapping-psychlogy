from django.contrib.auth.models import User
from .models import UserCharacteristics
import numpy as np

def get_probability(user, partner):
    sum = abs(user.b5_consc - partner.b5_consc)
    sum += abs(user.b5_extr - partner.b5_extr)
    sum += abs(user.b5_open - partner.b5_open)
    sum += abs(user.b5_consc - partner.b5_consc)
    sum += abs(user.b5_consc - partner.b5_consc)
    sum /= 5
    return sum

def get_partners(user):
    partners = UserCharacteristics.objects.all()
    return partners
    #probability = []
    #for partner in partners:
    #    probability.append(get_probability(user, partner))
    #return np.random.choice(partners, size=20, p=probability)
