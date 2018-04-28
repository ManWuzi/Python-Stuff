from bs4 import BeautifulSoup
import urllib2
import os, sys

ips = []
ports = []
both = []


url = "https://proxy-list.org/english/index.php" #url with http proxies

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}

if os.geteuid() != 0: #test for root or superuser
	print "[*] You must run this program as root!!"
	sys.exit()


if len(sys.argv) != 2:
	print "Usage: %s <location of configuration file>" %str(sys.argv[0])
	sys.exit()

try:
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
except:
	print "[*] ERROR: Could not open url!!"
	sys.exit()

soup = BeautifulSoup(html) #parsing html

#finding li tags so with class of proxy so we can pull the ip addresses and ports - check source code of page
for ips_ports in soup.findAll('li', attrs={'class':'proxy'}):
	if 'Proxy' in ips_ports.getText():
		pass
	both.append(ips_ports.getText())

for singles in both:
	try:
		ip_addr, port_num = singles.split(":") #separating ip addresses and ports
		ips.append(ip_addr)
		ports.append(port_num)
	except:
		pass		
	

f = open(sys.argv[1], "a")

for i in range(0,len(ports)):
	f.write("http\t%s\t%s\n" %(ips[i], ports[i]))


f.close()

print "[+] Done!!"
print "[*] Now you can browse anonymously with proxychains"


	
