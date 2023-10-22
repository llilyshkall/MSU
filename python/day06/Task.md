# Множества и словари
## Contents

1. [Мумбо-Юмбо](#мумбо-юмбо)
2. [Самое популярное слово](#Самое-популярное-слово)
3. [Карта подземелья](#карта-подземелья)
4. [Вычисление формулы](#вычисление-формулы)

## Мумбо-Юмбо
Файл - ```day06_task01.py```

Ввод представляет собой строки из букв латинского алфавита (последняя строка — пустая). Это письмена на языках двух племён: Mumbo и Jumbo. Чётные строки — слова одного языка, нечётные — другого (какого — неизвестно). Языки Mumbo и Jumbo имеют одинаковые гласные и разные согласные, причём согласных в языке Mumbo больше, чем в Jumbo. Все слова начинаются на гласную. Определить и вывести, какому языку — Mumbo или Jumbo — принадлежит первое слово, если известно, что в данном корпусе текстов: Использованы все начальные гласные (буква, на которую не начинается ни одно слово — согласная) Использованы все согласные

### Примеры

Входные данные
```
obmdobo
oututo
odbann
ufututu
omdan
uputupf
adabo
utupopot
obomna
utpouo
amdm
```
Результат работы
```
Mumbo
```

## Самое популярное слово
Файл - ```day06_task02.py```

Ввести построчно текст, состоящий из пробелов, переводов строки и латинских букв, и заканчивающийся пустой строкой. Вывести слово, которое чаще других встречается в тексте, если оно такое одно, и ---, если таких слов несколько.

### Примеры

Входные данные
```
Sed tempus ipsum quis eros tempus lacinia Cras finibus lorem ut lacinia egestas nunc nibh iaculis est convallis tincidunt
mi mi sed nisl Sed porttitor aliquam elit ullamcorper tincidunt arcu euismod quis Mauris congue elit suscipit leo varius
facilisis Cras et arcu sodales laoreet est vitae pharetra orci Integer eget nulla dictum aliquet justo semper molestie neque
Maecenas bibendum lacus tincidunt auctor varius purus felis ullamcorper dui et laoreet ligula ex et risus Donec eget
fringilla nibh Cras congue tincidunt accumsan Maecenas euismod eleifend elit ut rhoncus tortor sodales a Cras egestas
finibus lorem non tempor tincidunt aera
```
Результат работы
```
tincidunt
 ```

## Карта подземелья
Файл - ```day06_task03.py```

Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк, содержащих разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель. Две последние строки не содержат пробелов — это название входа в подземелье и название выхода. Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае. Пары могут повторяться или содержать одинаковые слова.

### Примеры

Входные данные
```
markers jumping
jumping guinea
skiing pre
markers gauge
skiing mpeg
solar jackson
skiing solar
guinea gauge
mpeg honor
pre honor
guinea gauge
pre mpeg
markers guinea
markers gauge
honor mpeg
markers jumping
skiing
jumping
```
Результат работы
```
NO
```

## Вычисление формулы
Файл - ```day06_task04.py```

Написать функцию evalform(formula, *args), принимающую переменное количество параметров. Обязателен только первый параметр — это строка с некоторой формулой. В формуле могут встречаться переменные. Имена переменных состоят из одной или нескольких букв. Остальные параметры — это значения этих переменных, если их перечислить в алфавитном порядке. Функция должна возвращать результат вычисления формулы. Проверять правильность или обрабатывать исключения не надо.

### Примеры

Входные данные
```
evalform("b*2 + a*3 + b//3 + c", 11, 3, 2)
```
Результат работы
```
42
```