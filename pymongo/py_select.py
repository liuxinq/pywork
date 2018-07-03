#!/usr/bin/python2
#coding=utf-8

from pymongo import MongoClient

client = MongoClient("192.168.100.104",27017)

db = client.db01

db.authenticate('dbuser','a')

col = db.test

for item in col.find():
    print item

client.close()
