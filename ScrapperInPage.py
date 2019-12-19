import re
from itertools import groupby

import bs4
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from Test import Scrapper


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
#Arr1 = []
#Arr1 = Scrapper(1)
#print(Arr1)

def PgScr(raw_data):
    data = raw_data
    z2 = 0
    countries = []
    for a in data:
        z = a.replace('/Internationals/UEFA+Euro/2020/Qualification/Play-Off+Round/1st+Round', '')
        raw_html = simple_get('https://www.marathonbet.ru/su/betting/Football/Internationals/UEFA+Euro/2020/Qualification/Play-Off+Round/1st+Round' + z)
        html = BeautifulSoup(raw_html, 'html.parser')
        #print(html)
        z1 = html.findAll('a', attrs={'class', 'member-link'})
        for z3 in z1:
            z3.find('p')
            countries.append(z3)
            y = [re.sub(r'<.+?>', r'', str(a)) for a in countries]
            #n = y[i]
            #i += 1
            print(y)
    new_y = []
    for x in y:
        if x not in new_y:
            new_y.append(x)
    return(new_y)

        #if z1 == z2:
        #print(y)
        #z2 = z1

def returner(list,id):
    return(list[id])

#returner(0)











