import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    A script to demonstrate Django ORM queries.
    """
    # Create instances
    author1, _ = Author.objects.get_or_create(name='George Orwell')
    author2, _ = Author.objects.get_or_create(name='J.R.R. Tolkien')

    book1, _ = Book.objects.get_or_create(title='1984', author=author1, publication_year=1949)
    book2, _ = Book.objects.get_or_create(title='Animal Farm', author=author1, publication_year=1945)
    book3, _ = Book.objects.get_or_create(title='The Hobbit', author=author2, publication_year=1937)

    library1, _ = Library.objects.get_or_create(name='Central Library')
    library1.books.add(book1, book2, book3)

    librarian1, _ = Librarian.objects.get_or_create(name='Mr. Smith', library=library1)

    print("--- Queries ---")

    # Query all books by a specific author (George Orwell)
    print("\n1. Books by George Orwell:")
    orwell_books = Book.objects.filter(author__name='George Orwell')
    for book in orwell_books:
        print(f"- {book.title}")

    # Query all books in a specific library (Central Library)
    print("\n2. Books in Central Library:")
    central_library_books = Library.objects.get(name='Central Library').books.all()
    for book in central_library_books:
        print(f"- {book.title}")

    # Retrieve the librarian for a specific library (Central Library)
    print("\n3. Librarian for Central Library:")
    librarian = Librarian.objects.get(library__name='Central Library')
    print(f"- {librarian.name}")

if __name__ == '__main__':
    run_queries()
