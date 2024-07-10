# Bookstore Program

Welcome to the Bookstore Program! This simple command-line application allows you to manage a collection of books in a database. You can add new books, update existing ones, delete books, and search for specific titles or authors.

## Features

- **Add Book**: Input a book's ID, title, author, and quantity to add it to the database.
- **Update Book**: Update the quantity of an existing book by providing its ID.
- **Delete Book**: Remove a book from the database by specifying its ID.
- **Search Books**: Search for books by title or author, and view matching results.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DamianSwarts/eBook-store.git
   ```

2. **Install Dependencies (Optional)**:
   If you're using a virtual environment, activate it first. Then install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Program**:
   ```bash
   python ebook_store.py
   ```

4. **Follow the Menu**:
   - Choose an option (1-4) to perform the corresponding action.
   - To exit, enter `0`.

## Usage

- **Adding a Book**:
  - Enter the book's ID, title, author, and quantity.
  - The book will be added to the database.

- **Updating a Book**:
  - Enter the book's ID to update.
  - Provide the new quantity.
  - The book's quantity will be updated.

- **Deleting a Book**:
  - Enter the book's ID to delete.
  - The book will be removed from the database.

- **Searching for Books**:
  - Enter a keyword (title or author) to search.
  - Matching books will be displayed.

## Example

```plaintext
Welcome to the bookstore program!

Please choose an option from the menu:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit

Enter your option: 1
Enter book ID: 4001
Enter book title: The Great Gatsby
Enter book author: F. Scott Fitzgerald
Enter book quantity: 20

Book added successfully!

...

Thank you for using the bookstore program. Goodbye!
```