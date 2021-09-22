"""
By now, you are familiar with the mechanism of inheritance.
Now it's time to go deeper and gain insight into multiple inheritance. Multiple inheritance is when a class has two or more parent classes.
We will see how it it implemented, what benefits it gives us, and what problems may arise.
"""
#TASK1
'''
Imagine that you need to create a program representing a class hierarchy.

This class hierarchy concerns different types of cars. You know that the class Vehicle is the base class. 
There are two classes, LandVehicle and WaterVehicle , that inherit from the class Vehicle.

As you can see, there are two additional classes, Car and Boat. 
Your task is to figure out where these classes fit into the hierarchy using the information about MRO and general logic and then program this hierarchy. 
You don't need to define any methods in the classes.
'''
#SOLUTION
class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class WaterVehicle(Vehicle):
    pass
class Boat(WaterVehicle):
    pass
class Car(LandVehicle):
    pass
class CarBoat(Car, Boat):
    pass

#TASK2
"""
Suppose we have the following class hierarchy:
"""
class Robot:
    def greet(self):
        print("I am a robot")


class Android(Robot):
    def greet(self):
        super().greet()
        print("I am an android")


class PersonalAssistant(Robot):
    def greet(self):
        super().greet()
        print("I am a personal assistant")


class AssistantAndroid(Android, PersonalAssistant):
    def greet(self):
        super().greet()
#SOLUTION (remember about class.__mro__)
# I am a robot
# I am a personal assistant
# I am an android