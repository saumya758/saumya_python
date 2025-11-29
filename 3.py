import re

books = {}
book_ids = set()

def add_book():
    book_id = input("Enter Book ID: ")
    if book_id in book_ids:
        print("Duplicate ID not allowed!")
        return
    
    name = input("Book Name: ")
    author = input("Author: ")
    category = input("Category: ")

    books[book_id] = {
        "name": name,
        "author": author,
        "category": category
    }
    book_ids.add(book_id)
    print("Book Added!")

def search_book():
    key = input("Enter keyword/regex: ")
    pattern = re.compile(key)

    for bid, info in books.items():
        if pattern.search(info["name"]) or pattern.search(info["author"]):
            print(bid, info)

def update_delete():
    bid = input("Enter Book ID: ")
    if bid not in books:
        print("Not found!")
        return
    
    ch = input("1-Update  2-Delete: ")
    if ch == "1":
        books[bid]["name"] = input("New Name: ")
        books[bid]["author"] = input("New Author: ")
        books[bid]["category"] = input("New Category: ")
        print("Updated!")
    else:
        del books[bid]
        book_ids.remove(bid)
        print("Deleted!")

def save_to_file():
    with open("library.txt", "w") as f:
        for bid, info in books.items():
            f.write(f"{bid},{info['name']},{info['author']},{info['category']}\n")

def read_file():
    with open("library.txt", "r") as f:
        for line in f:
            print(line.strip())
