from bs4 import BeautifulSoup
import cloudscraper
import pyfiglet
import os
from pystyle import *

scraper = cloudscraper.create_scraper()

def cls() :
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

def request_searchcc():
    Write.Print('Enter your keyword: ', Colors.red_to_purple)
    keyword = input()
    url = ('https://searchresults.cc/' + keyword)
    r = scraper.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

def extract_urls():
    search = request_searchcc().find_all('h4')
    resultados = []
    for urls in search:
        resultados.append(urls.text)
    return resultados

def save(urls):
    with open('URLS/urls.txt', 'w') as fp :
        for url in urls:
            # write each item on a new line
            fp.write("%s\n" % url)
    Write.Print('\nFinished :D', Colors.blue_to_yellow, interval=0.5)

def cartel(text):
    Write.Print("By Mocos0", Colors.red_to_yellow)
    Write.Print(pyfiglet.figlet_format(text, justify="center", font='slant'), Colors.red_to_yellow, interval=0.1)

if __name__ == '__main__':
    cls()
    cartel('PasteHub Scraper')
    save(extract_urls())
