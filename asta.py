#asta.py
from astadata import AstaData
from PyQt6.QtWidgets import QWidget,QTextEdit,QTableView,QLineEdit,QPushButton,QVBoxLayout,QTableWidget,QTableWidgetItem
from PyQt6.QtCore import QProcess
class Asta(QWidget):
    def __init__(self,dati):
        super().__init__()
        self.dati = dati
        nome,numero,budget1,giocatori="",0,0,[]
        nome,numero,budget1,giocatori=dati.getdata()
        self.numero=numero
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
        self.process.finished.connect(self.processo_terminato)


        self.show()
    
    def leggi_output(self):
        dati = self.process.readAllStandardOutput().data().decode("utf-8")
        self.output.append(dati)

    def invia_comando(self):
        comando = self.input.text()
        self.process.write((comando + "\n").encode("utf-8"))
        self.input.clear()

    def processo_terminato(self):
     self.blocco_squadre = []
     self.righe_per_squadra = 29
    # Apri il file generato dal processo
     try:
       with open("asta.txt", "r", encoding="latin-1") as f:
         righe = [r.strip() for r in f.readlines() if r.strip()]
         for i in range(0, len(righe), self.righe_per_squadra):
           blocco = righe[i:i+self.righe_per_squadra]  # prendi 29 righe alla volta
         if blocco:
            self.blocco_squadre.append(blocco)
     except FileNotFoundError:
      self.output.append("File asta.txt non trovato!")
     tab = QTableWidget()
     self.lay.addWidget(tab)
     tab.setColumnCount(self.numero)
     tab.setRowCount(self.righe_per_squadra)
     

     for col, squadra in enumerate(self.blocco_squadre):
        for row, riga in enumerate(squadra):
            tab.setItem(row, col, QTableWidgetItem(riga))
    
    
    
    
   

        


       