from bs4 import BeautifulSoup
import requests


def read_countries():
    countries = []
    file_path = 'countries.txt'
    with open(file_path) as fp:
        line = fp.readline()
        while line:
            countries.append(line.strip())
            line = fp.readline()
    return countries


def set_url(country):
    wiki_url = 'https://en.wikipedia.org/wiki/'+country
    return wiki_url


def read_html(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    return soup


def find_capital(soup):
    capital = soup.find_all('tr')[5].find('td').find('a').string
    return capital


def find_languages(soup):
    languages = ''
    lang = soup.find_all('tr')[6].find('td').find_all('a')
    for l in lang:
        if check_validity(l.string):
            languages += ' ,'+l.string
    return languages


def find_ethnic_groups(soup):
    ethnic_groups = ''
    e_groups = soup.find_all('tr')[7].find('td').find_all('a')
    for eg in e_groups:
        if check_validity(eg.string):
            ethnic_groups += ' ,' + eg.string
    return ethnic_groups


def find_religion_groups(soup):
    religion_groups = ''
    r_groups = soup.find_all('tr')[8].find('td').find_all('a')
    for rg in r_groups:
        if check_validity(rg.string):
            religion_groups += ' ,' + rg.string
    return religion_groups


def check_validity(my_str):
    if my_str[0] == '[':
        return False
    else:
        return True



