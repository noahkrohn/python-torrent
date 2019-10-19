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

        # Create the menus
        menuStrip = MenuStrip()
        menuItemFile = ToolStripMenuItem("File")
        menuStrip.Items.Add(menuItemFile)
        menuItemTools = ToolStripMenuItem("Tools")
        menuStrip.Items.Add(menuItemTools)

        # Create the File submenus
        submNew = ToolStripMenuItem("New")
        menuItemFile.DropDownItems.Add(submNew)
        submOpen = ToolStripMenuItem("Open")
        menuItemFile.DropDownItems.Add(submOpen)
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
