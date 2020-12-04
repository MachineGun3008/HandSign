# import NumberAK as n
# import VideoStream as vid
from Number import Number
from VideoStream import VideoStream

a = Number()
paths = a.FromTextToNumber('-100.02')
# print(paths)
vd = VideoStream()
vd.DisplayVideo(paths)
# paths = ['number\\dot']
# vd = VideoStream()
# vd.DisplayVideo(paths)