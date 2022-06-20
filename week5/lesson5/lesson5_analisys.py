# open() 
# close()
# with open()
# r w a w+ r+ x x+

# with open('text_analisys.txt', 'r') as file:
    # print(file.read()) rtype str
    # print(file.readline())  rtype str
    # print(file.readlines()) rtype list


# w - содержимое файла перезаписвется, очищает файл перед применением
# with open('text_analisys.txt', 'w') as file:
#     file.write('sdfsdf') #input str
#     file.writelines(['sdafasdf\n', 'sdfsdf\n', 'sdfsdf\n']



# file  = open('text_analisys.txt', 'w')
# file.write('Hello\n')
# file.write('Hello1234\n')
# file.seek(0)
# file.close()


# JSON - JavaScript Object Notation
import json

dct = {'name': 'Jonny', 'last_name': 'Depp', 'age': 65}

#dump, dumps - методы для сериализации(т.е конвертации)
#python обьектов в json обьекты

#dump(dict, file) -> производит запись преобразованного в JSON, python обьекта.
#python ---------------> Json

#dumps(object) - конвертирует python в json

# json_obj = json.dumps(dct)
# print(json_obj)
# print(type(json_obj)) #class str
# print(type(dct)) #class dict


# load(),loads() - методы для десериализации
# JSON -------------> Python
# json.load(json.obj, file)

# json_obj = json.dumps(dct)
# python_obj = json.loads(json_obj)
# json.load(json_file, python_file)

