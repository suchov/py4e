import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrive all of the anchor tags
for i in range(0, count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href')
    print(url)
