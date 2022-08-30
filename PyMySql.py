import sys
import pymysql.connections
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="123",
  database="products_db"
)
command = sys.argv


def create_table():
    with mydb.cursor() as cursor:
        sql_query = '''CREATE table if not exists Book_Info(
                id INT auto_increment PRIMARY KEY,
                title varchar(255) not null,
                author varchar(255) not null,
                is_exist boolean,
                price decimal(4,2)
                );
            '''
        cursor.execute(sql_query)
    mydb.commit()


def create_book(title,author,is_exist,price):
        with mydb.cursor() as cursor:
            sql_query = '''INSERT INTO Book_Info(
                                         title,author,is_exist,price) 
                           VALUES(%s,%s,%s,%s)
            '''
            cursor.execute(sql_query,(title,author,is_exist,price))
        mydb.commit()


def show_all():
    with mydb.cursor() as cursor:
        sql_query = '''SELECT * FROM Book_Info '''
        cursor.execute(sql_query)
    return cursor.fetchall()


def show_book(id):
    with mydb.cursor() as cursor:
        sql_query = '''SELECT * FROM Book_Info WHERE id = %s'''
        cursor.execute(sql_query,id)
    return cursor.fetchone()


def read_is_exist(id):
    with mydb.cursor() as cursor:
        sql_query = '''SELECT is_exist FROM Book_Info WHERE id = %s '''
        cursor.execute(sql_query,(id))
        result = cursor.fetchone()
    return result['is_exist']


def change_status(is_exist,id):
    with mydb.cursor() as cursor:
        sql_query = '''UPDATE Book_Info SET is_exist=%s WHERE id=%s'''
        cursor.execute(sql_query,(is_exist,id))
    mydb.commit()


def change_price(price,id):
    with mydb.cursor() as cursor:
        sql_query = '''UPDATE Book_Info SET price=%s WHERE id=%s'''
        cursor.execute(sql_query,(price,id))
    mydb.commit()


def remove(id):
    with mydb.cursor() as cursor:
        sql_query =f'''DELETE FROM Book_Info WHERE id=%s'''
        cursor.execute(sql_query,(id))
    mydb.commit()


def search(word):
    with mydb.cursor() as cursor:
        sql_query = f'''
                SELECT * FROM Book_Info WHERE title LIKE "%{word}%" or author LIKE "%{word}%"
        '''
        cursor.execute(sql_query)
    return cursor.fetchall()


if len(command) == 3 and command[1] == 'add' and command[2] == 'table':
    create_table()
elif len(command) == 3 and command[1] == 'add' and command[2] == 'book':
    title_ = input('Please enter book name: ')
    author_ = input('Please enter author name: ')
    is_exist_ = input('Please enter "1" if book is exist, if not enter "0":')
    price_ = input('Please enter book price:')
    create_book(title_,author_,is_exist_,price_)
elif len(command) == 3 and command[1] == 'show' and command[2] == 'all':
    print(show_all())
elif len(command) == 3 and command[1] == 'show' and command[2] == 'book':
    book_id = input('Please enter book id:')
    print(show_book(book_id))
elif len(command) == 3 and command[1] == 'change' and command[2] == 'status':
    book_id = input('Please enter book id:')
    if read_is_exist(book_id)==1:
        change_status(0,book_id)
    else:
        change_status(1,book_id)
elif len(command) == 3 and command[1] == 'change' and command[2] == 'price':
    book_id = input('Please enter book id:')
    new_price = input('Please enter new price:')
    change_price(new_price,book_id)
elif len(command) == 2 and command[1] == 'remove':
    book_id = input('Please enter book id:')
    remove(book_id)
elif len(command) == 2 and command[1] == 'search':
    searched_word= input('Please enter word which you want search:')
    print(search(searched_word))