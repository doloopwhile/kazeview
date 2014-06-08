from abc import (
    ABCMeta,
    abstractmethod,
)

from PySide.QtCore import (
    QObject,
    Signal,
)

from kazeview.util import method


@method.getter('currentIndex')
class AbstractImagePathList(QObject, metaclass=ABCMeta):
    changed = Signal()

    @abstractmethod
    def reload(self):
        pass

    def currentPath(self):
        if self.isEmpty():
            raise IndexError
        return self.paths()[self.currentIndex()]

    def count(self):
        return len(self.paths())

    def isEmpty(self):
        return bool(self.paths())

    def moveToPrev(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        self.jumpTo((self._currentIndex + 1) % self.count())

    def moveToNext(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        self.jumpTo((self._currentIndex + 1) % self.count())

    def moveToFirst(self):
        pass

    def moveToLast(self):
        pass

    def jumpTo(self, index):
        if index not in range(self.count()):
            raise IndexError("Index {} is out of range".format(index))
        if self.count() == 1:
            return
        if self._currentIndex == index:
            return
        self._currentIndex = index
        self.changed.emit()


@method.getter("imagePaths")
class DirectoryImagePathList(AbstractImagePathList):
    def __init__(self, directory_path, recursive=False *, model):
        super().__init__(self, DirectoryImagePathListImpl(directory_path, recursive))


class DirectoryImagePathListImpl
    def initialize(self):
        return self._getPaths()

    def reload(self, paths, index):
        currentPath = paths[index]
        newPaths = self._getPaths()

        if newPaths != paths:
            return paths, index

        try:
            newIndex = paths.index(currentPath)
        except IndexError:
            return newPaths, None
        else
            return newPaths, newIndex


    def _getPaths(self):
        match = model.matchExtension
        return list(filter(match, find_files(directory_path, recursive))


def find_files(directory_path, recursive, match):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filename:
            yield os.path.join(dirpath, filename)
        if recursive:
            return
