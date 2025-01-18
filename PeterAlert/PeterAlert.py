import wx
import sys
import os

app = wx.App(False)

########## la ventana ##########

window = wx.Frame(
    None,
    wx.ID_ANY,
    "Peter Alert",
    size=(200, 185),
    style=wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.FRAME_NO_TASKBAR
)
panel = wx.Panel(window)
window.Center()

########## la imagen ##########

if getattr(sys, 'frozen', False):
    route = os.path.join(sys._MEIPASS, "peter.png")
else:
    route = "peter.png"

peter = wx.Image(route, wx.BITMAP_TYPE_PNG)
bitmap = wx.StaticBitmap(panel, bitmap=wx.Bitmap(peter))

########## el boton ##########

boton = wx.Button(panel, label="OK", size=(60, 30))
boton.Bind(wx.EVT_BUTTON, lambda event: window.Close())

########## el sizer ##########

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(bitmap, 0, wx.ALIGN_CENTER | wx.ALL, 10)  
sizer.Add(boton, 0, wx.ALIGN_CENTER | wx.ALL, 10) 
panel.SetSizer(sizer)

########## mostrar la ventana ##########

window.Show()
app.MainLoop()
