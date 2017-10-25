# encoding:utf-8
import threading, time

def loop():
    print("loop start run")
    time.sleep(5)
    print("loop exit")

t1 = threading.Thread(target=loop, name="LoopThread-1")
t2 = threading.Thread(target=loop, name="LoopThread-2")
t1.start()
t2.start()
time.sleep(3)
print("code id endx")


