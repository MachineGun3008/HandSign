# import NumberAK as n
# import VideoStream as vid
from Number import Number
from VideoStream import VideoStream
from Sentence import Sentence
from CommonSentence import CommonSentence
import os


# a = Number()
# paths = a.FromTextToNumber('-100.02')
# print(paths)
# a = Sentence()
# paths = a.FromTextToVid('I have a family')
# print(paths)
# vd = VideoStream()
# vd.DisplayVideo(paths)
# paths = ['number\\dot']
# vd = VideoStream()
# vd.DisplayVideo(paths)
# print(os.path.isfile('data\\words\\PRON\\i.mp4'))

text = 'I have 20 cent'

CS = CommonSentence()
S = Sentence()
N = Number()
vd = VideoStream()

paths = CS.FindPath(text)

if paths != None:
	print(paths)
	vd.DisplayVideo(paths)
else:
	paths = S.FromTextToVid(text)
	print(paths)
	vd.DisplayVideo(paths)


# a = CommonSentence()
# paths = a.FindPath('Nice to meet you')
# print(paths)
# vd = VideoStream()
# vd.DisplayVideo(paths)