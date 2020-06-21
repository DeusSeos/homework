

class Movie():
    def __init__(self, title='', year='', rating=0, duration=0):
        self.title = title
        self.year = year
        self.rating = rating
        self.duration = duration

    def getTitle(self):
        return self.title

    def getDuration(self):
        return self.duration

    def getRating(self):
        return self.rating

    def getYear(self):
        return self.year

    def __str__(self):
        return "{0:<20}{1:<15}{2:<15}{3:<10}".format(self.title, self.year, self.rating, self.duration)



class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.usedSize = 0
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
       # return len(self._items)
        return self.usedSize;

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        if index > self.usedSize:
            print("Out of bounds write for index:", index)
            return
        else:
            return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        if index > self.usedSize:
            print("Out of bounds read for index:",index)
            return
        else:
            self._items[index] = newItem

    def pop(self, index):
        # TODO: need to add usedSize - reduce it
        # TODO: need remove dependency on None
        if index >= 0 and index < self.__len__()-1:
            """Index given is within range"""
            a = self._items[index]
            self._items[index] = None
            """resize the array"""
            i = self.__len__() - 1
            j = index
            while i > j:  # iterate from the index till end of list
                self._items[j] = self._items[j + 1]  # shift element from right to the left by one
                j += 1  # move index over to the right by one
            self.usedSize -= 1
            return a
        else:
            """Error message"""
            print("Index out of range.")
            return None

    def insert(self, index, value):
        """If array doesn't have empty space at the end grow by one the size"""
        if self._items[self.__len__() - 1] != None:
            for i in range(self.__len__() * 2):
                self._items.append(None)
        if index <= 0:
            index = 0
        # TODO: need to add usedSize
        # TODO: need remove dependency on None
        """if index is 0 and the first element is empty
        handles 1st element insertion"""
        if index == 0 and self._items[0] == None:
            self._items[0] = value

        elif self._items[index] == None:
            while self._items[index-1] == None and not index-1 < 0:
                index -= 1
            self._items[index] = value
        else:
            i = self.__len__()-1 # index at the end of the array

            while i > index: #iterate from the back of the array till index
                self._items[i] = self._items[i-1] #shift element from left to the right by one
                i -= 1 #move index over to the left by one
            self._items[index] = value
        self.usedSize += 1

    def remove(self, index):
        """Check if index is out of bounds if in bounds resets the value to Fillvalue of none"""

        # TODO: need to add usedSize - reduce it
        # TODO: need remove dependency on None
        if index >= 0 and index <= self.__len__()-1:
            self._items[index] = None

            i = self.__len__()-1
            j = index
            while i > j: #iterate from the index till end of list
                self._items[j] = self._items[j+1] #shift element from right to the left by one
                j += 1 #move index over to the right by one
            self._items[j] =None
            self.usedSize -= 1
        else:
            print("Index out of bounds")

    def __eq__(self, other):
        """Check if not same data type. If same evaluate array length if not the same"""
        print(len(self), len(other))
        if type(other) != type(self):
            return False
        elif len(self) != len(other):
            return False
        else:
            for ele, elem in zip(self, other):
                if ele != elem:
                    return False
        return True

