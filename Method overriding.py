"""
One important concept of object-oriented programming is overriding.
Overriding is the ability of a class to change the implementation of the methods inherited from its ancestor classes.
"""

#TASK1
"""
Triangles are geometric figures with 3 sides and equilateral triangles are triangles in which all three sides are equal. 
Given a triangle, we can calculate its perimeter.

Below you can see classes Triangle and EquilateralTriangle. 
The class Triangle has a method __init__ with three parameters for three sides and a method get_perimeter that calculates the perimeter of the triangle.

The class EquilateralTriangle should have a method __init__() with 1 parameter since all its sides have equal length. This method is not yet finished.

Your task is to finish the __init__() method for the equilateral triangles in a way that allows us to use the get_perimeter method of the class Triangle without overriding it. Use the function super() for that!
"""
#SOLUTION
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

#TASK2
"""
In the template below you can see a hierarchy of robots. 
There are a base class Robot and a subclass ServiceRobot. 
Objects of the class Robot have two attributes: name and variety. 
Variety represents the function of the robot, for example, service or military. 
The get_info method returns information about a particular instance.

The ServiceRobot represents the "service" variety of robots. 
Objects of this class have only the name attribute.

Your task is to change the __init__ method of the class ServiceRobot so that get_info() returns the correct information for the objects of ServiceRobot. 
There are several ways to do it, but we ask you to use the super() function.
"""
#SOLUTION
class Robot:
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety
        print("Robot")

    def get_info(self):
        return "{} is a {} robot".format(self.name, self.variety)


class ServiceRobot(Robot):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 'service')

chappi = ServiceRobot("Chappi")
print(chappi.get_info())

#TASK3
"""
Below you can see a hierarchy of classes.
"""
class Instrument:
    def __init__(self, size):
        self.size = size

class Stringed(Instrument):
    def __init__(self, n_strings):
        self.n_strings = n_strings

class Violin(Stringed):
    def __init__(self, cost):
        super().__init__(4)
        # ???
        self.cost = cost

my_violin = Violin(680)
print("size:", my_violin.size,
      "\nstrings:", my_violin.n_strings,
      "\ncost:", my_violin.cost)
"""
Select what we should write instead of the question marks in the Violin's __init__ 
so that the output will be as follows:

size: 50 
strings: 4 
cost: 680
"""
#SOLUTION:
super(Stringed, self).__init__(50)

#TASK4
"""
Imagine you are creating a system that manages different social media accounts. 
You've written a base class Account with parameters media, username and n_followers.

Now you want to create a subclass for a specific social media, let's say, Instagram. 
In addition to the attributes that any Account object has, you want to specify an attribute n_following.

Create the class InstagramAccount and override the __init__() method. 
The method should take parameters username, n_followers and n_following. 
The objects of the class InstagramAccount should also have the attribute media with the value "Instagram".
"""
#SOLUTION
class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")

class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following):
        self.username = username
        self.n_followers = n_followers
        self.n_following = n_following
        super().__init__('Instagram', username, n_followers)

#TASK5
"""
Everybody knows that dolphins are mammals. 
Below is a class Mammal with 2 methods: __init__ and greet. 
__init__ defines the attribute bio_class with the value mammal, while greet prints out I am a mammal!.

Create a class Dolphin. It should be a child class of the class Mammal and have the same __init__. 
However, you need to override the greet method so that in addition to the I am a mammal! 
it prints I am a dolphin!. Use the super() function. 
You don't need to define any additional attributes in the class Dolphin.
"""
#SOLUTION

class Mammal:
    def __init__(self):
        self.bio_class = "mammal"

    def greet(self):
        print("I am a {}!".format(self.bio_class))

class Dolphin(Mammal):
    def greet(self):
        super().greet()
        print('I am a dolphin!')
