import socket
import cv2
import numpy

host = ''
port = 1234

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
        
    server.listen(1)
    conn, addr = server.accept()
    message = []
    while True:
        length = conn.recv(1024 * 1024)
        if not length: break
        else: message.append(length)
    string = ''.join(message)
    data = numpy.fromstring(string, numpy.uint8)
        
    decimg = cv2.imdecode(data, 1)
    cv2.imshow("Remote Webcam", decimg)
        
    if cv2.waitKey(5)==27:break
        
cv2.destroyAllWindows()
