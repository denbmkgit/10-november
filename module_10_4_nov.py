import random
import threading
import time
from queue import Queue
from random import randint

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest




class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        to_wait = random.randint(3, 10)
        time.sleep(to_wait)

class Cafe:
    tables = []
    def __init__(self, queue, table):
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for i in range(1, 7):
                pass
                if self.tables[i].guest == None:
                    self.tables[i].guest = guest
                    print(f'{guest} сел(-а) за стол номер {tables[i]}')
                else:
                    break

    

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
print(len(guests), '- len guests')


print(tables[0])
tables[4].guest = guests_names[2]
print(tables[4].guest)

