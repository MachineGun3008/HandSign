import nltk
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
        
        list_path = []
        for pair in tags:
            list_path.append(self.path + pair[1] + '\\' + pair[0].lower())
        return list_path

t = Sentence()
print(t.FromTextToVid('I go to school but she comes home'))