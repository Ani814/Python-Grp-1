"""
Mini-Library Management System
- Pre‑loaded with 10 books
- Add a book (title/author/year)
- View all books (title + author)
- Search by title
- Borrow a book (remove from library)
"""

library = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "year": 1847},
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]

def show_books(books):
    if not books:
        print("The library is empty.")
    else:
        for idx, book in enumerate(books, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter year: ").strip()
    library.append({"title": title, "author": author, "year": year})
    print(f"Book '{title}' added successfully!\n")

def search_book():
    query = input("Enter title to search: ").strip().lower()
    found = [b for b in library if query in b['title'].lower()]
    if found:
        print("Matching books:")
        show_books(found)
    else:
        print("No books found.")

def borrow_book():
    show_books(library)
    try:
        choice = int(input("Enter the number of the book to borrow: ")) - 1
        if 0 <= choice < len(library):
            borrowed = library.pop(choice)
            print(f"You borrowed '{borrowed['title']}'. It has been removed from the library.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    while True:
        print("\n===== Mini Library =====")
        print("1. View all books")
        print("2. Add a book")
        print("3. Search by title")
        print("4. Borrow a book (remove from library)")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_books(library)
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()