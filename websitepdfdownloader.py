import urlparse
import urllib2
from bs4 import BeautifulSoup
import os

url = raw_input("Enter the url: ")
download_path = raw_input("Enter the download path: ")
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT  6.3; WOW64; rv:38.0) Gecko/20100101 Firefox/33.0"}
urls = []
visited = []
i = 0
urls.append(url)
visited.append(url)

while len(urls) >0:
    req = urllib2.Request(urls[0], None, headers)
    html = urllib2.urlopen(req)

    soup = BeautifulSoup(html.read())

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(urls[0], tag['href'])

        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])
            if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf' and os.path.exists(os.path.join(download_path,os.path.basename(tag['href']))) == False:
                current = urllib2.urlopen(tag['href'])
                try:
                    f = open(os.path.join(download_path, os.path.basename(tag['href'])), "wb")
                    print "[+]Downloading %s" %os.path.basename(tag['href'])
                    f.write(current.read())
                    f.close()
                    i+=1
                except KeyboardInterrupt:
                    print "\n[*]Download cancelled by user."
                    os.remove(os.path.basename(tag['href']))
                    break

                except URLError, e:
                    print "[*]There was an error while loading the webpage\n[*]Check internet connectivity"
           
    urls.pop(0)

print "Successfully downloaded %d" %i
