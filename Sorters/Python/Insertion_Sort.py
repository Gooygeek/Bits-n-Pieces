#
#
#


def insertion_sort(the_list):
    n = len(the_list)
    for k in range(1, n):
        temp = the_list[k]
        i = k - 1
        while i >= 0 and the_list[i] > temp:
            the_list[i + 1] = the_list[i]
            i -= 1
        the_list[i + 1] = temp
