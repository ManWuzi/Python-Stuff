import cv2
import socket
import numpy

host = '169.254.35.41'
port = 1234

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    result, imgencode = cv2.imencode('.jpg', frame, [1, 90])
    data = numpy.array(imgencode)
    stringData = data.tostring()
       
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))

        client.sendall(stringData)
        client.close()
    except:
        pass

capture.release()
