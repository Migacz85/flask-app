import os
from flask import Flask, render_template, request, flash, json, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'
all_users=[]

@app.route('/', methods=["GET", "POST"])
def index():
    
    
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
    
    if request.method == "POST":

        # When asking about all questions excluding first
        if session['current_question']!=0:
            # Check if user answer is correct
            next_answer=request.form["answer"]==questions[session['current_question']]["answer"]
            session['score']+=3-session['bad_answers']
        # When asking about first question
        else:  
            session['score']=0
            next_answer=True # Make all answer true
            session['user']=request.form["answer"] # Store users name
        
        if 'user' not in session:
            return redirect(url_for("reset"))
           
        # After 3 bad answers jump to next question
        if session['bad_answers']==3:
            next_answer=True
            session['bad_answers']=0
            session['score']+=0

        # Increment current_question when next_answer is true and don't when is a last question
        if next_answer and len(questions)!=session['current_question']: 
            session['current_question']=session['current_question']+1
        # Count bad answers
        else:
            session['bad_answers']+=1

        if session['current_question']==len(questions): 
             session['current_question']=0

        if next_answer:        
            flash("{}".format('Correct'))
        elif request.form["answer"]=="":
            flash("{}".format(''))
        else: 
            flash("{}".format('Bad Answer'))

    def check_for_user(user_tuple_list, session_user):
        test=False
        for tupe in user_tuple_list:
            if tupe[0] == session_user:
               test=True
            else: 
               test=False
        return test

    if not check_for_user(all_users, session["user"] ):
        user_and_score = (session["user"], session["score"])
        all_users.append(user_and_score)
        

    return render_template("home.html", 
    active_page='index', 
    question=questions[session['current_question']]["question"], 
    question_number=session['current_question'],
    score=session['score'],
    users=all_users,
    check=check_for_user(all_users, session["user"] )
    )

@app.route('/reset')
def reset():
    session['current_question']=0
    session['bad_answers']=0
    session['score']=0
    return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template("about.html", active_page='about')

if __name__ == '__main__':
   app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)

