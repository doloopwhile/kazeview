#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from kazeview.view.mainwindow import MainWindow
from kazeview.model.mainmodel import MainModel


def application():
    from PySide.QtGui import QApplication
    return QApplication([])

def parse_args():
    """
    Return parse command line arguments, or show help and exit
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("image_file")
    return parser.parse_args()


def main():
    args = parse_args()

    app = application()
    model = MainModel()
    main_window = MainWindow(model=model)
    model.openImage(args.image_file)
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
