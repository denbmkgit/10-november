import threading
import time
lock = threading.Lock()
print(lock.locked())

counter = 0

def increment(name):
    global counter
    with lock:
        for i in range(100):
            counter += 1
            print(name, counter, lock.locked())


def dicrement(name):
    global counter
    with lock:
        for i in range(100):
            counter -= 1
            print(name, counter, lock.locked())



thread_1 = threading.Thread(target=increment, args=('thread_1',))
thread_2 = threading.Thread(target=dicrement, args=('thread_2',))
thread_3 = threading.Thread(target=increment, args=('thread_3',))
thread_4 = threading.Thread(target=dicrement, args=('thread_4',))

thread_1.start()
thread_3.start()
thread_2.start()
thread_4.start()