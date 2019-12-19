import bs4
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
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
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)

def Scrapper(option):
    if option == 1:
        MyList=[]
        raw_html = simple_get('https://www.liveresult.ru/')
        html = BeautifulSoup(raw_html, 'html.parser')
        z = html.findAll('a', attrs={'class', 'nav-link'}, href=True)
        for a in z:
           if a['href'].find('/football/matches/match') == 0:
                MyList.append('https://liveresult.ru' + a['href'])
        buff = MyList
        return buff[3]
    else:
        print("")










