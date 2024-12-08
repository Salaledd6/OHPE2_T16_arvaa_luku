# pip install PySide6
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Arvaaluku(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Arvaa luku")
        self.setGeometry(200,200,350,200)

        self.luku = random.randint(1,10)

        self.alustaIkkuna()
    
    def alustaIkkuna(self):
        self.e1 = QLabel("Arvaa luku väliltä 1-10:", self)
        self.e1.setGeometry(10,10,150,30)

        self.t1 = QLineEdit(self)
        self.t1.setGeometry(10,40,150,30)
        self.t1.returnPressed.connect(self.tarkista_arvaus)

        self.p1 = QPushButton("Arvaa", self)
        self.p1.setGeometry(10,70,150,30)
        self.p1.clicked.connect(self.tarkista_arvaus)

        self.e2 = QLabel(self)
        self.e2.setGeometry(10,100,150,30)
        
    def tarkista_arvaus(self):
        self.arvattu_luku = int(self.t1.text())
        self.t1.clear()
        self.t1.setFocus()

        if self.arvattu_luku == self.luku:
            self.e2.setText("Jee, arvasit oikein!")
        else:
            self.e2.setText("Väärin meni")


def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Arvaaluku() # olio luokasta Arvaaluku, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()