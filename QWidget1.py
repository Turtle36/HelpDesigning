import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QBoxLayout

class fawwaz(QWidget):
    def __init__(self):
        super(fawwaz, self).__init__()
        self.main()
    def main(self):
        self.resize(200, 100)
        self.move(300, 300)
        self.setWindowTitle("Internalium")

        self.entry = QLineEdit()
        self.entry.setText("")

        self.entry2 = QLineEdit()
        self.entry2.setText("")

        self.button1 = QPushButton('Exit')
        self.button2 = QPushButton('Clear')

        self.button1.clicked.connect(self.ButtonClick1)
        self.button2.clicked.connect(self.ButtonClick2)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)

        layout = QVBoxLayout()
        layout.addWidget(self.entry)
        layout.addWidget(self.entry2)
        layout.addLayout(hbox)
        self.setLayout(layout)
    def ButtonClick1(self):
        self.close()
    def ButtonClick2(self):
        self.entry.setText("")
        self.entry2.setText("")

if __name__ == '__main__':
    a = QApplication(sys.argv)

    b = fawwaz()
    b.show()

    a.exec_()