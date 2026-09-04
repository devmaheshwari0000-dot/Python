# Hints:
# - Use re.findall with an email or URL regex; for URLs, look for http(s)://

# Solution:
import re
text = 'Visit https://example.com or http://test.org'
urls = re.findall(r'https?://[\w./-]+', text)
print(urls)
