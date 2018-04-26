import requests
import bs4
from flask import Flask

def get_news(category=''):
    index_url = "http://www.reddit.com/"
    session = requests.Session()
    session.headers.update({'User-Agent': 'Custom user agent'})
    response = session.get(index_url + category)
    print(response.text)
    ret = []
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    posts = soup.select("div#siteTable div.thing")
    for post in posts:
        dict = {}
        info = post.select("p.title a")[0]
        subreddit = post.select("p.tagline a")[1].text.capitalize()
        dict['title'] = info.text
        dict['link'] = info['href']
        dict['subreddit'] = subreddit
        ret.append(dict)
    return ret


def get_hot():
    return get_news()


def get_rising():
    return get_news('rising/')


def get_top():
    return get_news('top/')


posts = get_hot()
print(posts)