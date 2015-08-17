# pycoloman
Python Colocation Manager Software

Requires django

Installing
==========

Always use a virtualenv when installing python dependencies!


#### Ubuntu

```
sudo apt-get install python-virtualenv
```

Setup your virtualenv

```
virtualenv pycoloman
cd pycoloman
source bin/activate
```

After you've activated, you'll be reminded by your prompt changing:
```
(pycoloman)you@somemachine ~/pycoloman
```

Clone the repo

```
git clone https://github.com/Mancolo/pycoloman.git
cd pycoloman
```


Install the requirements
````
pip install -r ./requirements.txt
```

From the pcm directory, run the db migrations:
```
python manage.py migrate
```

Optional: Load up the sample database fixture. (Includes superuser admin with password admin)
```
python manage.py loaddata ./crm/fixtures/sample_db.yaml
```

Create a superuser to login with:
```
python manage.py createsuperuser
```

Run the dev server:
```
python manage.py runserver 0.0.0.0:8000
```

Then go to http://yourip:8000/admin/ and login with your superuser account to view the admin interface
