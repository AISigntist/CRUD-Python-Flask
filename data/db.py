"""
Database module to read blog data from SQLite database
"""

import sqlite3
import os


def get_db_path():
    """Get the path to the SQLite database file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'blog.db')


def get_blogs():
    """
    Fetch all blogs from the SQLite database
    Returns a list of dictionaries with blog data
    """
    db_path = get_db_path()
    
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found: {db_path}")
    
    conn = sqlite3.connect(db_path)
    # Set row_factory to return rows as dictionaries
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Fetch all blogs
    cursor.execute('SELECT * FROM blogs ORDER BY id')
    rows = cursor.fetchall()
    
    # Convert rows to list of dictionaries
    blogs = []
    for row in rows:
        blogs.append({
            'id': row['id'],
            'title': row['title'],
            'author': row['author'],
            'date': row['date'],
            'excerpt': row['excerpt'],
            'category': row['category']
        })
    
    conn.close()
    return blogs


def get_blog_by_id(blog_id):
    """
    Fetch a single blog by ID from the SQLite database
    Returns a dictionary with blog data or None if not found
    """
    db_path = get_db_path()
    
    if not os.path.exists(db_path):
        return None
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return {
            'id': row['id'],
            'title': row['title'],
            'author': row['author'],
            'date': row['date'],
            'excerpt': row['excerpt'],
            'category': row['category']
        }
    return None


def get_blogs_by_category(category):
    """
    Fetch all blogs by category from the SQLite database
    Returns a list of dictionaries with blog data
    """
    db_path = get_db_path()
    
    if not os.path.exists(db_path):
        return []
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM blogs WHERE category = ? ORDER BY id', (category,))
    rows = cursor.fetchall()
    
    blogs = []
    for row in rows:
        blogs.append({
            'id': row['id'],
            'title': row['title'],
            'author': row['author'],
            'date': row['date'],
            'excerpt': row['excerpt'],
            'category': row['category']
        })
    
    conn.close()
    return blogs

def add_blog(blog):
    """
    Add a new blog to the SQLite database
    Returns the ID of the new blog or None if failed
    """
    db_path = get_db_path()
    if not os.path.exists(db_path):
        return None
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO blogs (title, author, date, excerpt, category) VALUES (?, ?, ?, ?, ?)', (blog['title'], blog['author'], blog['date'], blog['excerpt'], blog['category']))
    conn.commit()
    return cursor.lastrowid
    conn.close()
    return None

def edit_blog(id, blog):
    """
    Edit a blog in the SQLite database
    Returns True if successful, False if failed
    """
    db_path = get_db_path()
    if not os.path.exists(db_path):
        return False
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE blogs SET title = ?, author = ?, date = ?, excerpt = ?, category = ? WHERE id = ?', (blog['title'], blog['author'], blog['date'], blog['excerpt'], blog['category'], id))
    conn.commit()
    return True

def delete_blog(id):
    """
    Delete a blog from the SQLite database
    Returns True if successful, False if failed
    """
    db_path = get_db_path()
    if not os.path.exists(db_path):
        return False
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM blogs WHERE id = ?', (id,))
    conn.commit()
    return True
    conn.close()
    return False