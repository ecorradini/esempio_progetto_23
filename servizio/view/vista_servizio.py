from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from servizio.controller.controllore_servizio import ControlloreServizio


class VistaServizio(QWidget):

    def __init__(self, servizio, parent=None):
        super(VistaServizio, self).__init__(parent)
        uic.loadUi('servizio/view/servizio.ui', self)
        self.controller = ControlloreServizio(servizio)

        self.labelNome.setText(self.controller.get_nome_servizio())
        self.labelTipo.setText(f"Tipo: {self.controller.get_tipo_servizio()}")
        self.labelPosizione.setText(f"Posizione: {self.controller.get_posizione_servizio()}")
        self.labelPrezzo.setText(f"Prezzo: {self.controller.get_prezzo_servizio()}€")