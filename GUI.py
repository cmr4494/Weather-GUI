'''
Implements a GUI using wxpython.
'''
import wx
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        self.temperature = wx.StaticText(blem,-1, style = wx.ALIGN_LEFT | wx.ST_ELLIPSIZE_MIDDLE)
        self.CreateStatusBar()  # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menu_about = filemenu.Append(wx.ID_ABOUT, "About", " Information about this program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)
    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, " Weather data tracker made by us","About", wx.OK)
        dlg.ShowModal()  # Shows it
        dlg.Destroy()


app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()





