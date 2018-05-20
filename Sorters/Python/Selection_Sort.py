#
#
#


def selection_sort(the_list):
    n = len(the_list)
    for k in range(n - 1):
        min_position = find_min(the_list, k)
        the_list[k], the_list[min_position] = the_list[min_position], the_list[k]


def find_min(the_list, mark):
    min_position = mark
    n = len(the_list)
    for i in range(mark + 1, n):
        if the_list[i] < the_list[min_position]:
            min_position = i
    return min_position
