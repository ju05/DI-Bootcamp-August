# TUPLES: Immutable and ordered

numbers = (10, 20, 30, 40, 50, 20)
number2 = tuple(numbers)
print(number2)

# numbers[1] = 200 #error because tuples are immutable
print(numbers[1])

#methods
print(numbers.count(20))
print(numbers.index(20))

#concatinate tuples 
fruits = ('apple', 'mango', 'kiwi', 'lime')
vegs = ('tomato', 'potato', 'lettuce')

fruits_vegs = fruits + vegs
print(fruits_vegs)


a,b,c,d,e,f = numbers
print(a)
print(b)
print(c)
print(d)

#SETS = unordered sequence not duplicated elements
my_set = {1,4,8,9}
my_set2 = set(my_set)

print(my_set, my_set2)

my_set.add(55)
print(my_set)

user_names = ['juli', 'john', 'juli', 'bob', 'mark', 'john']
set_user_name = set(user_names)
clean_user_name = list(set_user_name)
print(clean_user_name)

#set methods
names = {'Juliana', 'Israel', 'Dina'}
countries = {'USA', 'Brazil', 'Israel'}

print(names.intersection(countries))
print(names.difference(countries))
print(countries.difference(names))

#Create a set of your five favorite colors. Write code that:

# Adds a new color to the set (using add()).
# Finds the common elements between two sets (use a set of your friend's favorite colors)
# Removes all elements from the set of your favorite colors.
