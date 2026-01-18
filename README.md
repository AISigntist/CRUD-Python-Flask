# Python Flask Blog Application

A simple blog application built with Flask, Bootstrap, and SQLite. This tutorial application progressively builds features across multiple lesson files.

## Features

- Display a list of blog posts
- View individual blog post details
- Filter blogs by category
- Add new blog posts
- Edit existing blog posts
- Delete blog posts
- Modern, responsive design using Bootstrap 5
- Clean header with gradient background
- Card-based blog layout with hover effects
- Jinja2 templating for dynamic content
- SQLite database integration

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Navigate to the project directory:**
   ```bash
   cd tutorials/python-flask
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   ```bash
   cd data
   python create_database.py
   cd ..
   ```
   
   This will create the SQLite database (`blog.db`) and populate it with sample blog data.

## Running the Application

The project includes multiple lesson files that progressively build the application:

### Lesson 4 - Basic blog listing
```bash
python lesson4.py
```

### Lesson 5 - Blog listing with static data and detail views
```bash
python lesson5.py
```

### Lesson 6 - Full CRUD application with database (Recommended)
```bash
python lesson6.py
```

After running any of the lesson files, the application will be available at:
- **URL:** `http://localhost:5000`

The application runs in debug mode, so changes to code will automatically reload the server.

## Usage

### Lesson 6 - Full Application Routes

- **`/blogs`** - Displays the list of all blog posts
- **`/blog/<id>`** - View details of a specific blog post (e.g., `/blog/1`)
- **`/blog/category/<category>`** - Filter and display blogs by category (e.g., `/blog/category/Python`)
- **`/add_post`** - Add a new blog post (GET: form, POST: submit)
- **`/edit_post/<id>`** - Edit an existing blog post (GET: form, POST: submit)
- **`/delete_post/<id>`** - Delete a blog post

### Adding a Blog Post

1. Navigate to `http://localhost:5000/add_post`
2. Fill in the form with:
   - Title
   - Author
   - Date (format: YYYY-MM-DD)
   - Category
   - Excerpt
3. Click "Add Post"

### Editing a Blog Post

1. Click "Edit" on any blog post card
2. Or navigate to `http://localhost:5000/edit_post/<id>`
3. Modify the fields
4. Click "Update Post"

### Deleting a Blog Post

1. Click "Delete" on any blog post card
2. Or navigate to `http://localhost:5000/delete_post/<id>`

## Project Structure

```
python-flask/
├── lesson1.py              # Basic Flask setup
├── lesson2.py              # First route
├── lesson3.py              # Multiple routes
├── lesson4.py              # Template rendering with static data
├── lesson5.py              # Dynamic routes and blog details
├── lesson6.py              # Full CRUD application with database
├── data/
│   ├── __init__.py
│   ├── blogs.py            # Static blog data (list)
│   ├── db.py               # Database functions (CRUD operations)
│   ├── create_database.py  # Script to initialize database
│   └── blog.db             # SQLite database file
├── templates/
│   ├── layout.html         # Base template
│   ├── index.html          # Home page
│   ├── blogs.html          # Blog listing page
│   ├── blog.html           # Individual blog post view
│   ├── add_post.html       # Add blog post form
│   ├── edit_post.html      # Edit blog post form
│   ├── static-blogs.html   # Static blog listing (lesson 4)
│   └── 404.html            # 404 error page
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Dependencies

- **Flask 3.0.0** - Web framework
- **Werkzeug 3.0.1** - WSGI utilities (included with Flask)

## Database

The application uses SQLite for data persistence. The database file (`blog.db`) is located in the `data/` directory.

To reset the database with sample data:
```bash
cd data
python create_database.py
cd ..
```

## Troubleshooting

### ModuleNotFoundError
If you encounter import errors, make sure you're running the script from the `python-flask` directory:
```bash
cd tutorials/python-flask
python lesson6.py
```

### Database not found
If you see database-related errors, run the database initialization script:
```bash
cd data
python create_database.py
cd ..
```

### Port already in use
If port 5000 is already in use, you can change it in the lesson files:
```python
app.run(debug=True, port=5001)
```
