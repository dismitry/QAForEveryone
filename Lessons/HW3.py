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

# Определить, какая семья больше 
# 1) Программа имеет два input() 2) Членов семьи нужно перечислить через запятую. результат - программа выводит семью с бОльшим составом. 
# Если равно - print("Equal')

f1 = ('ma', 'son', 'ba', 'granny')
f2 = ('pa', 'ma', 'son')
print(type(f1))
print(type(f2))
if len(f1) > len(f2):
	print('f1')
elif len(f1) == len(f2):
	print('Equal')
else:
	print('f2')
# либо

family_1 = input()
family_2 = input()

f1 = list(family_1.split(","))
f2 = list(family_2.split(","))

if len(f1) > len(f2):
    print('First family bigger')
elif len(f2) > len(f1):
    print('Second family bigger')
else:
    print('Equal')

3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение

3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 

3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
