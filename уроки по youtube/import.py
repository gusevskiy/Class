from lesson3 import Player


Player.set_cls_field(10)
x = Player()
print(x.lvl)

Player.set_cls_field()
y = Player()
print(y.lvl)

y.lvl = 2.3