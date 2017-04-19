import http.client
import json

bibleverse = 'John 3:16-19'
#bibleverse = input()
bibleurl = bibleverse.replace(" ", "%20")
conn = http.client.HTTPSConnection("bible-api.com")
headers = {'Content-type': 'application/json'}
conn.request("GET", "/" +  bibleurl)
r1 = conn.getresponse()
#print(r1.status, r1.reason)
data1 = json.loads(r1.read().decode('utf-8'))

for i in data1['verses']:
    print(i['book_name'] + ' ' + str(i['chapter']) + ':' + str(i['verse']))
    print(i['text'])
