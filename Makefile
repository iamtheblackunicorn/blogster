clean: ; rm -rf *.lock db.sqlite3
mig: ; python manage.py migrate --run-syncdb
serve: ; python manage.py runserver
su: ; python manage.py createsuperuser
