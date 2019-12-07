import requests
from bs4 import BeautifulSoup
req = requests.get("https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E4%BC%BD%E5%8B%92%E5%B0%94%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89")

soup = BeautifulSoup(req.text, 'lxml')
# print(soup)
tb = soup.find_all('table', attrs={'class': 'roundy eplist bgl-伽勒尔 bd-伽勒尔'})[0]

trs = tb.find_all('tr')

urls = []
for tr in trs[1:]:
    a = tr.find_all('a')[0]
    urls.append('https://wiki.52poke.com'+a.attrs['href'])

print(urls)

import json
json.dump(urls, open('urls.json', 'w'))
