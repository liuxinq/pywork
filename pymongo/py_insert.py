#!/usr/bin/python2
#coding=utf-8

import json
import pymongo

## 连接mongodb库
def connect_mongodb():
    servers = "mongodb://192.168.100.104:27017"
    conn = pymongo.MongoClient(servers)
    db = conn.db01
    db.authenticate('dbuser', 'a')
    return db

db = connect_mongodb()
test = db.test

## 批量插入mongodb库
f = open('test.txt', 'r')
ok = True
data = {}
data["_id"] = 0
d = []
while ok:
    line = f.readline().strip("\n")
    if line == "":
        ok = False
    else:
        data["_id"] = data["_id"] + 1
        data["str1"] = line
        test.insert(data)