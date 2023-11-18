import requests
from bs4 import BeautifulSoup
import lxml
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
header = {"user-Agent": user}
session = requests.Session()

for j in range(1, 26):
    print(f"Page = {j}")
url = "https://allo.ua/ua/products/mobile/"



response = session.get(url, headers=header)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

all_products = soup.find_all('div', class_="products-layout__item without-options-1 without-options-3 without-options-4")

for product in all_products:
    if product.find("div", class_="v-pb__old"):
        price = product.find('span', class_="v-pb__cur discount")
        title = product.find("span", class_="product-card__title")
        print(len(all_products))




