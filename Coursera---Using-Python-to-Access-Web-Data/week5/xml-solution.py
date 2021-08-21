import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

link = input('Enter location: ')
print('Retrieving', link)
html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')
data = ET.fromstring(html)
# tags = data.findall('comments/comment')
# for tag in tags:
counts = data.findall('.//count')
sum = 0
for count in counts:
    sum = int(count.text) + sum
print(sum)