# Последовательности и цикл for
## Contents

1. [Перетасованная строка](#перетасованная-строка)
2. [Цифры по диагонали](#цифры-по-диагонали)
3. [Морской бой](#морской-бой)
4. [Объединение отрезков](#объединение-отрезков)

## Перетасованная строка
Файл - ```day03_task01.py```

Ввести построчно две строки и проверить, есть ли такое число n, что вторая строка получается из первой, если сначала взять каждый n-й символ, затем — каждый n-й, начиная с первого и т. д. до каждого n-го, начиная с n-1-го. Вывести наименьшее возможное n, а если такого числа нет — No.

### Примеры

Входные данные
```
qwertyuif
qruwtieyf
```
Результат работы
```
3
```

## Цифры по диагонали
Файл - ```day03_task02.py```

Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде прямоугольной матрицы N×M, заполненной из верхнего левого угла по следующему правилу: На каждом шаге заполняется очередная диагональ матрицы с одинаковой суммой координат Диагонали заполняются поочерёдно сверху вниз и снизу вверх (таким образом формируется непрерывный «путь» из верхнего левого угла в правый нижний)

Примеры

Входные данные
```
6, 5
```
Результат работы
```
0 2 3 9 0 9
1 4 8 1 8 0
5 7 2 7 1 6
6 3 6 2 5 7
4 5 3 4 8 9
```

## Морской бой
Файл - ```day03_task03.py```

Ввести несколько строк одинаковой длины, состоящих из символов «#» и «.». Ввод заканчивается пустой строкой. На получившемся поле изображены только прямоугольники, причём они не соприкасаются даже углами. Вывести количество этих прямоугольников.

### Примеры

Входные данные
```
###.....#.
###.##..#.
....##....
....##..#.
..........
..........
####..####
......####
......####
```
Результат работы
```
6
```

## Объединение отрезков
Файл - ```day03_task04.py```

Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой. Рассмотрим объединение этих отрезков и найдём длину этого объединения (т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).

Примеры

Входные данные
```
(66, 91), (152, 230), (21, 81), (323, 342), (158, 211), (286, 332), (294, 330), (18, 58), (183, 236)
```
Результат работы
```
213
```