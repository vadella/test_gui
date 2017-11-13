from PySide import QtCore
from PySide.QtCore import Qt
from test_gui.my_video_library import VideoLibrary


# http://w3cgeek.com/pyside-qtableview-example.html


class VideoLibraryModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, video_library: VideoLibrary):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._video_library = video_library

    def rowCount(self, parent):
        return len(self._video_library)

    def columnCount(self, parent):
        return len(self._video_library.header)

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self._video_library.data[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._video_library.header[col]
        return None

    def update_library(self, video_library: VideoLibrary):
        self.reset()
        # self.endRemoveRows()
        self.beginInsertRows(QtCore.QModelIndex(), 0, len(video_library) - 1)
        self._video_library = video_library
        self._data = [i for i in video_library.stream_info]
        self.endInsertRows()
        print(video_library)
        # self.dataChanged.emit(QtCore.QModelIndex(), QtCore.QModelIndex())
