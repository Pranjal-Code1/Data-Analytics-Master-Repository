import json
import random 
import string 
from pathlib import Path
from datetime import datetime


class Library:
    BASE_DIR = Path(__file__).resolve().parent
    database = BASE_DIR / "library.json"
    
    data = {"books": [], "members": []}

    # Load existing data to JSON or create your JSON file safely
    if database.exists():
        with open(database, "r") as f:
            content = f.read().strip()
            if content:
                data = json.loads(content)
    else:
        with open(database, 'w') as f:
            json.dump(data, f, indent=4)
    

    def gen_id(self, Prefix="B"):
        random_id = ""
        for i in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)
        return Prefix + "-" + random_id
    
    @classmethod
    def save_data(cls):
        with open(cls.database, 'w') as f:
            json.dump(cls.data, f, indent=4, default=str)

    def add_book(self):
        title = input("Enter book title : ")
        author = input("Enter the book author : ")
        copies = int(input("how many copies : "))

        book = {
            "id" : self.gen_id("B"),
            "title" : title,
            "author" : author,
            "total_copies": copies,
            "available_copies" : copies,
            "added_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Library.data['books'].append(book)
        Library.save_data()
        print("Book added successfully")

    def list_books(self):
        if not Library.data['books']:
            print("sorry no books found")
            return
        for b in Library.data['books']:
            print(f"{b['id']:12} {b['title'][:24]:25} {b['author'][:19]:20} {b['total_copies']}/{b['available_copies']:>3}")
        print()
    
    def add_member(self):
        name = input("Enter the name :- ")
        email = input("please enter the email: ")

        member = {
            "id" : self.gen_id("M"),
            "name" : name,
            "email": email,
            "borowed": []
        }

        Library.data['members'].append(member)
        Library.save_data()
        print("Member added successfully")

    def list_members(self):
        if not Library.data['members']:
            print("there are no members")
            return 
        for m in Library.data['members']:
            print(f"{m['id']:12} {m['name'][:24]:25} {m['email'][:29]:30}")
            print("this guy has currently ")
            print(f"{m['borowed']}")
        print()
    
    def borrow(self):
        member_id = input("Enter the member ID : ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("no such Id exist")
            return 
        member = members[0]

        book_id = input("enter the book id : ").strip()
        books = [b for b in Library.data['books'] if b['id'] == book_id]

        if not books:
            print("sorry no such id of book exist")
            return 
        book = books[0]
    
        if book['available_copies'] <= 0:
            print("sorry no copies available")
            return 
        
        borrow_entry = {
            "book_id" : book['id'],
            "title" : book['title'],
            "borrow_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        member['borowed'].append(borrow_entry)
        book['available_copies'] -= 1 
        Library.save_data()
        print("Book borrowed successfully")
    
    def return_book(self):
        member_id = input("Enter the member ID : ").strip()
        members = [m for m in Library.data['members'] if m['id'] == member_id]
        if not members:
            print("no such Id exist")
            return 
        
        member = members[0]

        if not member['borowed']:
            print("no borrowed books")
            return 
        
        print("borrowed books:")
        for i, b in enumerate(member['borowed'], start=1):
            print(f"{i}. {b['title']} ({b['book_id']})")
        
        try:
            choice = int(input("enter number to return : - "))
            selected = member['borowed'].pop(choice - 1)
        except Exception as err:
            print("invalid value ")
            return 
        
        books = [bk for bk in Library.data['books'] if bk['id'] == selected['book_id']]
        if books:
            books[0]['available_copies'] += 1
        
        Library.save_data()
        print("Book returned successfully")

    @classmethod
    def clear_database(cls):
        cls.data = {"books": [], "members": []}
        cls.save_data()
        print("All data has been completely cleared!")


library_system = Library()

while True:
    print("="*50)
    print("Library Management System")
    print("="*50)
    print("1. Add Book")
    print("2. List Books")
    print("3. Add Members")
    print("4. List members")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Clear Database")
    print("0. Exit the portal")
    print("-"*50)

    choice = input("What task you want to do: ").strip()

    if choice == "1":
        library_system.add_book()

    elif choice == "2":
        library_system.list_books()

    elif choice == "3":
        library_system.add_member()

    elif choice == "4":
        library_system.list_members()

    elif choice == "5":
        library_system.borrow()

    elif choice == "6":
        library_system.return_book()
    
    elif choice == "7":
        library_system.clear_database()
    
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")