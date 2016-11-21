import wx

class Example(wx.Frame):
	def __init__(self, title):
		super(Example, self).__init__(None, title = title, size = (250, 250))
		self.Centre()
		self.Show()
		dc = wx.ClientDC(self)
		dc.DrawLine(50, 60, 190, 60)

if __name__ == '__main__':
	app = wx.App()
	Example('Line')
	app.MainLoop()
