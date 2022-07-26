from person import Person, Manager
import shelve
import glob


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)


db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()


if __name__ == '__main__':
    print(glob.glob('person*'))
    db = shelve.open('persondb')
    print(len(db))
    print(list(db.keys()))
    bob = db['Bob Smith']
    print(bob)
    print(bob.lastName())
    for key in db:
        print(key, '=>', db[key])
    print('sorted')
    for key in sorted(db):
        print(key, '=>', db[key])
