#!/usr/bin/python

#http://192.168.1.120/UpgradeVersionAction_check.action?os=x86&version=2.4.0

import web
import json
urls=(
	'/','index',
	'/test','test',
	"/json","json_test",
	'/UpgradeVersionAction_check.action',"check",
	'/CheckAction_check.action','check_user',
	'/DoTerminalThreeYards','three_yard'
	)

class index:
	def GET(self):
		return "Hello,world!"

class test:
	def GET(self):
		return "Hello,test!"

class check:
	def GET(self):
		i = web.input()
		os = i.os
		version = i.version
		return "Hello ,Check! os=",os,"version=",version
	def POST(self):
		i = web.input(id=[])
		print i
		return "OS :" 

class json_test:
	def GET(self):
		pyDict = {'name':'sslvpn','length':12580,'version':'2.4.0.0','flag':False}
		web.header('Content_Type','application/json')
		return json.dumps(pyDict)

class check_user:
	def GET(self):
		pyDict = {'success':True,'compare':True}
		web.header('Content_Type','application/json')
		return json.dumps(pyDict)
	def POST(self):
		i = web.input(id=[])
		print i

		pyDict = {'success':True,'compare':True}
		web.header('Content_Type','application/json')
		return json.dumps(pyDict)

class three_yard:
	def GET(self):
		pyDict = {'success':True,'msg':'OK'}
		web.header('Content_Type','application/json')
		return json.dumps(pyDict)
	def POST(self):
		i = web.input(id=[])
		print i

		pyDict = {'success':True,'msg':'Bad'}
		web.header('Content_Type','application/json')
		return json.dumps(pyDict)


if __name__== "__main__":
	app = web.application(urls,globals())
	app.run()
