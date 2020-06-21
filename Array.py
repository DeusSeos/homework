import random


class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports iteration over a view of an array."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self._items[index] = newItem

    def pop(self, index):
        if index >= 0 and index < self.__len__():
            """Index given is within range"""
            a = self._items[index]
            self._items[index] = None
            """resize the array"""
            i = self.__len__() - 1
            j = index
            while i > j:  # iterate from the index till end of list
                self._items[j] = self._items[j + 1]  # shift element from right to the left by one
                j += 1  # move index over to the right by one
            return a
        else:
            """Error message"""
            print("Index out of range.")
            return None

    def insert(self, index, value):
        """If array doesn't have empty space at the end grow by twice the size"""
        if self._items[self.__len__()-1] != None:
            for create in range(self.__len__()*2):
                self._items.append(None)
        if index <= 0:
            index = 0

        """if index is less than 0 and the first element is empty
        handles 1st element insertion"""
        if index == 0 or self._items[0] == None:
            self._items[0] = value
        elif self._items[index] == None:
            self._items[index] = value
        else:
            i = self.__len__()-1 # index at the end of the array

            while i > index: #iterate from the back of the array till index
                self._items[i] = self._items[i-1] #shift element from left to the right by one
                i -= 1 #move index over to the left by one
            self._items[index] = value

    def remove(self, index):
        """Check if index is out of bounds if in bounds resets the value to Fillvalue of none"""
        if index >= 0 and index < self.__len__():
            self._items[index] = None
            i = self.__len__()-1
            j = index
            while i > j: #iterate from the index till end of list
                self._items[j] = self._items[j+1] #shift element from right to the left by one
                j += 1 #move index over to the right by one
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



if __name__ == "__main__":
    capacity = 20
    size = capacity // 2
    my_array = Array(capacity)
    temp_array = Array(capacity)
    for i in range(size):
        # What method is called?
        a = random.randint(1, capacity + 1)
        my_array[i] = a
        temp_array[i] = a

    print("len = ", len(my_array))

    for item in my_array:
        print(item, end=" ")
    print("\n", "-" * 60)

    for i in range(size - 1, 0, -1):
        print(my_array[i], end=", ")
    print()

    print(my_array)

    #temp_array.pop(1)
    print(temp_array, my_array)



    print( my_array == temp_array )
