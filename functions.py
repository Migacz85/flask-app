from tests import *
from flask import json

  
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)

points = 0
last_question = len(questions)
all_users=[]

def question(question_number):
    question=questions[question_number]['question']
    return question

def good_answer(user_answer, question_number, questions):
    test=False
    if user_answer==questions[question_number]['answer']:
        test=True
    else: 
        test=False
    return test

def next_answer(bad_answers, good_answer):            
    if good_answer==1:
        return True
    if bad_answers==3:
        bad_answers=0
        return True
        
def score(bad_answers):
    global points
    points+=3-bad_answers
    return points

def game_over(question):
    if question == last_question:
        return True
    else: False

# Leader Board functions

def lb_add_stats(player, score, all_users):
    user_and_score = [player, score]
    all_users.append(user_and_score)
    return all_users

def lb_check_for_user(session_user, user_list):
        test=False
        for user in user_list:
            if user[0] == session_user:
               test=True
        return test

def lb_update_player_score(session_user, score, user_list):
        test=False
        for user_stats in user_list:
            if user_stats[0] == session_user:
               user_stats[1] = score
        return user_list

def lb_winner(user_list):
    max=0
    user=''
    for user_points in user_list:
        if max < user_points[1]:
            max= user_points[1]
            user=user_points
    return user

def lb_sorted(user_list):
    ranking=[] #sorted list
    unsorted=0
    unsorted=list(user_list)
    
    while lb_winner(unsorted) in unsorted:
                ranking.append(lb_winner(unsorted))
                unsorted.remove(lb_winner(unsorted))

    return ranking


def lb_position(player_name, user_list):
    my_list_len=len(user_list)
    for i in range(0, my_list_len):
        if user_list[i][0]==player_name:
            return i    
    
            

# Good answer need to match with answers from answers.json
    # Answer to first question is 4
test_are_equal(good_answer('4', 0, questions), True)   # Good Answer
test_are_equal(good_answer('seven', 0, questions), False ) # Bad Answer

## next_answer is:
# Next question must be given when user answer badly 3 times
test_are_equal(next_answer(3,0), True)

# Next question must be given when user answer correctly
test_are_equal(next_answer(1,good_answer('4', 0, questions)), True )
test_are_equal(next_answer(2,good_answer('4', 0, questions)), True )

## score is:
# When user answer correctly at first attempt 3 points need to be added to score
test_are_equal(score(0), 3 )

# When user answer correctly on next question points need to add on
test_are_equal(score(0), 6 )
test_are_equal(score(2), 7 )

## game_over is:
# When user is on the last question
test_are_equal(game_over(last_question), True )

## Leaderboard is:
# Storing name and score of all players

test_are_equal(lb_add_stats('Marcin', 23, all_users), [['Marcin',23]] )
test_are_equal(lb_add_stats('Tomek', 13, all_users), [['Marcin',23], ['Tomek',13]] ) 

# Checking is user is already in leaderboard

test_are_equal(lb_check_for_user('Marcin', all_users)  ,True) 
test_are_equal(lb_check_for_user('Tomek', all_users)  ,True) 
test_are_equal(lb_check_for_user('John', all_users)  ,False) 

# Update player score in leaderboard by name 

test_are_equal(lb_update_player_score('Marcin', 25, all_users ), [['Marcin',25], ['Tomek',13]]  )
test_are_equal(lb_update_player_score('Tomek', 35, all_users ), [['Marcin',25], ['Tomek',35]]  )

# Leaderboard is finding player stats who have most points

test_are_equal(lb_winner(all_users), ['Tomek', 35])
test_are_equal(lb_winner([]), "")
test_are_equal(lb_winner(""), "")

# Leaderboard is sorting players by points

test_are_equal(lb_sorted(all_users), [['Tomek', 35], ['Marcin',25] ] )
lb_add_stats('John', 43, all_users)
test_are_equal(lb_sorted(all_users), [['John', 43],['Tomek', 35], ['Marcin',25] ] )
lb_add_stats('Johny', 38, all_users)
test_are_equal(lb_sorted(all_users), [['John', 43],['Johny', 38] ,['Tomek', 35], ['Marcin',25] ] )

test_are_equal(lb_sorted([]),[])

# Leaderboar can check actual postion of player

test_are_equal(lb_position('John', lb_sorted(all_users)), 0)
test_are_equal(lb_position('Tomek',lb_sorted(all_users)), 2)

print('tests passed')

