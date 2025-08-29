class AstaData:
    def __init__(self):
        self.nomeasta = ""
        self.numerogioc = 0
        self.budget = 0
        self.nomigiocatori = []

    def setdata(self, nomeast, numerogio, budge, nomigiocator):
        self.nomeasta = nomeast
        self.numerogioc = numerogio
        self.budget = budge
        self.nomigiocatori = nomigiocator

    def getdata(self):
        print("DATI:")
        print("Nome asta:", self.nomeasta)
        print("Numero giocatori:", self.numerogioc)
        print("Budget:", self.budget)
        print("Nomi giocatori:", self.nomigiocatori)
        return self.nomeasta,self.numerogioc,self.budget,self.nomigiocatori
