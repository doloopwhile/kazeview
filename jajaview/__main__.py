#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from .qt_compat import qt_import
qt_import('QWidget QApplication')
# class MainImageView(QWidget):
#     pass

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.show()
    app.exec_()


if __name__ == '__main__':
    main()

