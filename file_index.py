import datetime
import requests
import sys
from bs4 import BeautifulSoup

tz = datetime.timezone.utc
ft = "%Y-%m-%dT%H_%M_%S"
timestamp = datetime.datetime.now(tz=tz).strftime(ft)
file_name = 'output_' + timestamp + '.txt'

html_text = requests.get('https://www.heraldweekly.com/animal-parents-who-just-say-everything-we-feel-about-parenting/2?xcmg=1').text

soup = BeautifulSoup(html_text, 'lxml')

articles = soup.find_all('div', class_ = 'cgSlide')


for index, article in enumerate(articles):
    article_heading = article.find('h2').text
    article_paragraph = article.find_all('p')

    file = open(file_name, 'a')
    sys.stdout = file

    print(article_heading)

    for article in article_paragraph:
        print(article.text)

    print('\n')

    file.close()