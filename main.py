import sqlite3

import requests
import re
from bs4 import BeautifulSoup

from queries import insert_data_avto


pages = int(input("Сколько страниц вы хотите: "))
company_name = input("Марка: ")
model = input("Модель: ")

for i in range(1, pages + 1):
    response = requests.get(f"https://avtoelon.uz/avto/{model}/{company_name}/?page={i}").text
    soup = BeautifulSoup(response, 'html.parser')
    sale = soup.find_all('div', class_="row list-item a-elem")

    for ad in sale:
        info_top = ad.find('div', class_="a-info-top list-title")
        title = info_top.find('span', class_="a-el-info-title").get_text()
        price = info_top.find('span', class_='price').get_text(strip=True).split(':')[1]
        if ' ' in price:
            price = price.replace(' ', ' ')
        description = ad.find('div', class_="desc").get_text(strip=True)
        if ' ' in description:
            description = description.replace(' ', ' ')
        info_bot = ad.find('div', class_='a-info-bot')
        region = info_bot.find('a', class_='a-info-text__region').get_text()
        date = info_bot.find('span', class_='date').get_text()
        link = 'https://avtoelon.uz' + ad.find('a').get('href')

        # -----------------------------------------------------------------------------
        insert_data_avto(model, company_name, price, description, region, date, link)
        # -----------------------------------------------------------------------------

