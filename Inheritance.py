"""
This topic relates to advanced OOP. So, feel confident to explore and refresh your knowledge!
"""
"""
Inheritance is a mechanism that allows classes to inherit methods or properties from other classes.
Or, in other words, inheritance is a mechanism of deriving new classes from existing ones.
"""
#TASK1
"""
You've created a base class Car and a subclass Tesla.
Create an instance of the class Tesla. 
You can create any instance, just name the variable tesla_car.
"""
#SOLUTION
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class Tesla(Car):
    pass

tesla_car = Tesla('musk', 'blue')

#TASK2
"""
Mysterious things have happened on the Hogwarts Express! 
Someone enchanted a food trolley and all the goodies got mixed up on the shelves. 
While the trolley witch is looking for the culprit, you will place Drinks, Pastry and Sweets on three respective shelves.
These base classes have various children: for example, PumpkinJuice inherits from Drinks. 
Write a function that finds a parent class for an unknown class (not an instance of a class) stored in the variable child and prints out the parent's name.
"""
#SOLUTION
def find_the_parent(child):
    dictionary = {'Drinks': Drinks, 'Pastry': Pastry, 'Sweets': Sweets}
    for cls in dictionary.values():
        if issubclass(child, cls):
            print(cls.__name__)
            return

#TASK3
"""
Below you can see a class Star. There are varieties of stars based on their luminosity, temperature and other parameters. 
One of the types of stars is a yellow dwarf, which is what our Sun is.
Create a child class for Star and call it YellowDwarf. 
You don't need to create any methods for the class or any objects of the class, just the class itself.
"""
class Star:
    def __init__(self, name, spectral_class):
        self.name = name
        self.spectral_class = spectral_class

class YellowDwarf(Star):
    pass