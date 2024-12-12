from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel

class WinnersDialog(QDialog):
    def __init__(self, winners):
        super().__init__()
        self.setWindowTitle("Переможці")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Зобразити переможців
        winners_label = QLabel("Переможці в кожному раунді:")
        layout.addWidget(winners_label)
        for i, winner in enumerate(winners, 1):
            round_label = QLabel(
                f"Раунд {i}: {winner} ({'Синій танк' if winner == 1 else 'Червоний танк' if winner == 2 else 'Нічия'})"
            )

            layout.addWidget(round_label)

        # Кнопка "Закрити"
        close_button = QPushButton("Закрити")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)