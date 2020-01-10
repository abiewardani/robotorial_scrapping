from bs4 import BeautifulSoup
import requests

websiterUrl = requests.get("https://www.indopremier.com/module/saham/include/fundamental.php?code=TLKM&quarter=2").text
soup = BeautifulSoup(websiterUrl, "html5lib")

myTable = soup.find("table", {"class": "table-fundamental"})
datas = myTable.find('tbody').findAll("tr")

history = []
for row in datas:
    td_list = row.find_all("td")
    for rowTd in td_list:
        history.append(rowTd.text)

print(lastPrice)

def lastPrice():
    return "123"