from datetime import datetime
from selenium import webdriver
import json

PATH = "C:/Users/sony/Python/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/chart/top/")

now = datetime.now()
current_time = now.strftime("%d %B %Y, %H %M %S")

data = []
for film in driver.find_element_by_class_name("lister-list").find_elements_by_tag_name("tr"):
    for img in film.find_elements_by_tag_name("img"):
            
        data.append(
            {"No": film.text.split("\n")[0],
             "Judul": film.text.split("\n")[0][:len(film.text.split("\n")[0]) - 7],
             "Tahun": film.text.split("\n")[0][len(film.text.split("\n")[0]) - 5:len(film.text.split("\n")[0]) - 1],
             "Rating": film.find_element_by_class_name("ratingColumn").text,
             "Image": img.get_attribute("src"),
             "Tanggal_Scrapping": current_time
                    }
                )


hasil_scraping = open("final.json", "w")
json.dump(data, hasil_scraping, indent = 6)
hasil_scraping.close()    

driver.quit()

