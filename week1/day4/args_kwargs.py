#*args = arguments (simple sequence structure like a list/set/tuple)
#**kwargs = key word arguments (dictionary)

students = ['Harry', 'Ron', 'Hermione']

def welcome(*args):
    if args:
        for arg in args:
            print(f'{arg}, welcome to Hogwarts')

welcome('Harry', 'Ron', 'Hermione')

def format_info(**kwargs):
    if kwargs:
        print(kwargs)
    if kwargs['parseltongue']:
        print(f'{kwargs["name"]} can talk to snakes')


format_info(name = 'Harry', email = 'harry@hogwarts.com', age = 14, parseltongue = True)


welcome(*students) #if you want to pass a sequence on a function that acepts "args" you can unpack it using "*"