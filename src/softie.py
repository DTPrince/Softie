"""
### License
## MIT License
##
## Copyright (c) 2020 Derek Prince
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

### Status
## 8/18/2020 Start Development

"""

import sys, json

from pathlib import Path
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QCheckBox, \
    QGridLayout, QTabWidget, QVBoxLayout, QPushButton, QMenu, QFileDialog, QDialog
from PyQt5.QtCore import Qt, QSize, pyqtSlot, QCoreApplication


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize Tabs
        self.tabs = QTabWidget()
        self.tabSRE = QWidget()
        self.tabBV = QWidget()
        self.tabTemp = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tabSRE, "Soft Reserve Explorer")
        self.tabs.addTab(self.tabBV, "Boss View")
        self.tabs.addTab(self.tabTemp, "Don't remember")

        # Create first tab
        self.tabSRE.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tabSRE.layout.addWidget(self.pushButton1)
        self.tabSRE.setLayout(self.tabSRE.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Softie Soft Reserve Helper")
        # self.setWindowIcon(QIcon("pics/icons/window_icon.png"))

        # Set up table for tab widgets
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        # Set up toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        # toolbar actions
        button_action_File = QPushButton("&File", self)
        button_action_File.setStatusTip("File")
        toolbar.addWidget(button_action_File)

        # file menu in file->...
        fileMenu = QMenu()

        # import menu in file->import->...
        importMenu = fileMenu.addMenu('Import')
        importSRAction = QAction('Import Soft Reserves', self)
        importSRAction.setShortcut('Ctrl+I')
        importSRAction.setStatusTip('Import a csv soft reserve sheet')
        importSRAction.triggered.connect(self.importSR)
        importMenu.addAction(importSRAction)

        importRosterAction = QAction('Import Roster', self)
        importRosterAction.setShortcut('Ctrl+Shift+I')
        importRosterAction.setStatusTip('Import a roster from Exorsus')
        # importRoster.triggered.connect()
        importMenu.addAction(importRosterAction)

        importRaidAction = QAction('Load Raid', self)
        importRaidAction.setShortcut('Ctrl+L')
        importRaidAction.setStatusTip('Load an old or saved raid configuration')
        # importRaid.triggered.connect()
        importMenu.addAction(importRaidAction)

        newRaidAction = QAction('New Raid', self)
        newRaidAction.setShortcut('Ctrl+N')
        newRaidAction.setStatusTip('Create a new raid')
        # newRaidAction.triggered.connect(self.newRaid)
        fileMenu.addAction(newRaidAction)
        fileMenu.addMenu(importMenu)

        saveRaidAction = QAction('Save', self)
        saveRaidAction.setShortcut('Ctrl+S')
        saveRaidAction.setStatusTip('Save current raid')
        saveRaidAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveRaidAction)

        aboutAction = QAction('Action', self)
        aboutAction.setStatusTip('About')
        # aboutAction.trigger.connect()
        fileMenu.addAction(aboutAction)

        helpAction = QAction('Help', self)
        helpAction.setShortcut('Ctrl+/')
        helpAction.setStatusTip('Display help and hot keys')
        # helpAction.trigger.connect()
        fileMenu.addAction(helpAction)

        button_action_File.setMenu(fileMenu)

        # debug/convenience
        fileMenu.triggered.connect(lambda action: print(action.text()))

        button_action_Save = QAction(QIcon("pics/icons/disk.png"), "", self)
        button_action_Save.setStatusTip("Save")
        button_action_Save.triggered.connect(self.saveFile)
        toolbar.addAction(button_action_Save)

        self.setStatusBar(QStatusBar(self))
        self.setGeometry(300, 200, 800, 600)

    def contextMenuEvent(self, event):
        print("Context menu event!")

    def importSR(self, s):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        print(fname)
        if fname[0]:
            print("File name: ", fname[0])

    def saveFile(self, s):
        print("Save here", s)
        name = QFileDialog.getSaveFileName(self, 'Save File')
        if name[0]:
            file = open(name[0], 'w')
            # Prepare the json here and file dump it
            text = "tesssssst"
            file.write(text)
            file.close()

    def newRaid(self):
        print("Test")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
