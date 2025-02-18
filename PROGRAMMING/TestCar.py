#TestCar.py
from car import Car
car1 = Car('chelly', 'corvette', 2021, 'blue')
car2 =Car('Ford', 'Mustang', 2022, 'read')
print('\t', car1.make, '\n')
print('\t', car1.model, '\n')
print('\t', car1.year, '\n')
print('\t', car1.color, '\n')

car1.drive()
car1.stop()
car2 =Car('Ford', 'Mustang', 2022, 'read')
print('\t', car2.make, '\n')
print('\t', car2.model, '\n')
print('\t', car2.year, '\n')
print('\t', car2.color, '\n')

car2.drive()
car2.stop()