from selenium import webdriver
import pandas as pd

url="https://www.youtube.com/c/Freecodecamp/videos?view=0&sort=p&flow=grid"

driver=webdriver.Chrome()

driver.get(url)

vedios= driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")  # (elements) ayga element nhi

view=[]
tittle=[]
durat=[]
for vedio in vedios:
    views=vedio.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text 
    view.append(views)
    titles=vedio.find_element_by_xpath('.//*[@id="video-title"]').text
    tittle.append(titles)
    durats= vedio.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    durat.append(durats)

stuff= pd.DataFrame({
    "views on channel": view,
    "title of the vedio":tittle,
    "duration of the vedio":durat
})


stuff.to_csv("youtube.csv")