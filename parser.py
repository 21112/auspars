import math
import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open ('wlw_Parsing.csv','a',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            (data['Email'],
            data['Firma_name'],
            data['Firma_adresse']))
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'}
pa = 1

url = f"https://www.wlw.de/de/suche/it-projekte/page/"+ {str(pa)} +"?locationName=76530%20Baden-Baden,%20Deutschland&locationRadius=100km"

def get_cont_2fasa(re):
    soup = BeautifulSoup(re, features="html.parser")
    email = soup.find("div", class_= "location-and-contact__button-wrap").find("a",class_="location-and-contact__button nav-link").find("span")
    for e in email:
        print(e.strip(),end="")
    firmename = soup.find("h1", class_="business-card__title")
    for n in firmename:
        print(n.strip(), end="")
    firmeadress = soup.find("div", class_="business-card__address__content").find("span")
    for a in firmeadress:
        print(a.strip(),end="")
    data = {
        'Email': e.strip(),
        'Firma_name': n.strip(),
        'Firma_adresse': a.strip()
    }
    write_csv(data)
  


def get_html(url, params=''):
    resp = requests.get(url, headers=HEADERS, params=params)
    return resp

def content_get(html):
    soup = BeautifulSoup(html, features="html.parser")
    items = soup.find_all("div", class_="company-title-link-wrap")
    # pagination = soup.find("div", class_="pagination-next").find("a").get('href')
    # for p in pagination:
    #     url = wbseite + p
    s = []
    for i in items:
        s.append(i.find("a", class_='company-title-link').get('href'))
    return s

wbseite = 'https://www.wlw.de'

def show():
    html = get_html(url)
    while html.status_code == 200:   
        # o = content_get(html.text)         
        # for i in o:
        #     ur = wbseite + i
                    
        #     re = get_html(ur)

        #     get_cont_2fasa(re.text)    
        print(url) 
        pa+=1    
                     
    else: 
        print("Finish")            


show()

