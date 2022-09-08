# Напишите программу, которая проверяет здоровье персонажа в игре. Если оно равно или меньше нуля, выведите на экран False, в противном случае True.

x = -2
health = ''
if x <= 0:
  health = 'death'
else:
  health = 'live'
print(health)

# Напишите программу, которая на входе получает имя пользователя, cохраняет его в переменную и выводит строку  "Hello {user_name}!" 

x = input('user_name:');
print(f'Hello, {x}')

# вывод изображения квадратика

x = '*********\n*       *\n*       *\n*********'
print(x)

# Проверка на четность

x = int(input('num:'))
if x % 2 == 0:
  print('even')
else:
  print('odd')

# Проверка високосности

x = int(input('year:'))
if (x % 4 == 0 and x % 100 != 0) 
    or x % 400 == 0:
  print('bissextile')
else:
  print('non-leap')
  
# Напишите программу, которая печатает введенный текст заданное количество раз, построчно.

for text in range(5): 
  print('text')
