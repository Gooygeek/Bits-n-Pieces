#
#
#


def bubble_sort(the_list):
    n = len(the_list)
    for i in range(n - 1):
        for j in range(n - 1):
            if the_list[j] > the_list[j + 1]:
                the_list[i], the_list[j] = the_list[j], the_list[i]
