from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


class LoginDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.nickname = None

        self.setWindowTitle("Login")
        self.setFixedSize(300, 150)


        layout = QVBoxLayout()


        self.label = QLabel("Enter your nickname:")
        layout.addWidget(self.label)


        self.nickname_input = QLineEdit()
        layout.addWidget(self.nickname_input)


        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)


        self.setLayout(layout)


    def login(self):

        # Gets the nickname and closes the dialog.


        nickname = self.nickname_input.text().strip()

        if nickname:
            self.nickname = nickname
            self.accept()