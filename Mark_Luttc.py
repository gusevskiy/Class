'''
1.Каждая ссылка объект.атрибут инициирует новый независимый поиск. Python
  выполняет независимый поиск в дереве классов для каждого выражения с извлечением атрибута.
  Сюда входят ссылки на экземпляры и классы, сделанные за
  пределами операторов class (например, X.атрибут), а также ссылки на атрибуты экземпляра
  аргумента self в функциях методов класса. Каждое выражение
  self.атрибут в методе вызывает новый поиск для атрибута в self и выше.


'''
#######################################################################################
class FirstClass:
    '''класс с двуми методами'''
    '''принимает значения'''
    def setdata(self, value):
        self.data = value

    '''выводит значения'''
    def display(self):
        print(self.data)


class ScondClass(FirstClass):
    ''' Класс SecondClass определяет метод display для вывода в другом формате.
    За счет определения атрибута с таким же именем, как у атрибута в FirstClass, класс
    SecondClass фактически замещает атрибут display в своем суперклассе. Перегрузка'''
    def display(self):
        print('Curent value = "%s"' % self.data)


class ThirdClass(ScondClass):
    def __init__(self, value): # вызывается для ThirdClass(value)
        self.data = value

    def __add__(self, other): # вызывается для self + other
        return ThirdClass(self.data + other)

    def __str__(self): # вызывается для print(self), str()
        return '[ThirdClass: %s]' % self.data

    def mul(self, other): # изменение на месте
        self.data *= other
#########################################################################################

class rec: pass #обьект пустого пространства имен

rec.name = 'Bob'
rec.age = 40
#####################################################

def uppername(obj):
    '''возвращает обьект в верхнем регистре'''
    return obj.name.upper()




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
###############################
    # a = ThirdClass('abc')
    # a.display()
    # print(a)
    #
    # b = a + "xyz"
    # b.display()
    # print(b)
    #
    # a.mul(3)
    # print(a)
###############################
    #print(rec.name)
    x = rec()
    y = rec()
    print('1 - ', x.name, y.name)
    x.name = 'Sue'
    print('2 - ', x.name, y.name, rec.name)
    print('3 - ', list(rec.__dict__.keys())) #список внутренних имен класса
    print('4 - ', list(name for name in rec.__dict__ if not name.startswith('__')))
    print('5 - ', list(x.__dict__.keys()))
    print('6 - ', list(y.__dict__.keys()))
    print('7 - ', x.name, x.__dict__['name'])
    #print(x.__dict__['age']) # вызовет ошибку Индексирование словаря не производит поиск в иерархии наследования
    print('8 - ', x.__class__) # связь экземпляра с классом
    print('9 - ', rec.__bases__)
    print('10 - ', uppername(x))
    rec.method = uppername
    print('11 - ', x.method(), y.method())
    print('12 - ', rec.method(x))
