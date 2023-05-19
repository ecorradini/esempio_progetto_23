from listaservizi.model.lista_servizi import ListaServizi


class ControllerListaServizi():

    def __init__(self):
        self.model = ListaServizi()

    def get_lista_servizi(self):
        return self.model.get_lista_servizi()

    def get_servizio_by_index(self, index):
        return self.model.get_servizio_by_index(index)

    def save_data(self):
        self.model.save_data()