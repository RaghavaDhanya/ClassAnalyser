__author__ = 'Raghava'
import urllib2
import tempfile
import linecache

from bs4 import BeautifulSoup
usn="1mv14cs"
names=[]
sub=[[],[],[],[],[],[],[],[]]
for i in range(1,140):
    usn1=usn+(3-len(str(i)))*"0"+str(i)
    htmldata= urllib2.urlopen(r'http://results.vtu.ac.in/?submit=1&rid={}'.format(usn1)).read()
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.flush()
    temp.write(htmldata)
    soup = BeautifulSoup(linecache.getline(temp.name, int(242)),"lxml")
    # print(soup.prettify())

    complete_text = soup.getText()
    if (len(complete_text)>10):
        tables= soup('table')
        names+=[soup('b')[0].text]
        k=0
        for row in (tables[1].find_all('tr')[1:]) :
            if(k<8):
                tds = row.find_all('td')
                sub[k]+=[tds[3].text]
                k+=1
    temp.close()
for i in range(0,len(names)) :
    print(names[i],sub[0][i],sub[1][i],sub[2][i],sub[3][i],sub[4][i],sub[5][i],sub[6][i],sub[7][i])