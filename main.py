import sys

from PySide6.QtWidgets import QApplication

from gui.login_dialog import LoginDialog
from gui.chat_window import ChatWindow
from network import ClientSocket


def main():

    app = QApplication(sys.argv)


    # Open login window
    login = LoginDialog()

    if login.exec():

        nickname = login.nickname


        # Create socket connection
        client = ClientSocket(
            "127.0.0.1",
            55555,
            nickname
        )


        # Create chat window
        window = ChatWindow(client)


        # Connect received messages to GUI
        client.message_callback = window.receive_message


        # Connect to server
        client.connect()


        window.show()


    sys.exit(app.exec())


if __name__ == "__main__":
    main()