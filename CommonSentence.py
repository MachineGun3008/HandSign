import os

class CommonSentence:
    def FindPath(self, text):
        words = text.split(' ')
        link =  'data\\sentence\\' + ''.join([i[0].lower() for i in words]) + '.mp4'
        if os.path.isfile(link):
        	return [link]
        else:
        	return None
# a = CommonSentence()
# print(a.FindPath('How Are You?'))