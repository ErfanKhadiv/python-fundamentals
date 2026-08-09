import os
import json



def load_books():
    if os.path.exists("books.json"):
        try:
            with open("books.json", 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_books(books):
    with open("books.json", 'w') as file:
        json.dump(books, file, indent=4)


def get_menu_input(num1, num2):
    while True:
        try:
            choose = int(input("Choose: "))
            if num1 <= choose <= num2:
                return choose
            else:
                print(f"ENTER A NUMBER BETWEEN {num1} AND {num2}!")
        except ValueError:
            print("INVALID INPUT!")


def get_non_empty_input(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("INPUT CANNOT BE EMPTY!")


def books_not_empty(books):
    if books:
        return True
    print("NO BOOK TO SHOW!")
    return False


def check_book_exists(title, books):
    if books:
        for book in books:
            if book["title"] == title:
                return True
    return False


def add_book(title, pages, author, category, status, books):
    book = {
        "title": title,
        "pages": pages,
        "author": author,
        "category": category,
        "status": status
    }
    books.append(book)


def get_all_books(books):
    books_list = []
    for book in books:
        books_list.append(book)
    return books_list


def search_book(search_input, method, books):
    books_found = []
    for book in books:
        if book[method] == search_input:
            books_found.append(book)
    return books_found


def show_books(book_list):
    for i, book in enumerate(book_list, start=1):
        print(
            f"{i}. Title: {book['title'].capitalize()}\n"
            f"   Pages: {book['pages']}\n"
            f"   Author: {book['author'].capitalize()}\n"
            f"   Category: {book['category'].capitalize()}\n"
            f"   Status: {book['status'].capitalize()}\n"
        )


def available_books(books):
    available_books_list = []
    for book in books:
        if book["status"] == "available":
            available_books_list.append(book)
    return available_books_list


def borrowed_books(books):
    borrowed_books_list = []
    for book in books:
        if book["status"] == "borrowed":
            borrowed_books_list.append(book)
    return borrowed_books_list


def borrow_book(available_list, book_title):
    for book in available_list:
        if book["title"] == book_title:
            book["status"] = "borrowed"
            return True
    return False


def return_book(borrowed_list, book_title):
    for book in borrowed_list:
        if book["title"] == book_title:
            book["status"] = "available"
            return True
    return False


def delete_book(book_title, books):
        for i, book in enumerate(books, start=0):
            if book['title'] == book_title:
                books.pop(i)
                return True
        return False



books = load_books()
while True:
    print("""
    ###### Library Management System ######
    
    1. Add Book
    2. Show Books
    3. Search Book
    4. Borrow Book
    5. Return Book
    6. Delete Book
    7. Exit
    """)

    choose_menu = get_menu_input(1, 7)

    if choose_menu == 1:
        print("\n$$$$$$ ADD BOOK $$$$$$\n")
        while True:
            book_title = get_non_empty_input("Enter book title: ").lower()
            if check_book_exists(book_title, books):
                print("BOOK ALREADY EXISTS!")
                continue
            break
        while True:
            book_pages = get_non_empty_input("Enter number of pages: ")
            if book_pages.isdigit():
                book_pages = int(book_pages)
                break
            else:
                print("PAGE NUMBER SHOULD BE A DIGIT!")
        book_author = get_non_empty_input("Enter book author: ").lower()
        book_category = get_non_empty_input("Enter book category: ").lower()
        while True:
            book_status = get_non_empty_input("Is it available(Y/N): ").upper()
            if book_status in ['Y', 'N']:
                if book_status == 'Y':
                    book_status = "available"
                else:
                    book_status = "borrowed"
                break
            else:
                print("ENTER (Y) for YES and (N) for NO!")
        add_book(book_title,book_pages, book_author,
                 book_category, book_status, books)
        save_books(books)
        print("BOOK ADDED!")
        print("$$$$$$$$$$$$$$$$$$$$$$")

    elif choose_menu == 2:
        if books_not_empty(books):
            print("$$$$$$ BOOKS $$$$$$\n")
            show_books(books)
            print("$$$$$$$$$$$$$$$$$$$")

    elif choose_menu == 3:
        if books_not_empty(books):
            print("\n$$$$$$ SEARCH BOOKS $$$$$$\n")
            print("1. Search by book title\n"
                  "2. Search by book author\n"
                  "3. Search by book category\n")
            search_method = get_menu_input(1, 3)
            if search_method == 1:
                method = "title"
            elif search_method == 2:
                method = "author"
            else:
                method = "category"
            search_input = get_non_empty_input(f"Enter book {method}: ").lower()
            search_result = search_book(search_input, method, books)
            if search_result:
                print("\n$$$$$$ BOOKS FOUND $$$$$$\n")
                show_books(search_result)
                print("$$$$$$$$$$$$$$$$$$$$$$$$$")
            else:
                print("NO BOOKS FOUND!")

    elif choose_menu == 4:
        if books_not_empty(books):
            available_books_list = available_books(books)
            if available_books_list:
                print("$$$$$$ AVAILABLE BOOKS TO BORROW $$$$$$")
                show_books(available_books_list)
                book_to_borrow = get_non_empty_input("Enter book title to borrow: ").lower()
                if check_book_exists(book_to_borrow, books):
                    if borrow_book(available_books_list, book_to_borrow):
                        print("BOOK SUCCESSFULLY BORROWED!")
                        save_books(books)
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    else:
                        print("BOOK IS NOT AVAILABLE!")
                else:
                    print("BOOK DOESN'T EXISTS!")
            else:
                print("NO BOOKS ARE AVAILABLE")

    elif choose_menu == 5:
        if books_not_empty(books):
            borrowed_books_list = borrowed_books(books)
            if borrowed_books_list:
                print("$$$$$$ BORROWED BOOKS TO RETURN $$$$$$")
                show_books(borrowed_books_list)
                book_to_return = get_non_empty_input("Enter book title to return: ").lower()
                if check_book_exists(book_to_return, books):
                    if return_book(borrowed_books_list, book_to_return):
                        print("BOOK SUCCESSFULLY RETURNED!")
                        save_books(books)
                        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    else:
                        print("BOOK IS NOT BORROWED!")
                else:
                    print("BOOK DOESN'T EXISTS!")
            else:
                print("NO BOOKS ARE BORROWED")

    elif choose_menu == 6:
        if books_not_empty(books):
            print("$$$$$$ DELETE BOOK $$$$$$")
            book_to_delete = get_non_empty_input("Enter book title to delete: ").lower()
            if check_book_exists(book_to_delete, books):
                if delete_book(book_to_delete, books):
                    save_books(books)
                    print("BOOK DELETED!")
                else:
                    print("ERROR!")
            else:
                print("BOOK DOESN'T EXISTS!")

    elif choose_menu == 7:
        print("###### HAVE A NICE DAY! #######")
        break
    else:
        print("INVALID INPUT!")
