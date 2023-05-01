from PyQt5.QtWidgets import QAction, QMenu

from means import MyMean

listMeans = [
    MyMean.MyMean("文字", "word", desc="文字处理"),
    MyMean.MyMean("表格", "excel", children=[
        MyMean.MyMean("sheet分割", "sheet"),
    ], desc="表格处理"),
]


def toMean(parent):
    mean = QMenu("office", parent)
    if len(listMeans) == 0:
        mean.addAction("office")
    for item in listMeans:
        if len(item.children) > 0:
            impMenu = QMenu(item.title, parent)
            childActions = []
            for child in item.children:
                impAct = QAction(child.title, parent)
                childActions.append(impAct)
            impMenu.addActions(childActions)
            mean.addMenu(impMenu)
            pass
        else:
            itemAction = QAction(item.title)
            mean.addAction(itemAction)
            pass
    return mean


if __name__ == '__main__':
    print(listMeans)
