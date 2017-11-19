from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    #method2
    req = requests.get("https://habrahabr.ru/")
    soup = BeautifulSoup(req.content, 'html.parser')

    result = soup.select('li > article.post_preview > h2 > a')
    for i in result:
        print(i.get('href'))