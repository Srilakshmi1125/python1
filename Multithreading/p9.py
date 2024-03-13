import threading


class MyThread(Thread):

    def run(self):
        for i in range(5):
        time.sleep(1)
        print(i, " Child Thread ")

t1=MyThread()
t1.start()
t1.join()
th=threading.current_thread.name()
print("Current Thread: ",th)

t2=MyThread()
t2.start()
t2.join()
th=threading.current_thread.name()
print("Current Thread: ",th)