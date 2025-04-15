
class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, genre, read_status):
        new_book = Book(title, author, year, genre, read_status)
        self.books.append(new_book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def search_book(self, search_term):
        return [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]

    def display_books(self):
        for book in self.books:
            read_status = "Read" if book.read_status else "Unread"
            print(f'Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Status: {read_status}')

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(book.read_status for book in self.books)
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        print(f'Total books: {total_books}, Percentage read: {percentage_read:.2f}%')

def main():
    library = Library()
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = int(input("Enter publication year: "))
            genre = input("Enter genre: ")
            read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
            library.add_book(title, author, year, genre, read_status)

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            search_term = input("Enter title or author to search: ")
            results = library.search_book(search_term)
            if results:
                for book in results:
                    print(f'Found: {book.title} by {book.author}')
            else:
                print("No matching books found.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            library.display_statistics()

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
