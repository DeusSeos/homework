from MovieArray import Movie
from MovieArray import Array


def display(movieArray):
    if movieArray[0] == None:
        print("There are no movies to be displayed. Please select (a) in order to add to the movie list.")
        return 0
    displayed = 0
    print("\n# Title{0:15}Viewed{0:9}Rating{0:9}Duration(hrs){0:2}".format(''))
    print("_" * 2, "_" * 65)

    for element in movieArray:
        if element != None:
            displayed += 1
            print("{0:<3}".format(displayed), end='')
            print(element)
        else:
            break
    print()
    return displayed


def addMovie(movieArray):
    title = ''
    title = input("Enter the movie's name: ")
    isValid = False
    while not isValid:
        try:
            year = input("Enter the year you saw {} [ie 2020]: ".format(title)).strip()
            year = int(year)
            isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to an int: {1} \nPlease enter a valid year.".format(year, ex))
    isValid = False
    while not isValid:
        try:
            rating = input("Enter the rating for {} [1, 2, 3, 4, 5]: ".format(title))
            rating = float(rating)
            isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to a float: {1} \nPlease enter a valid rating.".format(rating, ex))
    isValid = False
    while not isValid:
        try:
            duration = input("Enter the duration (hours) for {} [1, 2, 3, 4, 5]: ".format(title))
            duration = float(duration)
            isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to a float: {1} \nPlease enter a valid rating.".format(duration, ex))
    movieArray.insert(len(movieArray), Movie(title=title, year=year, rating=rating, duration=duration))
    display(movieArray)


def sortDuration(movieArray=Array(0, None)):
    """Bubble Sorting implementation"""
    if len(movieArray) > 1 and type(movieArray[0]) == Movie:
        n = len(movieArray)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if type(movieArray[j]) == Movie and type(movieArray[j+1]) == Movie:
                    if movieArray[j].getDuration() > movieArray[j + 1].getDuration():
                        movieArray[j], movieArray[j + 1] = movieArray[j + 1], movieArray[j]
    else:
        print("Not enough movies to be sorted. Select (a) at the menu to enter more movies.\n")
        return None
    display(movieArray)


def removeMovie(movieArray=Array(0, None)):
    n = len(movieArray)
    if type(movieArray[0]) != Movie:
        print("There are no movies in the list. Select (a) at the menu to enter more movies.\n")
        return
    isValid = False
    while not isValid:
        try:

            index = input("Enter a movie's number to be removed (1-{}): ".format(n)).strip()
            index = int(index)
            if index < 1 or index > n:
                print("Value is not within bounds. Please enter a valid selection.")
                isValid = False
            else:
                isValid = True
        except ValueError as ex:
            print("{0} cannot be converted to an int: {1} \nPlease enter a valid year.".format(index, ex))
    movieArray.remove(index-1)
    display(movieArray)



def sortYear(movieArray=Array(0, None)):
    """Merge Sorting implementation"""

    n = len(movieArray)
    if n > 1 and type(movieArray[0]) == Movie:
        middle = n // 2
        left = []
        right = []
        for i in range(middle):
            if movieArray[i] == Movie:
                left.append(movieArray[i])
        for i in range(middle, n):
            if movieArray[i] == Movie:
                right.append(movieArray[i])

        sortYear(left)
        sortYear(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i].getYear() < right[j].getYear():
                movieArray[k] = left[i]
                i += 1
            else:
                movieArray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            movieArray[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            movieArray[k] = right[j]
            j += 1
            k += 1
    else:
        print("Not enough movies to be sorted. Select (a) at the menu to enter more movies.\n")
        return
    display(movieArray)


def sortTitle(movieArray=Array(0, None)):
    """XXXXX Sorting implementation"""

    n = len(movieArray)

    if n > 1 and type(movieArray[0]) == Movie and type(movieArray[1] == Movie):
        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if type(movieArray[minIndex]) == Movie and type(movieArray[j]) == Movie:
                    if movieArray[minIndex].getTitle() > movieArray[j].getTitle():
                        minIndex = j
            movieArray[i], movieArray[minIndex] = movieArray[minIndex], movieArray[i]
    else:
        print("Not enough movies to be sorted. Select (a) at the menu to enter more movies.\n")
        return
    display(movieArray)

def sortRating(movieArray=Array(0, None)):
    """Quick Sorting implementation"""

    n = len(movieArray)
    if n > 1 and type(movieArray[0]) == Movie and type(movieArray[1] == Movie):
        quickSortHelper(0,n-1,movieArray)
    else:
        print("Not enough movies to be sorted. Select (a) at the menu to enter more movies.\n")
        return
    display(movieArray)




def quickSortHelper(i,j,movieArray=Array(0,None)):
    if i < j:
        pivot = quickSortPartitionHelper(i,j,movieArray)
        quickSortHelper(i, pivot-1, movieArray)
        quickSortHelper(pivot+1, j, movieArray)

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def quickSortPartitionHelper(low,high,movieArray=Array(0,None)):
    i = (low - 1)  # index of smaller element

    pivot = movieArray[high].getRating()  # pivot

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if movieArray[j].getRating() <= pivot:
            # increment index of smaller element
            i = i + 1
            # swap the two elements
            movieArray[i], movieArray[j] = movieArray[j], movieArray[i]

    movieArray[i + 1], movieArray[high] = movieArray[high], movieArray[i + 1]
    return (i + 1)


    # The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index








if __name__ == '__main__':
    """movieArray = Array(3, None)
    movieArray.insert(2, (Movie("a", 1, 5, 1)))
    movieArray.insert(2, (Movie("b", 2, 4, 2)))
    movieArray.insert(2, (Movie("c", 3, 3, 3)))

    movieArray[3] = Movie("d", 4, 2, 4)"""





    movieArray = Array(5, None)
    movieArray.insert(2, (Movie("a", 1, 5, 1)))
    movieArray.insert(2, (Movie("b", 2, 4, 2)))
    movieArray.insert(2, (Movie("c", 3, 3, 3)))

    while True:
        options = ['L List all movies', '', 'A Add a movie', 'E Remove a movie', 'D Arrange by Duration',
                   'T Arrange by Title', 'V Arrange by year Viewed', 'R Arrange by Rating', 'Q Quit']
        for element in options:
            print(element)
        choice = input('\nYour choice: ').strip().lower()
        if choice == 'q':
            break
        elif choice == 'l':
            display(movieArray)
        elif choice == 'a':
            addMovie(movieArray)
        elif choice == 'e':
            removeMovie(movieArray)
        elif choice == 'd':
            sortDuration(movieArray)
        elif choice == 'v':
            sortYear(movieArray)
        elif choice == 't':
            sortTitle(movieArray)
        elif choice == 'r':
            sortRating(movieArray)
            #display(movieArray)
        else:
            print("Please pick one of the options listed.\n")
