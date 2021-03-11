"""Selection sort"""
import random


def selection_sort(sorted_list):
    for cur_pos in range(len(sorted_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(sorted_list)):
            if sorted_list[scan_pos] < sorted_list[min_pos]:
                min_pos = scan_pos
        sorted_list[min_pos], sorted_list[cur_pos] = sorted_list[cur_pos], sorted_list[min_pos]


def selection(data):
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data




# another variant unstable
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def select_sort_1(arr):
    i = len(arr)
    while i > 1:
        max = 0
        for j in range(i):
            if arr[j] > arr[max]:
                max = j
        swap(arr, i - 1, max)
        i -= 1


# another variant stable
def select_sort_stable(arr):
    if len(arr) == 0:
        return
    for j in range(len(arr)):
        min = j
        for i in range(j + 1, len(arr)):
            if (arr[i] < arr[min]): min = i
    if (min != j):
        value = arr[min]
        for l in range(min, j - 1, -1):
            arr[l] = arr[l - 1]
        arr[j] = value


def print_list(view_list):
    for item in view_list:
        print("%3d" % item, end="")
    print()


unsorted_list = []
for i in range(10):
    unsorted_list.append(random.randrange(100))
print_list(unsorted_list)
selection(unsorted_list)
print_list(unsorted_list)
