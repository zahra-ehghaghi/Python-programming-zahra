from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QGridLayout,
    QPushButton,
)
import sys


class CalculateSpeed(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        distance_label = QLabel("Distance:")
        self.distance_text = QLineEdit()

        self.type_combobox = QComboBox()
        self.type_combobox.addItems(["Metric (KM)", "Miles"])

        times_lable = QLabel("Times:")
        self.times_text = QLineEdit()

        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calc_speed)
        self.calc_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_text, 0, 1)
        grid.addWidget(self.type_combobox, 0, 2)

        grid.addWidget(times_lable, 1, 0)
        grid.addWidget(self.times_text, 1, 1)

        grid.addWidget(calc_button, 2, 0, 1, 3)
        grid.addWidget(self.calc_label, 3, 0, 1, 3)
        self.setLayout(grid)

    def calc_speed(self):
        distance = self.distance_text.text()
        times = self.times_text.text()
        speed = float(distance) / float(times)
        if self.type_combobox.currentText().__eq__("Metric (KM)"):
            speed = round(speed, 2)
            unit = "KM/H"
        elif self.type_combobox.currentText().__eq__("Miles"):
            speed = round(speed * 0.621371, 2)
            unit = "MPH"
        self.calc_label.setText(f"The value of speed is : {speed} {unit}")


app = QApplication(sys.argv)
speed_calc = CalculateSpeed()
speed_calc.show()
sys.exit(app.exec())
