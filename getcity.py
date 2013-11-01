#!/usr/bin/env python
#!coding=utf-8

import urllib2, re

url = "http://www.cnpm25.cn/"

r = urllib2.urlopen(url)
raw = r.read()

pat = re.compile('''<a href="city/(.*?)\.html" target="_blank"><strong>(.*?)</strong></a>''')

citylist = pat.findall(raw)

citydict = {}
for city in citylist:
    citydict[city[1]] = city[0]


result = open("citylist.txt", "w")

for city in citydict:
    result.write(city.replace("&nbsp;", "").strip()+","+citydict[city].strip()+"\n")

result.close()