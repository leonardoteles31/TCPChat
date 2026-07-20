from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton
)


class ChatWindow(QMainWindow):

    def __init__(self, client):
        super().__init__()

        self.client = client

        self.setWindowTitle("TCP Chat")
        self.setFixedSize(500, 600)


        # Main widget
        container = QWidget()
        self.setCentralWidget(container)


        # Layout
        layout = QVBoxLayout()


        # Chat display
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        layout.addWidget(self.chat_area)


        # Message input
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText(
            "Type a message..."
        )

        layout.addWidget(self.message_input)


        # Send button
        self.send_button = QPushButton("Send")

        self.send_button.clicked.connect(
            self.send_message
        )

        layout.addWidget(self.send_button)


        container.setLayout(layout)


    def send_message(self):

        # Sends message to the server.

        message = self.message_input.text().strip()

        if message:

            self.client.send(message)

            # Clear input after sending
            self.message_input.clear()



    def receive_message(self, message):

        # Displays messages received from server.
        
        self.chat_area.append(message)