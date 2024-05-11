from bs4 import BeautifulSoup
import requests


class Parser:
    def __init__(self):
        self.url = 'https://www.dvfu.ru/news'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0)\
         Gecko/20100101 Firefox/125.0'}
        page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page.text, "html.parser")

        self.allNews = soup.findAll('div', class_="news-item")
        self.count_n = 0

    def get_news(self, move='last'):
        if move == 'next':
            box = self.allNews[self.count_n - 1]
            self.count_n -= 1
        elif move == 'prev':
            box = self.allNews[self.count_n + 1]
            self.count_n += 1
        elif move == 'last':
            box = self.allNews[self.count_n]
        else:
            return ['Такой страницы нет', '']

        title = box.findNext('span', class_='news-item-short').text + '\n'

        link = box.findNext('a')['href']
        link = 'https://www.dvfu.ru' + link

        text = self.get_news_text(link)
        # article = f'*{title}*\n{text}\n{link}'

        return {'title': title, 'text': text, 'link': link}

    def get_news_text(self, link):
        text = ''
        page = requests.get(link, headers=self.headers)
        soup = BeautifulSoup(page.text, "html.parser")

        text_p = soup.findAll('p')[3:][:-16]
        for line in text_p:
            text += f'{line.text}\n'
        return text
