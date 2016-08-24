__author__ = 'Raghava'
import urllib2
import tempfile
import linecache
import Student
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
usn = "1mv14ec"
list = []
for i in range(1, 50):
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
        total=0
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
        total="".join([i if ord(i) < 128 else ' ' for i in tables[2].find_all('tr')[0].find_all('td')[3].text])
        list += [Student.Students(name, sem, result, marks, total)]
    temp.close()
arr={}
for i in list:
    for j in i.marks.keys():
        if j not in arr:
            arr[j]=0
        if i.marks[j][3] == 'P':
            arr[j]+=1
plt.bar(range(0,len(arr.values())),arr.values(),.9,color="blue",align='center')
plt.xticks(range(0,len(arr.values())),[i[i.index("(")+1:-1] for i in arr.keys()],rotation='vertical')
plt.subplots_adjust(bottom=0.15)
plt.show()