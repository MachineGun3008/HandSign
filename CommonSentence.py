class CommonSentence:
    def FindPath(self, text):
        words = text.split(' ')
        name =  ''.join([i[0].lower() for i in words]) 
        return ['data\\sentence\\' + name + '.mp4']
# a = CommonSentence()
# print(a.FindPath('How Are You?'))