import collections
import dataclasses


# 1
class Laptop:
    def __init__(self):
        Battery_full = Battery('Battery level is full')
        self.Battery = [Battery_full.level]


class Battery:
    def __init__(self, level):
        self.level = level


notebook = Laptop()
print(notebook.Battery)


# 2
class Guitar:
    def __init__(self,name,String_type):
        self.name = name
        self.String_type = String_type

    def new_guitar(self):
        return(f'this is {self.name} guitar with {self.String_type} string')
    
class GuitarInput:
    def __init__(self,name, String_Type):
        self.name = name
        self.String_Type = String_Type
        self.guitar = Guitar(name,String_Type)
    def show_info(self):
        return self.guitar.new_guitar()


String1 = GuitarInput('Jordan','Metal')
print('\n', String1.show_info())


# 3
class Calc:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def summ(self):
        return self.n1 + self.n2 + self.n3


summer = Calc(1, 2, 3)
print('\n', 'summ of 3 numbers is:', summer.summ())


# 4
class Pasta:
    def __init__(self, ingridients):
        self.ingridients = ingridients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls('bacon', 'parmesan', 'eggs')


past1 = Pasta(['eggs', 'forcemeat'])
print('\n', past1.ingridients)
past2 = Pasta.carbonara()
print(past2.ingridients)


# 5
class Concert:
    def __setattr__(self, key, value):
        if key == "visitors_count" and value > Concert.max_visitors_num:
            Concert.visitors_count = Concert.max_visitors_num
            print('\n', f'Max visitors count is {Concert.visitors_count}')


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6
@dataclasses.dataclass
class AdressBookDataClass:
    key: int
    name: str
    phone_number: str
    adress: str
    email: str
    birthday: str
    age: int


databook1 = AdressBookDataClass(1, 'Stewie', '123416111', 'Baker Street',
                                'StewieBaker@python.com', '21/01/2022', 0)
print('\n', databook1)

# 7
AdressBookDataClass1 = collections.namedtuple('AdressBookDataClass1', ['key', 'name', 'phone_number',
                                                                       'adress', 'email', 'birthday', 'age'])
databook2 = AdressBookDataClass1(2, 'Robert', '0987654321', 'Downing Street',
                                 'RobertDownie@assembler.org', '22/02/2023', -1)
print('\n', databook2)


# 8
class AdressBook:
    def __init__(self, key, name, phone_number, adress, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.adress = adress
        self.email = email
        self.birthday = birthday
        self.age = age

    def str(self):
        print('\n', f'Persons key: {self.key}, name:{self.name}, number:{self.phone_number}, '
                    f'adress: {self.adress},mail:{self.email},birthday:{self.birthday},age:{self.age}')


Some_person = AdressBook(3, 'Person', '985816211', 'personal street', 'someperson@email.git', '01/01/2122', -100)
Some_person.str()


# 9
class Person:
    name = 'John'
    age = 36
    country = 'USA'


someone = Person
print(someone.name, ' ', someone.age, ' ', someone.country)
someone.age = 22
print(someone.name, ' ', someone.age, ' ', someone.country)


# 10
@dataclasses.dataclass
class Student:
    id: int
    name: str


SomeStud = Student(777, 'Frank')
SomeStud.email = 'Studlife@stud.com'
print('\n', SomeStud, SomeStud.email)
