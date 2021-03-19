import pandas
import requests
from  bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page= requests.get(url)
print(page)
soup=BeautifulSoup(page.content,'html.parser')
iphones=soup.find_all(class_="_3O0U0u")
discounted_prices=[iphone.find(class_="_1vC4OE _2rQ-NK").get_text() for iphone in iphones]
iphone_names=[iphone.find(class_="_3wU53n").get_text() for iphone in iphones]
iphone_ratings=[iphone.find(class_="hGSR34").get_text() for iphone in iphones]
orignal=[iphone.find(class_="_3auQ3N _2GcJzG") for iphone in iphones]
orignal_price=[]
discount=[iphone.find(class_="VGWI6T") for iphone in iphones]
discount_percentage=[]
for i in orignal:
    if i!=None:
        a=i.get_text()
        orignal_price.append(a)
    else:
        orignal_price.append("price is ot reduced for this item")

for i in discount:
    if i!=None:
        a=i.get_text()
        discount_percentage.append(a)
    else:
        discount_percentage.append("no discount on this item yet")
scrapped_stuff=pandas.DataFrame ({
    "product name":iphone_names,
    "Ratings":iphone_ratings,
    "discounted price":discounted_prices,
    "orignal price":orignal_price,
    "percentage discount":discount_percentage,
})
#print(scrapped_stuff)
scrapped_stuff.to_csv("flipkart iphone scrapped.csv")
















                if element1.get_text()=="تم حجب النتائج عنك مؤقتاً":
                    break
                if element1.get_text()=="الرجاء تحديث الصفحة":
                    driver.refresh()
