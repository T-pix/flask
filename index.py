from flask import Flask,url_for,request,render_template
from markupsafe import escape
from datetime import datetime
app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def home():
    return render_template('initial.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prices')
def prices():
    return render_template('prices.html')



