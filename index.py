import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.heraldweekly.com/animal-parents-who-just-say-everything-we-feel-about-parenting/2?xcmg=1').text

soup = BeautifulSoup(html_text, 'lxml')

articles = soup.find_all('div', class_ = 'cgSlide')

for article in articles:
    article_heading = article.find('h2').text
    article_paragraph = article.find_all('p')
    print(article_heading)

    for article in article_paragraph:
        print(article.text)

    print('\n')