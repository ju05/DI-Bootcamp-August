# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# word = ''
user_str = (input("Enter a word with 10 characters:"))
asking = True
while asking: #while True    
    if len(user_str) == 10:
        word = user_str
        print(word[0])
        print(word[-1])
        asking = False
    elif len(user_str) < 10:    
        print('first if')
        user_str = (input("Not enough characters. Enter a word with 10 characters: "))
    elif len(user_str) > 10:
        print('elif')
        user_str = (input("Too long word. Enter a word with 10 characters: "))           

# Then, print the first and last characters of the given text.
# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:


import random
userinput_list = [user_str] # or [user_str]
random.shuffle(userinput_list)
shuffled_str = ''.join(userinput_list)
print('**', shuffled_str)

# # The user enters "Hello World"
# # Then, you have to construct the string character by character
# # H
# # He
# # Hel
# # ... etc
# # Hello World

output = ''
for letter in user_str:
    output += letter
    print(output)

# OTHER OPTION:
# for i in range(len(user_str)):
#     print(user_str[:i+1])

# user_list = []
# for i in range(len(user_str)):
#     user_list.append(user_str[:i+1])
# print(user_list)


# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod
# import random

# sent_user = (input("Enter a word with 10 characters:"))
# for i in range(1, len(sent_user)):
#     # print(pour_)
#     print(sent_user[:i + 1])
# # Bonus
sent_user_List = sent_user.split(",")
print(sent_user_List)
suff_list = [random.shuffle(sent_user_List)]
print(suff_list)
for caract in suff_list:
    suf_sent = "".join(suff_list)
print(suf_sent)