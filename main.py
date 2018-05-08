import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class GazeUI(QMainWindow, QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Screen Dimensions

        screenSize = QDesktopWidget().screenGeometry(-1)

        # Frames

        mainFrame = QFrame(self)
        mainFrame.resize((screenSize.width() / 2) + 20, (screenSize.height() / 2) + 20)
        mainFrame.move(70, 170)
        mainFrame.setFrameShape(QFrame.StyledPanel)

        # Main Radiograph

        mainRad = QLabel(self)
        radioGraph = QPixmap('CXR91_IM-2415-2001.jpg')
        mainRad.resize(screenSize.width() / 2, screenSize.height() / 2)
        mainRad.setGeometry(80, 180, screenSize.width() / 2, screenSize.height() / 2)
        mainRad.setPixmap(radioGraph.scaled(mainRad.size()))

        # Texts and Labels

        curDisease = QLabel('<b>Condition : </b>', self)
        curDisease.setGeometry(80, 115, 300, 50)
        curDisease.setFont(QFont('Times', 10))

        disease = QLabel('Cardiomegaly', self)
        disease.setGeometry(230, 113, 150, 50)
        disease.setFont(QFont('Monospace', 10))

        curName = QLabel('<b>Current Image : </b>', self)
        curName.setGeometry(80, 80, 150, 50)
        curName.setFont(QFont('Times', 10))
        curName.setToolTip('Radiograph name')
        curName.setStatusTip('Name of current Radiograph')

        imgName = QLabel('CXR11_IM-0067-1001-1001', self)
        imgName.setGeometry(230, 80, 300, 50)
        imgName.setFont(QFont('Monospace', 10))
        imgName.setToolTip('Radiograph name')
        imgName.setStatusTip('Name of current Radiograph')

        metrics = QLabel('<b>Accuracy Metrics</b>', self)
        metrics.setGeometry(1800, 100, 300, 50)
        metrics.setFont(QFont('Times', 15))
        metrics.setToolTip('Accuracy metrics for various diseases')
        metrics.setStatusTip('Accuracy vs Number of samples for various diseases')

        # Tooltip insertion and modification

        QToolTip.setFont(QFont('SansSerif', 10))

        # Create menu bar, toolbar and options

        prevAct = QAction(QIcon('previous.png'), 'Next', self)
        prevAct.setShortcut('Ctrl+P')
        prevAct.setStatusTip('Go to Previous Image')
        prevAct.setToolTip('Display Previous Image')

        nextAct = QAction(QIcon('next.png'), 'Next', self)
        nextAct.setShortcut('Ctrl+N')
        nextAct.setStatusTip('Go to Next Image')
        nextAct.setToolTip('Display Next Image')

        exitAct = QAction(QIcon('quit.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Quits the application')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(prevAct)
        self.toolbar.addAction(nextAct)
        self.toolbar.addAction(exitAct)

        menubar = self.menuBar()
        appMenu = menubar.addMenu('Menu')
        appMenu.addAction(exitAct)

        # # Layout
        #
        # hbox = QHBoxLayout(self)
        # hbox.addWidget(label)
        # vbox = QVBoxLayout()
        # vbox.addLayout(hbox)
        #
        # self.setLayout(vbox)

        # Setting Initial Window conditions and Title and Status bar

        self.setGeometry(0, 0, screenSize.width() / 2, screenSize.height() / 2)
        self.setWindowTitle('Gaze Metrics')
        self.setWindowIcon(QIcon('gaze.png'))
        self.center()
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')


        self.show()

    def closeEvent(self, event):
        '''
        Method to trigger quit message when quit(x) is clicked.
        :param event: Take the x click event
        :return: None
        '''

        reply = QMessageBox.question(self, 'Message', "Are you sure to Quit",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        '''
        Method to move the app window to the centre of the screen.
        :return: None
        '''

        # Get screen dimensions and center point.
        scr_dimensions = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        scr_dimensions.moveCenter(center_point)
        self.move(scr_dimensions.topLeft())

    def contextMenuEvent(self, event):
        '''
        Method to add and modify context/popup menu when right clicked with mouse.
        :param event: Mouse click event
        :return: None
        '''

        contexMenu = QMenu(self)

        quitAct = contexMenu.addAction('Quit')
        action = contexMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = GazeUI()
    sys.exit(app.exec_())
