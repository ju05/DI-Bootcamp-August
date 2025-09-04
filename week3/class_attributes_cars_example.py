class Car:
    cars_created = 0
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.cars_created += 1



c = Car('Ford', 'F150')

print(c.make)
print(c.model)

mycar = Car('Toyota', 'Corolla')
print(Car.cars_created)
print(mycar.cars_created)


class NewCar:
    cars_created = {}
    def __init__(self, make, model):
        self.make = make
        self.model = model
        if make not in NewCar.cars_created:
            NewCar.cars_created[make] = {}
        if model not in NewCar.cars_created[make]:
            NewCar.cars_created[make][model] = 0
        NewCar.cars_created[make][model] += 1



c = NewCar('Ford', 'F150')

print(c.make)
print(c.model)

mycar = NewCar('Toyota', 'Camry')
print(NewCar.cars_created)
print(mycar.cars_created)

mynewcar = NewCar('Toyota', 'Camri')
print(NewCar.cars_created)
