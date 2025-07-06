from bs4 import BeautifulSoup
import pandas as pd
import requests

def testing():
    
    resp = requests.get('https://finance.detik.com') #url

    #print(resp.content)
    #print(resp.status_code)

    soup = BeautifulSoup(resp.content, 'html.parser')

    #print(soup)

    rows = soup.select(".datafx .datafx__item") #datafx__item

    pair_data = []

    for r in rows:
        title = r.select_one(".datafx__item--title").get_text(strip=True)
        value = r.select_one(".datafx__item--value").get_text(strip=True)
        changes = r.select_one(".datafx__item--changes").get_text(strip=True)
        percent = r.select_one(".datafx__item--percent").get_text(strip=True)

        pair_data.append((dict
            stock = title,
            value = value,
            changes = changes,
            percent = percent                 
        ))

        #print(f"{title} \n {value} \n Change: {changes} \n Percent: {percent} \n")

    return pd.DataFrame.from_dict(pair_data)
