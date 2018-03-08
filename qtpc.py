import re
import urllib.request
url="http://www.58pic.com/piccate/3-0-0-8.html"
html=urllib.request.urlopen(url).read()
file=str(html)
pat='http://pic.qiantucdn.com/58pic.*?\..*?g'
pat2='http://pic.qiantucdn.com/58pic(.*?)\.(.*?)$'
results=re.compile(pat).findall(file)
for result in results:
    pic=re.compile(pat2).findall(result)
    picid = re.sub(r"/", "", pic[0][0])
    picname=picid+'.'+pic[0][1]
    print(picname)
    pat3 = '.*?_PIC2018$'
    picid3 = re.compile(pat3).findall(picid)
    if (len(picid3) > 0):
        trueurl = "http://pic.qiantucdn.com/58pic" + pic[0][0] + "." + pic[0][1]
    else:
        trueurl = "http://pic.qiantucdn.com/58pic" + pic[0][0] + "_1024." + pic[0][1]
    print(trueurl)
    print(picname)
