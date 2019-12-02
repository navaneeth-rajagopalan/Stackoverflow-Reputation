import urllib.request
import json
import re
from bs4 import BeautifulSoup

url = "https://data.stackexchange.com/stackoverflow/query/9320/find-stack-overflow-users-in-your-city-with-user-links?Location=Melbourne"

with urllib.request.urlopen(url) as url:
    html = url.read()
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find_all("script")[8]
    print("\n\n\n")
    p = re.compile(r'[\d\D]+"resultSets"=([\d\D]+?);')
    m = p.match(data)
    if m:
        result = m.group(1)
        print(result)
    print("\n\n\n")