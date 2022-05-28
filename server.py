import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2247))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    
    msg = "আমার সোনার বাংলা"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg #cutting the message into small chunks
    
    clientsocket.send(bytes(msg, "utf-8"))
    #clientsocket.close()
