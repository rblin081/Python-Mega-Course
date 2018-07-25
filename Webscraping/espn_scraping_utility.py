import requests
import os

def getBioImgURL(pSoup):
    return pSoup.find("div",{"class":"main-headshot"}).find("img")['src']  


def downloadImg(url, destination):
    filename, file_extension = os.path.splitext(url)
    file_extension = file_extension.split("&")[0]
    f = open(destination,'wb')
    f.write(requests.get('content'))
    f.close()




