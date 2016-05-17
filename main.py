import urllib2
from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    url = request.args.get("url")
    title_filters = request.args.get("title_filters")
    content_filters = request.args.get("content_filters")

    # Create/open request, spoof user agent for picky feeds
    req = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    feed_content = urllib2.urlopen(req)
    fetched_feed = feed_content.read()

    # Parse content to XML
    parsed_feed = etree.fromstring(fetched_feed)

    # Run filters
    if title_filters:
        for f in title_filters.split(","):
            filter_xpath = "//title[re:test(text(),'%s' , 'i')]/parent::*" % f
            for matched_item in parsed_feed.xpath(filter_xpath, namespaces={"re": "http://exslt.org/regular-expressions"}):
                matched_item.getparent().remove(matched_item)

    if content_filters:
        for f in content_filters.split(","):
            filter_xpath = "//description[re:test(text(),'%s' , 'i')]/parent::*" % f
            for matched_item in parsed_feed.xpath(filter_xpath, namespaces={"re": "http://exslt.org/regular-expressions"}):
                matched_item.getparent().remove(matched_item)

    # Convert back to string, return    
    filtered_feed = etree.tostring(parsed_feed)
    return unicode(filtered_feed), 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run()
