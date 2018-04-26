import requests
import bs4
import json
from flask import Flask, jsonify, make_response


app = Flask(__name__)


@app.route('/gethot', methods =['GET'])
def get_hot():
    return get_news()


@app.route('/getrising', methods=['GET'])
def get_rising():
    return get_news('rising/')


@app.route('/gettop', methods=['GET'])
def get_top():
    return get_news('top/')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Page not found'}), 404)


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
    return json.dumps(ret)


if __name__ == '__main__':
    app.run(debug=True)