import sys
from backend import  ChatBot
import threading
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication, QLineEdit, QPushButton


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot =ChatBot()
        self.setMinimumSize(700, 500)
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 480, 40)
        self.input_area.returnPressed.connect(self.send_message)
        self.push_button = QPushButton("Send", self)
        self.push_button.clicked.connect(self.send_message)
        self.push_button.setGeometry(500, 340, 100, 40)
        self.show()

    def send_message(self):
        user_input = self.input_area.text()
        self.chat_area.append(f"<p style='color:#333333' > Me: {user_input}</p>")
        self.input_area.clear()
        thread = threading.Thread(target=self.get_bot_reponse,args=(user_input,))
        thread.run()

    def get_bot_reponse(self,user_input):
        reponse = self.chatbot.generate_response(user_input)
        self.chat_area.append(f"<p style='color:#333333 ; background-color:#E9E9E9' > Bot: {reponse}</p>")

app = QApplication(sys.argv)
chatbotwindow = ChatBotWindow()
sys.exit(app.exec())
