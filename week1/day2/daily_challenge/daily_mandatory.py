# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.


number = int(input("Enter a number"))
lenght = int(input("Enter a lenght"))
multiples = []
for i in range(1,lenght):
    mult_num = (i * number)
    multiples.append(mult_num)
print(multiples)

# OPTION2:
# number = int(input("Write the number: "))
# lenght = int(input("Write the lenght: "))
# list1 = []
# for i in range(lenght):
#     list1.append(number+i*number)
# print(list1)

#OPTION3:


# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
user_str = "ppoeemm"

new_str = user_str[0]
for char in user_str:
    if char not in new_str:
        new_str = new_str + char
print(new_str)


user_string = input("Enter a string: ")
final_string = ""
for i in range(len(user_string)):
    if i == 0 or user_string[i] != user_string[i - 1]:
        final_string += user_string[i]
print(final_string)
