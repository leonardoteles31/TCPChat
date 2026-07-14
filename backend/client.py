import socket
import threading

# Ask the user to choose a nickname before connecting
nickname = input("Choose a nickname: ")

# Create a TCP socket using IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the chat server
client.connect(('127.0.0.1', 55555))


def receive():
    """
    Handles messages received from the server.

    The client continuously listens for incoming messages.
    If the server requests the nickname, it sends it.
    Otherwise, it displays the received message.
    """
    while True:
        try:
            # Receive data from the server and decode it
            message = client.recv(1024).decode('ascii')

            # Server requests the client's nickname
            if message == 'NICK':
                client.send(nickname.encode('ascii'))

            else: # Display messages received from other users
                print(message)
        except:
            # Handle connection errors or server shutdown
            print("An error occurred!")
            client.close()
            break


def write():
    """
    Sends messages typed by the user to the server.

    Each message is formatted with the user's nickname
    before being sent.
    """
    while True:
        message = f'{nickname}: {input("")}'

        # Encode and send the message to the server
        client.send(message.encode('ascii'))


# Create a thread to continuously receive messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Create a thread to continuously send messages
write_thread = threading.Thread(target=write)
write_thread.start()