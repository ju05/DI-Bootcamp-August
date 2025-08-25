#FUNCTIONS: REUSABLE PIECE OF CODE 

#SYNTAX

# def <name>():
#   indented block of code
#   returned value

# def say_hello():
#     print('Hello, I am a function output')

# say_hello() #calling the function

#passing information to the function: argument
def say_hello(language):
    if language == 'PT':
        print('Oi, eu sou uma funcao')

    elif language == 'HE':
        print('שלום אני פונקציה')
    
    else:
        print('Hello, I am a function')

# say_hello('HE')

# doc strings: documentation for the functions

def say_hello(language:str):
    '''prints a greeting depending on the language argument'''
    if language == 'PT':
        print('Oi, eu sou uma funcao')

    elif language == 'HE':
        print('שלום אני פונקציה')
    
    else:
        print('Hello, I am a function')

# say_hello('HE')


# multiple arguments and default values
# def say_hello_adv(language:str = 'EN', name:str = 'John Doe'):
#     '''prints a greeting depending on the language argument'''
#     if language == 'PT':
#         print(f'Oi {name}, eu sou uma funcao')

#     elif language == 'HE':
#         print(f'שלום {name} אני פונקציה')

#     elif language == 'EN':
#         print(f'Hello {name}, I am a function')
    
#     else:
#         print(f'The language {language} is not supported')

# say_hello_adv()

#positional arguments
def say_hello_adv(language:str = 'EN', name:str = 'John Doe'):
    '''prints a greeting depending on the language argument'''
    if language == 'PT':
        print(f'Oi {name}, eu sou uma funcao')

    elif language == 'HE':
        print(f'שלום {name} אני פונקציה')

    elif language == 'EN':
        print(f'Hello {name}, I am a function')
    
    else:
        print(f'The language {language} is not supported')

#positional arguments: we pass only the value
say_hello_adv('Sarah', 'PT')

#keyword arguments: we explicitly define to which argument the value is related
say_hello_adv(name = 'Sarah', language = 'PT')

#mixing positional and keyword argument: we can mix but every positional arguments need to come first
say_hello_adv('PT', name = 'Sarah')

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

def country_info(country:str = 'Naboo') -> tuple:
    '''prints the capital and the population of a country '''
    if country == 'Russia':
        capital = 'Moscow'
        population = 14380000

    elif country == 'Brazil':
        capital = 'Brasilia'
        population = 30080000
    
    elif country == 'Naboo':
        capital = 'Theed'
        population = 15080000
    
    else:
        print('this country is not supported')
        capital = 'unkown'
        population = 'unkown'
    
    return capital, population


print(country_info('Brazil'))

br_capital, br_population = country_info('Blabla')
print(br_capital)
print(br_population)

#return keyword: it return a value from the function

#scope 
# local scope: inside (indented after the function def) the function 
# we can NOT access a local variable on the global scope
# we only can access the variable on the local scope of a function if we use the "return" keyword

#global scope: not in the scope of a function (it is in the "main" file)
# we can access without modifying
# we can NOT modify it if we dont use the "global" keyword

bar_mitza = 13

def current_age():
    # age = 13
    # if age == bar_mitza:
    #     print('Mazal Tov!')

    global bar_mitza
    bar_mitza += 1

current_age()
print(bar_mitza)
