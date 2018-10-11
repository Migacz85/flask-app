import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html", active_page='index')

@app.route('/about')
def about():
    return render_template("about.html", active_page='about')

@app.route('/contact')
def contact():
    return render_template("contact.html", active_page='contact')

if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)