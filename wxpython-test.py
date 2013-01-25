#!/usr/bin/env python

import wx

class MainWindow(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.InitUI()
		self.SetSize((400, 250))
		self.Show()

	def InitUI(self):
		panel = wx.Panel(self)

		wx.StaticBox(panel, label='Static Box', pos=(5, 5), size=(390, 85))

		wx.StaticText(panel, label='Box is Box:', pos=(15, 30))
		text_firstname = wx.TextCtrl(panel, pos=(95, 26), size=(290, 25))

if __name__ == '__main__':
	app = wx.App()
	MainWindow(None, title="Buttons", style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
	app.MainLoop()
