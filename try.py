import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def main():
    """
    allow you to get size of your courant screen
    -1 is to precise that it is the courant screen
    """
    sizeObject = QDesktopWidget().screenGeometry(-1)
    print(type(sizeObject.height()))
    print(" Screen size : "  + str(sizeObject.height()) + "x"  + str(sizeObject.width()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())
