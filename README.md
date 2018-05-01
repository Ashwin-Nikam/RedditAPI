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
$ git clone https://github.com/Ashwin-Nikam/RedditAPI.git
$ cd RedditAPI
```
* Run the virtual environment
```
$ source venv/bin/activate
```
* Now that venv is running, we have all the necessary libraries installed. We can now run the server by executing the following command:
```
$ python3 Main.py
```

## Using the API
* Now that the server is running open any internet browser and type in the following URL:
```
http://127.0.0.1:5000
```
* You'll be taken to the welcome page of this basic API.

### Types of request
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
http://127.0.0.1:5000/getrising
```

## Tools and Technologies used
* [Python](https://www.python.org/)
* [HTML & CSS](https://www.w3schools.com/html/html_css.asp)
* [Flask](http://flask.pocoo.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## References
* http://melvin0008.github.io/blog/build-a-redditapi-using-python/ 