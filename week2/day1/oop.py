#OOP: OBJECT ORIENTED PROGRAMING

#Class = a blueprint of the object, where we will define what are the properties and behaviors of the object

#syntax

class Dog:
    
    #the constructor function
    def __init__(self, breed:str, nickname:str, color:str, age:int = None, is_trained = False):
        self.breed = breed
        self.nickname = nickname
        self.color = color
        self.age = age
        self.is_trained = is_trained
        if age == None:
            self.dogs_years_age = None
        else:
            self.dogs_years_age = age * 7

    #########  Methods = the behavior of the object #######
    def bark(self):
        print(f'{self.nickname} is barking')

    def sit(self):
        if self.is_trained:
            print(f'{self.nickname} is sitting')
        else:
            print(f'{self.nickname} is not trained')
    
    def rename(self, new_name):
        self.nickname = new_name
        return self



#creating an object from the class Dog:
dog1 = Dog('chowchow', 'lion', 'orange', 5)
dog2 = Dog('collie', 'laddy', 'bege and white', 15, True)

#creating a specific attribute to a specific dog (object)
dog2.is_service_dog = True

print(dog1.color) #dot notation to access the attributes of the object

print(dog1.__dict__)
print(dog2.__dict__)

# self is the internal dictionary that has the properties from the class
# {breed: -----, nickname: -------, color: -------}

#exercise1
#create a new attribute to the Dog class called "is_trained" the value is a boolean and the default is False
#then run the code again. What happens with the objects that were created before this new attribute was added?


#########  Methods = the behavior of the object #######
dog3 = Dog('labrador', 'Rex', 'gold', 7, True)

dog3.bark() #calling the method on the object (more common)
Dog.bark(dog3)#calling the method on the class and pass the object as argument

dog3.sit()
dog1.sit()

dog3.rename('Bob')
print(dog3.nickname)

#exercise2
#create a method to rename(new_name) the dog. Use the attributes to do so.

my_dogs = [dog1, dog2, dog3]

for dog in my_dogs:
    print(dog.nickname)

# everything in python is a class and the class 'type' is the metaclass of all in python
print(type(dog3))
print(type(15))
print(type(str))
print(type(bool))
print(type(type))