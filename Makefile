migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

admin:
	python manage.py createsuperuser

app:
	django-admin startapp $(word 2, $(MAKECMDGOALS))

up:
	python manage.py runserver

shell:
	python manage.py shell