import datetime
import os
import pickle
from unittest import TestCase

from Attività.Cliente import Cliente

class TestGestioneClienti(TestCase):

    def test_add_cliente(self):
        self.cliente = Cliente()
        self.cliente.aggiungiCliente("note", [], 345, "Eren", "Jaeger", datetime.datetime(1989, 10, 20),
                                     "prova", "prova", 1)
        clienti = None
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn(1, clienti)

    def test_rimuovi_cliente(self):
        clienti = None
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn(1, clienti)
        self.cliente.rimuoviCliente()
        self.assertIsNotNone(clienti)
        self.assertNotIn(1, clienti)
