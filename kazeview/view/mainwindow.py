from PySide.QtGui import (
    QMainWindow,
    QWidget,
    QToolBar,
)

from kazeview.view.mainimageview import (
    MainImageView,
)


class MainWindow(QMainWindow):
    def __init__(self, *, model):
        super().__init__()
        self._model = model

        self._imageView = MainImageView(model=self._model)
        self.setCentralWidget(self._imageView)

        self.addToolBar(ToolBar())

