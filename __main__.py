import csv, getpass, sys
from time import sleep
from os import system, name
from tabulate import tabulate

def reg_login():
    try:
        users_data_file = open("users_data.csv", 'r')
        users_data_file.close()
    except FileNotFoundError:
        users_data = open("users_data.csv", 'w', newline='')
        users_data_writer = csv.writer(users_data, delimiter=',')
        users_data_writer.writerow(['Username', 'Password'])
        print("Please create an account.")
        uname = input("Please choose an username\n:: ")
        pword = getpass.getpass("Please choose a password for your account\n:: ")
        record = [uname, pword]
        users_data_writer.writerow(record)

        lib_file_name = uname + ".csv"
        lib_file = open(lib_file_name, 'w', newline='')
        lib_file_writer = csv.writer(lib_file, delimiter=',')
        lib_file_writer.writerow(['Title','Author','Genre','Status'])
        lib_file.close()

def existing_up():
    global unames, pwords, users_data_writer, users_data_reader
    users_data_file = open("users_data.csv", 'r')
    users_data_reader = csv.reader(users_data_file)
    users_data_writer = csv.writer(users_data_file)
    unames = []
    pwords = []

    for row in users_data_reader:
        unames.append(row[0])
        pwords.append(row[1])

def user_reg():
    print("Please create an account.")
    uname = input("Please choose an username\n:: ")
    while uname in unames:
        print("Please select a different username.")
        uname = input("Please choose an username\n:: ")
    pword = getpass.getpass("Please choose a password for your account\n:: ")
    record = [uname, pword]
    users_data_writer.writerow(record)

    lib_file_name = uname + ".csv"
    lib_file = open(lib_file_name, 'w')
    lib_file_writer = csv.writer(lib_file, delimiter=',')
    lib_file_writer.writerow(['Title','Author','Genre','Status'])
    lib_file.close()

def login():
    print("================== login ==================")
    attempts = 0
    while attempts <= 3:
        attempts += 1
        print("Enter your login details below.")
        uname = input("Please enter your username\n:: ")
        if uname in unames:
            pword = getpass.getpass("Please enter your password\n:: ")
            if pword == pwords[unames.index(uname)]:
                global name_of_user
                name_of_user = uname
                print("================== successful ==================")
                print("Welcome!")
                break
            else:
                print("Wrong password. Please try again.")
        else:
            print("Wrong username.")
    else:
        print("3 unsuccessful attempts to login. Please try again later.")

def add_book():
    file_user = open(user_file_name, 'a', newline = '')
    file_user_writer = csv.writer(file_user, delimiter = ',')
    book_title = input("Name of book: ")
    book_author = input("Name of author: ")
    book_genre = input("Genre of the book: ")
    book_status_num = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read\nstatus: ")
    book_status = ''
    while True:
        if book_status_num == '1':
            book_status = 'Read'
            break
        elif book_status_num == '2':
            book_status = 'Reading'
            break
        elif book_status_num == '3':
            book_status = 'To-Be Read'
            break
        else:
            print("Enter valid number.")
            book_status_num == 'not-set'
    add_book = [book_title, book_author, book_genre, book_status]
    file_user_writer.writerow(add_book)
    file_user.close()

def search_book(search_book):
    global book_exists
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    for row in file_user_reader:
        if search_book == row[0]:
            print(row)
            book_exists = True
            break
    else:
        print("No such book found!")
        book_exists = False
    file_user.close()

def del_book(mod_book):
    search_book(mod_book)
    file_user = open(user_file_name, 'r')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    if book_exists:
        records = []
        for row in file_user_reader:
            if row[0] == mod_book:
                continue
            else:
                records.append(row)
        file_user.close()
        file_user = open(user_file_name, 'w', newline = '')
        file_user_writer = csv.writer(file_user, delimiter = ',')
        file_user_writer.writerows(records)
        file_user.close()
    

def update_book(mod_book):
   # del_book(mod_book)
   # if book_exists:
   #     add_book()
    search_book(mod_book)
    if book_exists:
        file_user = open(user_file_name, 'a+', newline = '')
        file_user_reader = csv.reader(file_user, delimiter = ',')
        file_user_writer = csv.writer(file_user, delimiter = ',')
        for book in file_user_reader:
            if book[0] == mod_book:
                row = book
        to_update = int(input("0.Exit 1.Title 2.Author 3.Genre 4.Status: "))        
        if to_update == 0:
            return
        elif to_update == 1:
            new_title = input("new title: ")
            row[0] = new_title
            print(row)
            file_user_writer.writerow(row)
            file_user.close()
            return 
        elif to_update == 2:
            new_auth = input("new author name: ")
            row[1] = new_auth
            print(row)
            file_user_writer.writerow(row)
            file_user.close()
            return
        elif to_update == 3:
            new_genre = input("new genre: ")
            row[2] = new_genre
            print(row)
            file_user_writer.writerow(row)
            file_user.close()
            return
        elif to_update == 4:
            new_book_status_num = input("Enter your choice:\n1. Read 2. Reading 3. To-Be Read\nstatus: ")
            while True:
                if new_book_status_num == '1':
                    book_status = 'Read'
                    break
                elif new_book_status_num == '2':
                    book_status = 'Reading'
                    break
                elif new_book_status_num == '3':
                    book_status = 'To-Be Read'
                    break
                else:
                    print("Enter valid number.")
                    new_book_status_num == 'not-set'
            row[3] = book_status
            print(row)
            file_user_writer.writerow(row)
            file_user.close()
            return


def data_print():
    file_user = open(user_file_name, 'r', newline = '')
    file_user_reader = csv.reader(file_user, delimiter = ',')
    data = []
    for row in file_user_reader:
        data.append(row)
    header = data.pop(0)
    print(tabulate(data, header, tablefmt = "pretty"))
    file_user.close()


def welcome():
    print("================== MANLIB ==================")
    reg_login()
    existing_up()
    cred = ' '
    while True:
        cred = int(input("0. Exit 1.Login 2.New account: "))
        if cred == 0:
            print("So long!")
            sys.exit()
        elif cred == 1:
            login()
            global user_file_name, name_of_user
            user_file_name = name_of_user + '.csv'         
            break
        elif cred == 2:
            user_reg()
            print("Please login after creating account.")

def clear():
        # for windows 
    if name == 'nt': 
        _ = system('cls')  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def progress():
    loaded = 0
    total = 100
    while loaded <= 100:
        clear()
        print("================== MANLIB ==================")
        print(loaded,"%")
        bar = str("[" + "="*loaded + "-"*(total - loaded) + "]")
        print(bar)
        sleep(1)
        loaded += 10
    else:
        clear()
        return

def splash_screen():
    print("================== MANLIB ==================")
    progress()
    clear()

clear()
user_file_name = ' '
name_of_user = ''
#splash_screen()
welcome()
book_exists = ''

while True:
    try:
        print("==================")
        crud = int(input("Please select:\n\t0. Exit\n\t1. Create\n\t2. Search\n\t3. Update\n\t4. Delete\n\t5. Entire library\nchoice: "))
        if crud == 0:
            print("So long..!\n==================")
            break
        elif crud == 1:
            add_book()
        elif crud == 2:
            book_to_search = input("Enter name of book to search for: ")
            search_book(book_to_search)
        elif crud == 3:
            book_to_update = input("Enter name of book to update: ")
            update_book(book_to_update)
            #file_user = open(user_file_name, 'a', newline = '')
            #file_user_writer = csv.writer(file_user, delimiter = ',')
            #file_user_writer.writerow(update_book(book_to_update))
            #file_user.close()
            del_book(book_to_update)
        elif crud == 4:
            book_to_delete = input("Enter name of book to delete: ")
            del_book(book_to_delete)
        elif crud == 5:
            data_print()
        else:
            print("Invalid choice.")
            print("==================")
        sleep(2)
    except: #Exception as e
        #print("error: {}".format(e))
        print("except Invalid choice.")
        #clear()