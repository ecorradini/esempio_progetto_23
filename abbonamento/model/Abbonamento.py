import time

class Abbonamento():
    def __init__(self, scadenza):
        self.scadenza = scadenza

    def scaduto(self):
        timestamp = int(time.time())
        return timestamp > self.scadenza
