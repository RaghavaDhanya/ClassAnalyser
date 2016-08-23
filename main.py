__author__ = 'Raghava'
import urllib2
import tempfile
import linecache
import Student
from bs4 import BeautifulSoup

usn = "1mv14cs"
list = []
for i in range(1, 10):
    usn1 = usn + (3 - len(str(i))) * "0" + str(i)
    htmldata = urllib2.urlopen(r'http://results.vtu.ac.in/?submit=1&rid={}'.format(usn1)).read()
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.flush()
    temp.write(htmldata)
    soup = BeautifulSoup(linecache.getline(temp.name, int(242)), "lxml")
    # print(soup.prettify())

    complete_text = soup.getText()
    if len(complete_text) > 10:
        tables = soup('table')
        name = soup('b')[0].text
        marks = {}
        sem = ''
        result = ''
        for tr in tables[0].find_all('tr'):
            td = tr.find_all('td')
            sem = td[1].text
            result = "".join([i if ord(i) < 128 else ' ' for i in td[3].text])
        k = 0
        for row in (tables[1].find_all('tr')[1:]):
            if k < 8:
                tds = row.find_all('td')
                marks[tds[0].text] = (tds[1].text, tds[2].text, tds[3].text, tds[4].text)
                k += 1
        list += [Student.Students(name, sem, result, marks, 100)]
    temp.close()
for i in range(0, len(list)):
    print(str(list[i]))