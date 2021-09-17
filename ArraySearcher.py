# takes an array of numbers as input, then applies the binary search algorithm to find the target number
# if target is less than the value at the halfway point of the array, do the search again in the left half
# if target is greater than value at halfway point, search again in the right half
# repeat until target is found, or there are no more indices left to search

def binarySearch ( list, target):
    mid = (len(list) - 1) // 2
    if target is list[mid]:
        print("target value found!")
        return target
    elif len(list) == 1 and list[0] != target:
        print("value isn't in list")
    elif target < list[mid]: # if the target is less than the middle value of the list, it must be left of middle
        rightPoint = (mid) - 1
        if rightPoint == 0: # this is necessary because if mid is equal to 1, (i.e. when array has 2 or 3 items), then rightpoint will be 0 and the call to binarysearch will result in an empty list
            rightPoint = 1
        binarySearch(list[: rightPoint], target)
    elif target > list[mid]: # if target is greater than the middle value of the list, it must be right of middle
        leftPoint = (mid) + 1 # set new left side to be one right of the middle value
        binarySearch(list[leftPoint:], target) # call the method again, this time with the new left and right sides

testList = []
testList.append(1)
testList.append(2)
testList.append(3)
testList.append(4)
testList.append(5)
testList.append(6)
testList.append(7)
binarySearch(testList, 8)
