import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip, QMainWindow, 
#     QPushButton, QApplication, QMessageBox, QDesktopWidget,
#     QAction, qApp)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class Button(QPushButton):
  
    def __init__(self, title, parent):
        super().__init__(title, parent)
        
        self.setAcceptDrops(True)
        

    def dragEnterEvent(self, e):
      
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        
        self.setText(e.mimeData().text())
    
    def mouseMoveEvent(self, e):

        if e.buttons() != Qt.RightButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)


    def mousePressEvent(self, e):
      
        super().mousePressEvent(e)
        
        if e.button() == Qt.LeftButton:
            print('press')

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.statusBar().showMessage('Ready')
        self.resize(500, 300)
        self.center()
        self.setWindowTitle('RatTrack')
        self.setWindowIcon(QIcon('sleepwaveripples.png'))        
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 100)       
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 100)
        self.statusBar().showMessage('Ready')
        exitAct = QAction(QIcon('long_evans_bear.png'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        impMenu = QMenu('Import', self)
        impAct = QAction('Import Video', self) 
        impMenu.addAction(impAct)
        
        newAct = QAction('New', self)        
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
        
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        viewMenu.addAction(viewStatAct)

        self.lbl = QLabel("Methodology", self)

        combo = QComboBox(self)
        combo.addItem("Bifurcation")
        combo.addItem("Neural Network")

        combo.move(150, 50)
        self.lbl.move(50, 50)

        combo.activated[str].connect(self.onActivated)

        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(150, 150)

        button = Button("Video", self)
        button.move(50, 150)

        self.button = Button('DD2', self)
        self.button.move(150, 250)

        self.show()
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self) :
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def toggleMenu(self, state):
        
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
        
    def contextMenuEvent(self, event):
       
        cmenu = QMenu(self)
        
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            qApp.quit()
    
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()

    def dragEnterEvent(self, e):
      
        e.accept()
        

    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

