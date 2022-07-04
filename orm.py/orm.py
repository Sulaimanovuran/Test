# import psycopg2

# connection = psycopg2.connect(   #\c db_name
#     database='db_pracrice',
#     user='uran',
#     password = '1',
#     host='localhost',
#     port='5432'
# )
# print('Ok')



# cursor.execute(
#     '''create table company(
#         id serial primary key,
#         name varchar(100) not null,
#         city varchar(50) not null
#     )
#     '''
# )
# print('Table created')
# connection.commit()
# connection.close()


# cursor.execute(
#     '''insert into company(name,city) values ('IBM', 'Los Angeles'), ('Apple', 'Cupertino'), ('HP','New York'), ('Dell','New Jersey')
#     '''
# )
# connection.commit()
# print('succes')
# connection.close()


# cursor.execute(
#     '''insert into company(name, city) values ('Samsung', 'Seoul')
#     '''
# )
# cursor.execute(
#     '''insert into company(name, city) values ('Toyota', 'Tokyo')
#     '''
# )

# connection.commit()
# print('succes yo')
# connection.close()


# cursor.execute(
#     '''select * from company;
#     '''
# )
# # print(cursor.fetchall())
# data = cursor.fetchall()
# for i in data:
#     print(i)
# cursor.close()

# cursor.execute(
#     'select name, city from company where id = 2'
# )
# data = cursor.fetchone()
# # print(data)


# cursor.execute(
#     '''UPDATE company set city = 'New Mexico' where id = 2'''
# )
# connection.commit()
# cursor.execute(
#     'select * from company order by id'
# )
# data = cursor.fetchall()
# for i in data:
#     print(*i)
# connection.close()

# cursor = connection.cursor()

# cursor.execute(
#     '''delete from company where id = 3'''
# )

# connection.commit()
# print(f'total coun: t{cursor.rowcount}')
# cursor.execute(
#     'select * from company order by id'
# )

# data = cursor.fetchall()
# print(data)
# connection.close()


# from sqlalchemy import create_engine

# engine = create_engine('''postgresql+psycopg2://uran:1@localhost:5432/db_pracrice''') #\c db_name
# print('connected')

# from sqlalchemy import Column, Table, Integer, String, MetaData

# metadata = MetaData()
# students_table = Table(
#     'students', metadata,
#     Column('Id', Integer, primary_key=True), 
#     Column('name', String),
#     Column('last_name', String)
# )
# # students_table.create(bind = engine)
# # print('succes')

# inserted = students_table.insert().values(name = 'John', last_name='Snow')
# engine.execute(inserted)
# print('succes')

# from sqlalchemy import select
# query = select([students_table.c.name, students_table.c.last_name])
# data = engine.execute(query).fetchall()
# print(data)