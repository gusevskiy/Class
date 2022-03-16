class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name   # Конструктор принимает три аргумента
        self.job = job     # Заполнить поля при создании
        self.pay = pay      # self - новый объект экземпляра

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self): # добавленный метод
        return '[Person: %s, %s]' % (self.name, self.pay)
        #return f'[Person: {self.name}, {self.pay}]'


class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)




if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)
#Manager: __init__ # возможно это в новой версии python ненужно
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--ALL three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
