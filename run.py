import os
from flask import Flask, render_template, request, flash, json, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=["GET", "POST"])
def index():
    
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
    
    if request.method == "POST":
        good_answer=request.form["answer"]==questions[session['current_question']]["answer"]
        # if request.form['restart_button'] == "Restart Game?":
        #    session['current_question']=0

        # increment when good_answer is true and don't when is a last question
        if good_answer and len(questions)!=session['current_question']: 
            session['current_question']=session['current_question']+1

        if session['current_question']==len(questions): 
             session['current_question']=0

        if good_answer:        
            flash("{}".format('Correct'))
        elif request.form["answer"]=="":
            flash("{}".format(''))
        else: 
            flash("{}".format('Bad Answer'))
    
    return render_template("home.html", active_page='index', question=questions[session['current_question']]["question"], question_number=session['current_question'])

@app.route('/reset')
def reset():
    session['current_question']=0
    
    return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template("about.html", active_page='about')

if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

