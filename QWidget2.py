import sys

from PyQt5.QtWidgets import QLineEdit ,QWidget, QHBoxLayout, QApplication, QVBoxLayout, QLabel
class fawwaz(QWidget):
    def __init__(self):
        super().__init__()
        self.main()
    def main(self):
        self.resize(200, 100)
        self.move(300, 300)
        self.entry = QLineEdit()
        self.entry.setText("Text...")

        self.label = QLabel()
        self.label.setText("Masukkan Text: ")

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        hbox.addWidget(self.entry)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addLayout(hbox)
        self.setLayout(layout)

if __name__ == '__main__':
    a = QApplication(sys.argv)

    b = fawwaz()
    b.show()

    a.exec_()