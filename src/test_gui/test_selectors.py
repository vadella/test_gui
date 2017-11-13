#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we select a file with a
QtGui.QFileDialog and display its contents
in a QtGui.QTextEdit.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PySide import QtGui
from pathlib import Path
from test_gui.my_video_library import VideoLibrary
from test_gui.video_library_gui import VideoLibraryModel


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        video_library_model = VideoLibraryModel(parent=self, video_library=VideoLibrary(None))
        table_view = QtGui.QTableView()
        table_view.setModel(video_library_model)

        self.table = table_view

        # self.textEdit = QtGui.QListWidget()
        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(self.table)
        self.statusBar()

        open_file = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.show_dialog)

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_file)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def show_dialog(self):
        fname = QtGui.QFileDialog.getExistingDirectory(self, 'Open file', )

        mkv_files = Path(fname).glob('**/*.mkv')
        lib = VideoLibrary(mkv_files)

        self.table.model().update_library(lib)
        # self.table.setModel(self.table.model())
        # self.textEdit.addItems(lib.stream_strings)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
