import threading
import time

class Knight(threading.Thread):
    def __init__(self, name=str, power=int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        war_days = 0
        while enemy > 0:
            time.sleep(0.1)
            war_days += 1
            enemy -= self.power
            if enemy >= 0:
                print(f'{self.name} сражается {war_days} дней, осталось {enemy} воинов.')
        print(f"{self.name} одержал победу спустя {war_days} дней(дня)!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

print('Все битвы закончились!')