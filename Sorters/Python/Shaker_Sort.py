"""
authour: Kieran Goldsworthy
date created: 19/03/2015
date modified: 19/03/2015
description: this will take a user input list, and order it using shaker sort. It will then print the results.
time complexity:
    best: polynomial
    worst: polynomial
parameters: a list
pre-conditions: a list is required, which contains order-able elements (i.e. numbers)
post-conditions: it will output a list that is a sorted version (lowest to highest) of the one the user input
"""

"""looks at each pair, going left and right through the list"""


def shaker_sort(a_list):
    for i in range(int(len(a_list) / 2)):
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                swap(j, j + 1, a_list)
        for k in range(len(a_list) - 1, 1, -1):
            if a_list[k] < a_list[k - 1]:
                swap(k, k - 1, a_list)
    print(a_list)


"""performs the swap"""


def swap(i, j, l):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp


print("type 'shaker_sort()' and in the brackets, your list")
