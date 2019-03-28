#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-24 12:03
@Author  : red
@Site    : 
@File    : get_xiaoli.py
@Software: PyCharm
"""
# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-24 11:52
@Author  : red
@Site    : 
@File    : get_jwc.py
@Software: PyCharm
"""
import urllib.request
import re
import random

uapools = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
]


def UA():
	opener = urllib.request.build_opener()
	thisua = random.choice(uapools)
	ua = ("User-Agent", thisua)
	opener.addheaders = [ua]
	urllib.request.install_opener(opener)


if __name__ == '__main__':
	UA()
	thisurl = "http://jwc.cuit.edu.cn/"
	data = urllib.request.urlopen(thisurl).read().decode("utf-8", "ignore")
	pat = '<div class="col-xs-3 c_b_a  service calendar">(.*?)</div>'
	rst = re.compile(pat, re.S).findall(data)
	print(rst)
