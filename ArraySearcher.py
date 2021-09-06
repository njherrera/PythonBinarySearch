# takes an array of numbers as input, then applies the binary search algorithm to find the target number
# if target is less than the value at the halfway point of the array, do the search again in the left half
# if target is greater than value at halfway point, search again in the right half
# repeat until target is found, or there are no more indices left to search

def binarySearch ( list, target):
    print(list)
    if target is list[0] and len(list) == 1:
        return target
        print("target found, value is: " + target)
    elif target is list[(len(list) - 1) // 2]:
        print("target value found!")
        return target
    elif len(list) == 1 and target != list[0]:
        print("target value not found in array")
        return
    elif target < list[(len(list) - 1) // 2]: # if the target is less than the middle value of the list, it must be left of middle
        print("going left")
        rightPoint = (len(list) - 1) // 2 - 1 # with test input of [4,5], this sets right point as length of list // 2 (1) - 1 (0), which of course results in a list with nothing in it
        binarySearch(list[: rightPoint], target)
    elif target > list[(len(list) - 1) // 2]: # if target is greater than the middle value of the list, it must be right of middle
        print("going right")
        leftPoint = (len(list) - 1) // 2 + 1 # set new left side to be one right of the middle value
        binarySearch(list[leftPoint:], target) # call the method again, this time with the new left and right sides

testList = []
testList.append(1)
testList.append(2)
testList.append(3)
testList.append(4)
testList.append(5)
testList.append(6)
testList.append(7)
testList.append(8)
binarySearch(testList, 5)
