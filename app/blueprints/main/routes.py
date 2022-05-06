from flask import render_template, current_app as app

# MAIN ROUTES
@app.route('/')
def home():
    return render_template('main/home.html')

@app.route('/contact')
def contact():
    return render_template('main/contact.html')

@app.route('/about')
def about():
    return render_template('main/about.html')

@app.route('/register')
def register():
    return render_template('register/register.html')

@app.route('/login')
def login():
    return render_template('register/login.html')