# GC-состав является важной характеристикой геномных последовательностей
# и определяется как процентное соотношение суммы всех гуанинов
# и цитозинов к общему числу нуклеиновых оснований в геномной последовательности.
#
# Напишите программу, которая вычисляет процентное содержание
# символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
#
# Например, в строке "acggtgttat" процентное содержание
# символов G и C равно \dfrac4{10} \cdot 100 = 40.0
# 10
# 4
# ​
# ⋅100=40.0, где 4 -- это количество символов G и C,  а 10 -- это длина строки.
a = input()
count_c = 0
count_g = 0
for i in a.upper():
    if i == "C":
        count_c += 1
    if i == "G":
        count_g += 1
print(((count_c+count_g)/len(a))*100)

# s = input().upper()
# print((s.count('G') + s.count('C'))/len(s) * 100)

# s=input().upper()
# k=0
# for i in ('G','C'):
#     k+=s.count(i)
# print(k*100/len(s))

# [print((n.count('c') + n.count('g')) / len(n) * 100) for n in [input().lower()]]