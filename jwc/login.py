#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-03-24 12:09
@Author  : red
@Site    : 
@File    : login.py
@Software: PyCharm
"""
# -*- coding: utf-8 -*-

import requests
import chardet

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
header = {
	"Origin": "http://login.cuit.edu.cn",
	"Referer": "http://login.cuit.edu.cn/Login/xLogin/Login.asp",
	'User-Agent': userAgent,
}


# def get_verify():


def mafengwo_login(account, password):
	# 马蜂窝模仿 登录
	print("开始模拟登录马蜂窝")

	post_url = "http://login.cuit.edu.cn/Login/xLogin/Login.asp"
	postData = {
		"WinW": 1680,
		"WinH": 975,
		"verifycode": "7k7",
		"txtId": account,
		"txtMM": password,
		"codeKey": 438448,
		"Login": "Check",
		"IbtnEnter.x": 33,
		"IbtnEnter.y": 51
	}

	response_res = requests.post(post_url, data=postData, headers=header)
	# 无论是否登录成功，状态码一般都是 statusCode = 200
	print(f"statusCode = {response_res.status_code}")


if __name__ == "__main__":
	# 从返回结果来看，有登录成功
	mafengwo_login("2015021331", "J2015021331")
