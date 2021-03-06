import requests
import bs4
import json
from flask import Flask, jsonify, make_response, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('WelcomePage.html')


@app.route('/gethot', methods =['GET'])
def get_hot():
    posts = get_news()
    return render_template("HotPage.html", posts=posts)


@app.route('/getrising', methods=['GET'])
def get_rising():
    posts = get_news('rising/')
    return render_template("RisingPage.html", posts=posts)


@app.route('/gettop', methods=['GET'])
def get_top():
    posts = get_news('top/')
    return render_template("TopPage.html", posts=posts)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error' : 'Page not found'}), 404)


@app.route('/r/<string:subreddit>', methods=['GET'])
def get_funny(subreddit):
    return get_news('r/'+subreddit+'/', 1)


def get_news(category='', cattype=0):
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
        dict['title'] = info.text
        dict['link'] = info['href']
        if cattype == 0:
            subreddit = post.select("p.tagline a")[1].text.capitalize()
            dict['subreddit'] = subreddit
        ret.append(dict)
    return ret


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    app.run(debug=True)