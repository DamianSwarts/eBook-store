import sqlite3

# Create a database and connect to it
connection = sqlite3.connect('ebookstore.db')
cursor = connection.cursor()

# Create the books table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS books
  (id INTEGER PRIMARY KEY,
  title TEXT,
  author TEXT,
  qty INTEGER)''')

# Populate the table with initial values
books = [
  (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
  (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
  (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
  (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
  (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]
cursor.executemany('INSERT OR IGNORE INTO books VALUES (?,?,?,?)', books)

# Function to add a new book to the database
def add_book():
    book_id = int(input("Enter book ID: "))
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book_qty = int(input("Enter book quantity: "))
    cursor.execute('INSERT INTO books VALUES (?,?,?,?)', (book_id, book_title, book_author, book_qty))
    connection.commit()
    print("\nBook added successfully!\n")

# Function to update book information
def update_book():
    book_id = int(input("Enter book ID to update: "))
    book_qty = int(input("Enter new quantity: "))
    cursor.execute('UPDATE books SET qty=? WHERE id=?', (book_qty, book_id))
    connection.commit()
    print("\nBook updated successfully!\n")

# Function to delete a book from the database
def delete_book():
    book_id = int(input("Enter book ID to delete: "))
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    connection.commit()
    print("\nBook deleted successfully!\n")

# Function to search for a specific book
def search_books():
    keyword = input("\nEnter book title or author to search: \n")
    cursor.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?', ('%'+keyword+'%', '%'+keyword+'%'))
    results = cursor.fetchall()
    if results:
        print("\nSearch results:\n")
        for row in results:
            print(row, "\n")
    else:
        print("\nNo matching books found.\n")

# Define a function to display the menu
def display_menu():
    print('''Please choose an option from the menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit''')

# Define a main function
def main():
    print("\nWelcome to the bookstore program!\n")
    # Display the menu
    display_menu()
    user_option = ""
    while True:
        try:
            # Prompt the user for an option
            user_option = int(input("Enter your option: "))
            break
        except ValueError:
            print('''\nPlease note that you can only enter the number of the option you select.
Not a symbol, letter, word or sentence.\n''')
            display_menu()

    # Loop until the user chooses to exit
    while user_option != 0:
        # Perform the corresponding function based on the option
        if user_option == 1:
            add_book()
        elif user_option == 2:
            update_book()
        elif user_option == 3:
            delete_book()
        elif user_option == 4:
            search_books()
        else:
            print("\nThe option you selected is not listed in the menu! Please try again.\n")
        # Display the menu again
        display_menu()
        # Prompt the user for another option
        user_option = int(input("Enter your option: "))   
    # Close the database connection
    connection.close()
    # Print a farewell message
    print("\nThank you for using the bookstore program. Goodbye!\n")

# Call the main function
if __name__ == "__main__":
    main()