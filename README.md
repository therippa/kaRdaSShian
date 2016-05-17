# KaRdaSShian

A **R**eally **S**uper **S**imple RSS feed filter.

## The Idea
For years I've been using RSS to manage the sites I read daily.  Unfortunately, some feeds I subscribe to are peppered with items I couldn't care less about (Kardashian news, Kanye news, etc).  

KaRdaSShian is a simple proxy that lets you load a feed, while filtering out the items you don't want to see.

The motivation behind this is that Feedly doesn't offer filtering (seriously?) and CommaFeed's filtering doesn't work very well.

## Installation
The proxy server will have to run on a publically-available address to work with most readers.  I'd recommend setting this up on a free-tier Amazon EC2 instance or Heroku dyno.

Make sure Python 2.7 is installed, and install the requirements:

	pip install -r requirements.txt
	
After that is done, spin up the server with:

	python main.py
	
I'd also recommend using nginx/gunicorn to run the server once you have it installed on its permanent home.  There is an excellent guide available [here](https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/).

## Usage
The application accepts three GET variables:

Name  | Value
------------- | -------------
URL  | Location of the feed to be loaded/filtered
content_filters  | Comma-delimited list of items to search the content of each post for  
title_filters  | Comma-delimited list of items to search the title of each post for

Any post in the feed matching the filters provided will be stripped from the output.  Here is an example of what the URL should look like:

	http://yoursite:5000/?url=http://www.someecards.com/combined-rss&content_filters=Kardashian,Kanye,Bieber,Stodden
