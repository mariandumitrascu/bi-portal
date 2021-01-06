
# BI Portal Based on Django


## Installation

Typical django project installation:

```bash

# clone the project
git clone https://github.com/mariandumitrascu/bi-portal.git

cd bi-portal

# install a python virtual environment
virtualenv env

# activate env
source ./env/bin/activate

# install dependencies
pip install -r requirements.txt

cd mainsite

# delete all migrations (optional)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# prepare database installation
python manage.py makemigrations

# build the database
python manage.py migrate

# create superuser
python manage.py createsuperuser

# launch the site
python manage.py runserver
```

Server should be live at http://127.0.0.1:8000/ now.
If you use the db as it is, username and password are `admin`



