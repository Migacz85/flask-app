# Math quiz

This project is a simple math quiz coded using python&flask.

## Development

## UX

The main idea in this UX process design was:

- Keep it simple.
- Focus to use bootstrap when possible.
- Deliver clean easy to read design.

## User Stories / Automated tests

- Next question must be given when user answer badly 3 times
- Next question must be given when user answer correctly
- When user answer correctly at first attempt 3 points need to be added to score
- When user answer correctly on next question points need to add on
- When user is on the last question game over is shown
- Storing name and score of all players
- Checking that user is already in leaderboard 
- Update player score in leaderboard by name 
- Leaderboard is finding player stats who have most points
- Leaderboard is sorting players by points
- Leaderboard can check actual position of player

## Technologies Used:

- Python
- Flask
- Bootstrap

## Features 

- Asking player a question and comparing them with prepared answers form file
- Showing all playing users on leaderboard
- Ranking players

### Features left to implement

- Show players stats without refreshing the browser

## Testing:

Automated tests are applied in game_functions.py and are identical as user stories.
In project, you can find also a cligame.py which is simple game simulation that works in terminal and is using functions from game_functions. 

For writing and testing individual functions it is much faster to do that in terminal using cligame.py than testing directly in browser. 

Tests are done every time a run.py or cligame.py is executed.

## Installation

First clone the project:

```
git clone https://github.com/Migacz85/flask-app.git
```

### Creating new environments for python3: 

To start developing the project you need to run this commands:

```
python -m venv venv   //initialize new environment.
source venv/bin/activate //enter to the new environment.
sudo pip3 install -r requirements.txt // install dependencies from files.
python run.py // this will run the flask server.
deactivate // If you will want to go out from the env you can close virtual env using this command.
```

### Other useful commands:

```
sudo pip3 install flask //install flask or other dependencies using this command.
pip3 uninstall flask // unistall flask
pip3 freeze --local show packages installed 
pip3 freeze --local >> requirements.txt // save dependencies to the file

which python // show you path for python
ls /usr/bin/ | grep python // show installed versions of python
```

If you will have problems with starting the server because of ports:

```
KILLING PROCCESSES ON PORTS:
lsof -i tcp:8080
kill -9 <PID>
```


## Deployment steps on heroku or other platforms:

```
heroku apps:info name_of_your_app - display url for your app and heroku git
echo web: python run.py > Procfile  //create procfile
heroku ps:scale web=1
git remote add heroku https://git.heroku.com/wvz.git  // add repository to remote
git push heroku
```

In heroku app: 

```
go to settings -> "Config vars" -> 
add IP on 0.0.0.0
add PORT on 5000
restart server
```

## Credits

### Media
- Background picture used in this site was taken from https://www.pexels.com/

### Acknowledgements

- Great thanks to codeinstitute.net for explaining me basics with python & flask
- When making this project I found @mormoran very helpfull from slack. Thank You too!


