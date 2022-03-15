'''
1.Каждая ссылка объект.атрибут инициирует новый независимый поиск. Python
  выполняет независимый поиск в дереве классов для каждого выражения с извлечением атрибута.
  Сюда входят ссылки на экземпляры и классы, сделанные за
  пределами операторов class (например, X.атрибут), а также ссылки на атрибуты экземпляра
  аргумента self в функциях методов класса. Каждое выражение
  self.атрибут в методе вызывает новый поиск для атрибута в self и выше.


'''

class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


class ScondClass(FirstClass):
    ''' Класс SecondClass определяет метод display для вывода в другом формате.
    За счет определения атрибута с таким же именем, как у атрибута в FirstClass, класс
    SecondClass фактически замещает атрибут display в своем суперклассе. Перегрузка'''
    def display(self):
        print('Curent value = "%s"' % self.data)


class ThirdClass(ScondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other


if __name__ == "__main__":
    # x = FirstClass()
    # y = FirstClass()
    #
    # x.setdata('King Arthur')
    # y.setdata(3.14159)
    #
    # x.display()
    # y.display()
    #
    # x.data = 'New value'
    # x.display()
    #
    # z = ScondClass()
    # z.setdata(42)
    # z.display()

    a = ThirdClass('abc')
    a.display()
    print(a)

    b = a + "xyz"
    b.display()
    print(b)

    a.mul(3)
    print(a)