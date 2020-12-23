import cv2
# from Sentence import Sentence
class VideoStream:
	def __init__(self):
		self.prefix = 'data\\'
		# self.suffix = '.mp4'
	def DisplayVideo(self, paths):
		for path in paths:
			cap = cv2.VideoCapture(path)
			if not cap.isOpened():
				print('Can not open {0}'.format(path))
				continue
			while cap.isOpened():
				ret, frame = cap.read()
				if ret == True:
					cv2.imshow('Frame', frame)

					if cv2.waitKey(25) & 0xFF == ord('q'):
						break

				else:
					# print('Fail in {0}'.format(path))
					break

			cap.release()

		cv2.destroyAllWindows()