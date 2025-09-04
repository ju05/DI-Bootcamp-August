# # Exercise 1 : 
# # Convert the two following lists, into dictionaries.
# # Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionary = dict(zip(keys, values))
print(dictionary)


# # # #  Exercise 2 : 
# # # # A movie theater charges different ticket prices depending on a person’s age.
# # # # if a person is under the age of 3, the ticket is free.
# # # # if they are between 3 and 12, the ticket is $10.
# # # # if they are over the age of 12, the ticket is $15.
# # # # Given the following object:
# # How much does each family member have to pay ?

# # # BEFORE BONUS
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = 0
for name, age in family.items():
   
    if age > 3 and age <= 12:
        price = 10
    elif age > 12:
         price = 15
    else:
        price = 0
    print(f"{name} should pay {price} $")
    total += price

print(f"total price is {total} $")

# # BONUS: Ask the user to input the names and ages instead of using the provided family variable 
family2 = {}
while True:
    f_member = input("Enter name and age csv (for exit - quit):").split(',')
    print(f_member)

    if "quit" in f_member:
        break
    else:
        family2[f_member[0]] = int(f_member[1])

print(family2)

price = 0
list_prices = []
for age in family2.values():
    if  3<= age <= 12:
        price += 10
        list_prices.append(10)
    elif age > 12 :
        price += 15
        list_prices.append(15)
print(f'The costs will be {list_prices}, total will be {price}')
print(price)



# #   Exercise 3: Zara
brand = {'name': 'Zara', 
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'], 
        'international_competitors': ['Gap', 'H&M', 'Benetton'], 
        'number_stores': 7000, 
        'major_color':{ 
                    'France': 'blue', 
                    'Spain': 'red', 
                    'US': 'pink green'}
}
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
brand.update({'number_stores': 2})
print('step3', brand)
# # 4. Print a sentence that explains who Zaras clients are.

types_of_clothes = brand['type_of_clothes']
phrase = "rich people buying "
for type in types_of_clothes:
    phrase += type + "," 
OPTION2:
print(f'zara clients are mostly {" ".join(magasin["type of clothes"][:-1])}')
print('step4', f'The clients of Zara are {phrase}')
brand.update({'country_creation': 'Spain'})
print('step 5', brand)
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
for key in brand.keys():
    if key == 'international_competitors':
        brand['international_competitors'].append('Desigual')

print('step6', brand)
# # # 7. Delete the information about the date of creation.
brand.pop('creation_date')
print('step7', brand)
# # # 8. Print the last international competitor.
print('setp8', brand['international_competitors'][-1])
# # # 9. Print the major clothes colors in the US.
print('step9', brand['major_color']['US'])
# # # 10. Print the amount of key value pairs (ie. length of the dictionary).
print('step10', len(brand))
# # # 11. Print the keys of the dictionary.
print('step 11', brand.keys())
# # # 12. Create another dictionary called more_on_zara with the following details:
more_zara = {'creation_date': 1975,
            'number_stores': 10000
}
# # # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_zara)
print('step13', brand)
# # # 14. Print the value of the key number_stores. What just happened ?
print('step14', brand['number_stores'])
# #The number 2 was updated to 10000

# # # Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
indexes = [i for i in range(len(users))]

# for i in range(len(users)):
#     indexes.append(i)

disney_users_A = dict(zip(users, indexes))
disney_users_B = dict(zip(indexes, users))
disney_users_C = dict(zip(sorted(users),indexes))


print(disney_users_A)
print(disney_users_B)
print(disney_users_C)

names_a = []
indexes_a = []
for index, name in enumerate(users):
    if 'i' in name:
        indexes_a.append(index)
        names_a.append(name)
        ziping = zip(names_a, indexes_a)
        result_a = dict(ziping)
print('step4a', result_a)

names_b = []
indexes_b = []
for index, name in enumerate(users):
    name = name.lower()
    if name[0] in ('m', 'p'):
        indexes_b.append(index)
        names_b.append(name)
        ziping = zip(names_b, indexes_b)
        result_b = dict(ziping)
print('step4b', result_b)    

# # Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# # Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# # Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# # Only recreate the 1st result for:
# # The characters, which names contain the letter “i”.
# # The characters, which names start with the letter “m” or “p”.
