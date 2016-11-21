from abc import ABCMeta, abstractmethod
from Point import Point
class Polygon(object):
	__metaclass__ = ABCMeta
	def __init__(self, points_list, **kwargs):
		for point in points_list:
			assert isinstance(point, Point),"input must be Point type"
		self.points = points_list[:]
		self.points.append(points_list[0])
		self.color = kwargs.get('color', '#000000')
	def drawPoints(self):
		points_xy = []
		for point in self.points:
			points_xy.append(point.xy)
		print points_xy
		return tuple(points_xy)
	def area(self):
		raise("not implement")
	def __lt__(self, other):
		assert isinstance(other, Polygon)
		return self.area < other.area
