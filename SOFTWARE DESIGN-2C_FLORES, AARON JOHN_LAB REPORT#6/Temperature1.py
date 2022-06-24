
from Temperature import*
import sys

class Temp(Ui_Main):
    def __init__(self,window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.FtoC)
        self.pushButton_2.clicked.connect(self.CtoF)
        self.textEdit
        self.textEdit_2
    def FtoC(self):
        if self.textEdit & self.textEdit_2 == NULL:
            print("No inputs found")
        else:
            x = self.textEdit.textChanged()
            celcius = x-32
            celcius *= 5
            celcius /= 9
            self.textEdit_2.show(celcius)
        

    def CtoF(self):
        if self.textEdit & self.textEdit_2 == NULL:
                print("No inputs found")
        else:
            y = self.textEdit_2.textChanged()
            f = y*(9/5)
            f +=32
            self.textEdit.show(f)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = Temp(MainWindow)
MainWindow.show()
app.exec()

        
