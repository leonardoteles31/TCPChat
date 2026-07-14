import threading
import socket

host = '127.0.0.1' # localhost
port = 55555

# start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Sends a message to all connected clients.
def broadcast(message):
    for client in clients:
        client.send(message)


# Receives messages from the client and broadcasts them to all other connected users.
def handle(client):
    while True:
        try:
            # Receive data from the client (maximum 1024 bytes)
            message = client.recv(1024)

            # Send received message to all connected clients
            broadcast(message)
        except:
            # Client disconnected, remove it from the server
            index = clients.index(client)
            clients.remove(client)
            client.close()

            # Get the nickname of the disconnected client
            nickname = nicknames[index]

            # Notify remaining users
            broadcast(f'{nickname} left the chat!'.encode('ascii'))

            # Remove nickname from the list
            nicknames.remove(nickname)
            break


def receive():

    """
    Accepts new client connections and initializes them.

    Creates a new thread for each client so multiple users
    can communicate simultaneously.
    """

    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask the client for their nickname
        client.send('NICK'.encode('ascii'))

        # Receive and store the nick name
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')

        # Notify everyone that a new user joined
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))

        # Confirm connection to the new client
        client.send('Connected to the server!'.encode('ascii'))

        # Create a new thread to handle this client independently
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is online!")
receive()
