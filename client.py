import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2247))

while True:
    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            #print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
            
        full_msg += msg.decode("utf-8")
        
        if len(full_msg)-HEADERSIZE == msglen:
            print("Transmission successfull!")
            print(full_msg[HEADERSIZE:])
            f = open("output.txt", 'wb')
            f.write(full_msg[HEADERSIZE:].encode("utf-8"))
            f.close()
            new_msg = True
            full_msg = ""
            
    print(full_msg)
