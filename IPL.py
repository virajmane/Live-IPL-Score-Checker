from flask import Flask
from bs4 import BeautifulSoup
import requests
import re

app = Flask("__name__")
base_url = "https://www.google.com/search?q=ipl"
req = requests.get(base_url).text
bs = BeautifulSoup(req, "html.parser")
match = bs.find_all('div', class_="BNeawe tAd8D AP7Wnd")[0]
team1 = bs.find_all('div', class_="BNeawe s3v9rd AP7Wnd lRVwie")[1]
team2 = bs.find_all('div', class_="BNeawe s3v9rd AP7Wnd lRVwie")[2]
overs1 = bs.find_all('span', class_="r0bn4c rQMQod")[0]
overs2 = bs.find_all('span', class_="r0bn4c rQMQod")[1]
innings1 = bs.find_all("div", class_="BNeawe deIvCb AP7Wnd")[1]
innings2 = bs.find_all("div", class_="BNeawe deIvCb AP7Wnd")[2]

match = re.search(">(.*)<", str(match)).group(1)
team1 = re.search(">(.*)<", str(team1)).group(1)
team2 = re.search(">(.*)<", str(team2)).group(1)
overs1 = re.search(">(.*)<", str(overs1)).group(1)
overs2 = re.search(">(.*)<", str(overs2)).group(1)
innings1 = re.search(">(.* )<", str(innings1)).group(1)
innings2 = re.search(">(.* )<", str(innings2)).group(1)
jsoc = [{"team1": team1, "team2": team2, "innings1": innings1, "innings2": innings2}]

@app.route("/")
def index():
  return f"<code>{jsoc}</code>"

@app.route("/api")
def api():
  return f'<code>{jsoc}</code>'

if __name__ == "__main__":
    app.run()
