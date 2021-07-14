"""
Here are bright examples of class instances
"""
#TASK1
"""
Write the class Movie and define the class constructor with such parameters as the title, director, and the year of release.

In the corresponding variables defined below, create such objects as "Titanic" (James Cameron, 1997), "Star Wars" (George Lucas, 1977), and "Fight Club" (David Fincher, 1999).
"""
#SOLUTION
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

#Creating a couple of instances as an example
titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)

#TASK2
"""
Below is the class Dog with the __init__ method. Imagine, you have a dog named Pumpkin (with a capital P!). 
Create an instance of the class Dog representing Pumpkin. The name of the variable should be pumpkin_dog.
"""
#SOLUTION
class Dog:
    def __init__(self, name):
        self.name = name
pumpkin_dog = Dog('Pumpkin')

#TASK3
"""
John works at the university. He deals with the information about a lot of students and he decided to create a program that would help him with it.

He devised a system for creating an id for each student: first letter of the name, last name, and then the birth year. For example, the id for John Smith (b. 1989) would look like JSmith1989.

John needs help finishing the code for the id and then applying it to the students. Your task is to define an instance attribute student_id in the __init__ method, calculate it, create an object of the class Student with the parameters from the input, and print the value of the id. Do NOT print the value inside of the __init__ method!

The input format:

Student information: the first line has the name, the second line has the last name, and the third has the birth year.

The output format:

The student_id of the student.
"""
#SOLUTION

class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.student_id = self.name[0] + self.last_name + str(self.birth_year)

student = Student(input(), input(), int(input()))
print(student.student_id)

"""
This could be done another way also: by using decorator @property
"""
#EXAMPLE
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    @property
    def student_id(self):
        return self.name[0] + self.last_name + str(self.birth_year)


student = Student(input(), input(), int(input()))
print(student.student_id)

#TASK4
"""
A right triangle is a triangle in which one angle is a right angle (90-degree angle). The side opposite to the right angle is called a hypotenuse and the other two sides are called legs (or catheti).

Here's a class RightTriangle with the class constructor. The constructor is missing the area attribute. Calculate the area S according to this formula:

area = 0.5 * leg_1 * leg_2

Three numbers ( input_c, input_a, and input_b) have already been read from the input. They represent a triangle: the first number is the length of the supposed hypotenuse, the other two are the legs. If the triangle with these sides is right, create an instance of the class RightTriangle and print its area (with one decimal). If the triangle is not right, print "Not right".
"""

"""
We can reach it with many ways, the one which we haven't tried - decorator @staticmethod. Let's see how it works.
"""
#SOLUTION
class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

    @staticmethod
    def area(leg_1, leg_2):
        return 0.5 * leg_1 * leg_2

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
if input_a ** 2 + input_b ** 2 == input_c ** 2:
    print(RightTriangle.area(input_a, input_b))
else:
    print('Not right')