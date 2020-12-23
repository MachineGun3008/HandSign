# import NumberAK as n
# import VideoStream as vid
from Number import Number
from VideoStream import VideoStream
from Sentence import Sentence
import os

# a = Number()
# paths = a.FromTextToNumber('-100.02')
# print(paths)
a = Sentence()
paths = a.FromTextToVid('I am going to school')
vd = VideoStream()
vd.DisplayVideo(paths)
# paths = ['number\\dot']
# vd = VideoStream()
# vd.DisplayVideo(paths)
# print(os.path.isfile('data\\words\\PRON\\i.mp4'))