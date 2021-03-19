import requests
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

page=requests.get("https://www.reddit.com/r/BabyYoda/")  # jis city ka temp scrap krwnana hai uska url dedo
soup=BeautifulSoup(page.content, 'html.parser')
images=soup.find_all("img",attrs={"alt":"Post image"})
number = 0

for image in images:
    image_src= image["src"]
    print(image_src)
    urllib.request.urlretrieve(image_src,str(number))
    number+=1