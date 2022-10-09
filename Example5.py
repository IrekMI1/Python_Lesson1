# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

coordinate_A = list(map(float, input('Введите через ", " координату (Х, У) точки А: ').split(', ')))
coordinate_B = list(map(float, input('Введите через ", " координату (Х, У) точки B: ').split(', ')))
distance_AB = ((coordinate_A[0] - coordinate_B[0]) ** 2 + 
               (coordinate_A[1] - coordinate_B[1]) ** 2) ** 0.5
print(f'расстояние межд точками А и B равна {round(distance_AB, 3)}')