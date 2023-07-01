import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QLineEdit,
    QWidget,
    QPushButton,
)


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_lable = QLabel("Name: ")
        self.name_text = QLineEdit()

        date_lable = QLabel("Date of birth MM/DD/YYYY: ")
        self.date_text = QLineEdit()

        calc_button = QPushButton("Calculate Age")
        calc_button.clicked.connect(self.calculage_age)
        self.output_label = QLabel("")

        grid.addWidget(name_lable, 0, 0)
        grid.addWidget(self.name_text, 0, 1)

        grid.addWidget(date_lable, 1, 0)
        grid.addWidget(self.date_text, 1, 1)
        grid.addWidget(calc_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)

    def calculage_age(self):
        year = datetime.now().year
        date_of_birth = self.date_text.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = year - year_of_birth
        self.output_label.setText(f"The age of {self.name_text.text()  }  is: {age}")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
