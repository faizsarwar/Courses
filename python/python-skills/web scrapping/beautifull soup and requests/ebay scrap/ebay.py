import requests
from  bs4 import BeautifulSoup
import pandas
url="https://www.ebay.com/sch/i.html?_from=R40&_nkw=ps5+skin&_sacat=0&LH_TitleDesc=0&_ipg=100"
page=requests.get(url)
#print(page.content)
soap=BeautifulSoup(page.content,'html.parser')
elements=soap.find_all(class_="s-item__wrapper clearfix")
ps5_name=[ps4.find(class_="s-item__title").get_text() for ps4 in elements]
ps5_price=[ps4.find(class_="s-item__price").get_text() for ps4 in elements]
ps5_country=[ps4.find(class_="s-item__location s-item__itemLocation").get_text() for ps4 in elements]
shipping_cost=[ps4.find(class_="s-item__shipping s-item__logisticsCost").get_text() for ps4 in elements]
condition=[ps4.find(class_="s-item__subtitle").get_text() for ps4 in elements]
stuff = pandas.DataFrame({
    "Product Name":ps5_name,
    "prodoct price":ps5_price,
    "Country":ps5_country,
    "Shiiping Cotst on this item":shipping_cost,
    "Product Condition":condition
})
stuff.to_csv("ebay ps5 scrapped.csv")