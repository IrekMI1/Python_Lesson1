# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).

coordinate = list(map(float, input('Введите через ", " координаты Х, У: ').split(', ')))
if 0 < coordinate[0] and 0 < coordinate[1]:
    print('1-я четверть.')
elif 0 > coordinate[0] and 0 < coordinate[1]:
    print('2-я четверть.')
elif 0 > coordinate[0] and 0 > coordinate[1]:
    print('3-я четверть.')
elif 0 < coordinate[0] and 0 > coordinate[1]:
    print('4-я четверть.')
else:
    print('Введена нулевая координата!')