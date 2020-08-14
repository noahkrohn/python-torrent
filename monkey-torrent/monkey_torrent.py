import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

from System.Drawing import *
from System.Windows.Forms import *

class MyForm(Form):
    def __init__(self):
        # Define the Window title and window size
        self.Text = 'Monkey Torrent'
        self.Size = Size(500, 500)
        self.Icon = Icon("favicon.ico")

        # Create the menus
        menuStrip = MenuStrip()
        menuItemFile = ToolStripMenuItem("File")
        menuStrip.Items.Add(menuItemFile)
        menuItemOptions = ToolStripMenuItem("Options")
        menuStrip.Items.Add(menuItemOptions)
        menuItemHelp = ToolStripMenuItem("Help")
        menuStrip.Items.Add(menuItemHelp)

        # Create the File submenus
        submOpenFile = ToolStripMenuItem("Add Torrent from File...")
        menuItemFile.DropDownItems.Add(submOpenFile)
        submOpenURL = ToolStripMenuItem("Add Torrent from URL...")
        menuItemFile.DropDownItems.Add(submOpenURL)
        submOpenMagnet = ToolStripMenuItem("Add Magnet Link...")
        menuItemFile.DropDownItems.Add(submOpenMagnet)
        menuItemFile.DropDownItems.Add(ToolStripSeparator())
        submCreateTorrent = ToolStripMenuItem("Create Torrent...")
        menuItemFile.DropDownItems.Add(submCreateTorrent)
        menuItemFile.DropDownItems.Add(ToolStripSeparator())
        submExit = ToolStripMenuItem("Exit")
        menuItemFile.DropDownItems.Add(submExit)
        submExit.Click += self.OnExit
        
        # Add menu to top
        self.Controls.Add(menuStrip)
        self.MainMenuStrip = menuStrip

        # Create child controls and initialize form
        pass

    def OnExit(self, sender, event):
        self.Close()

Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

frmMain = MyForm()
Application.Run(frmMain)
