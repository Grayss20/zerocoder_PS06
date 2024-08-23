import requests
from bs4 import BeautifulSoup


url = "https://"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all("tr")
data = []

for row in rows:
    cols = row.find_all("td")
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

print(data)