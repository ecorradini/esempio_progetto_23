from utilizzatore.model.Utilizzatore import Utilizzatore


class Bagnino(Utilizzatore):
    def __init__(self, id, nome, cognome, cf, indirizzo, email,
                 telefono, datanascita, luogonascita, licenza):
        super(Bagnino, self).__init__(id, nome, cognome, cf, indirizzo, email, telefono)
        self.datanascita = datanascita
        self.luogonascita = luogonascita
        self.licenza = licenza