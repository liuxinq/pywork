#coding *.* coding: utf-8 *.*

import MySQLdb
import threading
import time

def read(io):
    list = [0]
    while True:
        conn = MySQLdb.connect(user="dbuser", passwd="a", host="192.168.100.106", port=3307, db="db03", charset = "utf8")
        # cursorclass 使输出变为字典形式
        cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        sql = "select * from t_%s" % io
        print sql
        cur.execute(sql)
        info = cur.fetchone()
        if info not in list:
            print info
            list.append(info)
            list.pop(0)
        cur.close()
        conn.commit()
        time.sleep(2)

threads = []
for i in range(1,3):
    t = threading.Thread(target=read, args=(i,))
    threads.append(t)

if __name__ == "__main__":
    s = time.time()
    for t in threads:
        t.start()
    t.join()
    e = time.time()
    print "总耗时: %s" % (e - s)