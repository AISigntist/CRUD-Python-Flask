from flask import Flask, render_template
from data.blogs import get_blogs
from data.db import get_blogs, get_blog_by_id, get_blogs_by_category, add_blog, edit_blog, delete_blog

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static-blogs')
def static_blogs():
    """Display the list of blogs on the main page"""
    return render_template('static-blogs.html', blogs=get_blogs())

@app.route('/blogs')
def blogs():
    """Display the list of blogs on the main page"""
    return render_template('blogs.html', blogs=get_blogs())


if __name__ == '__main__':
    app.run(debug=True)
