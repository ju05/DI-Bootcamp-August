# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.
list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

list_1.extend(list_2)
print(list_1)

for i in list_2:
    list_1.append(i)
print(list_1)

list_3 = list_1 + list_2
print(list_3)


list_3 = [*list_1, *list_2]
print(list_3)

# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for i in range (1500, 2500):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

list = [x for x in range(1500, 2700) if x%5 == 0 and x%7 == 0]
print(list)

# Exercise 3: Check The Index
# Instructions
# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# print(names)
# name_asked = input("Pick your name:\t").capitalize()

# if name_asked in names:
#     index = names.index(name_asked)
#     print(f"{name_asked} is there on Index {index}")
# else:
#     print(f'{name_asked} is not in the list')


# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.

# numbers = []
# for i in range(3):
#     numbers.append(int(input('Give me a number')))
# print(f"The greatest number is:", max(numbers))


# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

import string
alpha = list(string.ascii_lowercase)
vowels = list("iouae")
for letter in alpha:
    if vowels.count(letter) > 0:
        print(letter + ": vowel")
    else:
        print(letter + ": consonant")

item = input("Enter an item: ")
print(f"{item} occurs at {alpha.index(item)}")

# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

# words = []
# words_string = input("Give me 7 words seperated by comma:\t")
# words = words_string.split(',')
# while len(words) != 7:
#     words_string = input("Give me 7 words seperated by comma:\t")
#     words = words_string.split(',')
# print(words)

# letter = input("Give me a single character:\t")
# for word in words:
#     # Check if the 'letter' is in the 'word'
#     if letter in word:
#         index = word.index(letter)
#         print(f"The first appearance of '{letter}' in '{word}' is at position {index+1}.")
#     else:
#         # If 'letter' doesn't exist in the 'word', print a friendly message
#         print(f"The letter '{letter}' does not exist in the word '{word}'.")

# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

# list_of_numbers = list(range(1, 1000001))

# print(min(list_of_numbers))
# print(max(list_of_numbers))
# print(sum(list_of_numbers))

# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# user_list = input("Enter numbers seperated by commas: ")
# user_list = user_list.split(",")
# user_tuple = tuple(user_list)
# print(user_list)
# print(user_tuple)

# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.

# import random

# games = 0
# wins = 0
# losses = 0

# input_number = 1

# while input_number > 0 or input_number < 11:

#     random_number = random.randint(0, 9)

#     input_number = int(input("Give me a random number between 0 and 9\nType in '10' if you want to quit:\t"))

#     if input_number == 10:
#         print("Goodbye")
#         break
#     else:
#         games += 1
#         if input_number == random_number:
#             print(f"Congratulations. You guessed right!\n The random number was also {random_number}")
#             wins += 1
#         else:
#             print(f"Sorry. You were wrong. The random number was {random_number} Try again?\n")
#             losses += 1

# print(f"You played {games} games and had {wins} wins and {losses} losses!")