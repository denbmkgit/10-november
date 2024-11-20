import  threading
import time

time_start = time.time()

def func1():
    for i in range(10):
        time.sleep(0.5)
        print(i, threading.current_thread())

def func2(x):
    for i in range(10):
        time.sleep(1)
        print(i, threading.current_thread())


thread = threading.Thread(target=func2, args=(1, ), daemon=True)
thread.start()
# thread.join()
print(thread.is_alive())
func1()

time_finish = time.time()
print()
# print(time_start)
# print(time_finish)
print(time_finish - time_start)
print(threading.enumerate())
print(threading.current_thread())