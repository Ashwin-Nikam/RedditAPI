# RedditAPI
Simple API for Reddit built using BeautifulSoup and Flask in Python. 

## Initial Setup
* Make sure you have python3 installed.
* Now we install pip as it makes it easier to download the latest version of Flask and BeautifulSoup globally. Execute the following command.
```
$ sudo apt-get install python3-pip
```
* Now we install a virtual environment using pip3
```
$ sudo pip3 install virtualenv 
```

## Running the server
* Clone this repo and cd into it.
```
$ git clone <this-repo>
$ cd <this-repo>
```
* Run the virtual environment
```
$ source venv/bin/activate
```
* Now that our venv is up and running we can install Flask and BeautifulSoup in our venv
```
$ pip3 install Flask
$ pip3 install bs4
```
* Now that all the necessary libraries are installed we can run the server by executing the following command:
```
$ python3 Main.py
```

## Using the API
* Now that the server is running open any internet browser and type in the following URL:
```
http://127.0.0.1:5000
```
* You'll be taken to the welcom page of this basic API.

### Types of request
* Type in the following URLs in the browser and see the results.

#### Get hot posts
```
http://127.0.0.1:5000/gethot
```

#### Get top posts
```
http://127.0.0.1:5000/gettop
```

#### Get rising posts
```
http://127.0.0.1:5000/gettop
```

## Tools and Technologies used
* [Python](https://www.python.org/)
* [HTML & CSS](https://www.w3schools.com/html/html_css.asp)
* [Flask](http://flask.pocoo.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## References
* http://melvin0008.github.io/blog/build-a-redditapi-using-python/ 