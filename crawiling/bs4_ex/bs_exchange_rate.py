from bs4 import BeautifulSoup as BS
import requests as req
import csv
url = "https://finance.yahoo.com/most-active"
res = req.get(url)
soup = BS(res.text, "html.parser")
trs =soup.select("table tr")

data_list=[]
for tr in trs:
    temp=[]

    if len(tr.select("td:nth-child(2)")) == 0:
        continue

    tit = tr.select("td:nth-child(2)")[0].get_text(strip=True)
    temp.append(tit)

    price = tr.select("td:nth-child(3) fin-streamer")[0].get_text(strip=True)
    temp.append(price)

    change1 = tr.select("td:nth-child(4) span")[0].get_text(strip=True)
    temp.append(change1)

    change2 = tr.select("td:nth-child(5) span")[0].get_text(strip=True)
    temp.append(change2)
   
    data_list.append(temp)

with open('yahoostock.csv','w',encoding="utf-8-sig",newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data_list)