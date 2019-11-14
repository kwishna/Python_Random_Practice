import os
import requests
from lxml import html
import wget

base_url = "http://inst.eecs.berkeley.edu/~cs61a/fa18/"

res = requests.get(base_url)
text = res.content

with open("response.txt", "w+") as f:
    print(text, file=f)

tree = html.fromstring(text)
elements = tree.xpath('//li/a[text()="8pp"]/@href')

with open("response.txt", "w+") as f:
    for i in set(elements):
        wget.download(url=base_url+i, out="./slides/")