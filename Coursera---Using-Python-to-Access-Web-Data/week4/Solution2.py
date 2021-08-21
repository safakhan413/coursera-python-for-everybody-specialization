# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#  http://py4e-data.dr-chuck.net/known_by_Fikret.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
lastName= ''
for i in range(0,7):
    # http: // py4e - data.dr - chuck.net / known_by_Fikret.html
    # tag = soup.select_one("a:nth-of-type(3)")
    tags = soup.find_all("a", limit=18)
    third_tag = tags[17]
    # print(third_tag.string)
    lastname = third_tag.string
    url = third_tag.get('href', None)
    # print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    continue

print(lastname)