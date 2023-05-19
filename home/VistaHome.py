from PyQt6.QtWidgets import QWidget
from PyQt6 import uic


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        uic.loadUi('home/vistahome.ui', self)