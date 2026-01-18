from flask import Flask, render_template, url_for, redirect
from data.blogs import get_blogs

app = Flask(__name__)


@app.route('/')
def index():
    """Redirect root URL to /blogs"""
    return redirect(url_for('blogs'))


@app.route('/blogs')
def blogs():
    """Display the list of blogs on the main page"""
    return render_template('blogs.html', blogs=get_blogs())


@app.route('/blog/<int:id>')
def blog(id):
    """Display the details of a blog post"""
    blog = next((blog for blog in get_blogs() if blog['id'] == id), None)
    if not blog:
        return render_template('404.html'), 404
    return render_template('blog.html', blog=blog)

@app.route('/blog/category/<string:category>')
def blog_category(category):
    """Display the list of blogs by category"""
    blogs = [blog for blog in get_blogs() if blog['category'] == category]
    if not blogs:
        return render_template('404.html'), 404
    return render_template('blogs.html', blogs=blogs, category=category)

if __name__ == '__main__':
    app.run(debug=True)
