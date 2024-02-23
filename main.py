from flask import Flask, url_for, request,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)


@app.route('/login')
def login():
    return 'login'

@app.route('/')
def index():
    return 'index'

# @app.route('/<name>')
# def hi(name):
#     return f'HEllo, {escape(name)}!'

@app.route('/user/<username>')
def profile(username):
    return f'{username}`s profile'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return f'Post {escape(post_id)}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def show_projects():
#     return 'The project X'

@app.route('/about')
def about():
    return 'About the page'

# @app.route('/login')
# def logi_get():
#     return show_the_login_form()

# @app.route('/login')
# def logi_post():
#     return do_the_login()

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='usr'))
    # print(url_for('static', filename='style.css'))