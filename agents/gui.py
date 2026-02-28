import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QColor, QPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ollama Assistant")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())