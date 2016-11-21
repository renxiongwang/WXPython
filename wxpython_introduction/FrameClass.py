import wx
class Example(wx.Frame):
	def __init__(self, title):
		super(Example, self).__init__(None, title = title, size = (600, 400))
		self.Centre()
		self.Show()
if __name__ == "__main__":
	app = wx.App()
	Example('Shapes')
	app.MainLoop()
