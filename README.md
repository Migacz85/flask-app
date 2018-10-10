// creating new enviroments for python3 
python -m venv venv   //initialize new enviroment
source venv/bin/activate //enter to the new enviroment
pip3 freeze --local // show dependencies in this env
sudo pip3 inastall -r requirements.txt // install dependencies from files
deactivate // close virtual env.
