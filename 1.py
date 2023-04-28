# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Ф-ция возвращает кортеж из трех элементов: путь, имя файла, расширение файла.

path_f = input('Укажите абсолютный путь файла: ')

def kortezh(str):
    arr = str.split('/')
    name_f = arr[-1].split('.')
    result = {str:{name_f[0]:name_f[1]}}
    return result

print(kortezh(path_f))