import queue
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
        q = queue.Queue()
        # print(guests)
        for t in range(len(tables)):
            # print(self.tables[t])
            for guest in guests:
                # print(guests)
                # print(guest)
                for g in range(len(guest)):
                    # print(type(guest), len(guest), 'G and GUESTS')#, guest[0], guest[1], guest[2], guest[3], guest[4], )
                    # guest.remove(guest[0])
                    # print(guest)

                    if self.tables[t].guest == None:
                        self.tables[t].guest = guest[g]
                        # print(self.tables[t].guest!= None)
                        print(f'{guest[g]} сел(-а) за стол номер {t+1}')
                        guest[g] = threading.Thread()
                        print(guest[g].is_alive())
                        guest[g].start()
                        print(guest[g].is_alive())
                        guest.remove(guest[0])
                        # print(self.tables[t].guest == None)



        for guest_to_queue in guest:
            # print(guest_gdut)
            q.put(guest_to_queue)
            print(f'{guest_to_queue} в очереди')
                    # elif self.tables[t].guest != None:
                    #     print(guest[g], g)
                    #     q.put(guest[g])
        #     items = list(q.queue)
        # print(items, 'it is items')
                    #
                    #
                    #
                    # elif self.tables[t].guest != None:
                    #     print(guest[g], g)
                    #               # q.put(guest[g])
        # time.sleep(11)
        # print(self.tables[t].guest == None)
        # print(self.tables[t].guest)


    def discuss_guests(self):
        pass


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]


caf = Cafe(Queue, tables)

caf.guest_arrival(guests_names)

# print(tables[0])
# tables[4].guest = guests_names[2]
# print(tables[4].guest)
