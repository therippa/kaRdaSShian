from flask import Flask, request
import feedparser
import json
import pprint
from bs4 import BeautifulSoup
from lxml import etree

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def hello_world():
    #feed = request.args.get('feed')
    #fetched_feed = feedparser.parse(feed)
    #pp = pprint.PrettyPrinter(indent=4)
    feedfile = open('sample.xml', 'r')
    fetched_feed = feedfile.read()
    #a = BeautifulSoup(fetched_feed, 'lxml')
    b = etree.fromstring(fetched_feed)

    for bad in b.xpath("//item/title[contains(text(),'Shia')]"):
    	print "foudn one"
    	bad.getparent().getparent().remove(bad)

    a = etree.tostring(b)
    return unicode(a), 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run()

