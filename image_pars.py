import requests
from bs4 import BeautifulSoup



HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'accept' : 'image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ru,en;q=0.9,de;q=0.8,en-US;q=0.7' }
   
c = 0
def get_html(url, params= ""):
    resp = requests.get(url, headers = HEADERS, params= params)
    return resp

def get_urls_for_content(resp):
    soup = BeautifulSoup(resp,"html.parser")
    url_c = soup.find_all("a",class_="wallpapers__link")
    ur =[]
    for i in url_c:
        ur.append("https://wallpaperscraft.ru" + i.get('href'))  
    return ur  

def get_content(urls):
    img_list=[]    
    for u in urls:
        global c
        c+=1    
        res = get_html(u)
        res = res.text
        soup = BeautifulSoup(res, "html.parser" )
        img = soup.find("a", class_="JS-Popup").get("href")
        srez = u[36:len(u)-10]
        req = get_html(img).content
        with open(f"dark/{srez}.jpg", "wb") as file:  # directory for files
            file.write(req)
            print(f'№ {c} Download {u}')

def starting():  
    for page in range(2,30):
        url = f"https://wallpaperscraft.ru/catalog/dark/3840x2160/page{page}"  # main page for download
        html = get_html(url)
        if html.status_code == 200:
            urls_cont = get_html(url)
            adders = get_urls_for_content(urls_cont.text)
            get_content(adders)
        else:
            print("no Site")    
starting()

