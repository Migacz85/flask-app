from functions import *

question_number=0
bad_answers=0
all_users=[]
player_score = 0 
user_answer =0
ranking=[]

#lb_add_stats('Marcin', 23, all_users)
#lb_add_stats('Tomek', 24, all_users)


user_answer=input('1. game simulation 2. Manual test parts of code: ')

if user_answer=='1':
    while user_answer!='exit':

        if not game_over(question_number):

            quest=question(question_number)
            print(quest)
            user_answer=input('Type your answer: ')
            if question_number==0:
                player_name=user_answer
                lb_add_stats(player_name, 0, all_users)

            if not good_answer(user_answer, question_number, questions):
                bad_answers+=1
                print(player_name, "%s is bad answer" %user_answer)
            else:
                if question_number!=0:
                    player_score+=3-bad_answers
                    lb_update_player_score(player_name, player_score, all_users)
                    all_users=lb_sorted(all_users) # error 
                    print('Current users stats:', all_users)
                    print('Current winner: ', lb_winner(all_users))
                    position=lb_position(player_name, all_users)
                    print(user_answer, "that was correct answer :-) Your position in ranking is:" , position)

            if next_answer(bad_answers,  good_answer(user_answer, question_number, questions)):
                question_number+=1
                bad_answers=0
                print(player_name, 'Next Question, You have %s points' % player_score)
        else:
            print('Game Over, Your score is: %s' % player_score)
            print(all_users)
            player_score=0
            bad_answers=0
            question_number=0
        

elif  user_answer=='2':
    print('Your code results in: ')
    
    lb_add_stats('Marcin', 23, all_users)
    lb_add_stats('Tomek', 24, all_users)

    player_name="Mig"

    lb_add_stats(player_name, 24, all_users)
    

    all_users=lb_sorted(all_users)
    position=lb_position(player_name, all_users)


    position=lb_position(player_name, lb_sorted(all_users))
    
    print(position)



