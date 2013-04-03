#!/usr/bin/env python

import wx

class Window(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)

		self.InitUI()
		self.SetSize((400, 250))
		self.Show()

	def InitUI(self):
		panel = wx.Panel(self)

		button = wx.Button(frame, -1, "Click Me")
if __name__ == '__main__':
	app = wx.App()
	Window(None, title="Buttons", style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
	app.MainLoop()
