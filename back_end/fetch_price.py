import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/85.0.4183.121 Safari/537.36"}


def fetch_name_price(product_url):
    page_html = requests.get(product_url, headers=header).text
    soup_beautiful = BeautifulSoup(page_html, 'html.parser')

    def amazon_page(soup):
        amazon_product_name = soup.find('span', class_='a-size-large product-title-word-break').text.strip()
        amazon_product_price = float(soup.find('span', class_='a-price-whole').text[:-1].replace('.', ''))

        obj = {"Name": amazon_product_name, "Price": amazon_product_price}
        return obj

    def gittigidiyor_page(soup):
        gittigidiyor_product_name = soup.find('h1', class_='title r-onepp-title').text
        gittigidiyor_product_price = float(soup.find('div', class_='lastPrice').text
                                           .strip()[:-3].replace('.', '').replace(',', '.'))

        obj = {"Name": gittigidiyor_product_name, "Price": gittigidiyor_product_price}
        return obj

    def hepsiburada_page(soup):
        hepsiburada_product_name = soup.find('h1', class_='product-name best-price-trick').text.strip()
        hepsiburada_product_price = float(soup.find('span', attrs={"id": "offering-price"}).text
                                          .strip().split()[0].replace('.', '').replace(',', '.'))

        obj = {"Name": hepsiburada_product_name, "Price": hepsiburada_product_price}
        return obj

    def n11_page(soup):
        n11_product_name = soup.find('h1', class_='proName').text.strip()
        n11_product_price = 0
        url = f"https://www.n11.com/arama?q={n11_product_name.replace(' ','%20').replace('(', '').replace(')','')}"
        n11_page_seller = soup.find('a', class_='main-seller-name').text

        n11_html = requests.get(url, headers=header).text
        n11_soup = BeautifulSoup(n11_html, 'html.parser')
        n11_list_items = n11_soup.find_all('li', class_='column')

        for i, item in enumerate(n11_list_items):
            name = item.find('span', class_='sallerName').text.strip()
            if name == n11_page_seller:
                n11_product_price = float(item.find('div', 'proDetail').find('span', class_='newPrice').ins.text
                                          .split()[0].replace('.', '').replace(',', '.'))
            break

        obj = {"Name": n11_product_name, "Price": n11_product_price}
        return obj

    def trendyol_page(soup):
        trendyol_product_name = soup.find('h1', class_='pr-new-br').text
        # Check if there's discount
        try:
            trendyol_product_price = float(soup.find('span', class_="prc-dsc").text[:-2]
                                           .replace('.', '').replace(',', '.'))
        except Exception:
            trendyol_product_price = float(soup.find('span', class_="prc-slg").text[:-2]
                                           .replace('.', '').replace(',', '.'))

        obj = {"Name": trendyol_product_name, "Price": trendyol_product_price}
        return obj

    if "gittigidiyor" in product_url:
        return gittigidiyor_page(soup_beautiful)
    elif "hepsiburada" in product_url:
        return hepsiburada_page(soup_beautiful)
    elif "trendyol" in product_url:
        return trendyol_page(soup_beautiful)
    elif "n11" in product_url:
        return n11_page(soup_beautiful)
    elif "amazon" in product_url:
        return amazon_page(soup_beautiful)
