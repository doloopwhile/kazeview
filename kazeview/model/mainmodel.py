from PySide.QtCore import (
    QObject,
    Signal,
)

from PySide.QtGui import (
    QImage,
)

import kazeview.util.method as method

@method.getter('path')
@method.eq_by_attr('path')
class ImageLoadError(OSError):
    def __init__(self, path):
        super().__init__()
        self._path = path


@method.getter('image')
class MainModel(QObject):
    imageChanged = Signal(QImage)
    imageLoadError = Signal(str)

    def openImage(self, path):
        try:
            image = self._loadImage(path)
        except self.LoadImageError:
            self.imageLoadError.emit(path)
        else:
            self._image = image
            self.imageChanged.emit(QImage(image))

    def _loadImage(self, path):
        image = QImage()
        if not image.load(path):
            raise ImageLoadError(path)
        else:
            return image

    def image(self):
        return self._image


def application():
    return QApplication([])
