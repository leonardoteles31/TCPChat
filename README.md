# TCP Chat

A simple multi-client TCP chat application built with **Python** using the `socket` and `threading` modules. This project demonstrates the fundamentals of network programming, client-server communication, and concurrent connections.

## Features

* Multiple clients can connect simultaneously.
* Nickname system for user identification.
* Real-time message broadcasting.
* Join and leave notifications.
* Localhost TCP communication.
* Multi-threaded server and client.

## Project Structure for while

```text
tcpchat/
│
├── server.py      # Starts the TCP chat server
├── client.py      # Connects a client to the server
└── README.md
```

## Technologies

* Python 3.14.3
* Socket Programming
* TCP/IP
* Multithreading

## Concepts Practiced

This project covers several important networking concepts:

* TCP sockets
* Client-server architecture
* IPv4 addressing
* Ports
* Concurrent programming with threads
* Message broadcasting
* Connection handling
* Basic network protocol design

## How It Works

### Server

The server:

1. Creates a TCP socket.
2. Binds to `127.0.0.1:55555`.
3. Waits for incoming client connections.
4. Requests each client's nickname.
5. Stores connected clients.
6. Broadcasts all received messages to every connected client.
7. Removes disconnected clients automatically.

### Client

The client:

1. Connects to the server.
2. Prompts the user for a nickname.
3. Starts two threads:

   * **Receive Thread** – listens for incoming messages.
   * **Write Thread** – sends user messages.
4. Displays all broadcasted messages in real time.

## Installation

Clone the repository:

```bash
git clone https://github.com//tcpchat.git
```

Enter the project directory:

```bash
cd tcpchat
```

No external libraries are required.

## Running the Project

### Start the server

```bash
python server.py
```

Expected output:

```text
Server is online!
```

### Start one or more clients

Open another terminal for each client:

```bash
python client.py
```

Choose a nickname when prompted:

```text
Choose a nickname:
```

Example:

```text
Choose a nickname: Leonardo
```

## Example

Server:

```text
Server is online!
Connected with ('127.0.0.1', 58423)
Nickname of the client is Leonardo!
```

Client 1:

```text
Choose a nickname: Leonardo
Connected to the server!
```

Client 2:

```text
Choose a nickname: Alice
Alice joined the chat!
```

Conversation:

```text
Leonardo: Hello!
Alice: Hi!
Leonardo: Welcome!
```

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project for educational and personal purposes.