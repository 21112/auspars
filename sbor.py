import math
import requests
from bs4 import BeautifulSoup
HEADERS = { 'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/86.0.4240.193 Safari/537.36',
            'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'ru,en;q=0.9,de;q=0.8,en-US;q=0.7'}
# param = "views-field views-field-nothing px-xs-1 font-weight-light"
url= "https://www.heubach-edelmetalle.de/"


def get_html(url, params=''):
    resp = requests.get(url, headers = HEADERS, params=params)
    return resp


def content_get(html):
    soup = BeautifulSoup(html,features="html.parser")
    items = soup.find_all("div",class_='views-field views-field-nothing px-xs-1 font-weight-light')
    s = []
    g = ["Euro","GOLD","SILBER","PLATIN","PALLADIUM"]

    for n, i in zip(g, items):
        s.append(
            {
                n: (i.find("span",class_='field-content').get_text(strip = True))

            }
        )    
    return s
html = get_html(url)    
o = content_get(html.text)

def show():
    g = ["Euro","GOLD","SILBER","PLATIN","PALLADIUM"]
    p = []
    html = get_html(url)
    if html.status_code == 200:

        o = content_get(html.text)
        for i in o:
            for a,b in i.items():
                b = b.strip("€")
                b = b.strip("$")
                for i in range(len(b)):
                    if b[i]==",":
                        p.append(b[0:i])
        for a,b in zip(g,p):
            b = int(b)
            print(a,b)
            if a == "SILBER" and b <17:
                print (f"Самое время начать покупать {a} по цене {b}")
show()