import peewee

db = peewee.PostgresqlDatabase(
    'orm',
    user = 'uran',
    password = '1',
    host = 'localhost', #127.0.0.1 
    port = 5432 # https, http
)
print()