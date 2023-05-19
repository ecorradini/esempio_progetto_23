from PyQt6.QtWidgets import QWidget
from PyQt6 import uic

from listaservizi.view.vista_lista_servizi import VistaListaServizi


class VistaHome(QWidget):
    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)
        uic.loadUi('home/vistahome.ui', self)

        self.servizi_button.clicked.connect(self.go_lista_servizi)

    def go_lista_servizi(self):
        self.vista_lista_servizi = VistaListaServizi()
        self.vista_lista_servizi.show()