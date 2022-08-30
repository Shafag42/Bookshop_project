from datetime import datetime
import  sys, os
from os.path import exists
if not  exists('book_list.txt'):
    file = open('book_list.txt', "x")
command = sys.argv
class Book:
    def set_id(self):
        with open('book_list.txt', 'r+') as f:
            obj = f.readlines()
            last_id = 1
            if obj:
                last_id = int(obj[-5].split(':')[1]) + 1
            ele = f'ID : {last_id}'
            f.write(f"{ele}\n")
        return True
    def add_book(self):
        title = input('Please enter book name: \n')
        author = input('Please enter writer name: \n')
        with open('book_list.txt', 'a+') as f:
                ele = f'Book name : {title}\nWriter name : {author}'
                f.write(f"{ele}\n")
                print('\nAdded successfully!')
    def set_date(self):
        with open('book_list.txt', 'a+') as f:
                obj = f.readlines()
                ele = f'Added in: {datetime.today().strftime("%d %B %Y")}'
                f.write(f"{ele}\n{'*' * 50}\n")
    def show_all(self):
        with open('book_list.txt', 'r+') as f:
            obj = f.readlines()
            if len(obj)==0:
                print('There is no book!')
            else:
                print('There are',len(obj)//5, 'books!\n',"*"*50)
                f.seek(0)
                for index, line in enumerate(f):
                    if index>=0:
                        print(line)
    def  show_book(self):
        id = input("Please enter ID: \n")
        print('*'*50)
        with open('book_list.txt', 'r+') as f:
            obj = f.readlines()
        for i in range(0, len(obj), 5):
            search = obj[i].split(':')[1].strip()
            if id == search:
                index = search
                index = i
                with open('book_list.txt', 'r+') as f:
                    for index_of_line, line in enumerate(f):
                        if index_of_line in range(index,index+5):
                            print(line)
    def remove_book(self):
        remove_id = input('Please enter ID: \n')
        with open('book_list.txt', 'r+') as f:
            obj = f.readlines()
            f.seek(0)
            for i in range(0, len(obj), 5):
                index = obj[i].split(':')[1].strip()
                if remove_id == index:
                    index_each_line = i
                    f.truncate()
                    for i in range(len(obj)):
                        if i not in range(index_each_line,index_each_line+5):
                            f.write(obj[i])
                    print('\nSuccesfully deleted!\n')
                    break
            else:
                print('\nID does not exist!\n')
book = Book()
if len(command) == 2 and command[1] == 'add':
    book.set_id()
    book.add_book()
    book.set_date()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'all':
    book.show_all()
elif len(command) == 3 and command[1] == 'show' and command[2] == 'book':
    book. show_book()
elif len(command) == 2 and command[1] == 'remove':
    book.remove_book()
else:
    print('Please, enter right input:)')