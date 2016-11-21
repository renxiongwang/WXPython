import wx

app = wx.App()
frame = wx.Frame(None, -1, title = 'wxtest.py', pos = (300, 400), size = (200, 150))

frame.Centre()

frame.Show()

app.MainLoop()
