from PySide.QtGui import (
    QToolBar,
)

class ToolBar(QToolBar):
    def __init__(self, *, model):
        self._toolBar = QToolBar(parent=self)
        prevImage = self._toolBar.addAction('prev')
        prevImage.triggered.connect(model.moveToPrevImage)

        nextImage = self._toolBar.addAction('next')
        nextImage.triggered.connect(self.moveToNextImage)
