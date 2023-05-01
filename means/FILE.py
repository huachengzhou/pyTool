from PyQt5.QtWidgets import QAction, QMenu

from means import MyMean

listMeans = [

]


def changeMenuEvent( state):
    print("means.FILE.py","changeMenuEvent", state)

def toMean(parent):
    mean = QMenu("文件", parent)
    if len(listMeans) == 0:
        mean.addAction("文件")
        # mean.triggered.connect(lambda checked: changeMenuEvent(checked))
        pass
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
            # mean.addAction(item.title)
            # print("sdsashas")
            itemAction = QAction(item.title, parent)
            itemAction.triggered.connect(changeMenuEvent)
            mean.addAction(itemAction)
            # mean.triggered[QAction].connect(changeMenuEvent)
            pass
    return mean


if __name__ == '__main__':
    print(listMeans)
