def binarySearch_bounded(list, item, lowerBound=0, upperBound=0):
    low = lowerBound
    if upperBound == 0:
        high = len(list) - 1
    else:
        high = upperBound
    while low <= high:
        mid = (low + high) // 2
        if item == list[mid]:
            return mid
        elif item < list[mid]: # Switch to > if list is in descending order
            high = mid - 1
        else:
            low = mid + 1
    return low