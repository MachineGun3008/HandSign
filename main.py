# import NumberAK as n
# import VideoStream as vid
from Number import Number
from VideoStream import VideoStream

a = Number()
paths = a.FromTextToUncompleteNumber('123456789')
vd = VideoStream()
vd.DisplayVideo(paths)