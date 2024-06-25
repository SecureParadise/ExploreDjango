# 1. Create Virtual Environment

python -m venv .VirtualEnvaramentName

eg :-) python -m venv .venv

##### Activate virtual Environment
###### Windows
.venv/Scripts/activate
###### Mac/Linux
source .venv/Scripts/activate
###### deactivate :- to deactivate virtual environment

## 2. Install Django
pip install Django
### Create porject
django-admin startproject PROJECTNAME
### Run porject
python manage.py runserver
