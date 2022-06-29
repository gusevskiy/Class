class Person:
    def __init__(self, name, job=None, pay=0):  # конструктор класса
        self.name = name   # Конструктор принимает три аргумента
        self.job = job     # Заполнить поля при создании
        self.pay = pay      # self. job=job мы сохраняем переданное значение
        # job в экземпляре для последующего применения.

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # просто для экономии печати
        # к 1 подставляется .10 #

    def __repr__(self):  # добавленный метод
        return '[Person: %s, %s]' % (self.name, self.pay)
        # return f'[Person: {self.name}, {self.pay}]'

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent+bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


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
    print('__ALL three__')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)