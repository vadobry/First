"""Test module"""
from typing import Any

file = open("../resources/DB.txt")
name_list: list[Any] = []
for line in file:
    line.strip()
    name_list.append(line[0:-1])
file.close()

"""Binary search"""
print(name_list)


def search(named_list, desired_element):
    lower_bound = 0
    upper_bound = len(named_list)
    found = False
    while lower_bound < upper_bound and found == False:
        middle_pos = (lower_bound + upper_bound) // 2
        if named_list[middle_pos] < desired_element:
            lower_bound = middle_pos + 1
        elif named_list[middle_pos] > desired_element:
            upper_bound = middle_pos
        else:
            found = True

    if found:
        print("Имя находится в ячейке", middle_pos)
    else:
        print("Имя не было найдено в списке.")


search(name_list, "GstRender.FullscreenScreen 0")
