import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


connected = True
print("You can easily disconnect from the Server with 'Q'")
while(connected):
    msg = input()
    if(msg == 'Q' or msg == 'q'):
        connected = False
    else:
        send(msg)

send(DISCONNECT_MSG)

    

