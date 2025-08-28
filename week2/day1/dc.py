class Farm:
    def __init__(self, name) -> object:
        self.name = name     
        self.animals = {}

    def add_animal(self, **new_animals):
        for animal, qua in new_animals.items():
            if animal in self.animals:
                self.animals[animal] += qua
                print(f'{qua} of {animal} was added')
            else:
                self.animals[animal] = qua
                print(f'{qua} {animal} was added')

macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5) 
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)

#using *args:

my_animals = ['sheep', 'cow', 'goat', 'chicken', 'hourses', 'dog']

macdonald.add_animal(sheep = 2, cow = 5, goat = 12) #using **kwargs
