
# reference:
# https://aws.amazon.com/blogs/devops/build-and-deploy-a-federated-web-identity-application-with-aws-elastic-beanstalk-and-login-with-amazon/

# reference flask w aws:
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

# reference eb w django
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

# IP Address	98.199.135.8
# Hostname	c-98-199-135-8.hsd1.tx.comcast.net



pip install virtualenv
# For Mac
# virtualenv --python=python3.7 weather-env
# For Windows
virtualenv env

source ./env/bin/activate
source /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/env/bin/activate

# install all required packages
# pip install -r requirements.txt

pip freeze
pip freeze >requirements.txt
#######################################################################################################
# clean python cache
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf


# sudo pip install dash dash-renderer dash-html-components dash-core-components plotly
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/mariandumitrascu/bi-portal.git
git branch -M main
git push -u origin main


# git remote add origin https://github.com/mariandumitrascu/sample-site-eb.git
git branch -M main
git push -u origin main


####################################################################################################
# django
pip install --upgrade pip
pip install django
pip install pillow
pip install django-widget-tweaks
pip install django-taggit
pip install django-debug-toolbar

# reference
# https://django-bootstrap3.readthedocs.io/en/latest/installation.html
# https://django-bootstrap4.readthedocs.io/en/latest/installation.html
# https://github.com/zostera/django-bootstrap3
pip install django-bootstrap4
pip uninstall django-bootstrap4

pip install django-bootstrap3

python -m django --version
# 3.1.4
django-admin startproject mainsite

cd /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite

python manage.py migrate
python manage.py startapp biportal


########################################################################################
python manage.py createsuperuser

python ./mainsite/manage.py runserver 8888
python manage.py runserver 8888

########################################################################################
# polls app

# By running makemigrations, you’re telling Django that you’ve made some changes to your models
# and that you’d like the changes to be stored as a migration.
python manage.py makemigrations polls

# The sqlmigrate command takes migration names and returns their SQL:
# this is not modifying anything in the database
python manage.py sqlmigrate polls 0002

# checks for any problems in your project without making migrations or touching the database.
python manage.py check

# takes all the migrations that haven’t been applied
# (Django tracks which ones are applied using a special table in your database called django_migrations)
# and runs them against your database - essentially,
# synchronizing the changes you made to your models with the schema in the database.
python manage.py migrate

#########################################################################################
# interact with the model and django api
python manage.py shell


#########################################################
# testing pools
python manage.py test polls

##############################################################################################################
##############################################################################################################
##############################################################################################################
# django-polymorfic

pip install django-polymorphic
python manage.py startapp polymorf
python manage.py makemigrations polymorf
# python manage.py sqlmigrate polymorf 0001
python manage.py migrate


##############################################################################################################
# blog
python manage.py startapp blog
python manage.py makemigrations blog
python manage.py migrate

#####################################
from blog.models import Blog
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()
exit()

##############################################################################################################
##############################################################################################################
##############################################################################################################
# beginers guide
cd /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite
python manage.py startapp boards
python manage.py runserver 8888

pip install Markdown
pip install django-widget-tweaks
pip install decouple

python manage.py makemigrations boards
python manage.py migrate

python manage.py test --verbosity=2

npm install --global htmlhint

#####################################################
# accounts
python manage.py startapp accounts


##############################################################################################################
##############################################################################################################
##############################################################################################################
python manage.py makemigrations biportal
python manage.py migrate
python manage.py runserver 8888

##############################################################################################################
##############################################################################################################
##############################################################################################################
pip install isort

# check which files will be sorted
isort --recursive --check-only .
isort .

##############################################################################################################
##############################################################################################################
##############################################################################################################
# accounts
python manage.py makemigrations accounts