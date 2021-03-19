import requests
from bs4 import BeautifulSoup
import pandas
url="https://www.samaan.pk/?s=ps4&post_type=product"
page=requests.get(url)
#print(page.content)
soup=BeautifulSoup(page.content,'html.parser')
#print(soup)
phone_lib=soup.find(class_='products columns-4')
elements=phone_lib.find_all(class_="product-inner")
ps4_name=[ps4.find(class_="woocommerce-loop-product__title").get_text() for ps4 in elements]
prices=[ps4.find(class_="woocommerce-Price-amount amount").get_text() for ps4 in elements]
stuff=pandas.DataFrame({
    "product name": ps4_name,
    "product price":prices
})
stuff.to_csv("samaanpk ps4 scrapped.csv")