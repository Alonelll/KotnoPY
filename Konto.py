class Konto:

    def __init__(self, kontoinhaber, iban, kontostand, zinsen):
        self.name = kontoinhaber
        self.iban = iban
        self.kontostand = kontostand
        self.zinsen = zinsen


class Girokonto(Konto):

    def __init__(self, dispobetrag):
        super().__init__()
        self.dispo = dispobetrag

    def transaction(self, value: float):
        input("welchen Betrag: " + value)
        print(f"Überweisung an: {self.name} IBAN: {self.iban} ein Betrag von {value}")


class Festgeldkonto(Konto):

    def __init__(self, runtime, maxbetrag):
        super().__init__()
        self.runtime = runtime
        self.max = maxbetrag


class Guthabenkonto(Konto):

    def __init__(self, guthaben):
        super().__init__()
        self.money = guthaben

