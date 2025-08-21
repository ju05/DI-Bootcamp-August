#LIST: A MUTABLE SEQUENCE OF ELEMENTS

my_list = ['Harry', 'Ron', 'Hermione', 'Luna']
my_list2 = list('Harry')

# print(my_list)
# print(my_list2)

#index: an index is a position number on the sequence and it starts from 0
# print(my_list[2])
# print(my_list[1:4]) #slicing

#mutable
my_list[2] = 'Draco'
# print(my_list)

# print(len(my_list))

#list methods
fruits = ['apple', 'mango', 'kiwi', 'lime']
fruits.append('banana') #adds an element to the last index of the list
# print(fruits)

fruits.insert(1, 'watermelon')
# print(fruits)

fruits.remove('mango')#removes one element at time and just the first occurance
# print(fruits)

fruits.pop() #default: deletes the last position
print(fruits)

fruits.pop(2)  #argument: the index to delete
print(fruits)

# method to check after the class
# copy()
# extend()
# clear()
# sort()
# sorted()


