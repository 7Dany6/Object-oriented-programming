"""
Here are bright examples of class instances
"""

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



titanic = Movie("Titanic", "James Cameron", 1997)
star_wars = Movie("Star Wars", "George Lucas", 1977)
fight_club = Movie("Fight Club", "David Fincher", 1999)

"""

"""