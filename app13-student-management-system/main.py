import sys
import mysql.connector
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon, QTextFormat
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QGridLayout,
    QPushButton,
    QMainWindow,
    QMenuBar,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QVBoxLayout,
    QToolBar,
    QStatusBar,
    QMessageBox,
)

class DataBaseConnection:
    def __init__(self,host="localhost", user="root",password="123456",database="school"):
        self.host = host
        self.user = user
        self. password = password
        self.databse = database
    def connect(self):
        connection = mysql.connector.connect(host=self.host, user = self.user,
                                             password = self.password, database = self.databse)
        return  connection

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("./icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        help_menu_item.addAction(about_action)

        search_action = QAction(QIcon("./icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        toolbar = QToolBar()
        toolbar.setMovable(True)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)
        self.addToolBar(toolbar)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        self.load_data()

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        children = self.statusbar.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        edit_button = QPushButton("Edit Student")
        edit_button.clicked.connect(self.edit)
        self.statusbar.addWidget(edit_button)

        delete_button = QPushButton("Delete Student")
        delete_button.clicked.connect(self.delete)
        self.statusbar.addWidget(delete_button)

    # def load_data(self):
    #     connection = DataBaseConnection().connect()
    #     cursor = connection.cursor()
    #     result = cursor.execute("SELECT * FROM students")
    #     select_rows = result
    #     self.table.setRowCount(0)
    #     for row_index, row_item in enumerate(select_rows):
    #         self.table.insertRow(row_index)
    #         for column_index, column_item in enumerate(row_item):
    #             self.table.setItem(
    #                 row_index, column_index, QTableWidgetItem(str(column_item))
    #             )
    #     cursor.close()
    #     connection.close()

    def load_data(self):
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        operation= "SELECT * FROM students"

        for result in cursor.execute(operation,multi=True):
            if result.with_rows:
                select_rows = result.fetchall()
                self.table.setRowCount(0)
                for row_index, row_item in enumerate(select_rows):
                    print(row_item)
                    self.table.insertRow(row_index)
                    for column_index, column_item in enumerate(row_item):
                       self.table.setItem(row_index, column_index, QTableWidgetItem(str(column_item)))
            else:
                print("Number of rows affected by statement '{}': {}".format(
                    result.statement, result.rowcount))

    def insert(self):
        insertdialog = InsertDialog()
        insertdialog.exec()

    def search(self):
        searchdialog = SearchDialog()
        searchdialog.exec()

    def edit(self):
        edit_dialog = EditDialog()
        edit_dialog.exec()

    def delete(self):
        delete_dialog = DeleteDialog()

    def about(self):
        about_dialog = AboutDialog()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        contet = """
        This application was created during the course "The python Mega course".
        Fell free to modify and reuse it
        """
        self.about(self, "About Page", contet)


class DeleteDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.index = mainwindow.table.currentRow()
        self.id = mainwindow.table.item(self.index, 0).text()
        self.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        button = self.question(
            self, "Delete Student!", "Are you sure to delete student?"
        )

        if button == QMessageBox.StandardButton.Yes:
            connection = DataBaseConnection().connect()
            cursor = connection.cursor()
            sql = "delete from students  where id = %s"
            cursor.execute(sql, (self.id,))
            connection.commit()
            cursor.close()
            connection.close()
            mainwindow.load_data()
            self.close()
            QMessageBox.information(self, "Success", "Student deleted successfully")
        else:
            self.close()


class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.index = mainwindow.table.currentRow()
        self.id = mainwindow.table.item(self.index, 0).text()
        name = mainwindow.table.item(self.index, 1).text()
        course = mainwindow.table.item(self.index, 2).text()
        mobile = mainwindow.table.item(self.index, 3).text()

        self.setWindowTitle("Edit Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()

        self.name = QLineEdit(name)
        self.name.setPlaceholderText("Name")
        layout.addWidget(self.name)

        self.courses = QComboBox()
        self.courses.addItems(("Biology", "Math", "Astronomy", "Physics"))
        self.courses.setCurrentText(course)
        layout.addWidget(self.courses)

        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        save_button = QPushButton("Update")
        save_button.clicked.connect(self.update_student)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def update_student(self):
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        sql = "update students set name=%s , course = %s , mobile=%s where id = %s"
        cursor.execute(
            sql,
            (self.name.text(), self.courses.currentText(), self.mobile.text(), self.id),
        )
        connection.commit()
        cursor.close()
        connection.close()
        mainwindow.load_data()
        self.close()
        pass


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add New Student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        layout = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")
        layout.addWidget(self.name)

        self.courses = QComboBox()
        self.courses.addItems(("Biology", "Math", "Astronomy", "Physics"))
        self.courses.setPlaceholderText("Courses")
        layout.addWidget(self.courses)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.add_student)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def add_student(self):
        name = self.name.text()
        course = self.courses.currentText()
        mobile = self.mobile.text()
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()
        insert_statement = "insert into students (name,course,mobile) values(%s,%s,%s)"
        cursor.execute(insert_statement, (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        mainwindow.load_data()
        self.close()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        layout = QVBoxLayout()
        self.search_text = QLineEdit()
        self.search_text.setPlaceholderText("Name")
        layout.addWidget(self.search_text)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_std)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def search_std(self):
        mainwindow.table.clearSelection()
        name = self.search_text.text()
        connection = DataBaseConnection().connect()
        cursor = connection.cursor()


        items = mainwindow.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            mainwindow.table.item(item.row(), 1).setSelected(True)
        cursor.close()
        connection.close()


app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec())
