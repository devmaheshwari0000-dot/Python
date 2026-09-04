# Hints:
# - Use ElementTree.fromstring to parse XML and find() to get elements.

# Solution:
import xml.etree.ElementTree as ET
s = '<root><child>value</child></root>'
root = ET.fromstring(s)
print(root.find('child').text)
