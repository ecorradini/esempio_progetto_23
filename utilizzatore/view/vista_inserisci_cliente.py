from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from utilizzatore.model.Cliente import Cliente


class VistaInserisciCliente(QWidget):

    def __init__(self, controller, callback, parent=None):
        super(VistaInserisciCliente, self).__init__(parent)
        uic.loadUi('utilizzatore/view/vista_inserisci_cliente.ui', self)
        self.controller = controller
        self.callback = callback

        self.btn_ok.clicked.connect(self.add_cliente)

    def add_cliente(self):
        nome = self.textNome.text()
        cognome = self.textCognome.text()
        cf = self.textCodiceFiscale.text()
        indirizzo = self.textIndirizzo.text()
        email = self.textEmail.text()
        telefono = self.textTelefono.text()
        eta = self.textEta.text()
        if nome == "" or cognome == "" or cf == "" or indirizzo == "" or email == "" or telefono == "" or eta == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.controller.aggiungi_cliente(Cliente(
                (nome+cognome).lower(),
                nome,
                cognome,
                cf,
                indirizzo,
                email,
                telefono,
                eta)
            )
            self.callback()
            self.close()