# if __name__ == '__main__':
#    print("Main Method")

# MultiThreading: If multiple threads are trying to execute which thread is executed first
# we cannot expect, it is decided by Thread Scheduler

import threading
# task 1: returns the current thread
t = threading.current_thread()
print(t)  # <_MainThread(MainThread, started 3612)>

# task 2: returns the main thread object
t = threading.main_thread()
print(t)  # <_MainThread(MainThread, started 8064310336)>

if threading.current_thread() == threading.main_thread():

    print("Main Method")  # Main Method

else:
    print("Some Other Thread")