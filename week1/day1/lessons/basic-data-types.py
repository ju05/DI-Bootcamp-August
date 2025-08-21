#BASIC VALUE TYPES

#STRINGS
my_name = "Juliana"

#check the lenght
print(len('Juliana'))

#access chars by index (indexes start from 0)
print(my_name[4])

my_name = 'John snow'

#they are immutable 

# my_name[0] = 'G'

# #String functions/ String Methods

# print(my_name.lower())
# print(my_name.upper())
# print(my_name.capitalize())
# print(my_name.title())

# student = 'Harry Potter'
# student2 = student.replace('r', 'i')
# print(student2)

# price = '15$'

# clean_price = price.strip('$')
# print(clean_price)

#exercise in class
# description = "strings are..."
# print(description.upper())
# description = description.replace('are', 'is')
# print(description)
# print(description[:7])

# #Numbers
# #integers (int)
# age_int = 35
# age_int += 5
# print(age_int)
# print(7 + (-5))
# print(10 / 2)
# print(10 % 3)

# #floats
# print(3.5 + 3)
# division = 10 / 3
# print(round(division, 2))

# # Type Casting

# age = int(input('how old are you?'))

# print(type(age))

# print(age + 10)

# height = float(input('What is your height?'))

# print(type(height))

# age = str(age)
# print(type(age))


#Boleans (True and False)

print(5 > 7)
print('5' == 5)
print(-1 != 1)


#General Useful knowledge

#Adding types

my_string = 'Hello World '
python = 'Python is fun'
print(my_string * 5)

#special characters
print('Hello, aren\'t you having fun?\n' * 5)
print('Hello, aren\'t you having fun?\t' * 5)

#the f' string

user_name = input('What\'s your name?')
day_week = 'Wednesday'

print('Welcome, <user_name>!')
print('Welcome, ' + user_name + '!')
print(f'Welcome, {user_name}! Today is {day_week}')

# Create a variable called first_name and a variable called last_name, and then print your full name using those two variables

first_name = 'Hermione'
last_name = 'Granger'

print(f'Hello, my name is {first_name} {last_name}')
print(first_name, last_name)