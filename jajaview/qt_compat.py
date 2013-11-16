# -*- coding: utf-8 -*-
import inspect

__all__ = ['qt_import']
_name_mappings_str = '''
    Signal QtCore pyqtSignal
    QObject QtCore
    QWidget      QtWidgets
    QApplication QtWidgets
'''

_name_mappings = {
    line.split()[0]: line.split()[1:]
        for line in _name_mappings_str.splitlines() if line.strip()
}

del _name_mappings_str

def qt_import(names):
    if isinstance(names, str):
        names = names.split()

    import_codes = []
    for name in names:
        import_args = _name_mappings[name]
        if len(import_args) == 1:
            import_codes.append('from PyQt5.{} import {}'.format(import_args[0], name))
        elif len(import_args) == 2:
            import_codes.append('from PyQt5.{} import {} as {}'.format(
                import_args[0], import_args[1], name))
        else:
            assert False, (name, import_args)

    frame = inspect.currentframe()
    try:
        # do something with the frame
        exec('\n'.join(import_codes), frame.f_back.f_locals)
    finally:
        del frame
