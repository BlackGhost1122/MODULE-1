#Урок 1  8 задание
#Хранение информации...


a = float(input('Введите размер файла (в Мбайтах): '))

b = float(input('Введите объем карты памяти (в Гбайтах): '))

b *= 1024

if b / round(a) < 1:

   print('Данный файл нельзя записать на карту памяти.')

else:

   print('Данный файл можно записать на карту памяти.')
