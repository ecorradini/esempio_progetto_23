class ControlloreServizio():
    def __init__(self, servizio):
        self.model = servizio

    def get_nome_servizio(self):
        return self.model.nome

    def get_tipo_servizio(self):
        return self.model.tipo

    def get_posizione_servizio(self):
        return self.model.posizione

    def get_prezzo_servizio(self):
        return str(self.model.prezzo)