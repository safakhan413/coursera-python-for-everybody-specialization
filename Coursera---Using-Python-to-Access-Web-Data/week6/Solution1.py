import urllib.request, urllib.parse, urllib.error
import json

sum = 0
while True:
    url = input('Enter url: ')
    if len(url) < 1: break
    info = urllib.request.urlopen(url).read().decode()
    result = json.loads(info)
    for r in result["comments"]:
        sum = int(r["count"]) + sum
    print(sum)
