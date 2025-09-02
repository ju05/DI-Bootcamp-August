import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#PYTHON I/O

#OLD SCHOOL SYNTAX

# try:
#     f = open('secrets.txt')
#     secret_data = f.read()
#     print(secret_data)
# except:
#     raise ValueError
# finally:
#     f.close()

#MODERN WAY 

# with open(f'{dir_path}\secrets.txt','a', encoding = 'utf-8') as f:
#     f.write('\nBla bla')
#     print('content sucessfully added')
   
#exercise - frist 3 bullets

#Read the file line by line
# with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:

#     for line in f:
#         print(f.readline())
#     print('end of document')

# with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:
#     # print(f.readline(4))
#     print(f.readlines()[4])

# # Read only the 5 first characters of the file
# with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:
#     print(f.readline(5))

# #readline() - singular = return one single line as a string. You can pass an argument - a number for slicing the string
# #readlines() - plural = retunr a list where each element is a line of the document. You can pass an argument - a number for slicing the list


# # Read all the file and return it as a list of strings. Then split each word into letters

# with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:
#     txt_content = f.readlines()
#     final_list = []
#     for line in txt_content:
#         final_list.append(list(line))

#     #list comprehension
#     final_list = [list(line) for line in txt_content]

#     print(final_list)

# #Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

# with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:
#     txt_content = f.readlines()

#     cleaned_list = [line.strip() for line in txt_content]

#     darth = cleaned_list.count('Darth')
#     luke = cleaned_list.count('Luke')
#     lea = cleaned_list.count('Lea')
#     print('darth:', darth, 'luke:', luke, 'lea:', lea)

# #Append your first name at the end of the file

# with open(f'{dir_path}\star_wars.txt','a', encoding = 'utf-8') as f:
#     f.write('\nJuliana')


with open(f'{dir_path}\star_wars.txt','r', encoding = 'utf-8') as f:
    txt_content = f.readlines()

    skywalker = []
    for name in txt_content:
        if name.strip() == 'Luke':
            skywalker.append(f'{name.strip()} Skywalker\n')
        else:
            skywalker.append(name)

with open(f'{dir_path}\star_wars.txt','w', encoding = 'utf-8') as f:
    f.seek(0) #ensures the cursor is in the beginning of the file
    f.writelines(skywalker) 

    print('it was added')


