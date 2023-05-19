from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listaservizi.controller.controller_lista_servizi import ControllerListaServizi


class VistaListaServizi(QWidget):

    def __init__(self, parent=None):
        super(VistaListaServizi, self).__init__(parent)
        uic.loadUi('listaservizi/view/lista_servizi.ui', self)

        self.controller = ControllerListaServizi()

        self.listview_model = QStandardItemModel(self.list_view)
        for servizio in self.controller.get_lista_servizi():
            item = QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        super(VistaListaServizi, self).closeEvent(event)