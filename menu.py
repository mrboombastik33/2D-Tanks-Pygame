import sys
import PyQt6
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QSpinBox, QPushButton, QWidget, QFormLayout
)

from PyQt6.QtCore import Qt

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tank Game Settings")
        self.setGeometry(100, 100, 300, 200)

        # Центральний віджет і макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Макет для введення
        form_layout = QFormLayout()

        # Timer setting
        self.timer_label = QLabel("Кількість секунд:")
        self.timer_spinbox = QSpinBox()
        self.timer_spinbox.setRange(10, 30)  # Minimum 10 seconds, max 10 minutes
        self.timer_spinbox.setValue(120)  # Default value
        form_layout.addRow(self.timer_label, self.timer_spinbox)

        # Tank count setting
        self.tank_count_label = QLabel("Кількість танків:")
        self.tank_count_spinbox = QSpinBox()
        self.tank_count_spinbox.setRange(1, 10)  # Мінімум 1 танк, максимум - невизначено
        self.tank_count_spinbox.setValue(2)  # Дефолтне значення
        form_layout.addRow(self.tank_count_label, self.tank_count_spinbox)

        layout.addLayout(form_layout)

        # Кнопки
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Почати")
        self.quit_button = QPushButton("Вийти")
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.quit_button)
        layout.addLayout(button_layout)

        # Button actions
        self.start_button.clicked.connect(self.start_game)
        self.quit_button.clicked.connect(self.close)

    def start_game(self):
        # Retrieve settings
        timer = self.timer_spinbox.value()
        tank_count = self.tank_count_spinbox.value()

        # For now, just print the settings (or pass them to your game logic)
        print(f"Starting game with timer: {timer} seconds and {tank_count} tanks.")

        # TODO: Integrate with the game class
        self.close()  # Закрити меню та почати гру

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())

