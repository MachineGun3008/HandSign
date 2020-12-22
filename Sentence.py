import nltk
from Number import Number
from Symbol import Symbol
import os
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
# import Number from Number
class Sentence:
    def __init__(self):
        # num = Number()
        self.path = 'data\\'

    def PraseSentence(self, text):
        return nltk.pos_tag(text)
    
    def FromTextToVid(self, text):
        # tokenizer = nltk.RegexpTokenizer(r"\w+")
        # words = tokenizer.tokenize(text)
        tags = nltk.tag.pos_tag(nltk.tokenize.word_tokenize(text), tagset= 'universal')
        
        num = Number()
        sym = Symbol()
        list_path = []
        for pair in tags:
            # list_path.append(self.path + pair[1] + '\\' + pair[0].lower())
            if pair[1] != 'NUM':
                link = self.path + 'words\\' + pair[1] + '\\' + pair[0].lower() + '.mp4'
                if os.path.isfile(link):
                    list_path.append(link)
                else:
                    list_path = list_path + sym.FromTextToSymbol(pair[0])
            else:
                list_path = list_path + num.FromTextToNumber(pair[0])
        return list_path

t = Sentence()
print(t.FromTextToVid('I love you'))