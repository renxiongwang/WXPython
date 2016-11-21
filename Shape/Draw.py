import wx
from  Point import Point
from Polygon import Polygon
from RectAngle import RectAngle
from TriAngle import TriAngle
class Example(wx.Frame):
	def __init__(self, title, shapes):
		super(Example, self).__init__(None, title = title, size = (600, 400))
		self.shapes = shapes
		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Centre()
		self.Show()
	def OnPaint(self, e):
		dc = wx.PaintDC(self)
		for shape in self.shapes:
			dc.SetPen(wx.Pen(shape.color))
			dc.DrawLines(shape.drawPoints())

if __name__ == '__main__':
	prepare_draws = []
	start_p = Point(50, 60)
	a = RectAngle(start_p, 100,80, color = "#ff0000")
	b = TriAngle([Point(50, 60), Point(100, 60), Point(50, 80)], color = "#ff1234")
	prepare_draws.append(a)	
	prepare_draws.append(b)
	for shape in prepare_draws:
		print shape.area()
	app = wx.App()
	Example('Shapes', prepare_draws)
	app.MainLoop()
