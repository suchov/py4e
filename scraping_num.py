# https://py4e-data.dr-chuck.net/comments_42.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "https://py4e-data.dr-chuck.net/comments_42.htm"
url = 'http://py4e-data.dr-chuck.net/comments_1128050.html'
# url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
    # Look at the parts of a tag
    y = str(tag)
    num = re.findall('[0-9]+', y)
    numlist = numlist + num

sum = 0
for i in numlist:
    sum = sum + int(i)

print(sum)
