from datetime import timedelta, date
import requests
import codecs
from time import sleep

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

class Hit:
    def __init__(self,  date,title, desc):
        self.title = title
        self.date = date
        self.desc = desc
    def __str__(self):
        return "[{title}, {date}, {desc}]"
        



def search(start_date, end_date, s):
    collected_news = []

    # ciclo que itera sobre as datas de fim e de inicio
    for single_date in daterange(start_date, end_date):
        session = requests.Session()
        response = session.get("https://expresso.pt/api/molecule/latest/economia?offset="+single_date.strftime("%Y-%m-%d"))
        parsed_html = BeautifulSoup(response.content)

        desc = []
        titl = []
        date = []

        for de in parsed_html.body.findAll('h2', attrs={'class': 'lead'}):
            desc.append(de.text)

        for dat in parsed_html.body.findAll('p', attrs={'class': 'publishedDate'}):
            date.append(dat.text)

        for div in parsed_html.body.findAll('h1', attrs={'class': 'title'}):
            titl.append(div.find('a').contents[0])

        for i in range(len(desc)):
            collected_news.append(Hit(date[i], titl[i], desc[i]))
        print("current date: "+ str(single_date))
        sleep(s)

    return collected_news
