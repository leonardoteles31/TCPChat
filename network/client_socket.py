import socket
import threading


class ClientSocket:
    def __init__(self, host, port, nickname):
        self.host = host
        self.port = port
        self.nickname = nickname

        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.running = True

        # Function that GUI will use when a message arrives
        self.message_callback = None


    def connect(self):

        # Connects the client to the server.

        self.client.connect((self.host, self.port))

        # Start listening thread
        receive_thread = threading.Thread(
            target=self.receive
        )

        receive_thread.daemon = True
        receive_thread.start()


    def receive(self):

        # Receives messages from server.

        while self.running:
            try:
                message = self.client.recv(1024).decode("ascii")

                if message == "NICK":
                    self.client.send(
                        self.nickname.encode("ascii")
                    )

                else:
                    # Send message to GUI
                    if self.message_callback:
                        self.message_callback(message)

            except:
                print("Connection error")
                self.close()
                break


    def send(self, message):

        # Sends message to server.


        formatted_message = f"{self.nickname}: {message}"

        self.client.send(
            formatted_message.encode("ascii")
        )


    def close(self):


        self.running = False
        self.client.close()