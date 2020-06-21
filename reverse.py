def reverse(aList):
    a = []
    length = len(aList)
    index = length-1
    for i in range(length):
        a.append(aList[index])
        index -= 1
    print(a)

if __name__ == '__main__':

    aList = [1, 2, 3, 4, 5]
    reverse(aList)      