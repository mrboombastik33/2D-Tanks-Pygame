import sys
import PyQt6
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QSpinBox, QPushButton, QWidget, QFormLayout
)
from Winners import *
from main import Game

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Ігрові налаштування гри 'Танки'")
        self.setGeometry(100, 100, 300, 200)

        # Центральний віджет і макет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Макет для введення
        form_layout = QFormLayout()

        # Визначення часу на один раунд
        self.timer_label = QLabel("Кількість секунд:")
        self.timer_spinbox = QSpinBox()
        self.timer_spinbox.setRange(10, 60)  # Мінімальна к-сть секунд - 30, максимальна - 60
        self.timer_spinbox.setValue(15)  # Значення за замовчуванням
        form_layout.addRow(self.timer_label, self.timer_spinbox)

        # Вибір раундів
        self.round_count = QLabel("Кількість раундів:")
        self.round_count_spinbox = QSpinBox()
        self.round_count_spinbox.setRange(1, 10)  # Мінімум 1 раунд, максимум 10
        self.round_count_spinbox.setValue(1)  # Дефолтне значення
        form_layout.addRow(self.round_count, self.round_count_spinbox)

        layout.addLayout(form_layout)

        # Кнопки
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Почати")
        self.quit_button = QPushButton("Вийти")
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.quit_button)
        layout.addLayout(button_layout)

        # Початок кнопок
        self.start_button.clicked.connect(self.start_game)
        self.quit_button.clicked.connect(self.close)

    def start_game(self):
        # Отримати налаштування
        timer = self.timer_spinbox.value()
        round_count = self.round_count_spinbox.value()

        # Закрити меню
        # self.close()

        # Почати гру
        game = Game(timer, round_count)
        winners = game.run()
        self.show_winners(winners)


    def show_winners(self, winners):
        self.show()
        self.dialog = WinnersDialog(winners)
        self.dialog.exec()
        # dialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec())


