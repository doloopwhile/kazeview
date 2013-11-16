# -*- coding: utf-8 -*-
from PySide import QtCore


@delegate('_changeHistory', 'canUndo canRedo')
class ImageSubModel:
    imageChanged = QtCore.Signal()

    def __init__(self):
        pass

    def _mainModel(self):
        pass

    def _view(self):
        pass

    def openImageFile(self, fileName=None):
        if fileName is None:
            fileName = self._view().askOpenImageFile()
            if fileName is None:
                return

        try:
            self._image = Image.fromFile(fileName)
        except Image.OpenError:
            self._view().notifyImageOpenError()
        self.imageChanged.emit(self._image)

    def saveImageFile(self, fileName=None):
        if fileName is None:
            fileName = self._view().askSaveImageFile()
            if fileName is None:
                return
        try:
            self._image.save(fileName)
        except Image.SaveError:
            self._view().notifyImageSaveError()

    def image(self):
        return self._image

    def changeImage(self, image):
        if image == self._image:
            return
        self._image = image
        self.imageChanged.emit(self._image)

    def canUndo(self):
        pass

    def canRedo(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass


@delegate('_imageSubModel', 'openImageFile saveImageFile'.split())
class MainModel:
    mainImageChanged = QtCore.Signal()

    def __init__(self):
        self._imageSubModel = ImageSubModel()
