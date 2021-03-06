"""Страница 54 том 2 Марк Луцк"""
"""Страница 84 том 2 Марк Луцк"""

from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Создает и обрабатывает записи о людях
    """

    def __init__(self, name, job=None, pay=0):  # конструктор класса
        self.name = name  # Конструктор принимает три аргумента
        self.job = job  # Заполнить поля при создании
        self.pay = pay  # self. job=job мы сохраняем переданное значение
        # job в экземпляре для последующего применения.

    def lastName(self):
        return self.name.split()[
            -1]  # предпологвется что фамилия написана последней

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # просто для экономии печати
        # к 1 подставляется .10 #

    # def __repr__(self):  # добавленный метод
    #     return '[Person: %s, %s]' % (self.name, self.pay)
    #     # return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    """
    Настроенная версия Person со специальными требованиями
    """

    def __init__(self, name, pay):  # переопределить конструктор
        Person.__init__(self, name, 'mgr', pay)  # выполнять исходный с mgr #

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    # Manager: __init__  # возможно это в новой версии python ненужно
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    # print('__ALL three__')
    # for obj in (bob, sue, tom):
    #     obj.giveRaise(.10)
    #     print(obj)
    # print(len(dir(bob)))
