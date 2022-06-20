#list comprehension


# Есть три вида comprehension:
    # list comprehension
    # set comprehension
    # dictionary comprehension



# l = []
# for i in range (1,11):
#     l.append(i)
# a = 'yes' if True else 'no'
# print (a)


# list_= [i for i in range(1,11)]  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print (list_)

# list_ = [i for i in range(0,11,2)]
# print (list_)
# list_ = [i for i in range(100) if i % 2 ==0]

# list_ = ['четное' if i % 2 == 0 else 'Нечетное' for i in range (100)]
# print(list_)

# import time
# start_time = time.time()
# print(start_time)


# import time
# start_time = time.time()
# l = []
# for i in range(500):
#     l.append(i)


# end_time = time.time()
# time1 = end_time - start_time


# start_time2 = time.time()
# list_ = [i for i in range(500)]
# end_time2 = time.time()
# time2 = end_time2 - start_time2

# print(time1 / time2)

# list_ = [i **2 if i % 2 == 0 else i ** 3 for i in range(101)]
# print(list_)

# list_ = [i ** 2 for i in range(101) if i % 2 == 0]
# print (list_)


# matrix = [
#     [0,0,0],
#     [1,1,1],
#     [2,2,2]
# ]
# list_ =[j for i in matrix for j in i]
# print (list_)


# matrix = [
#     [0,0,0],
#     [1,1,1],
#     [2,2,2]
# ]
# list_ =[j for i in matrix if i == 0 for j in i]

# some_text = 'hello world'
# list_ = [i for i in some_text if i == 'e' or i == 'o']
# print (list_)

# list_ = [True if i % 2 == 0 else False for i in range(10)]
# print(list_)

# print (any(list_)) # True если есть хоть один True
# print(all(list_)) # False если есть хоть один False 


# l = ['apple', 'banana', 'kiwi']
# list_ = [i for i in l if 'a' in i]
# print (list_)

# list_ = []
# list_1 = [[j for j in range(i)]  for i in range(10) ]
# print (list_1)

# list_ = max([i ** 2 for i in range(5)])
# print (list_)

# list_ = sum([i ** 2 for i in range(5)])
# print (list_)

# list_ =[ord(str(i))for i in range(10)]
# print (list_)


###### set



# list_ = [1,1,1,0,0,0]
# set_ = {i for i in list_}
# print(set_)

#### dict

# dict_ = {i: i **2 for i in range(10)}
# print (dict_)

# dict_ = {i: i**2 if i % 2 == 0 else i** 3 for i in range(10)}
# print(dict_)

# dict_ = {i: 'четное' if i % 2 == 0 else 'нечетное' for i in range(10)}
# print (dict_)

# dict_ = {'c': 5, 'b': 3, 'f': 2}
# dict_ = {key: 'четное' if value % 2 == 0 else 'нечетное' for key, value in dict_.items()}
# print (dict_)

# dict_ = {'a': [10,20], 'b': [30], 'c':[100,1]}
# dict_ = {key: max(v) for key,v in dict_.items()}
# print(dict_)

# dict_ = {1: 'hello', 2: 'world', 3: 'makers', 4: 'dictionary', 5: 'python'}
# dict_ = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k,v in dict_.items()}
# print(dict_)

# dict_ = {i: i ** 2 for i in range(1,10)}
# print (dict_)

# num = int(input('Введите число от 1 до 10: '))
# dict_ = {i: i**2 for i in range(1,500) if i % num == 0}
# print(dict_)


# list_ = []
# list_1 = [[j for j in range(i)]  for i in range(10) ]
# print (list_1)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# a = {k: [j for j in range(1,v+1)] for k,v in a.items()}
# print (a)

# dict_ = {'one': 23, 'two': 656, 'three': 323, 'four': 488}
# dict_ = {key: 'even' if value % 2 == 0 else 'odd' for key,value in dict_.items()}
# print(dict_)

# text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in text if i.isdigit() == True]
# print (list_)

# print (dir(str))


# a = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#  'Olga': {'history': 92, 'math': 96, 'literature': 81},
#   'Nik': {'history': 84, 'math': 85, 'literature': 87}
#   }


# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for key, value in a.items():
#     if value % 2 == 0:
#         b[key]=2
#     else:
#         b[key]=value
# print (b)

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for key, value in a.items():
#     if value == None:
#         a = a.pop(key)
# print (a)


# string = 'pythonist'
# dict_ = {i: string[i].count() for i in string}
# print (dict_)

# student = {"name": "Emma", "class": 9, "marks": 75}
# print(student['marks'])

# d = {1:2, 2:4, 3:9}
# print(d.pop(2))

# a = dict([(1,1) (2,4)])
# print(a)

# d = dict.fromkeys('a','b')
# print(d)

# a = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# b = {k: {k2 for k2,v2 in v.items() if v2 == max(v.values())} for k,v in a.items()}
# print (b)

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# my_dict = {k:{k2 for k2 in v.keys()} for k,v in my_dict.items()}
# print (my_dict)


# l = [i  for i in range(1,50)if i % 2 == 0]
# print(l)


# int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# new_list = [i for i in int_list if i % 2 == 0 and i > 0]
# print (new_list)

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print (int_list)

# l = [i if i % 2 == 0 else i ** 2 for i in range(1,11)]
# print(l)
# l = [True if i % 2 == 0 else False for i in range(1,10)]
# print (l)


# l = ['John', 'Sam', 'Alice', 'Anderson', 'Samuel', 'Mai', 'Svidrigailov', 'Tor', 'Winston', 'Sherlok']
# l = ['shorter' if len(i)<4 else 'longer' for i in l]
# print (l)


# text = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [int(i) for i in text if i.isdigit() == True]
# print (list_)


# from random import randint
# set_1 = { randint(1,100) for i in range(1,11)}
# set_2 = {randint(1,100) for i in range(1,11)}
# set_1 = set_1.update(set_2)

# print (set_1)

# dict_ = {'a': 5, 'b': 57, 'c': 23, 'd': 21}
# result = 1
# for key in dict_:    
#     result = result * dict_[key]

# print(result)


# school = {'1а':32, '1б':34, '2б':22, '6а':17, '7в':29}
# school['2б'] = 30
# school.setdefault('8а', 27)
# school.pop('1а')
# sum_people = 1
# for v in school.values():
#     sum_people = sum_people + v
# print (school)
# print(sum_people)

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split() if string_.isdigit() == True]
# print(list_)
# my_str = 'asdfadfasdfasdfasdf'
# k = [print(i) for i in my_str if i not in 'aeiou']

# print([i.lower() for i in 'HELLO'])