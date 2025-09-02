#Decorators are python built-in functions that we "apply" to our functions within the class, i.e methods
from datetime import datetime as dt, date
import pygame
from faker import Faker

class Person:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name)
        self.last_name = self.format_name(last_name)
        self.birth_date = self.parse_birthdate(birth_date)
        self._email = None #protected attribute - the underscore here is a convension in python #this practice is called encapsulation
    
    @staticmethod  #a method that don't really needs the self
    def format_name(name):
        return name.title()
    
    @staticmethod
    def parse_birthdate(date_str):
        return dt.strptime(date_str, '%d-%m-%Y').date()
    
    @classmethod
    def from_age(cls, first_name, last_name, age:int):
        current_year = dt.today().year
        birth_year = current_year - age
        birth_date = f'1-01-{birth_year}'
        return cls(first_name, last_name, birth_date)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    @property
    def email(self):
        initial = self.first_name[0].lower()
        email = f'{initial}.{self.last_name.replace(" ", ".").lower()}@gmail.com'
        return email
    
    ######## DUNDER METHOD ######

    def __str__(self):
        return f'Hello this is {self.first_name} {self.last_name}'
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __eq__(self, other):
        return self.last_name == other.last_name
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __add__(self, other):
        return self.age + other.age
   

p1 = Person('jhon', 'snow da silva', '21-08-1990')
print(repr(p1))
print(p1.birth_date)
print(p1.first_name)
print(p1.birth_date)
print(p1.age)
print(p1.email)
# p1.email = 'the choosen'
# print(p1.email)

#how to use a class method when creating the object:
p2 = Person.from_age('aria', 'stark', 18)
p3 = Person.from_age('Sansa', 'stark', 21)

print(p2 + p3)

# print(p2.birth_date)
# print(p2.email)

#search for options of #@property
# setter (p1.email = 'the choosen' and the output will be 'the.choosen@gmail.com')
# getter help you to retrieve the value
# deleter del p1.email

#create a property method that generates an gmail with initial of the first name. a dot and last name complete
# print(p1.email)
# output: j.snow@gmail.com


#Modules - Faker
fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
birth_date = dt.strftime(fake.date_of_birth(), '%d-%m-%Y')
print(first_name)

p4 = Person(first_name, last_name, birth_date)
print(p4.age)
