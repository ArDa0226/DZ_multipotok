# -*- coding: UTF-8 -*-

from threading import Thread
import time
def vivod_1():
    digits = range(11)
    for i in digits:
        print(i)
        time.sleep(1)

def vivod_2():
    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'j')
    for k in alpha:
        print(k)
        time.sleep(1)

thread_1 = Thread(target=vivod_1)
thread_2 = Thread(target=vivod_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()



