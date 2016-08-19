__author__ = 'Raghava'
import urllib2
import tempfile
import linecache

from bs4 import BeautifulSoup
usn=""
htmldata= urllib2.urlopen(r'http://results.vtu.ac.in/?submit=1&rid={}'.format(usn)).read()
temp = tempfile.NamedTemporaryFile(delete=False)
temp.flush()
temp.write(htmldata)
soup = BeautifulSoup(linecache.getline(temp.name, int(242)),"lxml")
tables= soup('table')
for row in tables[1].find_all('tr'):
    tds = row.find_all('td')
    print(tds[0].text,tds[1].text,tds[2].text,tds[3].text,tds[4].text)
