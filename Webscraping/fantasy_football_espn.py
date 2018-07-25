import requests
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from espn_scraping_utility import getBioImgURL

r = requests.get(
    "http://www.espn.com/fantasy/football/story/_/page/18RanksPreseason300PPR/2018-fantasy-football-ppr-rankings-top-300")
c = r.content


soup = BeautifulSoup(c, "html.parser")

playerRows = soup.find_all("tr",{"class":"last"})
arrPlayerIds = []
for playerRow in playerRows:    
    try:
        arrPlayerURLPart = playerRow.find(href=True)['href'].split("/")
        playerId = arrPlayerURLPart[len(arrPlayerURLPart)-2]
        if playerId.isnumeric():
            arrPlayerIds.append(playerId)
 #       playerLinks.append(playerRow.find(href=True)['href'])
    except:
        pass

#player picture info found at div class="main-headshot"
playerStatsURLTemplate = "http://www.espn.com/nfl/player/stats/_/id/{0}"
playerSplitsURLTemplate = "http://www.espn.com/nfl/player/splits/_/id/{0}"
playerGameLogURLTemplate = "http://www.espn.com/nfl/player/gamelog/_/id/{0}"

playerId = arrPlayerIds[1]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="./chromedriver")
driver.get(playerStatsURLTemplate.format(playerId))
content_element = driver.find_element_by_id("content")
content_html = content_element.get_attribute("innerHTML")
pSoup = BeautifulSoup(content_html,"html.parser")
img_url = getBioImgURL(pSoup)

driver.close()


