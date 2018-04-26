import json
import requests
import bs4


def get_news():
    index_url = "http://www.reddit.com/top/"
    session = requests.Session()
    session.headers.update({'User-Agent': 'Custom user agent'})
    response = session.get(index_url)
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


posts = get_news()
print("hello")