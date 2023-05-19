from utilizzatore.model.Utilizzatore import Utilizzatore


class Cliente(Utilizzatore):
    def __init__(self, id, nome, cognome, cf, indirizzo, email, telefono, eta):
        super(Cliente, self).__init__(id,nome,cognome,cf,indirizzo,email,telefono)
        self.eta = eta
        self.abbonamento = None

    def aggiungi_abbonamento(self, abbonamento):
        self.abbonamento = abbonamento

    def get_abbonamento(self):
        if self.abbonamento.scaduto():
            self.abbonamento = None
            return None
        else:
            return self.abbonamento
