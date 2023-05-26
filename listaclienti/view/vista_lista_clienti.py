from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from listaclienti.controller.controller_lista_clienti import ControllerListaClienti
from utilizzatore.view.vista_inserisci_cliente import VistaInserisciCliente


class VistaListaClienti(QWidget):

    def __init__(self, parent=None):
        super(VistaListaClienti, self).__init__(parent)
        uic.loadUi('listaclienti/view/lista_clienti.ui', self)
        self.controller = ControllerListaClienti()

        self.update_ui()

        self.new_button.clicked.connect(self.show_new_cliente)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.controller.get_lista_clienti():
            item = QStandardItem()
            item.setText(f"{cliente.cognome} {cliente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui)
        self.vista_inserisci_cliente.show()