import threading
import time
class thread1(threading.Thread):# step-1:create run mtd
    def run(self):
        for i in range(10):
            print('thread1:'+str(i))
            time.sleep(5)
class thread2(threading.Thread):
    # step-1:create run mtd
    def run(self):
        for i in range(10):
            print('thread2:'+str(i))
            time.sleep(2)
t1=thread1()
t1.start()
t2=thread2()
t2.start()