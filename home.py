import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QSpinBox,QTextEdit,QLabel,QLineEdit
from astadata import AstaData
from asta import Asta


app = QApplication(sys.argv)
attuale=None

class NuovWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nuova Asta")
        self.resize(400, 350)
        self.lay=QVBoxLayout()
        self.setLayout(self.lay)
        self.nomeasta=QLineEdit()
        self.nomeast=QLabel("Nome Lega")
        self.giocatori=QSpinBox()
        self.giocator=QLabel("Numero Giocatori")
        self.giocatori.setMinimum(6)
        self.giocatori.setMaximum(20)
        self.budget=QLineEdit()
        self.budge=QLabel("Budget")
        self.nomi=QTextEdit()
        self.nom=QLabel("Nomi dei giocatori. Scrivere Separato da virgola")
        self.ok=QPushButton("Crea asta")
        self.lay.addWidget(self.nomeast)
        self.lay.addWidget(self.nomeasta)
        self.lay.addWidget(self.giocator)
        self.lay.addWidget(self.giocatori)
        self.lay.addWidget(self.budge)
        self.lay.addWidget(self.budget)
        self.lay.addWidget(self.nom)
        self.lay.addWidget(self.nomi)
        self.lay.addWidget(self.ok)
        self.ok.clicked.connect(self.setdata)

    def setdata(self):
        listagioc=self.nomi.toPlainText()
        listagio=[]
        listagio=listagioc.split(",")
        global attuale
        attuale=AstaData()
        attuale.setdata(self.nomeasta.text(),self.giocatori.value(),self.budget.text(),listagio)
        self.asta = Asta(attuale)
        self.asta.show()
        self.close()
       
        

def newf():
    global neww
    neww = NuovWindow()
    neww.show()
    window.close()

# Finestra principale
window = QWidget()
window.setWindowTitle("Astone FANTACALCIONE")
window.resize(400, 100)

nuova = QPushButton("Nuova Asta")
continua = QPushButton("Continua Asta")

lay = QVBoxLayout()
lay.addWidget(nuova)
lay.addWidget(continua)

nuova.clicked.connect(newf)

window.setLayout(lay)
window.show()

sys.exit(app.exec())