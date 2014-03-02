from PySide.QtGui import (
    QWidget,
    QPainter,
    QColor,
)

class MainImageView(QWidget):
    def __init__(self, *, model):
        super().__init__()
        self._model = model
        self._image = None

        model.imageLoadError.connect(print)
        model.imageChanged.connect(self.setImage)

    def setImage(self, image):
        self._image = image
        self.update()

    def paintEvent(self, event):
        if self._image is None:
            return

        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("gray"))
        painter.drawImage(self.rect(), self._image)

