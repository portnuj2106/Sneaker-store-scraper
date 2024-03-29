import requests
import re
from bs4 import BeautifulSoup
import time
import pandas as pd

from get_info import get_name, get_price, get_description, get_details

sneakers_links = []
sneakers = []
base_url = 'https://en.afew-store.com'


def save_info():
    for page in range(1, 5):
        url = f'{base_url}/collections/footwear?page={page}'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        product_links = soup.find_all('a', class_='product-card')  # Assuming this class exists

        for link in product_links:
            href = link.get('href')
            if href:
                sneakers_links.append(f'{base_url}{href}')

        for link in sneakers_links:
            r = requests.get(link)
            page = BeautifulSoup(r.content, 'html.parser')
            name = get_name(page)
            price, with_discount = get_price(page)
            description = get_description(page)
            style, colorway, gender, material, manufacturer, series, purpose = get_details(page)
            item_info = {
                'name': name,
                'price': price,
                'with_discount': with_discount,
                'description': description,
                'colorway': colorway,
                'gender': gender,
                'material': material,
                'manufacturer': manufacturer,
                'series': series,
                'purpose': purpose,
            }
            print(item_info)
        sneakers.append(item_info)
    print(sneakers)
    print(len(sneakers))
    time.sleep(3)


if __name__ == '__main__':
    save_info()


