"""Insertion sort"""
import random


def insertion_sort(unsorted_list):
    # Start whit the second element
    # Use this item to insert it into the list
    for key_pos in range(len(unsorted_list)):
        # get the value of the element oto insert
        key_value = unsorted_list[key_pos]
        # Scan the left side
        scan_pos = key_pos - 1
        # Go throughout each element by moving them up until we reach the cell with the smaller element
        while (scan_pos >= 0) and (unsorted_list[scan_pos] > key_value):
            unsorted_list[scan_pos + 1] = unsorted_list[scan_pos]
            scan_pos = scan_pos - 1
        # everything has been moved, now we will insert element tj the rigth of the last cell
        unsorted_list[scan_pos + 1] = key_value


unsorted_list = []
for i in range(10):
    unsorted_list.append(random.randrange(100))
print(unsorted_list)
insertion_sort(unsorted_list)
print(unsorted_list)