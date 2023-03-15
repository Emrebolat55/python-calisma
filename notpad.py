import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QRadioButton,QLabel,QPushButton,QVBoxLayout,QFileDialog,QTextEdit,QHBoxLayout
from PyQt5.QtWidgets  import QAction,qApp,QMainWindow


class Notepad(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init__ui()
        
    def init__ui(self):
        
        self.yazı_alanı = QTextEdit()
        
        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("kaydet")
        
        h_box = QHBoxLayout()
        
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        
        v_box = QVBoxLayout()
        
        v_box.addWidget(self.yazı_alanı),
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("NotePad")
        
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
    
    def yaziyi_temizle(self):
        self.yazı_alanı.clear()
        
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(dosya_ismi[0],"r") as file:
            self.yazı_alanı.setText(file.read())        
        
    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        
        with open(dosya_ismi[0],"w") as file:
            
            file.write(self.yazı_alanı.toPlainText())

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()


        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)


        self.menuleri_olustur()
    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç",self) # menü bar oluşturma
        dosya_ac.setShortcut("Ctrl+O") # kısa yol belirlemek için

        dosya_kaydet = QAction("Dosya Kaydet",self) # menübar oluşturma

        dosya_kaydet.setShortcut("Ctrl+S") #kısayol ekleme

        temizle = QAction("Dosyayı Temizle",self) #menübar ekleme
        temizle.setShortcut("Ctrl+D") # kısayol ekleme

        cikis = QAction("Çıkış",self) # menübar ekler

        cikis.setShortcut("Ctrl+Q") #kısayolunu ekler
        
        #yukarıdaki ifadeleri pencereye ekler 
        dosya.addAction(dosya_ac) 
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response) # hangi actiona basıldığını öğrenmek için


        self.setWindowTitle("Metin Editörü")

        self.show()

    def response(self,action):

        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()

        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosyayı Temizle":
            self.pencere.yaziyi_temizle()

        elif action.text() == "Çıkış":
            qApp.quit()








app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())