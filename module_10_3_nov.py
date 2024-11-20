import threading
import time
from random import randint



class Bank:
    def __init__(self, balance=0, lock=bool):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            random_sum = randint(50, 500)
            self.balance += random_sum
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

                print(f'Пополнение: {random_sum}. Баланс {self.balance}')
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_sum = randint(50, 500)
            print(f'Запрос на {random_sum}')
            if self.balance >= random_sum:
                # self.lock.release()
                self.balance -= random_sum
                print(f'Снятие: {random_sum}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))


th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')
