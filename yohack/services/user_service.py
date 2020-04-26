from django.contrib.auth.models import User
from ...models import UserCharacteristics

def all():
    return User.objects.all()