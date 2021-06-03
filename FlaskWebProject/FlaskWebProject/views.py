"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')              # These are known as decorators and cause the function below to be called whenever the link in the 
@app.route('/home')          # web page is accessed. So in this example, going to http://host/home will call the function home()
def home():
    """Renders the home page."""
    return render_template(  # Notice that title and year are being passed to the render template function so they will appear on the web page
        'index.html',        # index.html is located in the folder templates (the s is vital and is done for you)
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# If you add a Web page you start with a decorator 
# Then define a function
# This function renders a template
# It's up to you to make the template - it's best to start with a simple one like contact.html