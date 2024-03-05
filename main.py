from source import app
import socket

ip = socket.gethostbyname(socket.gethostname())

app.run(ip, 7777, True)