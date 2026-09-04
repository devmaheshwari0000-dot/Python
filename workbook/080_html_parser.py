# Example 80: HTML parsing with html.parser
# Topics: html.parser or use BeautifulSoup (external)
from html.parser import HTMLParser
class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start', tag)

# Task: extract all links from an HTML string (use regex or parser)
