# Example 79: XML parsing with ElementTree
# Topics: xml.etree.ElementTree
import xml.etree.ElementTree as ET
root = ET.Element('root')
ET.SubElement(root, 'child').text = 'content'
print(ET.tostring(root))

# Task: parse a small XML string and extract a value
