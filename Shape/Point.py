import math
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __sub__(self, other):
		return Point(self.x - other.x, self.y - other.y)
	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	@property
	def xy(self):
		return (self.x, self.y)
	def __str__(self):
		return "x={0}, y={1}".format(self.x, self.y)
	def __repr__(self):
		return str(self.xy)
	
	def dist(a, b):
		return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

if __name__ == '__main__':
	a = Point(1, 2)
	b = Point(3, 4)
	c = a + b
	d = a - b
	print a, b, c, d
	print a.xy
	print str(a)
	print repr(a)
	print a.dist(b)
