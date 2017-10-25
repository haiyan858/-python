# #_*_ coding: utf-8 _*_
# test_threading2.py

import threading,time

def loop():
	print("loop function start run")
	time.sleep(5)
	print("loop function exit")

t = threading.Thread(target=loop,name="LoopThread_test")
t.setDaemon(True)
t.start()
print("code is end")
