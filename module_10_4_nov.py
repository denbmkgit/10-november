import random
import threading
import time
from queue import Queue
from random import randint
from typing import Iterable
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

    def __init__(self, queue=Queue, tables=Iterable):
        self.queue = queue
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            print(guests)
            print(guest)
            for g in guest:
                print(g, guest, 'G and GUESTS')
                
                for i in range(1, 5):

                    if self.tables[i].guest == None:
                        self.tables[i].guest = g
                        print(f'{g} сел(-а) за стол номер {i}')


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

caf = Cafe(Queue, tables)

caf.guest_arrival(guests_names)


print(tables[0])
tables[4].guest = guests_names[2]
print(tables[4].guest)

