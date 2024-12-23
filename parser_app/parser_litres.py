import requests
from bs4 import BeautifulSoup as BS4

URL = 'https://www.litres.ru'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


#1 make request
def get_html(url, params=""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


#2 get data
def get_data(html):
    bs = BS4(html, features="html.parser")
    items = bs.find_all('div', class_="ArtsGrid_grid__K8Emb")
    litres_list = []
    for item in items:
        title = item.find("div", class_="ArtInfo_info__BgoQR").get_text()
        parts = title.split(".")
        result = parts[0] + "." if len(parts) > 1 else title.strip()
        title = result
        image = URL + item.find("div", class_="Art_content__image__1N92h").find("img").get("src")
        formats = item.find("div", class_="ArtFormat_format__weVS9").get_text(strip=True)
        price = item.find("div", class_="ArtPrice_finalPrice__sFS_4").get_text(strip=True)
        litres_list.append(
            {
                "title": title,
                "image": image,
                "formats": formats,
                "price": price,
            }
        )
    return litres_list


#3 func parsing
def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        litres_list2 = []
        for page in range(1,10):
            response = get_html("https://www.litres.ru/popular/", params={"page": page})
            litres_list2.extend(get_data(response.text))
        return litres_list2
    else:
        raise Exception('Error in parsing')


# print(parsing())