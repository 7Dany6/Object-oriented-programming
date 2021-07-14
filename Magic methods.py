"""
There are different ways to enrich the functionality of your classes in Python. One of them is creating custom methods which you've already learned about.
Another way, the one that we'll cover in this topic, is using "magic" methods.
What is more, believe it or not but I'm sure you've encountered them previously. Don't believe?
Dive into magic methods of object-oriented programming in Python right now!
"""
"""
So far we've been calling __init__ the constructor of the class, but in reality, it is its initializer. 
New objects of the class are in fact created by the __new__ method that in its turn calls the __init__ method.
"""
#TASK1
"""
Anne is writing a program that deals with the books in a bookstore. She created a class Book and defined all the necessary attributes: author, title, price, and book_id.
She would like to print out information about books in a concise and uniform way, but she doesn't know how to do that.
Help Anne by defining the right method so that she can easily print out information about her books in the following format: {title} by {author}. ${price}. [{book_id}].
For instance, if we have Book("George Orwell", "1984", 13.59, 1956789), the method should return 1984 by George Orwell. $13.59. [1956789].
"""
#SOLUTION:
class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id
    def __str__(self):
        return f'{self.title} by {self.author}. ${self.price}. [{self.book_id}]'
"""
Solution implies two options: magic method __str__ would suit as well
"""
#TASK2
"""
You want your program to work in a way that at any given time there can be no more than 10 puppies.
Define __new__ method so that this restriction is placed on the class.
"""
#SOLUTION
