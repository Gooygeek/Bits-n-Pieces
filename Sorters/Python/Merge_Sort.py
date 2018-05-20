#
#
#


def merge_sort(array):
    tmp = [None] * len(array)
    start = 0
    end = len(array) - 1
    merge_sort_aux(array, start, end, tmp)


def merge_sort_aux(array, start, end, tmp):
    if start < end:  # 2 or more still to sort
        mid = (start + end) // 2

        # split in to two halves
        merge_sort_aux(array, start, mid, tmp)
        merge_sort_aux(array, mid + 1, end, tmp)

        # merge
        merge_arrays(array, start, mid, end, tmp)

        # copy back in to original
        for i in range(start, end + 1):
            array[i] = tmp[i]


def merge_arrays(a, start, mid, end, tmp):
    ia = start
    ib = mid + 1
    for k in range(start, end + 1):
        if ia > mid:  # a is finished, copy b
            tmp[k] = a[ib]
            ib += 1
        elif ib > end:  # b is finished, copy a
            tmp[k] = a[ia]
            ia += 1
        elif a[ia] <= a[ib]:  # a[ia] is the item to copy
            tmp[k] = a[ia]
            ia += 1
        else:  # b[ib] is the item to copy
            tmp[k] = a[ib]
            ib += 1
