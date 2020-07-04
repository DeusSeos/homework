class Student:

    def __init__(self, name, score, next=None):
        self.name = name

        self.score = score
        self.next = next


def perfect_score_list(head):
    perfectScoreList = []


    nextStudent = head
    while nextStudent != None:
        if nextStudent.score == 100:
            perfectScoreList.append(nextStudent.name)
        nextStudent = nextStudent.next
        return perfectScoreList

aList = []
while True:
    print("Enter q to quit")
    name = input("Enter the student's name: ")
    if name.strip().lower() == 'q':
        break
    score = input("Enter the student's score: ")
    if score.strip().lower() == 'q':
        break
    a = Student(name, score)
    aList.append(a)

for i in range(len(aList)):
    if i == len(aList) - 1:
        break
    aList[i].next = aList[i + 1]

print(perfect_score_list(aList[0]))


# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None


# head = LinkedList(a)
#     .next =

#
# def clone(self):
#     tempList = []
#
#     newstack = ArrayStack()
#     for items in self.items:
#         tempList
#
#     return newstack


class GeometricShape:

    def __init__(self):
        pass

    def getArea(self):
        pass

    def getVolume(self):
        pass


class Square(GeometricShape):
    def __init__(self, sides):
        self.sides = sides

    def getArea(self):
        return self.sides * self.sides


class Cube(GeometricShape):
    def __init__(self, sides):
        self.sides = sides

    def getArea(self):
        pass

    def getVolume(self):
        return self.sides * self.sides * self.sides

