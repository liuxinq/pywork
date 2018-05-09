#!/usr/bin/python
import redis

r = redis.Redis(host='192.168.100.104',port=6379,db=0)

f = open('m_key.txt')
f1 = open('m_value.txt','w')
ok = True
while ok:
    line = f.readline()
    line = line.strip('\n')
    if line == '':
        ok = False
    else:
        a = r.get(line)
        f1.write(a + '\n')


#print r.mget('name','age')