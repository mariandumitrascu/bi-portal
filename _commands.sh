
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
git remote add origin https://github.com/mariandumitrascu/sample-site-django3.git
git branch -M main
git push -u origin main


# git remote add origin https://github.com/mariandumitrascu/sample-site-eb.git
git branch -M main
git push -u origin main

##################################################################################################
eb init -p python-3.6 flask-demo --region us-east-1
eb init

##################################################################################################
eb create flask-env
eb open

##################################################################################################
eb status

##################################################################################################
eb deploy

##################################################################################################
eb terminate --force


# ec2
ec2-3-95-29-190.compute-1.amazonaws.com

ssh -i /Users/marian.dumitrascu/Dropbox/Work/current/hudi/aws-hudi-demo/key-pairs/md-labs-key-pair.pem ec2-user@ec2-3-95-29-190.compute-1.amazonaws.com
ssh -i /Users/marian.dumitrascu/Dropbox/Work/current/hudi/aws-hudi-demo/key-pairs/md-labs-key-pair.pem root@ec2-3-95-29-190.compute-1.amazonaws.com

# the app was deployed:
/opt/python/bundle/2/app/application.py

# configure ssl for beanstack
# https://colintoh.com/blog/configure-ssl-for-aws-elastic-beanstalk

####################################################################################################
# django

pip install django
python -m django --version
# 3.1.4
django-admin startproject mysite

cd /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/sample-site-django3/mysite

python manage.py migrate
python manage.py startapp polls

########################################################################################
python manage.py createsuperuser

python ./mysite/manage.py runserver 8989
python manage.py runserver 8989

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
cd /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/sample-site-django3/mysite
python manage.py startapp boards
python manage.py runserver 8989

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