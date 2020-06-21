from Array import Array

class Movie():
    def __init__(self, title ='', year = '', rating = 0, time = 0):
        self.title = title
        self.year = year
        self.rating = rating
        self.time = time

    def getTitle(self, title):
        return self.title

    def getTime(self, time):
       return self.time

    def getRating(self, rating):
       return self.rating

    def getYear(self, year):
        return self.year