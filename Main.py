import json

import requests
import bs4


def get_news():
    index_url = "http://www.reddit.com/"
    response = requests.get(index_url)
    ret = []
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    posts = soup.select("div#siteTable div.thing")
    for post in posts:
        info = post.select("p.title a")[0]
        subreddit = post.select("p.tagline a")[1].text.capitalize()
        ret.append({"title":info.text, "link":info["href"], "subreddit": subreddit})
    return json.dumps(ret)


print(get_news())