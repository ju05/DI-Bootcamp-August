#LOOPS: FOR LOOPS AND WHILE LOOPS

#FOR LOOP: WE HAVE A KNOWN STOP POINT
#SYNTAX
#for <variable> in <sequence/iterable>:
    #indented block of code that will happen in each iteration

#sequences that we can loop through it
#- strings
#- lists
#- tuples
#- sets
#- range

#Looping through a string (basic sequence)
for char in 'student':
    print(char)


#Looping through a list (structured sequence)

# fruits = ['apple', 'watermelon', 'banana']

# for each_fruit in fruits:
#     print(f'I love {each_fruit}')

print(list(range(11)))


student = 'Hermione'

numbers = []
for i in range(1, 21):
    numbers.append(i)

print(numbers)

for i in numbers:
    if numbers.index(i) % 2 == 0:
        print(i)

# print(numbers)


#WHILE LOOP: CONDITIONAL LOOP AND NOT KNOWN NUMBER OF ITERATIONS

i = 0
while i <= 10:
    print('hello')
    i += 1

# keep_asking = True option: use a "flag"
toppings_list = []

while True:
    topping = input('enter the topping you want on your pizza, or "q" to quit: ')
    if topping == 'q':
        break
        # keep_asking = False - if you use a flag
    toppings_list.append(topping)
    
print(toppings_list)
    
