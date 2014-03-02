from PyQt4.QtGui import QFrame

class HLine(QFrame):
    def __init__(self, margin=5, parent=None):
        QFrame.__init__(self, parent)
        self.setFrameStyle(QFrame.HLine | QFrame.Sunken)
        self.setFixedHeight(margin*2)

class VLine(QFrame):
    def __init__(self, margin=5, parent=None):
        QFrame.__init__(self, parent)
        self.setFrameStyle(QFrame.VLine | QFrame.Sunken)
        self.setFixedWidth(margin*2)
