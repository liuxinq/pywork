#!/usr/bin/python2
#coding=utf-8

import json
f = open('test.txt', 'r')

#data = {"id": 1, "name": "dbuser"}
#print json.dumps(data)

ok = True
data = {}
data["id"] = 0
while ok:
    line = f.readline().strip("\n")
    if line == "":
        ok = False
    else:
        data["id"] = data["id"] + 1
        data["str1"] = line
        in_json = json.dumps(data)
        print json.loads(in_json)
        print type(json.loads(in_json))