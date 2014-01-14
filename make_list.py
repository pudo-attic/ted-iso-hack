import requests
from lxml import html
from datetime import datetime

URL = 'https://webgate.ec.europa.eu/publications/ted-export/%s/'
AUTH = ('ted-export', 'R2-dHqZ3')

#def download_file(url):
#    print [url]
#    res = requests.get(url, auth=AUTH, stream=True)
#    _, fn = url.rsplit('/', 1)
#    with open(fn, 'wb') as fh:
#        for l in res.iter_content():
#            fh.write(l)

with open('iso_list.txt', 'w') as fh:
    for year in range(2010, datetime.utcnow().year+1):
        res = requests.get(URL % year, auth=AUTH)
        doc = html.fromstring(res.content)
        urls = [a.get('href') for a in doc.findall('.//a') if 'monthly.iso' in a.get('href')]
        for url in urls:
            url = url.replace('//', '//' + AUTH[0] + ':' + AUTH[1] + '@')
            fh.write(url + '\r\n')

