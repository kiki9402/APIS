import requests
from bs4 import BeautifulSoup

def hangang_data():
    url = "https://hangang.life"
    res = requests.get(url)
    res.raise_for_status()#요청

    soup = BeautifulSoup(res.text, "lxml")
    temp = soup.find("span", attrs={"class": "bold"})
    bold2 = soup.find("span",attrs={"class": "bold", "style": "color: rgba(255, 255, 255, 0.9);"})

    return {
        "temperature": temp.get_text(),
        "quote": bold2.get_text()
    }
