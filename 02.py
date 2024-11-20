import  threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay


    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1



    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')

thread_1 = MyThread('thread_1', 5, 1)
thread_2 = MyThread('thread_2', 3, 0.5)

thread_1.start()
thread_2.start()