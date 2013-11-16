# -*- coding: utf-8 -*-

qt_import('QObject')

class ChangeHistory(QObject):
    changed = Signal()
    def __init__(self, initial_value, history):
        super.__init__(self)
        self._history = list(history)
        self._pos = 0

    def change(self, value):
        pass

    def currentValue(self)
        return self._history[self._pos]

    def undo():
        self.move(-1)

    def redo():
        self.move(1)

    def canUndo():
        pass

    def canRedo():
        pass

    # private methods
    def _move(self, delta):
        if not self._canMove(delta):
            return
        self._pos += delta
        self.changed.emit(self.currentValue())

    def _canMove(self, delta):
        return in_list_range(self._pos + delta, self._history)
