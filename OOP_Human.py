import random

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'Я - {}, сытость - {}, у меня еды - {}, денег на счету - {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            cprint('{} поел, еды осталось {}'.format(self.name, self.food), color='green')
            self.fullness += 10
            self.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='green')
        self.money += 50
        self.fullness -= 10

    def shopping(self):
        if 50 <= self.money:
            cprint('{} сходил в магазин'.format(self.name), color='cyan')
            self.money -= 50
            self.food += 50
        else:
            cprint('{} недостаточно средств'.format(self.name), color='red')

    def play_DOTA(self):
        cprint('{} играл в доту весь день'.format(self.name), color='magenta')
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()


igor = Man(name='Игорь')
for day in range(1, 366):
    print('===================== день {} ========================'.format(day))
    igor.act()
    print(igor)
