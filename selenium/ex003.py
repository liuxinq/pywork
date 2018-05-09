# coding: UTF-8

from selenium import webdriver
import time

browser = webdriver.Firefox()

url= 'http://www.baidu.com'

#通过get方法获取当前URL打印
print "now access %s" %(url)
browser.get(url)
time.sleep(2)

print "浏览器最大化"
browser.maximize_window()  #将浏览器最大化显示
time.sleep(2)

browser.find_element_by_id("kw").send_keys(u"酷狗")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()