from abc import ABCMeta, abstractmethod
from Polygon import Polygon
from Point import Point
class RectAngle(Polygon):
	def __init__(self, startPoint, w, h, **kwargs):
		self._w = w
		self._h = h
		Polygon.__init__(self, [startPoint, startPoint + Point(w, 0), startPoint + Point(w, h), startPoint + Point(0, h)], **kwargs)
	def area(self):
		return self._w*self._h
