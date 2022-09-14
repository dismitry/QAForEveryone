# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

# Дан список ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]: 1) получите сумму всех чисел; 2*) распечатайте все строки, где есть буква 'a'

stroka = ['Hi', 'ananas', 2, None, 75, 'pizza', 35, 100]

chisla = [i for i in stroka if isinstance(i, (int, float))]
print(sum(chisla))
# либо
cymma = stroka[2]+stroka[4]+stroka[6]+stroka[7]
print(cymma)

# Превратите лист в кортеж

list = ('cat', 'dog', 'horse', 'cow')
print(list)
print(type(list)) # Литеральное объявление
# либо
list1 = tuple('cat dog horse cow')
print(list1)
print(type(list1)) # Через функцию tuple
