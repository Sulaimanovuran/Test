'''
ORM (Object Reltion Mapping - обьектно реляционное отображение) -
технология программирования, которя связывает базы данных с концеациями обьектно ориентированных 
языков программирования.
'''

from views import *
from settings import db

get_categories()
db.close