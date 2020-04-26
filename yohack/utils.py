from django.contrib.auth.models import User
from .models import UserCharacteristics
import numpy as np
from scipy.spatial import distance as ds
from scipy.special import softmax 
import json
from gensim.models import KeyedVectors

model_path = 'model_vector.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True) 

def vectorize_string(interest_string):
    '''
    Args:
        interest_string: строка слов-интересов через пробел
    Return:
        interest_json: json-строку, в которой список векторов слов
    '''
    interest = [model.wv[word] for word in interest_string.split(' ')]
    interest_json = json.dumps(interest)
    return interest_json

class Matcher(): 
    def __init__(self, user):
        self.user = user #UserCharacteristics.objects.all().first()
        self.partners = UserCharacteristics.objects.filter()
    
    def _compare_interests(self, partner):
        user = self.user.interest
        interests_user = np.array(json.loads(user))
        interests_partner = np.array(json.loads(partner))
        return 1-ds.cosine(np.mean(interests_user), np.mean(interests_spartner))
    
    def _compare_spheres(self, partner):
        user = self.user.sphere.split(' ')
        if len(set(user) & set(partner)) == 0:
            return 0     
        else: return 1
    
    def _compare_big5(self, partner):
        big5 = abs(user.b5_consc - partner.b5_consc)
        big5 += abs(user.b5_extr - partner.b5_extr)
        big5 += abs(user.b5_open - partner.b5_open)
        big5 += abs(user.b5_consc - partner.b5_consc)
        big5 += abs(user.b5_consc - partner.b5_consc)
        return 1 - big5/5
    
    def _compare_money(self, partner):
        if self.user.is_startuper == 1:
            return int(self.user.money >= partner)
        else: return int(self.user.money <= partner)
        
    def get_partners(self):
        probs = []
        for partner in self.partners:
            match_interests = self._compare_interests(self, partner.interest)
            match_spheres = self._compare_spheres(self, partner.sphere.split(' '))
            match_big5 = self._compare_big5(self, partner)
            match_money = self._compare_money(self, partner.money)
            probs.append(match_interests + match_spheres + match_big5 + match_money)
            
        probs = softmax(probs)
        return np.random.choice(self.partners, size=min(len(self.partners),10), p=probs, replace=False)
