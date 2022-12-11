# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

ls = [1, 1, 2, 3, 4, 4, 4, 7, 7, 9, 2, 5]

    
ls = sorted(ls)
_list = list(set(ls) - set([ls[i] for i in range(len(ls)-1) if ls[i] == ls[i+1]]))
print(_list)



# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

newList  = [2, 3, 4, 5, 6]


halsLs = math.ceil(len(newList) / 2)
newSum = [newList[i] * newList[len(newList)-i-1] for i in range(halsLs) ]
print(newSum)


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

newList = [1.1, 1.2, 3.1, 10.01]

_min= lambda x: max(x) - min(x)
result = _min(list((map(lambda i: round(i % 1, 3),newList))))
print(result)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = 45

def convert(num): 
  result = []
  while num != 0:
    result.append(1) if num % 2 else result.append(0)
    num = num // 2
  result = int("".join(map(str, reversed(result))))
  return result  

print(convert(number))
