def get_links(product_name):
    amazon_link = f"https://www.amazon.com.tr/s?k={product_name}&rh=n%3A13709880031%2Cn%3A13709907031"
    gittigidiyor_link = f"https://www.gittigidiyor.com/cep-telefonu?k={product_name}"
    hepsiburada_link = f"https://www.hepsiburada.com/ara?q={product_name}&kategori=2147483642_371965"
    trendyol_link = f"https://www.trendyol.com/sr?q={product_name}&qt={product_name}&st={product_name}&lc=109460&os=1"
    n11_link = f"https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu?q={product_name}"

    website_links = {
        "amazon": amazon_link,
        "gittigidiyor": gittigidiyor_link,
        "hepsiburada": hepsiburada_link,
        "trendyol": trendyol_link,
        "n11": n11_link
    }

    return website_links
