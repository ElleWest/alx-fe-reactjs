# Django Models Project

This project demonstrates advanced Django concepts including model relationships, views, authentication, and permissions.

## Project Structure

```
django-models/
├── LibraryProject/          # Main Django project
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── ...
├── relationship_app/       # Main Django app
│   ├── models.py          # Model definitions
│   ├── views.py           # View implementations
│   ├── urls.py            # App URL patterns
│   ├── query_samples.py   # Sample database queries
│   └── templates/         # HTML templates
└── manage.py              # Django management script
```

## Features Implemented

### Task 0: Advanced Model Relationships

- **Author Model**: Basic author information
- **Book Model**: Books with foreign key to Author
- **Library Model**: Libraries with many-to-many relationship to Books
- **Librarian Model**: One-to-one relationship with Library
- **UserProfile Model**: Extended user model with roles
- **Custom Permissions**: Added to Book model for access control

### Task 1: Django Views and URL Configuration

- **Function-based View**: `list_books` - displays all books
- **Class-based View**: `LibraryDetailView` - shows library details
- **URL Patterns**: Configured routing for all views
- **Templates**: HTML templates for rendering views

### Task 2: User Authentication

- **Login/Logout**: Using Django's built-in authentication views
- **Registration**: Custom registration view with UserCreationForm
- **Templates**: Authentication templates (login.html, logout.html, register.html)

### Task 3: Role-Based Access Control

- **UserProfile Model**: Extends User with role field (Admin, Librarian, Member)
- **Role-based Views**: Separate views for each user role
- **Access Control**: Using `@user_passes_test` decorator
- **Auto Profile Creation**: Django signals create UserProfile automatically

### Task 4: Custom Permissions

- **Custom Permissions**: `can_add_book`, `can_change_book`, `can_delete_book`
- **Permission-based Views**: Views protected by `@permission_required` decorator
- **Access Control**: Granular permissions for book operations

## Installation and Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ElleWest/alx-fe-reactjs.git
   cd alx-fe-reactjs/Alx_DjangoLearnLab/django-models
   ```

2. **Create and activate virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create superuser** (optional):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Available URLs

- `/books/` - List all books
- `/library/<id>/` - View library details
- `/login/` - User login
- `/logout/` - User logout
- `/register/` - User registration
- `/admin/` - Admin dashboard (Admin role required)
- `/librarian/` - Librarian dashboard (Librarian role required)
- `/member/` - Member dashboard (Member role required)
- `/add_book/` - Add new book (permission required)
- `/edit_book/<id>/` - Edit book (permission required)
- `/delete_book/<id>/` - Delete book (permission required)

### Sample Queries

Run the sample queries to test relationships:

```bash
python manage.py shell
exec(open('relationship_app/query_samples.py').read())
```

### User Roles

New users are automatically assigned the 'Member' role. To change user roles:

1. Access Django admin at `/admin/`
2. Login with superuser credentials
3. Navigate to User profiles and modify roles

## Database Relationships

- **One-to-Many**: Author → Books (One author can have many books)
- **Many-to-Many**: Library ↔ Books (Libraries can have many books, books can be in many libraries)
- **One-to-One**: Librarian ↔ Library (Each library has one librarian)
- **One-to-One**: User ↔ UserProfile (Extended user information)

## Security Features

- CSRF protection on all forms
- User authentication required for role-based views
- Permission-based access control for book operations
- Secure password handling using Django's built-in authentication

## Contributing

This project is part of the ALX Django learning curriculum. Feel free to fork and extend with additional features.
