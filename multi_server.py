import thread, socket, sys, os, subprocess

socks = []
clients = []

def refresh():
	for i in range(len(clients)):
		print "[]Client " +str(i+1) + " : " + str(clients[i])

	print "[*] Press Ctrl + C to select a client or 0 to quit"



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('' , 9999))

s.listen(10)


while True:
	try:
		try:
			sock, addr = s.accept()
		except socket.timeout:
			pass

		if(sock):
			socks.append(sock)
			clients.append(addr)
			os.system("clear")

		refresh()
		
	except KeyboardInterrupt:
		os.system("clear")
		refresh()

		select = input("[*]Select a client: ")

		if select == 0:
			print "[*] Exiting..."
			sys.exit()

		conn = socks[select-1]

		while True:
			data = raw_input(">")
			
			if data.strip() == 'quit':
				break

			else:
				conn.send(data.strip())
				
			print conn.recv(1024)
		
		conn.close()	
	
	 
s.close()

