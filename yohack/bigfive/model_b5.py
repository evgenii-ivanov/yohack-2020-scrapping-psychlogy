import ktrain
from ktrain import text as txt
import pickle
import json
import numpy as np
import pymorphy2
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import pymorphy2
import math

class DetectorText():
    
    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer()
        self.model_agree = txt.load_model('models/model_b5_agree')
        self.model_consc = txt.load_model('models/model_b5_consc')
        self.model_extr = txt.load_model('models/model_b5_extr')
        self.model_neur = txt.load_model('models/model_b5_neur')
        self.model_open = txt.load_model('models/model_b5_open')
        #self.preproc = pickle.load(open('models/model_b5.preproc', 'rb'))
        
    def _extract_features(self, text):
        len_sents, len_words = len(sent_tokenize(text)), len(word_tokenize(text))
        avg_sent = len_sents/len_words
        words = re.findall('\w+-?\w+', text)
        caps = len(re.findall('[A-Z]+', text))/len(words)
        excl = re.findall('[\?!]+', text)
        words_num, excl_num = len(words), len(excl)/len_sents

        tags = [self.morph.parse(word)[0].tag for word in words]
        pos = [tag.POS for tag in tags]
        verbs = (pos.count('VERB') + pos.count('PRTS') + pos.count('PRTF'))/len(words)
        nouns = pos.count('NOUN')/len(words)
        other_pos = (pos.count('INTJ') + pos.count('PRCL'))/len(words)
        per1, per3 = sum(['1per' in el for el in tags])/words_num, sum(['3per' in el for el in tags])/words_num

        return np.array([[avg_sent, caps, excl_num, verbs, nouns, other_pos, per1, per3]])
    
    def get_b5(self, text):
        '''
        Args:
            text (str): текст для определения черт
            
        Return:
            preds (dict): словарь с чертами и соответствующими предсказаниями
        '''
        feats = self._extract_features(text)
        _, prepr, _ = txt.texts_from_array(x_train=[text], y_train=[''], x_test=[text], y_test=[''], maxlen=300)
        data_pred = [feats] + [prepr[0]]
        
        preds = (self.model_agree.predict(data_pred),self.model_extr.predict(data_pred),
                 self.model_consc.predict(data_pred),self.model_neur.predict(data_pred),
                 self.model_open.predict(data_pred))
        preds = dict(zip(('agree', 'extr', 'consc', 'neur', 'open'), map(float,map(np.squeeze, preds))))
        return preds
    
#образец вызова модели    
#dt = DetectorText()
#dt.get_b5(text)