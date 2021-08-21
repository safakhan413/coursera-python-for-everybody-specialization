from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # comment number can be etxracted withs string
    # print('TAG:', tag.string)
    x = int(tag.string)
    sum = sum + x
    # print(x)
    # http: // py4e - data.dr - chuck.net / comments_42.html
    # print('URL:', tag.get('href', None))
    # print('URL:', tag.contents[0])
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
print('final sum - ', sum)