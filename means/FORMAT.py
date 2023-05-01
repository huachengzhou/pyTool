from PyQt5.QtWidgets import QAction, QMenu

from means import MyMean

listMeans = [

]


def toMean(parent):
    mean = QMenu("格式化操作", parent)
    if len(listMeans) == 0:
        mean.addAction("格式化操作")
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
            itemAction = QAction(item.title, parent)
            mean.addAction(itemAction)
            pass
    return mean


if __name__ == '__main__':
    print(listMeans)
