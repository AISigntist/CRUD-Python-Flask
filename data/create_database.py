"""
Script to create SQLite database from blogs.py data
"""

import sqlite3
import os
from blogs import get_blogs

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'blog.db')

def create_database():
    """Create SQLite database and populate it with blog data"""
    
    # Remove existing database if it exists
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")
    
    # Connect to SQLite database (creates if doesn't exist)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create blogs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            date TEXT NOT NULL,
            excerpt TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    
    # Get blog data
    blogs = get_blogs()
    
    # Insert blog data
    for blog in blogs:
        cursor.execute('''
            INSERT INTO blogs (id, title, author, date, excerpt, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            blog['id'],
            blog['title'],
            blog['author'],
            blog['date'],
            blog['excerpt'],
            blog['category']
        ))
    
    # Commit changes
    conn.commit()
    
    # Verify data
    cursor.execute('SELECT COUNT(*) FROM blogs')
    count = cursor.fetchone()[0]
    
    print(f"Database created successfully: {DB_PATH}")
    print(f"Total blogs inserted: {count}")
    
    # Show sample data
    cursor.execute('SELECT id, title, category FROM blogs LIMIT 5')
    print("\nSample data:")
    for row in cursor.fetchall():
        print(f"  ID: {row[0]}, Title: {row[1]}, Category: {row[2]}")
    
    # Close connection
    conn.close()
    
    return DB_PATH

if __name__ == '__main__':
    db_path = create_database()
    print(f"\nDatabase file location: {db_path}")
