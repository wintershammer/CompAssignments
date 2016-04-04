import urllib.request
import re
import urllib.parse


def visit(urlStr):
    page = urllib.request.urlopen(urlStr) 
    text = page.read().decode('utf-8') 
    page.close()
    return text
    
def analyse(url):
    text = visit(url)
    links = []
    rexp = re.compile(r'<a[^>]* href="([^"]*)">(.+?)</a>',re.DOTALL)
    matches = rexp.finditer(text)
    for item in matches:
        if not(re.match(r'#.+',item.group(1))): #ignore anchors
            links.append((item.group(2),urllib.parse.urljoin(url,item.group(1))))
    return links

    
for label,url in analyse('http://di.ionio.gr/~mistral/tp/compilers/lecturedoc/unit3/module1.html'):
    print(label,":",url)
    #print(visit(url))
