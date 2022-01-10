import requests
from bs4 import BeautifulSoup

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/85.0.4183.121 Safari/537.36"}

def gittigidiyor_most_cheap(product_name):
    gittigidiyor_sorted_link = f"https://www.gittigidiyor.com/cep-telefonu?k={product_name}&sra=hpa"
    page_html = requests.get(gittigidiyor_sorted_link, headers=header).text
    soup = BeautifulSoup(page_html, 'html.parser')

    div = soup.find('div', class_='pmyvb0-0')

    gittigidiyor_cheapest_name = div.li.a.h3.text
    gittigidiyor_cheapest_link = div.li.a['href']
    gittigidiyor_cheapest_price = float(div.li.a.find('span', class_='buy-price').text
                                            .strip()[:-3].replace('.', '').replace(',', '.'))

    obj = {
        "Website": "Gittigidiyor",
        "Name": gittigidiyor_cheapest_name,
        "Price": gittigidiyor_cheapest_price,
        "Link": gittigidiyor_cheapest_link
    }

    return obj

def hepsiburada_most_cheap(product_name):
    hepsiburada_sorted_link = f"https://www.hepsiburada.com/ara?q={product_name}" \
                              f"&kategori=2147483642_371965&siralama=artanfiyat"
    page_html = requests.get(hepsiburada_sorted_link, headers=header).text
    soup = BeautifulSoup(page_html, 'html.parser')

    li = soup.find('li', class_='productListContent-item')
    hepsiburada_cheapest_name = li.div.h3.text
    hepsiburada_cheapest_link = 'https://www.hepsiburada.com' + li.a['href']

    html = requests.get(hepsiburada_cheapest_link, headers=header).text
    hepsiSoup = BeautifulSoup(html, 'html.parser')
    hepsiburada_cheapest_price = float(hepsiSoup.find('span', attrs={"id": "offering-price"}).text
                                       .strip().split()[0].replace('.', '').replace(',', '.'))

    obj = {
        "Website": "Hepsiburada",
        "Name": hepsiburada_cheapest_name,
        "Price": hepsiburada_cheapest_price,
        "Link": hepsiburada_cheapest_link
    }

    return obj

def n11_most_cheap(product_name):
    n11_sorted_link = f"https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?q={product_name}&srt=PRICE_LOW"
    page_html = requests.get(n11_sorted_link, headers=header).text
    soup = BeautifulSoup(page_html, 'html.parser')

    li = soup.find('li', class_='column')
    n11_cheapest_name = li.find('h3', class_='productName').text.strip()
    n11_cheapest_price = float(li.find('div', 'proDetail').find('span', class_='newPrice').ins.text
                               .split()[0].replace('.', '').replace(',', '.'))
    n11_cheapest_link = li.find('div', class_='pro').a['href']

    obj = {
        "Website": "N11",
        "Name": n11_cheapest_name,
        "Price": n11_cheapest_price,
        "Link": n11_cheapest_link
    }

    return obj

def trendyol_most_cheap(product_name):
    trendyol_sorted_link = f"https://www.trendyol.com/sr?q={product_name}&qt={product_name}&st={product_name}" \
                           f"&lc=109460&os=1&sst=PRICE_BY_ASC"
    page_html = requests.get(trendyol_sorted_link, headers=header).text
    soup = BeautifulSoup(page_html, 'html.parser')
    div = soup.find('div', class_='p-card-wrppr')

    trendyol_cheapest_name = div.find('span', class_='prdct-desc-cntnr-name').text
    try:
        trendyol_cheapest_price = float(div.find('div', class_='prc-box-dscntd').text[:-3]
                                        .replace('.', '').replace(',', '.'))
    except Exception:
        trendyol_cheapest_price = float(div.find('div', class_='prc-box-sllng').text[:-3]
                                        .replace('.', '').replace(',', '.'))

    trendyol_cheapest_link = 'https://www.trendyol.com' + div.a['href']

    obj = {
        "Website": "Trendyol",
        "Name": trendyol_cheapest_name,
        "Price": trendyol_cheapest_price,
        "Link": trendyol_cheapest_link
    }
    return obj

def best_price_sorted_list(product_name):
    price_list = [gittigidiyor_most_cheap(product_name), hepsiburada_most_cheap(product_name),
                  n11_most_cheap(product_name), trendyol_most_cheap(product_name)]

    sorted_list = sorted(price_list, key=lambda x: x['Price'])
    return sorted_list
