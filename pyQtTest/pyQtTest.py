import sys
from tkinter import Button

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

import sys # Только для доступа к аргументам командной строки
print("i")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Some Title")
        self.setFixedSize(QSize(400,300))
        button1 = QPushButton("Button 1")
        button1.setCheckable(True)
        button1.clicked.connect(self.button1_pressed)
        self.setCentralWidget(button1)

        self.setCentralWidget(button1)

    def button1_pressed(self):
        print("b1 was pressed")

# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()


# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.