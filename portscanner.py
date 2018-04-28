import socket
import thread
import Queue

q = Queue.Queue()
nthreads = 50

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        print "[*] Port ", port, " is open!!"
    except socket.error:
        pass
 
def threader():
    while not q.empty():
        worker = q.get()
        portscan(worker)
        q.task_done()
    
host = raw_input("Enter the server address/name: ")
start_port = input("What is the starting port: ")
stop_port = input("What is the last port: ")
ip = socket.gethostbyname(host)
print '-' * 40

for i in range(start_port, stop_port):
    q.put(i)

for j in range(nthreads):
    thread.start_new_thread(threader, ())

q.join()

raw_input("Press any key to exit...")

    


    
