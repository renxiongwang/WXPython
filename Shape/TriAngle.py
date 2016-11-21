from Polygon import Polygon
from Point import Point

class TriAngle(Polygon):
	def __init__(self, Points, **kwargs):
		assert len(Points)==3, 'More than 3 Points'
		Polygon.__init__(self, Points, **kwargs)
	def area(self):
		return 10
