# DATA STRUCTURES: LISTS, TUPLES, SETS AND DICTIONARIES

#HOW TO WORK WITH THEM ON FUNCTIONS

students = ['Harry', 'Hermione', 'Ron', 'Luna']

def welcome():
    for name in students:
        print(f'{name}, Welcome to Hogwarts!')

welcome()

def get_house():
    for i, name in enumerate(students):
        students[i] = f'{name} - Griffyndor'

    if name == 'Luna':
        students[i] = f'{name} - Ravenclaw'

get_house()
print(students)
# students[0] = f'{students[0]} - Griffyndor'

#FUNCTIONS AND DICTIONARIES




countries_capitals = {
        "USA": "Washington, D.C.",
        "UK": "London",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Naboo": "Theed"
}

def country_info(country_name:str)->str:
        '''return the capital of a given country based on the dict countries_capitals'''
        if country_name in countries_capitals.keys():
            return countries_capitals[country_name]

print(country_info("Germany"))