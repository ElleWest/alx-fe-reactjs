import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None

def list_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None

def retrieve_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None

if __name__ == "__main__":
    # Sample usage
    print("=== Sample Queries ===")
    
    # Create sample data if it doesn't exist
    author, created = Author.objects.get_or_create(name="J.K. Rowling")
    book1, created = Book.objects.get_or_create(title="Harry Potter and the Philosopher's Stone", author=author)
    book2, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author)
    
    library, created = Library.objects.get_or_create(name="Central Library")
    library.books.add(book1, book2)
    
    librarian, created = Librarian.objects.get_or_create(name="John Smith", library=library)
    
    # Run sample queries
    print("\n1. Query all books by a specific author:")
    query_books_by_author("J.K. Rowling")
    
    print("\n2. List all books in a library:")
    list_books_in_library("Central Library")
    
    print("\n3. Retrieve the librarian for a library:")
    retrieve_librarian_for_library("Central Library")