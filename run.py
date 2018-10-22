import os
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("{}".format(request.form["answer"]))
    return render_template("home.html", active_page='index')

@app.route('/about')
def about():
    return render_template("about.html", active_page='about')

if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

