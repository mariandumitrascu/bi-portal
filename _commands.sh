# this file contains a collection of bash commands used during the research and development of the project
# it should not be executed


# reference:
# https://aws.amazon.com/blogs/devops/build-and-deploy-a-federated-web-identity-application-with-aws-elastic-beanstalk-and-login-with-amazon/

# reference flask w aws:
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

# reference eb w django
# https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

# github repo:
# https://github.com/mariandumitrascu/bi-portal

pip install virtualenv
# For Mac
# virtualenv --python=python3.7 weather-env
# For Windows
virtualenv env

source ./env/bin/activate
source /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/env/bin/activate
cd /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite
python manage.py runserver 8888
python /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite/manage.py runserver 0.0.0.0:8888


######################################################################################################
# inside container
cd /workspaces/bi-portal/mainsite
python manage.py runserver 8888
python /workspaces/bi-portal/mainsite/manage.py runserver 8888

# install all required packages
# pip install -r requirements.txt

pip freeze
pip freeze >requirements.txt
pip freeze >/Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/requirements.txt
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
pip install sorl-thumbnail
pip install pyppeteer
pip install markdown
pip install python-pptx
# pip install tornado

# reference:
# https://github.com/fabiocaccamo/django-admin-interface
pip install django-admin-interface

# reference:
# https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/
pip install python-dotenv


# reference
# https://django-bootstrap3.readthedocs.io/en/latest/installation.html
# https://django-bootstrap4.readthedocs.io/en/latest/installation.html
# https://github.com/zostera/django-bootstrap3
pip install django-bootstrap4
pip uninstall django-bootstrap4

# reference:
# https://github.com/douglasmiranda/django-admin-bootstrap

pip install django-bootstrap3

pip install django-crispy-forms


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

python manage.py startapp pptlayouts
python manage.py makemigrations pptlayouts
python manage.py migrate


#############################################################################################################
#############################################################################################################
#############################################################################################################
# reset the db
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/db.sqlite3"  -delete

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8888


python manage.py collectstatic
python manage.py loaddata admin_interface_theme_bootstrap.json
python manage.py loaddata admin_interface_theme_foundation.json
python manage.py loaddata admin_interface_theme_uswds.json

# test url:
# https://public.tableau.com/en-us/gallery/holiday-consumer-spending?tab=featured&type=featured

# texts:
# Short Term Disability Utilization Overview
# Represents Data from January 1, {last year} through December 31, {last year}


# http://127.0.0.1:8888/admin/biportal/snippethtml/2/change/


# original header color: #0C4B33

# save butttons
#0C4B33
#0C3C26


# elsticbeanstack
/Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/mainsite
mkdir .ebextensions

eb init -p python-3.7 guardian-biportal
eb init
eb create django-env
eb deploy

docker build -f /Users/marian.dumitrascu/Dropbox/Work/Current/python-cms/bi-portal/.devcontainer/Dockerfile -t vsc-bi-portal-aaa9b47b59e44357bcb22ae8d6b29645 --build-arg VARIANT=3.8 --build-arg INSTALL_NODE=false

python manage.py findstatic admin/css/base.css

################################################################################################
# quick commands for deployments:

ansible-playbook ansible-eks/main.yaml
ansible-playbook ansible-eks/retract.yaml

ansible-playbook ansible-ec2/main.yaml
ansible-playbook ansible-ec2/retract.yaml

# #############################################################################################
# interact with the ec2
# ec2-54-159-159-10.compute-1.amazonaws.com

export ec2-18-234-57-99.compute-1.amazonaws.com
echo $ec2
ssh -i ~/.ssh/id_rsa ec2-user@$ec2

ssh -i ~/.ssh/id_rsa ec2-user@ec2-34-204-70-23.compute-1.amazonaws.com
ssh ec2-user@ec2-54-159-159-10.compute-1.amazonaws.com

# commands that should run on the ec2 after is launched
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 156021229203.dkr.ecr.us-east-1.amazonaws.com
docker run -itd --name guardian-grrf -p 80:8888 --rm '156021229203.dkr.ecr.us-east-1.amazonaws.com/cts-aia-guardian-grrf:1.0.3'