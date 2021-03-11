"""base trening"""
import random

list_unsort = []
for i in range(10):
    list_unsort.append(random.randrange(100))
print(list_unsort)

min_el = list_unsort[0]
for i in range(1, len(list_unsort)):
    if list_unsort[i] < min_el:
        min_el = list_unsort[i]
print(f"Минимальный элемент массива:{min_el}")

max_el = list_unsort[0]
for i in range(1, len(list_unsort)):
    if not list_unsort[i] <= max_el:
        max_el = list_unsort[i]
print(f"Максимальный элемент массива:{max_el}")

print(f"Не отсортированный массив:{list_unsort}")


def bubble_sort(sort_list):
    """bubble sort"""
    score_in = 0
    score_out = 0
    for out_int in range(1, len(sort_list) - 1):
        flag = 0
        score_out = score_out + out_int
        for in_int in range(len(sort_list) - out_int):
            score_in = score_in + in_int
            if sort_list[in_int] > sort_list[in_int + 1]:
                sort_list[in_int], sort_list[in_int + 1] = sort_list[in_int + 1], sort_list[in_int]
                flag = 1
        if flag == 0:
            break
    print(f"Внешний цикл прошел :{score_out} раз")
    print(f"Внутрений цикл прошел :{score_in} раз")


bubble_sort(list_unsort)
print(f"Отсортированный  массив(bubble_sort):{list_unsort}")

list_unsort2 = []
for i in range(10):
    list_unsort2.append(random.randrange(100))

print(f"Не отсортированный массив:{list_unsort2}")


def bubble_si_sort(sort_list):
    """sustainable implementation"""
    score_in = 0
    score_out = 0
    for out_int in range(0, len(sort_list) - 1):
        flag = 0
        min_flag = out_int
        for in_int in range(out_int, (len(sort_list) - 1) - out_int):
            score_in = score_in + in_int
            score_out = score_out + out_int
            if sort_list[in_int] > sort_list[in_int + 1]:
                sort_list[in_int], sort_list[in_int + 1] = sort_list[in_int + 1], sort_list[in_int]
                flag = 1
            if sort_list[in_int] < sort_list[min_flag]:
                min_flag = in_int
        if flag == 0:
            break
        if min_flag != out_int:
            sort_list[min_flag], sort_list[out_int] = sort_list[out_int], sort_list[min_flag]
    print(f"Внешний цикл прошел :{score_out} раз")
    print(f"Внутрений цикл прошел :{score_in} раз")


bubble_si_sort(list_unsort2)
print(f"Отсортированный  массив(bubble_ins_sort):{list_unsort2}")
