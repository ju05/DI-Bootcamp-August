# # # 🌟 Exercise 1 : Set
# # # Instructions
# # # Create a set called my_fav_numbers with all your favorites numbers.
# # # Add two new numbers to the set.
# # # Remove the last number.
# # # Create a set called friend_fav_numbers with your friend’s favorites numbers.
# # # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

# my_fav_numbers = {3,5,7,8,13,18,21,23,24}
# my_fav_numbers.add(33)
# my_fav_numbers.add(49)
# # sets are unordered, so we cant remove the last element without knowing its value
# my_fav_numbers.remove(24)
# print("my favorite numbers", my_fav_numbers)

# my_fav_numbers.update(my_fav_numbers)
# friend_fav_numbers ={7,26,2001,2005}
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print("our favorite numbers", our_fav_numbers)


# # # 🌟 Exercise 2: Tuple
# # # Instructions
# # # Given a tuple which value is integers, is it possible to add more integers to the tuple?
# # # my_tuple = 1,5,15,21,24
# # # my_tuple.add(11)
# # # answer: It`s not possible to add something to a tuple.`

# # # 🌟 Exercise 3: List
# # # Instructions
# # # Using this list 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # Remove “Banana” from the list.
# basket.remove("Banana")
# # Remove “Blueberries” from the list.
# basket.pop()
# # Add “Kiwi” to the end of the list.
# basket.append("Kiwi")
# # Add “Apples” to the beginning of the list.
# basket.insert(0,"Apples")
# # Count how many apples are in the basket.
# apples = basket.count("Apples")
# print(apples)
# # Empty the basket.
# # basket.clear()
# # Print(basket)
# print(basket)

# # # 🌟 Exercise 4: Floats
# # # Instructions
# # # Recap – What is a float? What is the difference between an integer and a float?
# # # integer is a whole number and float is a decimal number
# # # # Can you think of another way to generate a sequence of floats?
# # # # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# sequence = []
# for i in range (1,6):
#     decimal =  i + 0.5
#     sequence.append(i)
#     sequence.append(decimal)
# print(sequence[1:-1])
# print(type(sequence[0]))
# # #  OR ---------------------------------------------------------
# decimal_list = [i+0.5 for i in range(1,6)]
# decimals = []
# decimals.extend(range(1,6))
# decimals.extend(decimal_list)
# decimals.sort()
# print(decimals)



# # # # 🌟 Exercise 5: For Loop
# # # # Instructions
# # # # Use a for loop to print all numbers from 1 to 20, inclusive.
# # # # Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
# numbers = list(range(1,22))  # Adjusting the range to match index with value
# for each_num in numbers:
#     if numbers.index(each_num) % 2 == 0:
#         print(each_num)

# # # 🌟 Exercise 6 : While Loop
# # # Instructions
# # # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# while True:
#     user_name = input("Enter your name")
#     if user_name.lower() == "juliana":
#         

# # # 🌟 Exercise 7: Favorite Fruits
# # # Instructions
# # # Ask the user to input their favorite fruit(s) (one or several fruits).
# user_fruits = input("Enter your favorite fruits separated with a single space").split()
# # #---------OOOOR
# user_fruits.join(",")

# new_fruit = input("Enter any fruit")
# if new_fruit in user_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print(new_fruit)
#     print("You chose a new fruit. I hope you enjoy")

# # # # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# # # # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# # # # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # # # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # # # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# # # Exercise 8: Who Ordered A Pizza ?
# # # Instructions
# # # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# all_toppings = []
# while True:
#     topping = input("Enter a pizza topping: ")
#     print(f"{topping} was added to your pizza")
#     all_toppings.append(topping)
#     if topping == "quit":
#         all_toppings.pop()
#         print(all_toppings)
#         break
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# # Exercise 9: Cinemax
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# # Ask a family the age of each person who wants a ticket.
# # Store the total cost of all the family’s tickets and print it out.

# # A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# # Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# # At the end, print the final list.
# total_cost = 0
# while True:
#     age = input("Enter the age of the person or type 'done' to finish: ")
#     if age == 'done':
#         break
#     if age < 3:
#         ticket_cost = 0
#     elif age >= 3 and age <= 12:
#         ticket_cost = 10
#     else:
#         ticket_cost = 15
#         total_cost += ticket_cost
# print("Total cost of tickets: $", total_cost)

# teenagers = ['John', 'Jane', 'Mark', 'Mike', 'Kate']

# for teen in teenagers[:]:  # We use a slice to iterate so that we can modify the list in-place
#     age = int(input(f"How old is {teen}? "))
#     if age < 16 or age > 21:
#         # The expression 16 < age > 21 isn't what you might expect it to be.
#         # # In Python, chained comparisons like 16 < age <= 21 are a shorthand for 16 < age and age <= 21.
#         # # But if you try 16 < age > 21, it translates to 16 < age and age > 21, which is logically impossible because no number can be both greater than 16 and greater than 21 simultaneously.
#         teenagers.remove(teen)
#         print(f"{teen} is not allowed to watch the movie.")

# print(teenagers)

# teenagers = ['John', 'Jane', 'Mark', 'Mike', 'Kate']

# teenagers = [teenager for teenager in teenagers if not 16 <= int(input(f"Enter {teenager} age: ")) <= 21]

# print(teenagers)



# # # Exercise 10

# # # Using the list below :

# # The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
# # We need to prepare the orders of the clients:
# # Create an empty list called finished_sandwiches.
# # One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# # After all the sandwiches have been made, print a message listing each sandwich that was made, such as:


# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich",
#                    "Avocado sandwich", "Pastrami sandwich",
#                    "Egg sandwich", "Chicken sandwich",
#                    "Pastrami sandwich"]

# finished_sand = []
# while 'Pastrami sandwich' in sandwich_orders:
#     sandwich = sandwich_orders.remove('Pastrami sandwich')




