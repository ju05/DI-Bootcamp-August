# Exercise 1 : Hello World 4x
print('Hello world \n'*4)

# # Exercise 2 : Some Math
result = (99**3)*8
print(result)

print(99**3*8)

# # Exercise 3 : What Is The Output ?
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3) #error
print("Hello" == "hello") #False

# # Exercise 4 : Your Computer Brand
computer_brand = 'HP'
print(f'I have a {computer_brand} computer')

# Exercise 7 : Odd Or Even
user_number = int(input('give me a number'))
if (user_number % 2 == 0):
    print('odd')
else:
    print('even')


# #Exercise 8: Who Ordered A Pizza ?

toppings = []

while True:
    user_toppings = input('Enter a pizza topping or enter \'quit\': \n')
    if user_toppings != 'quit':
        toppings.append(user_toppings)
        print('We\'ll add that topping to your pizza \n')
    else:
        break

price = len(toppings) * 2.5 + 10
print('Your toppings are: \n') 

for topping in toppings:
    print(topping)

print(f'The total price of your pizza is {price}')


# # Exercise 9

total_price = 0
ages_of_person = input('Enter the age of each person separate with a single space \n').split(' ')

for age in ages_of_person:
    if 3 < int(age) < 12:
        total_price += 10
    elif int(age) > 12:
        total_price += 15

print(f'Total cost is {total_price}')

names = ['John', 'Bill', 'Lisa', 'Samanta']
permitted_names = names[:]
for name in names:
    age = int(input(f'Enter {name}\'s age: '))
    if 16 <= age <= 21:
        permitted_names.remove(name)

print(permitted_names)




