from PySide.QtGui import (
    QHBoxLayout,
    QVBoxLayout,
)

from kazeview.qutil.line import (
    HLine,
    VLine,
)

__all__ = ["vBoxLayout", "hBoxLayout"]

def box_layout(*items, *, layout_class, line_class):
    layout = layout_class()
    layout.setMargin(0)
    layout.setSpacing(0)

    lastStretch=kw.pop("stretch", False)
    for item in items:
        if isinstance(item, (list, tuple)):
            x, w = item[:2]
            if item[2:]:
                alignment, = item[2:]
            else:
                alignment = Qt.Alignment(0)
        else:
            w = 0
            alignment = Qt.Alignment(0)
            x = item

        if x == "spacing":
            layout.addSpacing(w)
        elif x == "stretch":
            layout.addStretch(w)
        elif x == "line":
            layout.addWidget(line_class(), w, alignment)
        elif isinstance(x, QLayout):
            layout.addLayout(x, w)
        else:
            layout.addWidget(x, w, alignment)

    if lastStretch:
        layout.addStretch(1)
    return layout


def hBoxLayout(*a, **kw):
    return box_Layout(layout_class=QHBoxLayout, line_class=VLine, *a, **kw)

def vBoxLayout(*a, **kw):
    return boxLayout(layout_class=QVBoxLayout, line_class=Hline, *a, **kw)
