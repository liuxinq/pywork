#coding=utf8

import threading,time
import MySQLdb

conn = MySQLdb.connect(
    host='192.168.100.106',
    port=3307,
    user='dbuser',
    passwd='a',
    db='db03',
)
cur = conn.cursor()

def select1(sql):
    print  threading.currentThread().getName(),"准备执行"
    s = time.time()
    cur.execute(sql)
    e = time.time()
    print "执行耗时: %s" % (e -  s)

threads = []
for i in range(1,2):
    sql = "select id,k from t_%s" % i
    t = threading.Thread(target=select1, args=(sql,))
    threads.append(t)

if __name__ == '__main__':
    print "获取数据库连接成功，准备执行SQL..."
    s = time.time()
    for t in threads:
        t.start()
    t.join()
    e = time.time()
    print "总耗时: %s" % (e - s)

cur.close()
conn.close()