from flask import Flask, render_template, url_for, request, redirect, flash
from data.db import get_blogs, get_blog_by_id, get_blogs_by_category, add_blog, edit_blog, delete_blog

app = Flask(__name__)


@app.route('/blogs')
def blogs():
    """Display the list of blogs on the main page"""
    return render_template('blogs.html', blogs=get_blogs())


@app.route('/blog/<int:id>')
def blog(id):
    """Display the details of a blog post"""
    blog = get_blog_by_id(id)
    if not blog:
        return render_template('404.html'), 404
    return render_template('blog.html', blog=blog)

@app.route('/blog/category/<string:category>')
def blog_category(category):
    """Display the list of blogs by category"""
    blogs = get_blogs_by_category(category)
    if not blogs:
        return render_template('404.html'), 404
    return render_template('blogs.html', blogs=blogs, category=category)


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """Display the form to add a new blog post"""
    if request.method == 'POST':
        title = request.form['title']
        excerpt = request.form['excerpt']
        category = request.form['category']
        author = request.form['author']
        date = request.form['date']
        add_blog({'title': title, 'excerpt': excerpt, 'category': category, 'author': author, 'date': date})
        return redirect(url_for('blogs'))
    else:
        return render_template('add_post.html')

@app.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    """Display the form to edit a blog post"""
    blog = get_blog_by_id(id)
    if not blog:
        return render_template('404.html'), 404
    if request.method == 'POST':
        title = request.form['title']
        excerpt = request.form['excerpt']
        category = request.form['category']
        author = request.form['author']
        date = request.form['date']
        edit_blog(id, {'title': title, 'excerpt': excerpt, 'category': category, 'author': author, 'date': date})
        return redirect(url_for('blog', id=id))
    else:
        return render_template('edit_post.html', blog=blog)

@app.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    """Delete a blog post"""
    blog = get_blog_by_id(id)
    if not blog:
        return render_template('404.html'), 404
    if request.method == 'GET':
        delete_blog(id)
        #flash('Blog post deleted successfully', 'success')
        return redirect(url_for('blogs'))
    else:
        return render_template('blog.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)
