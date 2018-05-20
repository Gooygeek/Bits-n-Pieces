#
#
#


def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_aux(array, start, end)


def quick_sort_aux(array, start, end):
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary - 1)
        quick_sort_aux(array, boundary + 1, end)


def partition(array, start, end):
    mid = (start + end) // 2
    pivot = array[mid]
    swap(array, start, mid)

    boundary = start

    for k in range(start + 1, end + 1):
        if array[k] < pivot:
            boundary += 1
            swap(array, k, boundary)

    swap(array, start, boundary)
    return boundary


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
