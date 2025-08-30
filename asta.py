#asta.py
from astadata import AstaData
from PyQt6.QtWidgets import QWidget,QTextEdit,QTableView,QLineEdit,QPushButton,QVBoxLayout
from PyQt6.QtCore import QProcess
class Asta(QWidget):
    def __init__(self,dati):
        super().__init__()
        self.dati = dati
        nome,numero,budget1,giocatori="",0,0,[]
        nome,numero,budget1,giocatori=dati.getdata()
        nomi_str = ",".join(giocatori)
        self.setWindowTitle(nome)
        self.resize(400, 350)
        self.lay=QVBoxLayout()
        self.setLayout(self.lay)
        self.output=QTextEdit()
        self.output.setReadOnly(True)
        self.input=QLineEdit()
        self.input.returnPressed.connect(self.invia_comando)
        self.lay.addWidget(self.output)
        self.lay.addWidget(self.input)

        self.process = QProcess(self)
        self.process.setProgram("./asta.sh")
        self.process.setArguments([nome, str(numero), str(budget1), nomi_str])
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.leggi_output)
        self.process.start()

        self.show()
    
    def leggi_output(self):
        dati = self.process.readAllStandardOutput().data().decode("utf-8")
        self.output.append(dati)

    def invia_comando(self):
        comando = self.input.text()
        self.process.write((comando + "\n").encode("utf-8"))
        self.input.clear()

        


       