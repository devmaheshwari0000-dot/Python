# Hints:
# - Subclass HTMLParser and implement handle_starttag/handle_endtag/handle_data, or use regex for quick link extraction.

# Solution:
from html.parser import HTMLParser
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for k, v in attrs:
                if k == 'href':
                    self.links.append(v)

p = LinkParser()
html = '<a href="http://x">X</a>'
p.feed(html)
print(p.links)
