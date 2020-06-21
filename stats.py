import random


def median(aList):
    numList = sorted(aList)
    index = (len(numList)-1)//2

    if (len(numList)%2):
        return numList[index]
    else:
        return (numList[index] + numList[index +1])/2.0

def mode(aList):
    numList = sorted(aList)
    lenList = len(numList)
    numDict = {}
    for number in numList:
        if number in numDict:
            numDict[number] += 1
        else:
            numDict[number] = 1
    highest = max(numDict, key = numDict.get)
    return highest


if __name__ == '__main__':


    randomList = []
    
    for i in range(random.randrange(0, 1000)):
        randomList.append(random.randrange(0,2000))

    print(mode(randomList))
    print(median(randomList))
