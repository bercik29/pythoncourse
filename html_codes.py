
#!/usr/bin/env pyhon

import requests as req
import re

resp = req.get("http://www.webcode.me")
content = str(resp.content, 'utf-8')
# print(content)

pattern = re.compile(r'(</?.*>)') #(</?.*>)
found = re.findall(pattern, content)
tagWords = []

tagWords = re.split('(</?.*\s>)', found)

# found = re.findall(pattern, content)
# i = 0

# for tag in found:
#         tagReplace = tag.replace(*, ' ')
#         tagReplace = tag.replace('<', ' ')
#         tagReplace.strip()
#         tagWords = []
#         tagWords = re.split(' ', tagReplace)
        
#         for i in range(len(tagWords)):
#             pattern = re.compile(r'(</?.*\s)') #
#             found = re.findall(pattern, tagWords[i])
#             if not found:
#                 print(tagWords[i])
