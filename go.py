#!/usr/bin/env python
#!coding=utf-8

import urllib2, re

cityname = "{query}"

citylist_file = open("citylist.txt", "r")
citylist_raw = citylist_file.readlines()

citylist = []
for line in citylist_raw:
    citylist.append(line.split(","))

citydict = dict(citylist)

citypinyin = citydict[cityname].replace("\n", "").strip()
url = "http://www.cnpm25.cn/city/%s.html" % citypinyin

r = urllib2.urlopen(url)
raw = r.read()

pat = re.compile('''jin_value = "(\d+)";''')
info_list = pat.findall(raw)

if info_list:
    pm = int(info_list[0])
    air = "优"
    if pm > 50 and pm <= 100:
        air = "良"
    elif pm > 100 and pm <= 150:
        air = "轻度污染"
    elif pm > 150 and pm <= 200:
        air = "中度污染"
    elif pm > 200 and pm <= 300:
        air = "重度污染"
    elif pm > 300:
        air = "严重污染，活不下去"

    print '''<?xml version="1.0"?><items><item arg="%s" valid="yes" ><title>PM 2.5 Info</title><subtitle>PM2.5 at %s is %s. 空气质量：%s</subtitle><icon>pm.png</icon></item></items>''' % (citypinyin, cityname, pm, air)
else:
    print '''<?xml version="1.0"?><items><item valid="yes" ><title>PM 2.5 Info</title><subtitle>The city name is invalid or there is no PM2.5 info for it.</subtitle><icon>pm.png</icon></item></items>'''