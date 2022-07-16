import requests
import re
import html

s = requests.get('http://www.columbia.edu/~fdc/sample.html')
data = html.unescape(s.text)
title = re.findall(r'<h3.+>.+</h3>', data)
title_final = []
for elem in title:
    res = re.sub(r'<h3.+[^/h3]>|</h3>', '', elem)
    title_final.append(res)
print(title_final)
