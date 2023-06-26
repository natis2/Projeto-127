import bs4
from bs4 import BeautifulSoup
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

star_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")

browser.get(START_URL)

browser.get(star_url)

time.sleep(10)

scarped_data = []

stars_data = []

csv_data = []

info_stars = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table", attrs={"class","wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    sopa= BeautifulSoup(browser.page_source,"html.parser") 
    tabelas = sopa.find("table", attrs={"class","wikitable"})
    tabela_body = tabelas.find('tbody')
    tag_tr = tabela_body.find_all('tr')

    for tag_csv in tag_tr:
        tag_td = tag_csv.find_all('td')
        print(tag_td)

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)

        temp_list = []
        temp_list_2 = []


        for col_data in table_cols:
            print(col_data.text)

            data = col_data.text.strip()
            print(data)

            temp_list.append(data)

        scarped_data.append(temp_list)


        for td_data in tag_td:
            print(td_data.text)

            stardata = td_data.text.strip()
            print(stardata) 

            temp_list_2.append(stardata)   

        csv_data.append(temp_list_2)    

          
scrape()
for i in range(0,len(scarped_data)): 
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]
 
    required_data = [Star_names,Distance,Mass,Radius,Lum]
    stars_data.append(required_data)

for i in range(0,len(csv_data)): 
    star_name = csv_data[i][1]
    star_distance = csv_data[i][3]
    star_mass = csv_data[i][5]
    star_radius = csv_data[i][6] 

    require_star = [star_name,star_distance,star_mass,star_radius] 
    info_stars.append(require_star)

    

headers = ['Star_name','Distance','Mass','Radius','Luminosity']

header_two = ['star name','star distance','star mass','star radius']



star_df_1 = pd.DataFrame(stars_data, columns=headers)

star_df_1.to_csv('scraped_data.csv',index=True,index_label="id")

star_df_2 = pd.DataFrame(info_stars, columns=header_two)

star_df_2.to_csv('scraped_data_two.csv',index=True,index_label="id")