"""
Generally speaking, an abstract class is a template that can be used to create other classes.
Once we have a template, we do not work with it directly, we create other objects based on this template and work with them instead.
Abstract classes operate in a similar manner.
Feature of abstract classes is that they have abstract methods.
Abstract methods are methods that generally do not have any implementation and they are declared with the @abstractmethod decorator.
"""

#TASK1
"""
Below you can see the abstract class EquilateralPolygon (it represents geometric shapes where all sides have the same length). 
Create a subclass Square. 
Do not forget to override the get_area method (it should return the area of the square).
"""
#SOLUTION
from abc import ABC, abstractmethod


class EquilateralPolygon(ABC):
    def __init__(self, side):
        self.side = side

    @abstractmethod
    def get_area(self):
        ...

class Square(EquilateralPolygon):
    def get_area(self):
        return self.side ** 2

#TASK2
"""
Create an abstract class Human, a template for all humans. 
It should have an abstract method say_hello (takes only self as a parameter). 
The method should not have any implementation.
"""
#SOLUTION
from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def say_hello(self):
        ...

#TASK3
"""
Coming back to our game example, add a Wizard class to the mix! 
You can come up with any spells and fighting methods for them, 
but you need to implement the class correctly.
"""
#SOLUTION
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...

    def sing_song(self):
        print("No songs for me!")

class Wizard(Player):
    def fight(self):
        print('I wanna to transform u into a frog!')
    def do_spell(self):
        print('I have nothing to say anymore!')

#TASK4
"""
Bank accounts can be of different types. 
We have created an abstract class Account that can serve as a template for other accounts. 
It has two methods, abstract method add_money and regular method add_interest.

Your task is to create subclasses SavingsAccount and Deposit:

SavingsAccount: we can add no less than $10 at a time. 
The interest rate is zero, so no percentage of the sum is paid back to the account.
Deposit: we can add no less than $50 at a time. 
Deposits have a fixed interest rate, so a percentage of the money is paid back to the account.
"""
#SOLUTION
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        ...

    def add_interest(self):
        ...


class SavingsAccount(Account):
    def add_money(self, amount):
        if amount >= 10:
            self.sum += amount
        else:
            print('Cannot add to SavingsAccount: amount too low.')


class Deposit(Account):
    def add_money(self, amount):
        if amount < 50:
            print('Cannot add to Deposit: amount too low.')
        else:
            self.sum += amount

    def add_interest(self):
        self.sum *= (self.interest + 1)